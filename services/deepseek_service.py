import requests
import os

DEEPSEEK_API_KEY = "sk-***************************"
DEEPSEEK_API_URL = 'https://api.deepseek.com/chat/completions'

def call_deepseek_api(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {DEEPSEEK_API_KEY}',
    }
    data = {
        'model': 'deepseek-chat',
        'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': prompt},
        ],
        'temperature' : 0.3,
        'stream': False,
    }
    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']


