from together import Together
from dotenv import load_dotenv
import os

load_dotenv()

def call_deepseek_api(prompt: str):
    """
    Version améliorée avec :
    - Encodage base64 de l'image
    - Streamming des résultats
    - Gestion du format de réponse
    """
    client = Together(api_key=os.getenv("DEEPSEEK_API_KEY"))
    
    # Préparation du payload
    messages = [{
        "role": "user",
        "content": prompt
    }]

    # Configuration de l'appel API
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=messages,
        temperature=0.1,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>", "<|eom_id|>"],
        stream=False
    )

    return response.choices[0].message.content


# import requests
# import os

# DEEPSEEK_API_KEY = "sk-***************************"
# DEEPSEEK_API_URL = 'https://api.deepseek.com/chat/completions'

# def call_deepseek_api(prompt):
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {DEEPSEEK_API_KEY}',
#     }
#     data = {
#         'model': 'deepseek-chat',
#         'messages': [
#             {'role': 'system', 'content': 'You are a helpful assistant.'},
#             {'role': 'user', 'content': prompt},
#         ],
#         'temperature' : 0.3,
#         'stream': False,
#     }
#     response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
#     response.raise_for_status()
#     return response.json()['choices'][0]['message']['content']


