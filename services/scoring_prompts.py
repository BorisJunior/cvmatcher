from services.deepseek_service import call_deepseek_api

def generate_formation_prompt(cv_formation, jd_formation):
    """
    Génère le prompt pour la section Formation.
    """
    return f"""
    **Fiche de poste**
    - **Formation requise :** {jd_formation}

    **CV**
    - **Formation :** {cv_formation}

    ### Règles d’évaluation pour la formation :
    1. Correspondance du diplôme avec les exigences du poste (5 points) :
       - 5 : Le dernier diplôme obtenu correspond au niveau minimum requis en terme de niveau et de domaine ou spécialisation.
       - 0 : Le diplôme n'atteint pas le minimum requis ou n'est pas cohérent avec la filière requise.

    2. Reconnaissance de l’établissement (3 points) :
       - 3 : L'établissement est reconnu ou aucune exigence d'établissement n'est mentionnée.
       - 0 : Si le diplôme ne correspond pas au minimum requis.

    3. Certifications pertinentes (2 points) :
       - 2 : Une ou plusieurs certifications strictement liées au domaine du poste.
       - 0 : Pas de certification pertinente ou non mentionnée.

    ### Tâche :
    Évaluez la section "Formation" du CV par rapport à la fiche de poste, selon les règles ci-dessus rigoureusement et strictement.
    Fournissez une note sur 10 avec une explication concise mais précise.

    ### Réponse :
    <formation_explication> {{développer le raisonnement pour noter la formation selon les règles en étant bref mais précis   }}</formation_explication>

    <note_formation> {{mets ici uniquement que la note de la formation sur 10 sans détails et commentaires}} </note_formation>
    """


def generate_experience_prompt(cv_experience, jd_experience):
    """
    Génère le prompt pour la section Expériences Professionnelles.
    """
    return f"""
    **Fiche de poste**
    - **Expérience requise :** {jd_experience}

    **CV**
    - **Expériences professionnelles :** {cv_experience}

    ### Règles d’évaluation pour l'expérience professionnelle :
    1. Nombre d'années d'expérience minimum (5 points) :
       - Basé sur le calcul précis des mois d'expériences en rapport avec le domaine (hors stage).

    2. Cohérence des expériences (2 points) :
       - 2 points : Si la durée moyenne des expériences pertinentes est de 2 ans minimum.
       - 1 point : Si la durée moyenne est entre 1 et 2 ans.
       - 0 point : Si plusieurs postes montrent une instabilité manifeste (moins de 1 an).

    3. Bonus pour réalisations significatives (3 points) :
       - 3 points : Réalisations spécifiques, mesurables et parfaitement alignées avec les attentes du poste.
       - 2 points : Réalisations pertinentes mais manquant de détails ou non chiffrées.
       - 1 point : Réalisations pertinentes provenant principalement des projets.

    ### Tâche :
    Évaluez la section "Expériences Professionnelles" du CV par rapport à la fiche de poste, selon les règles ci-dessus.
    Fournissez une note sur 10 avec une explication concise mais précise.

    ### Réponse :
    <xp_professionnelles_explication> {{développer le raisonnement pour noter les expériences selon les règles en étant bref mais précis}} </xp_professionnelles_explication>

    <note_xp_professionnelles> {{mets ici uniquement que la note des expériences sur 10 sans détails et commentaires}} </note_xp_professionnelles>
    """

def generate_hard_skills_prompt(cv_hard_skills, jd_hard_skills, cv_experiences):
    """
    Génère le prompt pour la section Hard Skills.
    """
    return f"""
    **Fiche de poste**
    - **Compétences techniques requises :** {jd_hard_skills}

    **CV**
    - **Compétences techniques mentionnées :** {cv_hard_skills}
    - **Expériences professionnelles :** {cv_experiences}

    ### Règles d’évaluation :
    1. Pour chaque compétence technique requise mentionnée dans la fiche de poste :
       - 7 points : Si la compétence est explicitement mentionnée dans les compétences techniques du CV.
       - +3 points : Si la compétence est utilisée dans les expériences professionnelles.
          - 3 points complets : Si la compétence est explicitement mentionnée comme utilisée dans une ou plusieurs expériences.
          - 2 points : Si la compétence n'est pas explicitement mentionnée, mais son usage peut être raisonnablement déduit des expériences décrites.

    2. Si une compétence requise est absente des "Hard Skills" du CV :
       - Évaluer les chances que le candidat maîtrise cette compétence (0–6 points) :
         - 6 points : La compétence est probablement maîtrisée ou très proche d’autres compétences déjà démontrées.
         - 4–5 points : La compétence semble indirectement maîtrisée, mais nécessite peut-être une adaptation.
         - 2–3 points : La compétence est marginalement liée aux expériences ou à la formation, mais sans preuve claire de maîtrise.
         - 0–1 point : Aucun lien évident ou pertinent entre la compétence et le profil du candidat.
       - Ajouter des points si la compétence est utilisée dans les expériences professionnelles :
         - +1,5 points : Si la compétence est explicitement mentionnée comme utilisée dans une expérience.
         - +0,5 point : Si l'utilisation de la compétence peut être raisonnablement déduite des descriptions d'expérience.

    
    ### Tâche :
    - Évaluez chaque compétence mentionnée dans la fiche de poste en appliquant les règles ci-dessus.
    - Fournissez une note individuelle sur 10 pour chaque compétence.
    - Calculez la moyenne des notes pour déterminer une note globale sur 10 pour les compétences techniques.

    ### Réponse attendue :
    <hard_skills_explication> {{développer le raisonnement pour noter les compétences techniques selon les règles en étant bref mais précis}} </hard_skills_explication>

    <note_hard_skills> {{mets ici uniquement que la note globale techniques sur 10 sans détails et commentaires}} </note_hard_skills>
    """


def generate_soft_skills_prompt(cv_soft_skills, jd_soft_skills, cv_experiences):
    """
    Génère le prompt pour la section Soft Skills.
    """
    return f"""
    **Fiche de poste**
    - **Compétences transversales requises :** {jd_soft_skills}

    **CV**
    - **Compétences transversales :** {cv_soft_skills}
    - **Expériences professionnelles :** {cv_experiences}

    ### Règles d’évaluation :
    - 5 points : Si la compétence est mentionnée explicitement dans le CV.
    - 0 point : Si la compétence est absente du CV.
    - +3 points : Si des résultats ou comportements concrets illustrent la compétence.
    - +2 points : Si la compétence peut être déduite du contexte

    ### Tâche :
    - Évaluez chaque compétence mentionnée dans la fiche de poste en appliquant les règles ci-dessus.
    - Fournissez une note individuelle sur 10 pour chaque compétence.
    - Calculez la moyenne des notes pour déterminer une note globale sur 10 pour les compétences transversales.


    ### Réponse :
    <soft_skills_explication> {{développer le raisonnement pour noter les compétences transversales selon les règles en étant bref mais précis}} </soft_skills_explication>

    <note_soft_skills> {{mets ici uniquement que la note globale des compétences transversales sur 10 sans détails et commentaires}} </note_soft_skills>
    """

def generate_languages_prompt(cv_langues, jd_langues):
    """
    Génère le prompt pour la section Langues.
    """
    return f"""
    **Fiche de poste**
    - **Langues requises :** {jd_langues}

    **CV**
    - **Langues mentionnées :** {cv_langues}

    ### Règles d’évaluation :
    #### Étape 1 : Notation des langues individuelles
    - **Français** :
      - 10 points : Si le candidat est natif ou mentionne un niveau avancé/bilingue.
      - 7 points : Si mentionné à un niveau intermédiaire.
      - 0 point : Si le français n’est pas mentionné et ne peut être déduit du profil.
    - **Anglais** :
      - 7 points : Si un niveau avancé/bilingue est explicitement mentionné.
      - 6 points : Si mentionné à un niveau intermédiaire.
      - +3 points : Si une certification pertinente est mentionnée pour un niveau avancé ou bilingue (ex. : TOEFL, IELTS).
      - +2 points : Si une certification est mentionnée pour un niveau intermédiaire.

    #### Étape 2 : Pondération des langues dans le score final
    - Si l’anglais est explicitement requis :
      - 40% pour le français.
      - 60% pour l’anglais.
    - Si l’anglais n’est pas explicitement mentionné :
      - 60% pour le français.
      - 40% pour l’anglais.

    ### Tâche :
    - Évaluez chaque langue mentionnée dans le CV par rapport aux exigences de la fiche de poste.
    - Fournissez une note individuelle sur 10 pour le français, l'anglais, et toute autre langue pertinente.
    - Appliquez la pondération appropriée pour calculer un score global sur 10 pour la section "Langues".

    ### Réponse attendue :
    <langues_explication> {{développer le raisonnement pour noter les langues selon les règles en étant bref mais précis}} </langues_explication>

    <note_langues> {{mets ici uniquement que la note finale des langues sur 10 sans détails et commentaires}} </note_languages>
    """

