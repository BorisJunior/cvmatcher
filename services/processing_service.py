import os
import time
import io
import uuid
import fitz  # PyMuPDF
from PIL import Image
from flask import app
from services.global_state import progress_status, cv_json_global, jd_json_global, scores_global
from services.deepseek_service import call_deepseek_api
from services.json_parser import parse_to_json
from services.response_parser import parse_llm_response
from services.text_formatter import format_explanation
from services.scoring_prompts import *
from services.llama_vision_service import generate_vision_response
from redis import Redis
import json

redis_client = Redis(host="localhost", port=6379, db=0, decode_responses=True)

save_progress = lambda progress : redis_client.set("progress", json.dumps(progress))

# ----------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------
def pdf_to_image(pdf_path, output_folder):
    """
    Convertit la première page d'un PDF en image JPEG.
    Retourne le chemin de l'image générée.
    """
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    pix = page.get_pixmap()
    
    img = Image.open(io.BytesIO(pix.tobytes("ppm")))
    img_filename = f"{uuid.uuid4()}.jpg"
    img_path = os.path.join(output_folder, img_filename)
    img.save(img_path, "JPEG", quality=85)
    
    doc.close()
    return img_path

def load_prompt(template_path, **kwargs):
    """
    Charge un fichier de prompt et le formate avec les arguments passés.
    """
    with open(template_path, 'r', encoding='utf-8') as file:
        template = file.read()
    return template.format(**kwargs)


# ----------------------------------------------------------
# Core Processing Logic
# ----------------------------------------------------------
def structure_cv_and_jd(image_path, job_description):
    """
    Appelle LLaMA Vision pour extraire les infos du CV (à partir d'une image)
    et DeepSeek pour structurer la description de poste, en parallèle.
    """

    cv_prompt = load_prompt('prompts/cv_prompt.txt')
    jd_prompt = load_prompt('prompts/jd_prompt.txt', description_poste=job_description)
    print(jd_prompt)
    print('start vision response')
    structured_cv = generate_vision_response(cv_prompt, image_path)
    print('vision response done')
    progress_status = {"progress": 34, "message": "🛠️ Extraction & structuration du CV et de la JD..."}
    save_progress(progress_status)
    structured_jd = call_deepseek_api(jd_prompt)
    print('jd response done')
    """  
    with ThreadPoolExecutor() as executor:
        future_cv = executor.submit(generate_vision_response, cv_prompt, image_path)
        future_jd = executor.submit(call_deepseek_api, jd_prompt)

        structured_cv = future_cv.result()
        structured_jd = future_jd.result()
    """

    return structured_cv, structured_jd

def calculate_scores(cv_json, jd_json):
    """
    Calcule les scores des différentes sections en parallèle.
    """

    scores = {}

    def calculate_section_score(section):
        """
        Envoie un prompt pour une section spécifique.
        """
        if section == "Formation":
            prompt = generate_formation_prompt(cv_json.get("Formation", "Non mentionné"),
                                               jd_json.get("Formation", "Non mentionné"))
        elif section == "Xp_Professionnelles":
            prompt = generate_experience_prompt(cv_json.get("Xp_Professionnelles", "Non mentionné"),
                                                jd_json.get("Xp_Professionnelles", "Non mentionné"))
        elif section == "Hard_Skills":
            prompt = generate_hard_skills_prompt(cv_json.get("Hard_Skills", "Non mentionné"),
                                                 jd_json.get("Hard_Skills", "Non mentionné"),
                                                 cv_json.get("Xp_Professionnelles", "Non mentionné"))
        elif section == "Soft_Skills":
            prompt = generate_soft_skills_prompt(cv_json.get("Soft_Skills", "Non mentionné"),
                                                 jd_json.get("Soft_Skills", "Non mentionné"),
                                                 cv_json.get("Xp_Professionnelles", "Non mentionné"))
        elif section == "Langues":
            prompt = generate_languages_prompt(cv_json.get("Langues", "Non mentionné"),
                                               jd_json.get("Langues", "Non mentionné"))
        else:
            return section, {}

        response = call_deepseek_api(prompt)
        return section, parse_llm_response(response)

    sections = ["Formation", "Xp_Professionnelles", "Hard_Skills", "Soft_Skills", "Langues"]
    """ with ThreadPoolExecutor() as executor:
        futures = [executor.submit(calculate_section_score, section) for section in sections]
        for future in futures:
            section, result = future.result()
            scores[f"note_{section.lower()}"] = result.get(f"note_{section.lower()}", "Non disponible")
            scores[f"{section.lower()}_explication"] = format_explanation(
                result.get(f"{section.lower()}_explication", "Non disponible")
            ) """
    
    print('sections', sections)
    for section in sections:
        section, result = calculate_section_score(section)
        scores[f"note_{section.lower()}"] = result.get(f"note_{section.lower()}", "Non disponible")
        scores[f"{section.lower()}_explication"] = format_explanation(
            result.get(f"{section.lower()}_explication", "Non disponible"))
        print(f"{section.lower()} score", scores[f"note_{section.lower()}"])
    return scores

def clean_numeric_values(values):
    cleaned_values = []
    for value in values:
        # If the value is a string and contains a '/'
        if isinstance(value, str) and '/' in value:
            # Split the string by '/' and take the numerator (first part)
            numerator = value.split('/')[0]
            # Convert the numerator to a float or int
            cleaned_values.append(float(numerator) if '.' in numerator else int(numerator))
        else:
            # If the value is already numeric, add it directly
            cleaned_values.append(float(value) if isinstance(value, str) and '.' in value else int(value))
    return cleaned_values

def background_processing(filepath, job_description):
    """
    Fonction exécutant le traitement en arrière-plan.
    1) Conversion PDF -> Image si besoin
    2) Extraction / structuration via LLaMA Vision & DeepSeek
    3) Calcul des scores
    """
    global progress_status, cv_json_global, jd_json_global, scores_global

    try:
        progress_status = {"progress": 0, "message": "🔍 Vérification du fichier CV..."}
        save_progress(progress_status)
        

        
        # Étape 1 : Vérifier l'extension. Si PDF, conversion en image
        extension = os.path.splitext(filepath)[1].lower()
        if extension == '.pdf':
            image_path = pdf_to_image(filepath, app.config['UPLOAD_FOLDER'])
        else:
            # On considère que le fichier uploadé est déjà une image
            image_path = filepath

        print('file path', image_path)
        # Étape 2 : Structurer le CV via LLaMA Vision + JD via DeepSeek    
        structured_cv, structured_jd = structure_cv_and_jd(image_path, job_description)
        

        print('structured_cv', structured_cv)
        print('structured_jd', structured_jd)   
        redis_client.set('structured_cv', json.dumps(structured_cv))
        redis_client.set('structured_jd', json.dumps(structured_jd))
        cv_json_global, user_info = parse_to_json(structured_cv)
        jd_json_global, _ = parse_to_json(structured_jd)

        # Étape 3 : Calcul des scores
        progress_status = {"progress": 67, "message": "🤖 Calcul du score avec notre Super IA..."}
        save_progress(progress_status)
        


        scores_global = calculate_scores(cv_json_global, jd_json_global)

        redis_client.set("cv_json_global", json.dumps(cv_json_global))
        redis_client.set("jd_json_global", json.dumps(jd_json_global))
        redis_client.set("scores_global", json.dumps(scores_global))
        redis_client.set("user_info", json.dumps(user_info))

        print('scores_global', scores_global)

        scores_notes = [scores_global['note_formation'], scores_global['note_hard_skills'], scores_global['note_langues'], scores_global['note_soft_skills'], scores_global['note_xp_professionnelles']]
        cleaned_scores_notes = clean_numeric_values(scores_notes)
        note_generale = sum(cleaned_scores_notes) / 5
        redis_client.set("note_generale", note_generale)

        print("note_generale", note_generale)

        progress_status = {"progress": 100, "message": "✅ Traitement terminé. Préparation de la page des résultats..."}
        save_progress(progress_status)
    except Exception as e:
        progress_status = {"progress": 0, "message": f"❌ Erreur : {e}"}
        save_progress(progress_status)
