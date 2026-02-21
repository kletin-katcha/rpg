"""Árvores de herança racial por raça estruturada."""
from .arvores_habilidades_massivas import gerar_ramificacoes
from .racas_mvp_estruturadas import RACAS_MVP_ESTRUTURADAS

ARVORES_HABILIDADES_RACAS = {}
for id_raca in RACAS_MVP_ESTRUTURADAS.keys():
    ARVORES_HABILIDADES_RACAS[id_raca] = {
        "nome": f"Herança de {id_raca.replace('_', ' ').title()}",
        "ramificacoes": gerar_ramificacoes(f"raca_{id_raca}", id_raca),
    }
