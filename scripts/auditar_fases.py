"""Checklist rápido para auditoria de cobertura funcional por fases (1-25)."""

from __future__ import annotations

import subprocess
import sys


CHECKS = [
    [sys.executable, "-m", "unittest", "tests/test_phase1_game_flow.py"],
    [sys.executable, "-m", "unittest", "tests/systems/test_phase12_advanced_combat.py"],
    [sys.executable, "-m", "unittest", "tests/systems/test_phase15_world_director.py"],
    [sys.executable, "-m", "unittest", "tests/systems/test_phase20_urban_crisis.py"],
    [sys.executable, "-m", "unittest", "tests/systems/test_phase21_25_expansion_suite.py"],
    [sys.executable, "-m", "unittest", "tests/systems/test_phase21_25_diagnostics.py"],
    [sys.executable, "-m", "unittest", "tests/systems/test_phase1_25_end_to_end.py"],
]


def main() -> int:
    for cmd in CHECKS:
        print("$", " ".join(cmd))
        proc = subprocess.run(cmd)
        if proc.returncode != 0:
            return proc.returncode

    print("auditar_fases: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
