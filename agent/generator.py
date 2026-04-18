# agent/generator.py

"""
Code generation module.

Generates a full repository as JSON.
"""

from openai import OpenAI
from .config import MODEL, GOAL

client = OpenAI()


def generate_repo(error: str | None = None) -> str:
    prompt = build_prompt(GOAL, error)

    response = client.responses.create(
        model=MODEL,
        input=prompt,
    )

    return response.output_text


def build_prompt(goal: str, error: str | None) -> str:
    return f"""
You are an autonomous coding agent.

Goal:
{goal}

CRITICAL REQUIREMENTS:

- Return ONLY valid JSON (no markdown, no explanations)
- All files must be included
- Project must run with:
    python -m api.main
- Use proper Python package imports
- DO NOT use sys.path hacks
- All directories must include __init__.py
- Imports must work as package imports (e.g., from domain.models import Note)

Architecture:
- domain/
- application/
- infrastructure/
- api/
- tests/

Testing:
- Use pytest
- Use fastapi.testclient.TestClient
- Tests must pass

Dependencies:
- fastapi
- uvicorn
- sqlite3 (standard library)

Previous error:
{error}

Output format:
{{
  "api/main.py": "...",
  "domain/models.py": "...",
  "tests/test_notes.py": "..."
}}
"""