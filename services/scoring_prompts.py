def generate_formation_prompt(cv_formation, jd_formation, cv_certification):
    """
    Génère le prompt pour la section Formation.
    """
    return f"""
    **Fiche de poste**
    - **Formation requise :** {jd_formation}

    **CV**
    - **Formation :** {cv_formation}
    - **Certification :** {cv_certification}

    ### Règles d’évaluation pour la formation :
    1. Correspondance du diplôme avec les exigences du poste (5 ou 0 points) :
       - 5 points : Le dernier diplôme obtenu correspond au niveau minimum requis en terme de niveau et de domaine ou spécialisation.
       - 0 point : Le diplôme n'atteint pas le minimum requis ou n'est pas cohérent avec la filière requise.

    2. Reconnaissance de l’établissement (3 points) :
       - 3 points : L'établissement est reconnu ou aucune exigence d'établissement n'est mentionnée.
       - 0 point : Si le diplôme ne correspond pas au minimum requis.

    3. Certifications pertinentes (2 points) :
       - 2 points : Une ou plusieurs certifications strictement liées au domaine du poste.
       - 0 points : Pas de certification pertinente ou non mentionnée.

    ### Tâche :
    Évaluez la section "Formation" du CV par rapport à la fiche de poste, selon les règles ci-dessus rigoureusement et strictement.
    Fournissez une note sur 10 avec une explication concise mais précise.
    Veillez à développer brièvement votre raisonnement (chain-of-thought) pour justifier la note.

    ### Exemples de sortie attendue :

    **Exemple 1**:
    <formation_explication>
    Le candidat a obtenu un Master en Informatique, correspondant au niveau minimum requis (Licence) dans le même domaine.
    L’établissement est reconnu et il dispose d’une certification Scrum Master en rapport direct avec le poste.
    Tout est conforme aux exigences.
    </formation_explication>
    <note_explication>
    Diplome : 5/5
    Etablissement : 3/3
    Certifications : 2/2
    </note_explication>
    <note_formation> 10 </note_formation>

    **Exemple 2**:
    <formation_explication>
    Le candidat mentionne un BTS en Marketing alors que le poste requiert un diplôme en Data Science de niveau Master.
    Le diplôme n’est pas cohérent avec le domaine ni le niveau requis.
    Aucune certification pertinente n’est mentionnée.
    </formation_explication>
    <note_explication>
    Diplome : 0/5
    Etablissement : 0/3
    Certifications : 0/2
    </note_explication>
    <note_formation> 0 </note_formation>

    ### Réponse :
    <formation_explication>
    {{développer le raisonnement pour noter la formation selon les règles en étant bref mais précis}}
    </formation_explication>
    <note_explication>
    {{détaillez la répartition des points : Diplome : x/5, Etablissement : x/3, Certifications : x/2}}
    </note_explication>
    <note_formation>
    {{mets ici uniquement la note de la formation sur 10, sans détails supplémentaires}}
    </note_formation>
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
    1. Nombre d'années d'expérience minimum (5 ou 0 points) :
       - 5 points : si le nombre précis des mois d'expériences en rapport avec le domaine (hors stage) est égal ou supérieur au minimum requis.
       - 0 point : si inférieur

    2. Cohérence des expériences (2 ou 1 ou 0 points) :
       - 2 points : Si la durée moyenne des expériences pertinentes est de 2 ans minimum.
       - 1 point : Si la durée moyenne est entre 1 et 2 ans.
       - 0 point : Si plusieurs postes montrent une instabilité manifeste (moins de 1 an).

    3. Bonus pour réalisations significatives (3 ou 2 ou 1 points) :
       - 3 points : Réalisations spécifiques, mesurables et parfaitement alignées avec les attentes du poste.
       - 2 points : Réalisations pertinentes mais manquant de détails ou non chiffrées.
       - 1 point : Réalisations pertinentes provenant principalement des projets.

    ### Tâche :
    Évaluez la section "Expériences Professionnelles" du CV par rapport à la fiche de poste, selon les règles ci-dessus.
    Fournissez une note sur 10 avec une explication concise mais précise.
    Veillez à développer brièvement votre raisonnement (chain-of-thought) pour justifier la note.

    ### Exemples de sortie attendue :

    **Exemple 1 :**
    <xp_professionnelles_explication>
    Le candidat possède 7 ans d’expérience en Data Science, dont 5 ans spécifiquement en Machine Learning,
    ce qui répond parfaitement aux exigences minimales du poste.
    Ses différentes expériences sont cohérentes, avec une durée moyenne de 2,5 ans par poste,
    démontrant une stabilité et une progression logique.
    Enfin, le CV met en avant plusieurs réalisations significatives et chiffrées, telles que
    l’optimisation d’un modèle de détection d’anomalies ayant réduit les faux positifs de 30 %,
    ainsi que le déploiement d’un pipeline MLOps en production.
    </xp_professionnelles_explication>
    <note_explication>
    Expérience : 5/5
    Cohérence : 2/2
    Bonus : 3/3
    </note_explication>
    <note_xp_professionnelles> 10 </note_xp_professionnelles>

    **Exemple 2 :**
    <xp_professionnelles_explication>
    Le candidat dispose de 6 ans d’expérience en développement et machine learning,
    répondant aux exigences du poste.
    Cependant, ses expériences sont marquées par des transitions fréquentes,
    avec une durée moyenne de 1,5 an par poste, ce qui réduit la cohérence.
    Les réalisations mentionnées sont pertinentes mais restent générales et peu chiffrées,
    par exemple « amélioration des modèles de classification » sans précision sur l’impact
    ou les métriques obtenues.
    </xp_professionnelles_explication>
    <note_explication>
    Expérience : 5/5
    Cohérence : 1/2
    Bonus : 2/3
    </note_explication>
    <note_xp_professionnelles> 8 </note_xp_professionnelles>

    **Exemple 3 :**
    <xp_professionnelles_explication>
    Le candidat possède 3 ans d’expérience en Data Science, ce qui est en deçà
    des exigences minimales du poste.
    Les expériences sont relativement cohérentes, avec des durées moyennes de 2 ans,
    montrant une certaine stabilité.
    Le CV présente quelques réalisations pertinentes, comme l’entraînement d’un modèle
    de recommandation utilisé en production, mais manque de détails chiffrés.
    </xp_professionnelles_explication>
    <note_explication>
    Expérience : 3/5
    Cohérence : 2/2
    Bonus : 2/3
    </note_explication>
    <note_xp_professionnelles> 7 </note_xp_professionnelles>

    **Exemple 4 :**
    <xp_professionnelles_explication>
    Le candidat a accumulé 2 ans d’expérience, principalement en développement FullStack,
    avec seulement 6 mois en Data Science, ce qui est largement insuffisant
    par rapport aux attentes du poste.
    Les transitions fréquentes entre différents domaines et postes montrent un manque de cohérence,
    avec une durée moyenne de moins d’un an.
    Les réalisations mentionnées sont principalement issues de projets personnels ou académiques,
    avec peu d’impact démontré dans un cadre professionnel.
    </xp_professionnelles_explication>
    <note_explication>
    Expérience : 2/5
    Cohérence : 0/2
    Bonus : 1/3
    </note_explication>
    <note_xp_professionnelles> 3 </note_xp_professionnelles>

    **Exemple 5 :**
    <xp_professionnelles_explication>
    Le candidat a 5 ans d’expérience en Data Science et Machine Learning,
    répondant tout juste aux critères du poste.
    Ses expériences sont cohérentes, avec une moyenne de 2 ans par poste.
    Cependant, les réalisations mentionnées sont trop générales et manquent
    d’exemples concrets d’impact business ou technique, ce qui limite leur valeur.
    </xp_professionnelles_explication>
    <note_explication>
    Expérience : 5/5
    Cohérence : 2/2
    Bonus : 1/3
    </note_explication>
    <note_xp_professionnelles> 8 </note_xp_professionnelles>

    ### Réponse :
    <xp_professionnelles_explication>
    {{développer le raisonnement pour noter les expériences selon les règles en étant bref mais précis}}
    </xp_professionnelles_explication>
    <note_explication>
    {{détaillez la répartition des points : Expérience : x/5, Cohérence : x/2, Bonus : x/3}}
    </note_explication>
    <note_xp_professionnelles>
    {{mets ici uniquement la note des expériences sur 10, sans détails supplémentaires}}
    </note_xp_professionnelles>
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
    1. Vérifier si la compétence technique est mentionnée ou déduite (7 ou 4 ou 0 points) :
       - 7 points : la compétence est explicitement mentionnée.
       - 4 points : la compétence n'est pas explicitement mentionnée mais peut être déduite (à partir d'expériences ou projets).
       - 0 point : la compétence n'est ni mentionnée ni déduite.

    2. Évaluer l'utilisation de la compétence dans les expériences (3 ou 0 points) :
       - 3 points : la compétence est effectivement utilisée (c’est-à-dire décrite dans une ou plusieurs expériences professionnelles).
       - 0 point : la compétence n'est pas utilisée dans les expériences.

    ### Tâche :
    - Évaluez chaque compétence de la fiche de poste en appliquant ces règles.
    - Fournissez une note individuelle sur 10 pour chaque compétence (mention/déduction + utilisation).
    - Calculez la moyenne de ces notes pour donner la note globale sur 10, sans l'arrondir.

    ### Exemples de sortie attendue :

    **Exemple 1**:
    <hard_skills_explication>
    - SQL : n'est pas explicitement mentionnée dans le CV, mais elle peut être déduite de son expérience 
      en tant que Data Analyst où il a manipulé des bases de données relationnelles. De plus, il l'a 
      utilisée dans un projet interne de reporting automatisé.

    - JavaScript : la compétence est bien mentionnée dans la section « Compétences Techniques », 
      mais aucune mission ne prouve son utilisation concrète dans les expériences professionnelles.

    - Docker : ni mentionné ni déductible d'une expérience ; aucune trace de conteneurisation 
      ou déploiement l'impliquant.
    </hard_skills_explication>
    <note_explication>
    SQL: 10
    JavaScript: 7
    Docker: 0
    </note_explication>
    <note_hard_skills> 5.6667 </note_hard_skills>

    **Exemple 2**:
    <hard_skills_explication>
    - Machine Learning : compétence explicitement mentionnée dans la liste des hard skills. 
      Elle est également utilisée dans plusieurs expériences (entraînement de modèles de classification, 
      projets d’analyse prédictive en production).

    - Cloud Computing : pas explicitement listé, mais peut être déduit de son poste d’Ingénieur DevOps 
      mentionnant l’utilisation d’AWS. Il a mis en place des pipelines CI/CD sur cette plateforme, 
      prouvant l’usage concret du Cloud.
    </hard_skills_explication>
    <note_explication>
    Machine Learning: 10
    Cloud Computing: 7
    </note_explication>
    <note_hard_skills> 8.5 </note_hard_skills>

    ### Réponse :
    <hard_skills_explication>
    {{Pour chaque compétence requise, détaillez si elle est mentionnée, déduite ou absente, 
    puis précisez si elle est réellement utilisée dans une ou plusieurs expériences (en mentionnant lesquelles). 
    Soyez bref, précis et structuré.}}
    </hard_skills_explication>

    <note_explication>
    {{Indiquez la note de chaque compétence, sans autre commentaire. 
    Ex. : 
    CompétenceA: 10
    CompétenceB: 4
    CompétenceC: 7}}
    </note_explication>

    <note_hard_skills>
    {{Faites la moyenne des notes individuelles, sans arrondir, et retournez seulement cette valeur.}}
    </note_hard_skills>
    """



def generate_soft_skills_prompt(cv_soft_skills, jd_soft_skills, cv_experiences):
    """
    Génère le prompt pour la section Soft Skills.
    """
    return f"""
    **Fiche de poste**
    - **Soft skills requises :** {jd_soft_skills}

    **CV**
    - **Soft Skills mentionnées :** {cv_soft_skills}
    - **Expériences professionnelles :** {cv_experiences}

    ### Règles d’évaluation :
    1. Vérifier si la soft skill est mentionnée ou déduite (7 ou 4 ou 0 points) :
       - 7 points : la compétence comportementale est explicitement mentionnée (ex. “Excellente communication”).
       - 4 points : la compétence n'est pas explicitement mentionnée, mais peut être déduite 
                    d’autres éléments du CV (ex. postes/managers indiquant du leadership).
       - 0 point : la compétence n'est ni mentionnée ni déduite.

    2. Évaluer l'utilisation de la soft skill dans les expériences (3 ou 0 points) :
       - 3 points : la compétence est concrètement mise en pratique dans une ou plusieurs expériences 
                    (ex. cas de gestion de conflit, projet d’équipe, prise de parole en public...).
       - 0 point : aucune expérience ne prouve l'usage effectif de cette soft skill.

    ### Tâche :
    - Évaluez chaque soft skill mentionnée dans la fiche de poste, en appliquant ces règles.
    - Fournissez une note individuelle sur 10 pour chacune (mention/déduction + utilisation).
    - Calculez la moyenne de ces notes pour en déduire la note globale sur 10, sans arrondir.

    ### Exemples de sortie attendue :

    **Exemple 1**:
    <soft_skills_explication>
    - Communication : explicitement mentionnée dans la liste des soft skills,
      et confirmée par l'expérience de porte-parole sur un projet client.
    - Leadership : compétence non explicitement listée, mais déduite de son rôle de chef d’équipe 
      (5 personnes) sur un projet inter-service. 
      Utilisation confirmée par la réussite du projet sous sa supervision.
    </soft_skills_explication>
    <note_explication>
    Communication: 10
    Leadership: 10
    </note_explication>
    <note_soft_skills> 10 </note_soft_skills>

    **Exemple 2**:
    <soft_skills_explication>
    - Collaboration / Esprit d'équipe : mentionnée dans le CV, mais aucune expérience 
      ne montre son usage pratique (pas d’exemple de projet en équipe).
    - Adaptabilité : ni mentionnée ni déductible, aucune situation professionnelle décrite 
      où il a dû s’adapter à un changement majeur.
    </soft_skills_explication>
    <note_explication>
    Collaboration: 7
    Adaptabilité: 0
    </note_explication>
    <note_soft_skills> 3.5 </note_soft_skills>

    **Exemple 3**:
    <soft_skills_explication>
    - Résolution de problèmes : non listée dans les soft skills, mais déduite de son expérience 
      en tant que référent pour gérer des incidents critiques sur un système de production.
      Les exemples concrets cités (analyse de bugs, coordination avec l’équipe de développement)
      confirment qu’il utilise cette compétence.
    - Communication : explicitement mentionnée, mais aucune expérience ne démontre un usage clair 
      (pas de présentation, d’animation d’atelier, etc.).
    </soft_skills_explication>
    <note_explication>
    Résolution de problèmes: 7
    Communication: 7
    </note_explication>
    <note_soft_skills> 7 </note_soft_skills>

    ### Réponse :
    <soft_skills_explication>
    {{Pour chaque soft skill requise, détaillez si elle est mentionnée, déduite ou absente, 
    puis précisez si elle est concrètement utilisée dans une ou plusieurs expériences. 
    Restez concis et précis.}}
    </soft_skills_explication>
    <note_explication>
    {{Indiquez simplement la note pour chaque soft skill, par exemple :
    Communication: 10
    Leadership: 4
    ...}}
    </note_explication>
    <note_soft_skills>
    {{Faites la moyenne des notes individuelles (sans arrondir) et retournez seulement cette valeur.}}
    </note_soft_skills>
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
    1. Niveau mentionné (7 ou 4 ou 0 points) :
       - 7 points : la langue est mentionnée avec un niveau intermédiaire ou plus (B2, C1, C2, "Fluent", etc.).
       - 4 points : la langue est mentionnée avec un niveau inférieur à intermédiaire (A1, A2, "Débutant", etc.).
       - 0 point : la langue n'est pas mentionnée du tout.
    2. Certifications (3 ou 0 points) :
       - 3 points : une certification de niveau intermédiaire ou supérieur (TOEIC, TOEFL, DELF B2, Goethe-Zertifikat C2, etc.).
       - 0 point : pas de certification ou certification de niveau inférieur à intermédiaire.

    ### Tâche :
    - Évaluez chaque langue exigée dans la fiche de poste en appliquant ces règles.
    - Fournissez une note individuelle sur 10 (niveau + certification) pour chaque langue.
    - Calculez la moyenne de ces notes pour déterminer la note globale sur 10, sans arrondir.

    ### Exemples de sortie attendue :

    **Exemple 1**:
    <langues_explication>
    L'anglais a été mentionné comme niveau B2. Aucune certification n’est précisée.
    Le candidat a indiqué un niveau A2 en espagnol. Il ne possède aucune certification.
    Le français n’est pas mentionné sur le CV.
    </langues_explication>
    <note_explication>
    Anglais: 7
    Espagnol: 4
    Français: 0
    </note_explication>
    <note_langues> 3.6667 </note_langues> 

    **Exemple 2**:
    <langues_explication>
    L’allemand est mentionné avec un niveau C2, et le candidat détient un Goethe-Zertifikat C2.
    L’italien est mentionné comme « débutant » sans plus de détails. Aucune certification n’est précisée.
    </langues_explication>
    <note_explication>
    Allemand: 10
    Italien: 4
    </note_explication>
    <note_langues> 7 </note_langues>

    **Exemple 3**:
    <langues_explication>
    L'anglais a été mentionné comme "Fluent". Pas de certification indiquée.
    Le français est mentionné niveau A2, ce qui reste inférieur à B2. 
    Aucune certification n’a été signalée pour ces deux langues.
    </langues_explication>
    <note_explication>
    Anglais: 7
    Français: 4
    </note_explication>
    <note_langues> 5.5 </note_langues> 

    ### Réponse :
    <langues_explication>
    {{Pour chaque langue requise, indiquez le niveau mentionné (ou absence). 
    S’il existe une certification, précisez-la avec son niveau. Restez concis.}}
    </langues_explication>
    <note_explication>
    {{Énumérez la note de chaque langue, par exemple :
    Anglais: 7
    Espagnol: 4
    ...}}
    </note_explication>
    <note_langues>
    {{Calculez la moyenne des notes individuelles, sans arrondir, et retournez uniquement cette valeur.}}
    </note_langues>
    """


