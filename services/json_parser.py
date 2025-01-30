import re


import re
import json

def parse_to_json(output):
    """
    Convertit une sortie structurée (texte avec des sections `##`) en JSON.
    """
    # Regex pour identifier les sections avec le préfixe '##'
    section_pattern = r"(?:## |\*\*)(.*?)(?:\n|\*\*\n)"

    # Trouver toutes les sections
    sections = re.findall(section_pattern, output)

    # Découper la sortie en lignes pour un traitement plus facile
    lines = output.splitlines()

    # Dictionnaire pour stocker les données structurées
    output_json = {}

    current_section = None

    for line in lines:
        # Si la ligne correspond à un titre de section
        if line.startswith("## "):
            current_section = line[3:].strip()
            output_json[current_section] = ""
        elif line.startswith("##"):
            current_section = line[2:].strip()
            output_json[current_section] = ""
        elif line.startswith("**"):
            current_section = line[2:-2].strip()
            output_json[current_section] = ""
        # Sinon, ajouter le contenu à la section actuelle
        elif current_section:
            output_json[current_section] += line.strip("*+\t") + "\n"

    # Nettoyage des espaces supplémentaires dans le contenu des sections
    for section in output_json:
        output_json[section] = output_json[section].strip()


    json_info = {}
    if section == "Json_info":
        try:
            json_info = json.loads(output_json[section])
        except:
            pass

    return output_json, json_info

# def parse_to_json(output):
#     """
#     Convertit une sortie structurée (texte avec des sections `##`) en JSON.
#     """
#     # Regex pour identifier les sections avec le préfixe '##'
#     section_pattern = r"## (.*?)\n"

#     # Trouver toutes les sections
#     sections = re.findall(section_pattern, output)

#     # Découper la sortie en lignes pour un traitement plus facile
#     lines = output.splitlines()

#     # Dictionnaire pour stocker les données structurées
#     output_json = {}

#     current_section = None

#     for line in lines:
#         # Si la ligne correspond à un titre de section
#         if line.startswith("## "):
#             current_section = line[3:].strip()
#             output_json[current_section] = ""
#         # Sinon, ajouter le contenu à la section actuelle
#         elif current_section:
#             output_json[current_section] += line + "\n"

#     # Nettoyage des espaces supplémentaires dans le contenu des sections
#     for section in output_json:
#         output_json[section] = output_json[section].strip()

#     return output_json
