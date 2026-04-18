# agent/tester.py

"""
Testing module.

Responsible for:
- executing pytest inside the generated project
- returning structured success/failure results
- acting as the PRIMARY validation mechanism
"""

import subprocess
import sys
from .config import WORKDIR


def run_tests():
    """
    Execute pytest in the generated project.

    This is the PRIMARY validation step of the agent.

    Returns:
        (bool, str):
            - success flag (True if all tests pass)
            - error output (stdout + stderr if failure)

    Behavior:
        - Runs pytest in the generated project directory
        - Captures output for debugging and feedback loop
        - Does NOT raise exceptions (agent handles flow)
    """

    result = subprocess.run(
        [sys.executable, "-m", "pytest"],
        cwd=WORKDIR,
        capture_output=True,
        text=True
    )

    # --------------------------------------------------------
    # SUCCESS CASE
    # --------------------------------------------------------
    if result.returncode == 0:
        return True, ""

    # --------------------------------------------------------
    # FAILURE CASE
    # --------------------------------------------------------
    error_output = result.stdout + "\n" + result.stderr

    return False, error_output


# ============================================================
# OPTIONAL: DEBUG HELPER
# ============================================================

def run_tests_verbose():
    """
    Run pytest with live output (useful for debugging the agent itself).

    Not used in the main loop, but helpful during development.
    """

    subprocess.run(
        [sys.executable, "-m", "pytest", "-v"],
        cwd=WORKDIR
    )