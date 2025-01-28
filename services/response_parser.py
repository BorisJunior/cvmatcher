import re

def parse_llm_response(response):
    """
    Parse la réponse du LLM pour extraire les informations encadrées par des balises spécifiques.
    Retourne un dictionnaire JSON structuré.
    """
    try:
        parsed_response = {
            "formation_explication": extract_tag_content(response, "formation_explication"),
            "note_formation": extract_tag_content(response, "note_formation"),
            "xp_professionnelles_explication": extract_tag_content(response, "xp_professionnelles_explication"),
            "note_xp_professionnelles": extract_tag_content(response, "note_xp_professionnelles"),
            "hard_skills_explication": extract_tag_content(response, "hard_skills_explication"),
            "note_hard_skills": extract_tag_content(response, "note_hard_skills"),
            "soft_skills_explication": extract_tag_content(response, "soft_skills_explication"),
            "note_soft_skills": extract_tag_content(response, "note_soft_skills"),
            "langues_explication": extract_tag_content(response, "langues_explication"),
            "note_langues": extract_tag_content(response, "note_langues"),
        }
        return parsed_response
    except Exception as e:
        print(f"[ERREUR] Problème lors du parsing de la réponse : {e}")
        return {}


def extract_tag_content(response, tag):
    """
    Extrait le contenu d'une balise spécifique dans une réponse donnée.
    """
    pattern = f"<{tag}>(.*?)</{tag}>"
    match = re.search(pattern, response, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "Non mentionné"
