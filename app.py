from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import time

import io
import uuid
# import fitz  # PyMuPDF
from PIL import Image

# Import des services
from services.scoring_prompts import *
from services.global_state import progress_status, cv_json_global, jd_json_global, scores_global
from services.processing_service import background_processing, redis_client, save_progress
import json

app = Flask(__name__)
app.secret_key = 'supersecretkey'

app.config['UPLOAD_FOLDER'] = './uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)






@app.route("/", methods=["GET", "POST"])
def index():
    """
    Page d'accueil avec le formulaire pour soumettre le CV et la description de poste.
    """
    if request.method == "POST":
        global progress_status

        # Récupération des fichiers et de la description
        cv_file = request.files['cv']
        job_description = request.form['job_description']

        # Sauvegarder le fichier temporairement
        filename = secure_filename(cv_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        cv_file.save(filepath)

        # Réinitialisation du statut de progression
        progress_status = {"progress": 0, "message": "Initialisation..."}
        save_progress(progress_status)

        # Lancer le traitement en arrière-plan
        thread = Thread(target=background_processing, args=(filepath, job_description))
        thread.start()
        

        # Redirection vers la page de chargement
        return redirect(url_for('loading'))

        # background_processing(filepath, job_description)
        
        return redirect(url_for('result'))


    return render_template("index.html")

@app.route("/loading")
def loading():
    """
    Page de chargement avec animation de progression.
    """
    return render_template("loading.html")

@app.route("/progress")
def progress():
    """
    Endpoint pour renvoyer l'état d'avancement en JSON.
    """
    progress = json.loads(redis_client.get("progress"))
    return progress

@app.route("/result")
def result():
    """
    Page des résultats, affichant les données traitées.
    """ 
    cv = json.loads(redis_client.get("cv_json_global"))
    jd = json.loads(redis_client.get("jd_json_global"))
    user_info = json.loads(redis_client.get("user_info"))
    scores = json.loads(redis_client.get("scores_global"))
    # note_globale = float(redis_client.get('note_generale'))
    # note_globale = round(note_globale, 2)
    note_globale = 10
    
    return render_template("result.html", cv_json=cv, jd_json=jd, scores=scores, note_globale=note_globale, user=user_info)

if __name__ == "__main__":
    app.run(debug=True)
