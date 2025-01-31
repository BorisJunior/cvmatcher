from together import Together
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

def call_deepseek_api(prompt: str):
    url = "https://api.fireworks.ai/inference/v1/chat/completions"
    payload = {
    "model": "accounts/fireworks/models/deepseek-v3",
    "max_tokens": 16384,
    "top_p": 1,
    "top_k": 40,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "temperature": 0.6,
    "messages": [
        {
        "role": "user",
        "content": prompt
        }
    ]
    }
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer *********"
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
        
    else:
        # Handle the case where the API call was not successful
        raise Exception(f"API call failed with status code {response.status_code}: {response.text}")



""" def call_deepseek_api(prompt: str):
    url = "http://localhost:11434/api/generate"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json.dumps(data), headers=headers)
    
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json()
        
        # Extract the response text
        response_text = response_data.get("response", "")
        
        # Filter out the <think> tags and their content
        filtered_response = ""
        in_think_tag = False
        for line in response_text.splitlines():
            if line.startswith("<think>"):
                in_think_tag = True
            elif line.startswith("</think>"):
                in_think_tag = False
            elif not in_think_tag:
                filtered_response += line + "\n"
        
        # Strip any leading/trailing whitespace and return the filtered response
        return filtered_response.strip()
    
    else:
        # Handle the case where the API call was not successful
        raise Exception(f"API call failed with status code {response.status_code}: {response.text}") """


# def call_deepseek_api(prompt: str):
#     """
#     Version améliorée avec :
#     - Encodage base64 de l'image
#     - Streamming des résultats
#     - Gestion du format de réponse
#     """
#     client = Together(api_key=os.getenv("TOGETHER_AI_API_KEY"))
    
#     # Préparation du payload
#     messages = [{
#         "role": "user",
#         "content": prompt
#     }]

#     # Configuration de l'appel API
#     response = client.chat.completions.create(
#         model="deepseek-ai/DeepSeek-V3",
#         messages=messages,
#         temperature=0.1,
#         top_p=0.7,
#         top_k=50,
#         repetition_penalty=1,
#         stop=["<|eot_id|>", "<|eom_id|>"],
#         stream=False
#     )

#     return response.choices[0].message.content



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


