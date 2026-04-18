# agent/installer.py

"""
Dependency installer / healing module.

Handles ONLY external dependencies.
Skips internal modules (domain, application, etc.).
"""

import subprocess
import sys


# Known internal modules (must NEVER be pip-installed)
INTERNAL_MODULE_PREFIXES = (
    "domain",
    "application",
    "infrastructure",
    "api",
    "tests",
)


def install_missing(error: str | None) -> bool:
    """
    Attempt to install missing external dependencies.

    Returns:
        True  → attempted fix
        False → nothing to fix
    """

    if not error:
        return False

    if "No module named" not in error:
        return False

    try:
        pkg = error.split("'")[1]
    except Exception:
        return False

    # --------------------------------------------------------
    # SKIP INTERNAL MODULES
    # --------------------------------------------------------
    if pkg.startswith(INTERNAL_MODULE_PREFIXES):
        print(f"[installer] Skipping internal module: {pkg}")
        return False

    # --------------------------------------------------------
    # INSTALL EXTERNAL PACKAGE
    # --------------------------------------------------------
    print(f"[installer] Installing package: {pkg}")

    subprocess.run(
        [sys.executable, "-m", "pip", "install", pkg],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return True