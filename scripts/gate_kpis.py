from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

"""Gate de KPI para readiness de produção.
Falha com código != 0 quando thresholds mínimos são violados.
"""

from rpg.game import Game
from rpg.systems.expansion import simular_balance_headless


THRESHOLDS = {
    "taxa_vitoria_min": 0.55,
    "hp_final_medio_min": 8,
    "ouro_min_pos_rotina": 300,
}


def coletar_kpis() -> dict[str, float]:
    game = Game()
    game.criar_jogador("KPI", "humano", "guerreiro")
    game.executar_acao_cidade("coletar_item_inicial")
    game.executar_acao_cidade("avancar_dia")
    game.executar_acao_cidade("cacar_lobo")

    sim = simular_balance_headless(30)

    return {
        "taxa_vitoria": float(sim["taxa_vitoria"]),
        "hp_final_medio": float(sim.get("hp_final_medio", 0)),
        "ouro_pos_rotina": float(game.state.cidade.ouro),
    }


def avaliar(kpis: dict[str, float]) -> list[str]:
    erros: list[str] = []
    if kpis["taxa_vitoria"] < THRESHOLDS["taxa_vitoria_min"]:
        erros.append(
            f"taxa_vitoria abaixo do mínimo: {kpis['taxa_vitoria']:.2f} < {THRESHOLDS['taxa_vitoria_min']:.2f}"
        )
    if kpis["hp_final_medio"] < THRESHOLDS["hp_final_medio_min"]:
        erros.append(
            f"hp_final_medio abaixo do mínimo: {kpis['hp_final_medio']:.2f} < {THRESHOLDS['hp_final_medio_min']:.2f}"
        )
    if kpis["ouro_pos_rotina"] < THRESHOLDS["ouro_min_pos_rotina"]:
        erros.append(
            f"ouro_pos_rotina abaixo do mínimo: {kpis['ouro_pos_rotina']:.2f} < {THRESHOLDS['ouro_min_pos_rotina']:.2f}"
        )
    return erros


def main() -> int:
    kpis = coletar_kpis()
    erros = avaliar(kpis)
    print(f"KPI snapshot: {kpis}")
    if erros:
        for erro in erros:
            print(f"KPI FAIL: {erro}")
        return 1
    print("kpi_gate: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
