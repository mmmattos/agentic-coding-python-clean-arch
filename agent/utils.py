# agent/utils.py

"""
Utility functions for the agent.

Provides:
- filesystem helpers
- process cleanup (port handling)
"""

import os
import subprocess
from .config import WORKDIR, PORT


# ============================================================
# FILE SYSTEM
# ============================================================

def write_files(file_map: dict):
    """
    Write generated files to disk.

    Args:
        file_map (dict):
            Mapping of file paths → file contents
            Example:
                {
                    "api/main.py": "...",
                    "domain/models.py": "..."
                }

    Behavior:
        - Creates directories as needed
        - Overwrites files on each attempt
    """

    for path, content in file_map.items():
        full_path = os.path.join(WORKDIR, path)

        # Ensure directory exists
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w") as f:
            f.write(content)


# ============================================================
# PROCESS / PORT MANAGEMENT
# ============================================================

def clean_port():
    """
    Kill any process using the configured port.

    Prevents conflicts between agent iterations
    (e.g., previous run still holding port 8000).
    """

    try:
        subprocess.run(
            f"lsof -ti :{PORT} | xargs kill -9",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except Exception:
        # Silently ignore failures (non-critical)
        pass