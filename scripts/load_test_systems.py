from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

"""Teste de carga leve para validar escala de catálogos e loops centrais."""

from time import perf_counter

from rpg.content.loader import load_all_catalogs
from rpg.game import Game


def run() -> dict[str, float]:
    inicio = perf_counter()
    for _ in range(200):
        load_all_catalogs()
    t_catalogos = perf_counter() - inicio

    game = Game()
    game.criar_jogador("Load", "humano", "guerreiro")

    inicio_loop = perf_counter()
    for _ in range(120):
        game.executar_acao_cidade("coletar_item_inicial")
        game.executar_acao_cidade("cacar_lobo")
        game.executar_acao_cidade("descansar")
    t_loop = perf_counter() - inicio_loop

    return {
        "catalogos_200x_s": round(t_catalogos, 4),
        "loop_120x_s": round(t_loop, 4),
    }


def main() -> int:
    resultado = run()
    print(f"load_test: {resultado}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
