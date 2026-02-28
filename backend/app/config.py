# backend/app/config.py

import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Ollama server URL
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

# Worker and judge model names
WORKER_MODELS = [
    os.getenv("WORKER_MODEL_1", "llama3-8b"),
    os.getenv("WORKER_MODEL_2", "mistral-7b"),
    os.getenv("WORKER_MODEL_3", "mixtral-8x7b"),
    os.getenv("WORKER_MODEL_4", "deepseek-7b")
]

JUDGE_MODEL = os.getenv("JUDGE_MODEL", "llama3-34b")

# Temperature settings
WORKER_TEMP = float(os.getenv("WORKER_TEMP", 0.7))  # creative responses
JUDGE_TEMP = float(os.getenv("JUDGE_TEMP", 0.3))    # factual

# Max tokens per response
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1024))

# Optional logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
