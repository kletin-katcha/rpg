"""Classes únicas vinculadas ao nível de raça."""
from typing import Dict, Any

from .racas_mvp_estruturadas import RACAS_MVP_ESTRUTURADAS

CLASSES_UNICAS_RACIAIS: Dict[str, Dict[str, Any]] = {}
for id_raca, dados_raca in RACAS_MVP_ESTRUTURADAS.items():
    id_classe = dados_raca["classe_unica_racial"]
    CLASSES_UNICAS_RACIAIS[id_classe] = {
        "nome": id_classe.replace("_", " ").title(),
        "descricao": f"Classe única da raça {dados_raca['nome']}.",
        "lore": "Requer afinidade racial avançada e marcos narrativos.",
        "stats_primarios": ["forca", "destreza", "inteligencia"],
        "ataques_base_disponiveis": ["ataque_basico", "ataque_preciso"],
        "habilidades_iniciais": [f"postura_{id_classe}", f"tecnica_{id_classe}"],
        "equipamento_inicial": {},
        "classe_unica_racial": True,
        "raca_vinculada": id_raca,
    }
