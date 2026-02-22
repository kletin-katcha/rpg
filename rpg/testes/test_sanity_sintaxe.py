"""Teste de sanidade para garantir ausência de SyntaxError no repositório."""

import subprocess
import sys
import unittest
from pathlib import Path


class TestSanitySintaxe(unittest.TestCase):
    def test_verificacao_sintaxe_repositorio(self):
        raiz = Path(__file__).resolve().parents[2]
        script = raiz / "scripts" / "verificar_sintaxe.py"
        resultado = subprocess.run(
            [sys.executable, str(script)],
            cwd=raiz,
            check=False,
            capture_output=True,
            text=True,
        )
        if resultado.returncode != 0:
            self.fail(f"Validação de sintaxe falhou:\nSTDOUT:\n{resultado.stdout}\nSTDERR:\n{resultado.stderr}")


if __name__ == "__main__":
    unittest.main()
