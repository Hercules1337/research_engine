# backend/app/config.py

# Ollama URL
OLLAMA_URL = "http://localhost:11434"

# Worker models
WORKER_MODELS = [
    "llama3-8b",
    "mistral-7b",
    "mixtral-8x7b",
    "deepseek-7b"
]

# Judge model
JUDGE_MODEL = "llama3-34b"

# Temperature settings
WORKER_TEMP = 0.7   # more creative responses
JUDGE_TEMP = 0.3    # factual, precise

# Max tokens for LLM responses
MAX_TOKENS = 1024
