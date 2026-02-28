# backend/app/utils.py

import requests
from config import OLLAMA_URL, MAX_TOKENS

def call_ollama_model(model_name: str, prompt: str) -> str:
    """
    Calls a local Ollama model and returns its response.
    """
    url = f"{OLLAMA_URL}/v1/completions"
    data = {
        "model": model_name,
        "prompt": prompt,
        "max_tokens": MAX_TOKENS,
    }
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()["completion"]
    except Exception as e:
        return f"Error calling model {model_name}: {str(e)}"
