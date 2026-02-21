from typing import Dict, Any, List

_STATS_CICLO = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]


RACAS_MASSIVAS_BASE: List[Dict[str, Any]] = [
    {"id": "alto_nordico", "nome": "Alto Nórdico", "descricao": "Povo resistente das montanhas geladas."},
    {"id": "bretao_arcano", "nome": "Bretão Arcano", "descricao": "Linhas de sangue com forte aptidão mágica."},
    {"id": "dunmer_cinzento", "nome": "Dunmer Cinzento", "descricao": "Guerreiros místicos de regiões vulcânicas."},
    {"id": "bosmer_silvestre", "nome": "Bosmer Silvestre", "descricao": "Arqueiros e batedores de florestas antigas."},
    {"id": "altmer_dourado", "nome": "Altmer Dourado", "descricao": "Estudiosos de magia avançada e tradições élficas."},
    {"id": "redguard_desertico", "nome": "Redguard Desértico", "descricao": "Espadachins de resistência ímpar."},
    {"id": "orc_ferreo", "nome": "Orc Férreo", "descricao": "Clãs militares com foco em guerra e forja."},
    {"id": "khajiit_lunar", "nome": "Khajiit Lunar", "descricao": "Caçadores ágeis guiados por ciclos lunares."},
    {"id": "argoniano_pantano", "nome": "Argoniano do Pântano", "descricao": "Especialistas em venenos e adaptação extrema."},
    {"id": "imperial_legionario", "nome": "Imperial Legionário", "descricao": "Estratégia, disciplina e comando de tropas."},
    {"id": "sylvano_ancestral", "nome": "Sylvano Ancestral", "descricao": "Guardam pactos com espíritos da mata."},
    {"id": "draconato_primordial", "nome": "Draconato Primordial", "descricao": "Descendentes de linhagens dracônicas antigas."},
    {"id": "fae_crepuscular", "nome": "Fae Crepuscular", "descricao": "Seres feéricos com domínio de ilusões."},
    {"id": "goliath_colosso", "nome": "Goliath Colosso", "descricao": "Gigantes de altitude com força colossal."},
    {"id": "tiefling_abissal", "nome": "Tiefling Abissal", "descricao": "Pactos infernais e magia de risco."},
    {"id": "aasimar_aurora", "nome": "Aasimar da Aurora", "descricao": "Canalizam energia sagrada e proteção."},
    {"id": "anao_runaferro", "nome": "Anão Runaferro", "descricao": "Mestres de runas e engenharia bélica."},
    {"id": "halfling_errante", "nome": "Halfling Errante", "descricao": "Exploradores oportunistas e diplomatas."},
    {"id": "yuan_ti_oracular", "nome": "Yuan-ti Oracular", "descricao": "Conhecimento proibido e manipulação arcana."},
    {"id": "myconid_simbionte", "nome": "Myconid Simbionte", "descricao": "Rede fúngica viva e controle biológico."},
]


ARQUETIPOS_SUBRACA = [
    ("montanhes", "Montanhês"),
    ("costeiro", "Costeiro"),
    ("nomade", "Nômade"),
    ("arcano", "Arcano"),
    ("veterano", "Veterano"),
    ("mistico", "Místico"),
]


def _gerar_variacoes(id_raca: str, nome_raca: str, indice: int) -> List[Dict[str, Any]]:
    variacoes = []
    for i, (id_arquetipo, nome_arquetipo) in enumerate(ARQUETIPOS_SUBRACA):
        stat = _STATS_CICLO[(indice + i) % len(_STATS_CICLO)]
        id_sub_raca = f"{id_raca}_{id_arquetipo}"
        id_classe_unica = f"classe_{id_sub_raca}"
        variacoes.append({
            "id": id_sub_raca,
            "nome": f"{nome_raca} {nome_arquetipo}",
            "descricao": f"Vertente {nome_arquetipo.lower()} da raça {nome_raca.lower()}.",
            "modificadores_stats": {stat: 1},
            "classes_unicas_sub_raca": [id_classe_unica],
        })
    return variacoes


RACAS_MASSIVAS: Dict[str, Dict[str, Any]] = {}
for idx, base in enumerate(RACAS_MASSIVAS_BASE):
    RACAS_MASSIVAS[base["id"]] = {
        "nome": base["nome"],
        "descricao": base["descricao"],
        "lore": f"{base['nome']} possui tradição própria e conflitos regionais relevantes para o mundo.",
        "modificadores_stats": {_STATS_CICLO[idx % len(_STATS_CICLO)]: 1},
        "habilidades_raciais": [f"passiva_{base['id']}", f"afinidade_{base['id']}"],
        "variacoes": _gerar_variacoes(base["id"], base["nome"], idx),
    }
