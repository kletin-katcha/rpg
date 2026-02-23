from uuid import uuid4

from rpg.content.loader import load_catalog
from rpg.core.errors import RegraNegocioError
from rpg.core.types import CharacterState

from .rules import BASE_ATTRIBUTES, aplicar_xp


def sub_racas_por_raca(raca_id: str) -> dict[str, dict]:
    sub_racas = load_catalog("sub_racas")
    return {sid: s for sid, s in sub_racas.items() if s["raca_id"] == raca_id}


def criar_personagem(nome: str, raca_id: str, classe_id: str, sub_raca_id: str | None = None) -> CharacterState:
    nome_limpo = nome.strip()
    if not nome_limpo:
        raise RegraNegocioError("Nome do personagem é obrigatório")

    racas = load_catalog("racas")
    classes = load_catalog("classes")

    if raca_id not in racas:
        raise RegraNegocioError(f"Raça inválida: {raca_id}")
    if classe_id not in classes:
        raise RegraNegocioError(f"Classe inválida: {classe_id}")

    opcoes_sub_raca = sub_racas_por_raca(raca_id)
    if not opcoes_sub_raca:
        raise RegraNegocioError(f"Não existem sub-raças cadastradas para '{raca_id}'")

    if sub_raca_id is None:
        sub_raca_id = next(iter(opcoes_sub_raca.keys()))
    if sub_raca_id not in opcoes_sub_raca:
        raise RegraNegocioError(f"Sub-raça inválida para {raca_id}: {sub_raca_id}")

    atributos = dict(BASE_ATTRIBUTES)

    for atributo, bonus in racas[raca_id].get("bonus", {}).items():
        atributos[atributo] = atributos.get(atributo, 0) + bonus

    for atributo, bonus in opcoes_sub_raca[sub_raca_id].get("bonus", {}).items():
        atributos[atributo] = atributos.get(atributo, 0) + bonus

    return CharacterState(
        id=str(uuid4()),
        nome=nome_limpo,
        raca_id=raca_id,
        sub_raca_id=sub_raca_id,
        classe_id=classe_id,
        nivel=1,
        xp=0,
        atributos=atributos,
        hp_atual=100,
        hp_max=100,
    )


def conceder_xp(personagem: CharacterState, ganho_xp: int) -> CharacterState:
    return aplicar_xp(personagem, ganho_xp)
