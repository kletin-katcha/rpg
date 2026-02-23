from rpg.core.types import CharacterState, EnemyState, CombatContext, CombatResult


def calcular_ataque_personagem(personagem: CharacterState) -> int:
    forca = personagem.atributos.get("forca", 5)
    return max(1, 4 + forca)


def _calcular_ataque_inimigo(inimigo: EnemyState) -> int:
    bonus = 0
    if inimigo.arquetipo == "agressivo":
        bonus = 2
    elif inimigo.arquetipo == "defensivo":
        bonus = 1
    elif inimigo.arquetipo == "boss" and inimigo.fase >= 2:
        bonus = 3
    return inimigo.ataque_base + bonus


def _aplicar_fase_boss(inimigo: EnemyState) -> None:
    if inimigo.arquetipo == "boss" and inimigo.fase == 1 and inimigo.hp_atual <= inimigo.hp_max // 2:
        inimigo.fase = 2


def resolver_turno(contexto: CombatContext) -> CombatResult:
    personagem = contexto.personagem
    inimigo = contexto.inimigo

    dano_causado = 0
    dano_recebido = 0

    velocidade_personagem = personagem.atributos.get("destreza", 5)
    personagem_ataca_primeiro = velocidade_personagem >= inimigo.velocidade

    def ataque_inimigo() -> int:
        dano = max(
            1,
            _calcular_ataque_inimigo(inimigo)
            + contexto.bonus_dano_inimigo
            - personagem.atributos.get("constituicao", 5) // 3
            - contexto.reducao_dano_personagem,
        )
        if inimigo.arquetipo == "venenoso":
            dano += 1
        personagem.hp_atual = max(0, personagem.hp_atual - dano)
        return dano

    def ataque_personagem() -> int:
        dano_base = calcular_ataque_personagem(personagem) + contexto.bonus_dano_personagem
        if inimigo.arquetipo == "defensivo":
            dano_base = max(1, dano_base - 1)
        inimigo.hp_atual = max(0, inimigo.hp_atual - dano_base)
        _aplicar_fase_boss(inimigo)
        return dano_base

    if personagem_ataca_primeiro:
        dano_causado = ataque_personagem()
        if inimigo.hp_atual > 0:
            dano_recebido = ataque_inimigo()
    else:
        dano_recebido = ataque_inimigo()
        if personagem.hp_atual > 0:
            dano_causado = ataque_personagem()

    return CombatResult(
        dano_causado=dano_causado,
        dano_recebido=dano_recebido,
        inimigo_derrotado=inimigo.hp_atual == 0,
        personagem_derrotado=personagem.hp_atual == 0,
    )
