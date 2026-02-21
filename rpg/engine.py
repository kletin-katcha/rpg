"""Regras puras do jogo reboot."""

from .catalog import RACAS, SUB_RACAS, CLASSES
from .domain import Personagem


def criar_personagem(nome: str) -> Personagem:
    nome_limpo = nome.strip()
    if not nome_limpo:
        raise ValueError("Nome inválido")
    return Personagem(nome=nome_limpo)


def aplicar_bonus(personagem: Personagem, bonus: dict[str, int]) -> None:
    for atributo, valor in bonus.items():
        campo = f"base_{atributo}"
        if hasattr(personagem, campo):
            setattr(personagem, campo, getattr(personagem, campo) + valor)


def aplicar_raca(personagem: Personagem, raca_id: str) -> None:
    dados = RACAS.get(raca_id)
    if not dados:
        raise ValueError("Raça inválida")
    personagem.raca = raca_id
    aplicar_bonus(personagem, dados.get("bonus", {}))


def listar_sub_racas(raca_id: str) -> dict:
    return SUB_RACAS.get(raca_id, {})


def aplicar_sub_raca(personagem: Personagem, sub_raca_id: str) -> None:
    if not personagem.raca:
        raise ValueError("Defina a raça antes da sub-raça")
    dados = listar_sub_racas(personagem.raca).get(sub_raca_id)
    if not dados:
        raise ValueError("Sub-raça inválida")
    personagem.sub_raca = sub_raca_id
    aplicar_bonus(personagem, dados.get("bonus", {}))


def aplicar_classe(personagem: Personagem, classe_id: str) -> None:
    dados = CLASSES.get(classe_id)
    if not dados:
        raise ValueError("Classe inválida")
    personagem.classe = classe_id
    for habilidade in dados.get("habilidades", []):
        if habilidade not in personagem.habilidades:
            personagem.habilidades.append(habilidade)
