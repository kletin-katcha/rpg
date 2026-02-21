"""Catálogo principal de raças para fluxo de criação em duas etapas."""
from typing import Dict, Any

RACAS_MVP_ESTRUTURADAS: Dict[str, Dict[str, Any]] = {
    "alto_nordico": {"nome": "Alto Nórdico", "descricao": "Povo resistente das montanhas geladas.", "classe_unica_racial": "thane_das_neves"},
    "bretao_arcano": {"nome": "Bretão Arcano", "descricao": "Linhas de sangue com forte aptidão mágica.", "classe_unica_racial": "cavaleiro_runaico"},
    "dunmer_cinzento": {"nome": "Dunmer Cinzento", "descricao": "Guerreiros místicos de regiões vulcânicas.", "classe_unica_racial": "lamina_de_cinzas"},
    "bosmer_silvestre": {"nome": "Bosmer Silvestre", "descricao": "Arqueiros e batedores de florestas antigas.", "classe_unica_racial": "guardiao_do_bosque"},
    "altmer_dourado": {"nome": "Altmer Dourado", "descricao": "Estudiosos de magia avançada e tradições élficas.", "classe_unica_racial": "arconte_solar"},
    "redguard_desertico": {"nome": "Redguard Desértico", "descricao": "Espadachins de resistência ímpar.", "classe_unica_racial": "duelista_de_hamon"},
    "orc_ferreo": {"nome": "Orc Férreo", "descricao": "Clãs militares com foco em guerra e forja.", "classe_unica_racial": "senhor_da_fornalha"},
    "khajiit_lunar": {"nome": "Khajiit Lunar", "descricao": "Caçadores ágeis guiados por ciclos lunares.", "classe_unica_racial": "dancarino_da_lua"},
    "argoniano_pantano": {"nome": "Argoniano do Pântano", "descricao": "Especialistas em venenos e adaptação extrema.", "classe_unica_racial": "xama_escamado"},
    "imperial_legionario": {"nome": "Imperial Legionário", "descricao": "Estratégia e comando de tropas.", "classe_unica_racial": "prefeito_de_guerra"},
    "sylvano_ancestral": {"nome": "Sylvano Ancestral", "descricao": "Guardam pactos com espíritos da mata.", "classe_unica_racial": "tecelao_de_espinhos"},
    "draconato_primordial": {"nome": "Draconato Primordial", "descricao": "Descendentes de linhagens dracônicas.", "classe_unica_racial": "voz_do_dragao"},
    "fae_crepuscular": {"nome": "Fae Crepuscular", "descricao": "Seres feéricos com domínio de ilusões.", "classe_unica_racial": "ilusionista_velado"},
    "goliath_colosso": {"nome": "Goliath Colosso", "descricao": "Gigantes de altitude com força colossal.", "classe_unica_racial": "tita_de_pedra"},
    "tiefling_abissal": {"nome": "Tiefling Abissal", "descricao": "Pactos infernais e magia de risco.", "classe_unica_racial": "jurado_do_abismo"},
    "aasimar_aurora": {"nome": "Aasimar da Aurora", "descricao": "Canalizam energia sagrada.", "classe_unica_racial": "custodio_da_aurora"},
    "anao_runaferro": {"nome": "Anão Runaferro", "descricao": "Mestres de runas e engenharia bélica.", "classe_unica_racial": "engenheiro_runaferro"},
    "halfling_errante": {"nome": "Halfling Errante", "descricao": "Exploradores oportunistas.", "classe_unica_racial": "cartografo_ardiloso"},
    "yuan_ti_oracular": {"nome": "Yuan-ti Oracular", "descricao": "Conhecimento proibido e manipulação arcana.", "classe_unica_racial": "profeta_ofidico"},
    "myconid_simbionte": {"nome": "Myconid Simbionte", "descricao": "Rede fúngica viva.", "classe_unica_racial": "mestre_micelial"},
}
