from rpg.content.loader import load_catalog
from rpg.core.errors import RegraNegocioError
from rpg.core.types import CharacterState, EnemyState, CombatContext, CombatResult
from rpg.systems.character.service import conceder_xp
from rpg.systems.inventory.service import adicionar_item_catalogado

from .rules import resolver_turno


def criar_inimigo(monstro_id: str) -> EnemyState:
    monstros = load_catalog("monstros")
    if monstro_id not in monstros:
        raise RegraNegocioError(f"Monstro inválido: {monstro_id}")
    m = monstros[monstro_id]
    return EnemyState(
        id=m["id"],
        nome=m["nome"],
        nivel=m["nivel"],
        hp_atual=m["hp_max"],
        hp_max=m["hp_max"],
        ataque_base=m["ataque_base"],
        velocidade=m.get("velocidade", 5),
        arquetipo=m.get("arquetipo", "agressivo"),
    )


def combater_ate_fim(
    personagem: CharacterState,
    monstro_id: str,
    inventario: dict[str, int],
    mutadores_combate: dict[str, int] | None = None,
) -> dict:
    inimigo = criar_inimigo(monstro_id)
    historico: list[CombatResult] = []
    log_turnos: list[dict] = []

    mutadores_combate = mutadores_combate or {}

    while inimigo.hp_atual > 0 and personagem.hp_atual > 0:
        resultado = resolver_turno(
            CombatContext(
                personagem=personagem,
                inimigo=inimigo,
                bonus_dano_personagem=mutadores_combate.get("bonus_dano_personagem", 0),
                reducao_dano_personagem=mutadores_combate.get("reducao_dano_personagem", 0),
                bonus_dano_inimigo=mutadores_combate.get("bonus_dano_inimigo", 0),
            )
        )
        historico.append(resultado)
        log_turnos.append(
            {
                "turno": len(historico),
                "dano_causado": resultado.dano_causado,
                "dano_recebido": resultado.dano_recebido,
                "hp_personagem": personagem.hp_atual,
                "hp_inimigo": inimigo.hp_atual,
                "inimigo_derrotado": resultado.inimigo_derrotado,
                "personagem_derrotado": resultado.personagem_derrotado,
            }
        )

    recompensa_xp = 0
    recompensa_loot: dict[str, int] = {}
    if inimigo.hp_atual == 0:
        info = load_catalog("monstros")[monstro_id]
        recompensa_xp = info["xp"]
        conceder_xp(personagem, recompensa_xp)
        recompensa_loot = info.get("loot", {})
        for item_id, qtd in recompensa_loot.items():
            adicionar_item_catalogado(inventario, item_id, qtd)

    return {
        "vitoria": inimigo.hp_atual == 0,
        "hp_final_personagem": personagem.hp_atual,
        "xp_recebido": recompensa_xp,
        "loot": recompensa_loot,
        "turnos": len(historico),
        "fase_final_inimigo": inimigo.fase,
        "log_turnos": log_turnos,
    }
