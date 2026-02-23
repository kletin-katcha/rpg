from statistics import mean

from rpg.systems.character.service import criar_personagem
from rpg.systems.combat.service import combater_ate_fim


def simular_rodada_combate(nome: str, raca: str, classe: str, encontros: list[str]) -> dict:
    personagem = criar_personagem(nome, raca, classe)
    inventario: dict[str, int] = {}
    resultados = []

    for monstro_id in encontros:
        out = combater_ate_fim(personagem, monstro_id, inventario)
        resultados.append(out)
        if personagem.hp_atual <= 0:
            break

    turnos = [r["turnos"] for r in resultados]
    xp_total = sum(r["xp_recebido"] for r in resultados)

    return {
        "vitorias": sum(1 for r in resultados if r["vitoria"]),
        "derrotas": sum(1 for r in resultados if not r["vitoria"]),
        "xp_total": xp_total,
        "turno_medio": mean(turnos) if turnos else 0,
        "hp_final": personagem.hp_atual,
        "nivel_final": personagem.nivel,
        "inventario": inventario,
    }


def gerar_relatorio_balance() -> dict:
    base = simular_rodada_combate(
        nome="BalanceBot",
        raca="humano",
        classe="guerreiro",
        encontros=["lobo_cinzento", "lobo_cinzento", "goblin_batedor"],
    )
    return {
        "cenario_base": base,
        "sanidade": {
            "nao_morreu": base["hp_final"] > 0,
            "turno_medio_aceitavel": base["turno_medio"] <= 10,
            "ganhou_xp": base["xp_total"] > 0,
        },
    }
