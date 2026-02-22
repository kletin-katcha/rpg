from rpg.core.types import CharacterState, EnemyState, CombatContext, CombatResult


def calcular_ataque_personagem(personagem: CharacterState) -> int:
    forca = personagem.atributos.get("forca", 5)
    return max(1, 4 + forca)


def resolver_turno(contexto: CombatContext) -> CombatResult:
    personagem = contexto.personagem
    inimigo = contexto.inimigo

    dano_causado = calcular_ataque_personagem(personagem)
    inimigo.hp_atual = max(0, inimigo.hp_atual - dano_causado)

    dano_recebido = 0
    if inimigo.hp_atual > 0:
        dano_recebido = max(1, inimigo.ataque_base - personagem.atributos.get("constituicao", 5) // 3)
        personagem.hp_atual = max(0, personagem.hp_atual - dano_recebido)

    return CombatResult(
        dano_causado=dano_causado,
        dano_recebido=dano_recebido,
        inimigo_derrotado=inimigo.hp_atual == 0,
        personagem_derrotado=personagem.hp_atual == 0,
    )
