# agent/main.py

"""
Main entrypoint for the autonomous coding agent.

This module orchestrates the full agent loop:

    generate → run → test → fix

The agent:
- generates a repository from a goal
- executes the application
- validates correctness via pytest
- feeds errors back into the model
- repeats until success or max attempts
"""

import json

from .config import GOAL, MAX_ATTEMPTS
from .generator import generate_repo
from .executor import run_app, stop_app
from .tester import run_tests
from .installer import install_missing
from .utils import clean_port, write_files


def main():
    """
    Run the autonomous agent loop.
    """

    # --------------------------------------------------------
    # PREPARE ENVIRONMENT
    # --------------------------------------------------------
    clean_port()

    error = None

    # --------------------------------------------------------
    # AGENT LOOP
    # --------------------------------------------------------
    for attempt in range(MAX_ATTEMPTS):

        print(f"\n--- Attempt {attempt + 1} ---")

        # ----------------------------------------------------
        # STEP 1: GENERATE REPOSITORY
        # ----------------------------------------------------
        raw = generate_repo(error)

        try:
            file_map = json.loads(raw)
        except Exception:
            error = "Invalid JSON output from model"
            continue

        # ----------------------------------------------------
        # STEP 2: WRITE FILES
        # ----------------------------------------------------
        write_files(file_map)

        # ----------------------------------------------------
        # STEP 3: RUN APPLICATION
        # ----------------------------------------------------
        success, process, run_error = run_app()

        if not success:
            if install_missing(run_error):
                error = run_error
                continue

            error = run_error
            continue

        # ----------------------------------------------------
        # STEP 4: VALIDATE (PYTEST)
        # ----------------------------------------------------
        test_ok, test_error = run_tests()

        # Always stop the running app
        stop_app(process)

        if test_ok:
            print("\nSUCCESS: All tests passed. System is valid.")
            break

        # ----------------------------------------------------
        # STEP 5: SELF-HEALING LOOP
        # ----------------------------------------------------
        if install_missing(test_error):
            error = test_error
            continue

        # Feed test failure back into next generation
        error = test_error


# ============================================================
# CLI ENTRYPOINT
# ============================================================

if __name__ == "__main__":
    main()