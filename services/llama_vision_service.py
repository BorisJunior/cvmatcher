from together import Together
import base64

def encode_image(image_path: str) -> str:
    """Encode une image en base64"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def generate_vision_response(prompt: str, image_path: str) -> str:
    """
    Version améliorée avec :
    - Encodage base64 de l'image
    - Streamming des résultats
    - Gestion du format de réponse
    """
    client = Together(api_key='**************************')
    
    # Préparation du payload
    messages = [{
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encode_image(image_path)}"
                }
            }
        ]
    }]

    # Configuration de l'appel API
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
        messages=messages,
        temperature=0.3,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>", "<|eom_id|>"],
        stream=False
    )

    return response.choices[0].message.content
