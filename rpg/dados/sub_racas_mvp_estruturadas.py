"""Catálogo dedicado de sub-raças indexadas por raça."""
from typing import Dict, Any

from .racas_mvp_estruturadas import RACAS_MVP_ESTRUTURADAS

_ARQUETIPOS = [
    ("montanhes", "Montanhês", "forca"),
    ("costeiro", "Costeiro", "destreza"),
    ("nomade", "Nômade", "constituicao"),
    ("arcano", "Arcano", "inteligencia"),
    ("veterano", "Veterano", "sabedoria"),
    ("mistico", "Místico", "carisma"),
]

SUB_RACAS_MVP_ESTRUTURADAS: Dict[str, Dict[str, Dict[str, Any]]] = {}
for id_raca, dados_raca in RACAS_MVP_ESTRUTURADAS.items():
    nome_raca = dados_raca["nome"]
    SUB_RACAS_MVP_ESTRUTURADAS[id_raca] = {}
    for id_arqu, nome_arqu, stat in _ARQUETIPOS:
        id_sub = f"{id_raca}_{id_arqu}"
        SUB_RACAS_MVP_ESTRUTURADAS[id_raca][id_sub] = {
            "id": id_sub,
            "nome": f"{nome_raca} {nome_arqu}",
            "descricao": f"Variação {nome_arqu.lower()} da raça {nome_raca.lower()}.",
            "modificadores_stats": {stat: 1},
        }
