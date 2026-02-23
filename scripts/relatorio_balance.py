from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from rpg.systems.balance import gerar_relatorio_balance


if __name__ == "__main__":
    r = gerar_relatorio_balance()
    print("Relatório de Balanceamento (Fase 5)")
    print(r)
