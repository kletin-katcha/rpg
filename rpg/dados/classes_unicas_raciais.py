from typing import Dict, Any

from .racas_massivas import RACAS_MASSIVAS


def _titulo_de_subraca(nome_sub_raca: str) -> str:
    return f"Especialista de {nome_sub_raca}"


CLASSES_UNICAS_SUBRACAIS: Dict[str, Dict[str, Any]] = {}
for dados_raca in RACAS_MASSIVAS.values():
    for variacao in dados_raca.get("variacoes", []):
        id_sub_raca = variacao["id"]
        id_classe = f"classe_{id_sub_raca}"
        nome_classe = _titulo_de_subraca(variacao["nome"])
        CLASSES_UNICAS_SUBRACAIS[id_classe] = {
            "nome": nome_classe,
            "descricao": f"Classe única da sub-raça {variacao['nome']}.",
            "lore": "Trilha avançada desbloqueável por evolução e afinidade de sub-raça.",
            "stats_primarios": ["forca", "destreza", "inteligencia"],
            "ataques_base_disponiveis": ["ataque_basico", "ataque_preciso"],
            "habilidades_iniciais": [f"postura_{id_classe}", f"tecnica_{id_classe}"],
            "equipamento_inicial": {},
            "classe_unica_sub_racial": True,
            "sub_raca_vinculada": id_sub_raca,
        }
