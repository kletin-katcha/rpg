from rpg.content.loader import load_catalog
from rpg.core.errors import RegraNegocioError
from rpg.core.types import CharacterState


def listar_arvore(arvore_id: str = "combate_base") -> dict:
    arvores = load_catalog("arvores_habilidades")
    if arvore_id not in arvores:
        raise RegraNegocioError(f"Árvore inválida: {arvore_id}")
    return arvores[arvore_id]


def habilidades_disponiveis(personagem: CharacterState, arvore_id: str = "combate_base") -> list[str]:
    arvore = listar_arvore(arvore_id)
    desbloqueadas = set(personagem.habilidades_desbloqueadas)
    disponiveis: list[str] = []

    for nodo in arvore.get("nodos", []):
        nodo_id = nodo["id"]
        if nodo_id in desbloqueadas:
            continue
        requer = set(nodo.get("requer", []))
        if requer.issubset(desbloqueadas):
            disponiveis.append(nodo_id)
    return disponiveis


def desbloquear_habilidade(personagem: CharacterState, habilidade_id: str, arvore_id: str = "combate_base") -> CharacterState:
    if habilidade_id in personagem.habilidades_desbloqueadas:
        raise RegraNegocioError(f"Habilidade já desbloqueada: {habilidade_id}")

    disponiveis = habilidades_disponiveis(personagem, arvore_id)
    if habilidade_id not in disponiveis:
        raise RegraNegocioError(
            f"Habilidade indisponível: {habilidade_id}. Disponíveis: {disponiveis or 'nenhuma'}"
        )

    personagem.habilidades_desbloqueadas.append(habilidade_id)
    _aplicar_efeito_habilidade(personagem, habilidade_id)
    return personagem


def _aplicar_efeito_habilidade(personagem: CharacterState, habilidade_id: str) -> None:
    if habilidade_id == "postura_ofensiva":
        personagem.atributos["forca"] = personagem.atributos.get("forca", 0) + 1
    elif habilidade_id == "golpe_reforcado":
        personagem.hp_max += 5
        personagem.hp_atual = min(personagem.hp_atual + 5, personagem.hp_max)
