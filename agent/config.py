# agent/config.py

"""
Central configuration for the agent.

This file defines:
- project paths
- generation goal
- model configuration
- execution parameters
"""

import os

# ============================================================
# PATHS
# ============================================================

WORKDIR = "project_agent_coded_python_clean_arch"

# Ensure directory exists
os.makedirs(WORKDIR, exist_ok=True)

# ============================================================
# AGENT GOAL
# ============================================================

GOAL = """
Build a Clean Architecture notes REST API in Python.

Structure:
- domain/models.py
- application/services.py
- infrastructure/db.py
- api/main.py
- tests/test_notes.py

Requirements:
- Use FastAPI
- Use SQLite
- POST /notes
- GET /notes
- Include pytest tests
- Must run with: python api/main.py
"""

# ============================================================
# MODEL CONFIG
# ============================================================

MODEL = "gpt-4.1-mini"

# ============================================================
# EXECUTION SETTINGS
# ============================================================

MAX_ATTEMPTS = 5
SERVER_START_DELAY = 3  # seconds
PORT = 8000