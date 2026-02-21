from typing import Dict, Any, List

from .classes_unicas_raciais import CLASSES_UNICAS_RACIAIS
from .classes_unicas_raciais import CLASSES_UNICAS_SUBRACAIS

TOTAL_RAMIFICACOES_PADRAO = 500


def gerar_ramificacoes(id_arvore: str, foco: str, total: int = TOTAL_RAMIFICACOES_PADRAO) -> List[Dict[str, Any]]:
    ramificacoes = []
    for i in range(1, total + 1):
        tier = ((i - 1) // 50) + 1
        ramificacoes.append({
            "id": f"{id_arvore}_n{i:03d}",
            "nome": f"{foco} - Nó {i}",
            "descricao": f"Aprimoramento {i} da árvore de {foco.lower()}.",
            "tier": tier,
            "custo_pontos": 1 + ((i - 1) % 5),
            "requisitos": [] if i == 1 else [f"{id_arvore}_n{i-1:03d}"],
        })
    return ramificacoes


def _criar_arvore(id_arvore: str, nome: str, foco: str) -> Dict[str, Any]:
    return {
        "id": id_arvore,
        "nome": nome,
        "foco": foco,
        "ramificacoes": gerar_ramificacoes(id_arvore, foco),
    }


ARVORES_UNIVERSAIS: Dict[str, Dict[str, Any]] = {
    "universal_combate": _criar_arvore("universal_combate", "Constelação do Combate", "Combate"),
    "universal_sobrevivencia": _criar_arvore("universal_sobrevivencia", "Constelação da Sobrevivência", "Sobrevivência"),
    "universal_metalurgia": _criar_arvore("universal_metalurgia", "Constelação da Metalurgia", "Metalurgia"),
    "universal_magia": _criar_arvore("universal_magia", "Constelação Arcana", "Magia"),
}


CLASSES_COM_ARVORE = [
    "guerreiro", "mago", "ladino", "arqueiro", "clerigo", "bardo",
    "sentinela_runico", "arcanista_de_campo",
] + list(CLASSES_UNICAS_RACIAIS.keys())
] + list(CLASSES_UNICAS_SUBRACAIS.keys())


ARVORES_POR_CLASSE: Dict[str, Dict[str, Any]] = {
    id_classe: _criar_arvore(f"classe_{id_classe}", f"Trilha de {id_classe.replace('_', ' ').title()}", id_classe)
    for id_classe in CLASSES_COM_ARVORE
}


RACAS_COM_ARVORE = [
    "alto_nordico", "bretao_arcano", "dunmer_cinzento", "bosmer_silvestre", "altmer_dourado",
    "redguard_desertico", "orc_ferreo", "khajiit_lunar", "argoniano_pantano", "imperial_legionario",
    "sylvano_ancestral", "draconato_primordial", "fae_crepuscular", "goliath_colosso", "tiefling_abissal",
    "aasimar_aurora", "anao_runaferro", "halfling_errante", "yuan_ti_oracular", "myconid_simbionte",
]

ARVORES_POR_RACA: Dict[str, Dict[str, Any]] = {
    id_raca: _criar_arvore(f"raca_{id_raca}", f"Herança de {id_raca.replace('_', ' ').title()}", id_raca)
    for id_raca in RACAS_COM_ARVORE
}


def get_catalogo_arvores() -> Dict[str, Dict[str, Dict[str, Any]]]:
    return {
        "universais": ARVORES_UNIVERSAIS,
        "classes": ARVORES_POR_CLASSE,
        "racas": ARVORES_POR_RACA,
    }
