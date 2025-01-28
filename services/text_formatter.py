import re

def format_explanation(text):
    """
    Formate une explication brute en HTML en respectant les retours à la ligne et le gras.
    - Convertit `**texte**` en `<strong>texte</strong>`.
    - Respecte les retours à la ligne en ajoutant `<br>`.
    """
    # Convertir `**texte**` en `<strong>texte</strong>`
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)

    # Ajouter des retours à la ligne HTML pour chaque ligne
    text = text.replace("\n", "<br>")

    return text
