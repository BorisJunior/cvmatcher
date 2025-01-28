from services.deepseek_service import call_deepseek_api

prompt = """Voici une fiche de poste brute :

Les missions du poste
Vos missions

Au sein d'Euro-Information, la Data Factory coordonne dans toute la France les travaux autour de la data, depuis sa collecte jusqu'à son analyse et sa restitution, et met ses ressources à disposition de l'ensemble du Groupe.

Basées à Nantes, les équipes Data Science travaillent au sein de la Data Factory et sont chargées pour Crédit Mutuel Alliance Fédérale et ses filiales :
- De l'élaboration des modèles prédictifs dans tous les métiers de la bancassurance,
- De la mise en oeuvre de méthodes avancées en data science pour améliorer la connaissance client et la performance commerciale,
- Du développement des modèles de risque de crédit, de risque de taux et de risques opérationnels dans le cadre de la réglementation bancaire prudentielle,
- Des études sur les sujets de data science,
- De la veille technologique, du conseil, de l'accompagnement, de la formation et la diffusion de bonnes pratiques dans le domaine de la statistique et du machine learning, en ce qui concerne les méthodes théoriques et les outils logiciels.

Au quotidien, vous travaillerez en étroite collaboration avec d'autres métiers de la Data Factory (Machine Learning Engineer, Data Architect, Data Engineer, Data Officer, etc.) mais aussi avec les équipes informatiques et les utilisateurs concernés : Direction Commerciale, Direction des Risques, de la Conformité, Gestion actif-passif, etc.

En évoluant dans ces équipes, vous pourrez être amené(e) à travailler sur tous les sujets traités par elles, dans des activités :
- D'exploration des données et d'analyse des besoins métiers,
- De modélisation par des méthodes variées de statistique et de machine learning,
- D'industrialisation de modèles de machine learning
- D'accompagnement et de support des data scientists métiers du Groupe,
- De réflexion, d'expérimentation et de mise en oeuvre des outils de data science.

Ce que vous allez vivre chez nous
- Télétravail (2 jours par semaine)
- Rémunération fixe versée sur 13 mois
- RTT
- Intéressement, participation et abondement
- Plan épargne entreprise et PERCO
- Contrat de santé collectif
- Prévoyance
- Retraite supplémentaire prise en charge à 100% par l'employeur
- Conditions bancaires et assurances préférentielles
- Politique parentale avantageuse

Ce que nous allons aimer chez vous

Vous avez un diplôme Bac +5 en statistique, data science ou mathématiques appliquées (Master 2, ENSAI, ENSAE, école d'ingénieur).

Vous avez de bonnes connaissances et un fort intérêt pour la statistique, le machine learning et la data science.

Vous maîtrisez Python ou R.

Une bonne pratique de l'anglais est souhaitable.

Vous êtes animé(e) par l'envie de faire parler la donnée.

Vous êtes doté(e) de capacités et de goût pour l'analyse des chiffres et l'investigation.

Vous avez des qualités de persévérance, de rigueur, de précision et de rédaction.

Vous aimez travailler en équipe et communiquer, transmettre vos connaissances.

Vous êtes curieux(se), motivé(e), autonome et vous savez faire preuve d'initiative et de réactivité.


**Tâche** :
Structure cette fiche de poste en suivant impérativement le format suivant et les délimiteurs. Utilise `##` pour délimiter les sections principales. Extrait pour chaque section toutes les informations disponibles dans la fiche de poste. Si une information n’est pas disponible, mentionne "Non mentionné". Respecte la structure suivante :

## Titre_Poste
{Titre exact du poste}

## Domaine
{Indiquer le domaine ou la spécialisation}

## Missions
{Lister les missions et responsabilités en détail.}

## Hard_Skills
{Lister les compétences techniques requises ou valorisées, comme les outils, langages de programmation, frameworks.}

## Soft_Skills
{Lister les qualités ou compétences transversales mentionnées, comme leadership, communication.}

## Langues
{Lister les langues demandées et leur niveau, si mentionné.}

## Formation
{Indiquer le niveau d'études minimum requis}
{Indiquer le domaine ou filière d'études}
{Indiquer les établissements reconnus. Si ce n'est pas indiqué, mettre "non exigé"}

## Xp_Professionnelles
{Indiquer le nombre d'années d'expérience requis, les types de postes ou secteurs d'activité valorisés.}

## Projets
{Lister des projets types ou réalisations exemplaires mentionnées.}

## Certifications
{Lister les certifications ou licences exigées ou valorisées.}

## Autres
{Autres informations}

Fournis la fiche de poste structurée dans ce format.

*Réponse*:
"""
res = call_deepseek_api(prompt)

print(res)