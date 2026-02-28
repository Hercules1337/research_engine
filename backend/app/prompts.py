# backend/app/prompts.py

# Example worker prompt template
WORKER_PROMPT_TEMPLATE = """
You are a research assistant AI.
Given the query below, provide a clear, concise answer with facts where possible.

Query:
{query}
"""

# Example judge prompt template
JUDGE_PROMPT_TEMPLATE = """
You are the judge AI.
Compare the answers from multiple worker AIs below.
1. Identify similarities.
2. Identify discrepancies.
3. Summarize the overall findings clearly.

Worker outputs:
{worker_outputs}

Provide a structured JSON with keys:
- summary
- similarities
- discrepancies
"""
