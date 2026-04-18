# agent/executor.py

"""
Execution module.

Runs the generated API using module mode:
    python -m api.main

This ensures proper package imports.
"""

import subprocess
import sys
import time
from .config import WORKDIR, SERVER_START_DELAY


def run_app():
    """
    Start the generated application.

    Returns:
        (success, process, error)
    """

    process = subprocess.Popen(
        [sys.executable, "-m", "api.main"],
        cwd=WORKDIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    time.sleep(SERVER_START_DELAY)

    if process.poll() is None:
        return True, process, ""

    stdout, stderr = process.communicate()
    return False, None, stderr or stdout


def stop_app(process):
    if not process:
        return

    try:
        process.terminate()
        process.wait(timeout=2)
    except Exception:
        process.kill()