"""Pipeline local único para validações essenciais do projeto."""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

CMDS = [
    [sys.executable, "scripts/verificar_sintaxe.py"],
    [sys.executable, "scripts/validar_content.py"],
    [sys.executable, "scripts/validar_referencias_content.py"],
    [sys.executable, "-m", "unittest", "discover", "tests"],
    [sys.executable, "scripts/relatorio_balance.py"],
    [sys.executable, "scripts/gate_kpis.py"],
    [sys.executable, "scripts/load_test_systems.py"],
]


if __name__ == "__main__":
    for cmd in CMDS:
        print("$", " ".join(cmd))
        result = subprocess.run(cmd, cwd=ROOT)
        if result.returncode != 0:
            raise SystemExit(result.returncode)
    print("check_all: OK")
