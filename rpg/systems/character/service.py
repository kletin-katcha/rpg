from uuid import uuid4

from rpg.content.loader import load_catalog
from rpg.core.errors import RegraNegocioError
from rpg.core.types import CharacterState

from .rules import BASE_ATTRIBUTES, aplicar_xp


def criar_personagem(nome: str, raca_id: str, classe_id: str) -> CharacterState:
    nome_limpo = nome.strip()
    if not nome_limpo:
        raise RegraNegocioError("Nome do personagem é obrigatório")

    racas = load_catalog("racas")
    classes = load_catalog("classes")

    if raca_id not in racas:
        raise RegraNegocioError(f"Raça inválida: {raca_id}")
    if classe_id not in classes:
        raise RegraNegocioError(f"Classe inválida: {classe_id}")

    atributos = dict(BASE_ATTRIBUTES)
    for atributo, bonus in racas[raca_id].get("bonus", {}).items():
        atributos[atributo] = atributos.get(atributo, 0) + bonus

    return CharacterState(
        id=str(uuid4()),
        nome=nome_limpo,
        nivel=1,
        xp=0,
        atributos=atributos,
        hp_atual=100,
        hp_max=100,
    )


def conceder_xp(personagem: CharacterState, ganho_xp: int) -> CharacterState:
    return aplicar_xp(personagem, ganho_xp)
