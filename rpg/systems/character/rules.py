from rpg.core.types import CharacterState

BASE_ATTRIBUTES = {
    "forca": 5,
    "agilidade": 5,
    "destreza": 5,
    "constituicao": 5,
    "inteligencia": 5,
    "sabedoria": 5,
    "carisma": 5,
    "vitalidade": 5,
    "vontade": 5,
    "percepcao": 5,
    "precisao": 5,
    "resistencia": 5,
    "espirito": 5,
    "sorte": 5,
    "fe": 5,
}


def xp_para_proximo_nivel(nivel_atual: int) -> int:
    return 100 * max(1, nivel_atual)


def aplicar_xp(personagem: CharacterState, ganho_xp: int) -> CharacterState:
    if ganho_xp <= 0:
        return personagem

    personagem.xp += ganho_xp
    while personagem.xp >= xp_para_proximo_nivel(personagem.nivel):
        personagem.xp -= xp_para_proximo_nivel(personagem.nivel)
        personagem.nivel += 1
        personagem.hp_max += 10
        personagem.hp_atual = personagem.hp_max
        personagem.atributos["constituicao"] = personagem.atributos.get("constituicao", 0) + 1
        personagem.atributos["vitalidade"] = personagem.atributos.get("vitalidade", 0) + 1
    return personagem
