# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: CLASSES AVANÇADAS
================================================================================================
"""
from typing import List, Dict

CLASSES_AVANCADAS: List[Dict] = [
    # --- Combinações Marciais Puras ---
    {"id_classe": "mestre_das_armas", "nome": "Mestre das Armas", "requisitos": {"nivel_minimo": 20, "classes_necessarias": ["guardiao", "berserker"]}, "descricao_curta": "Perito em todas as formas de combate físico."},
    {"id_classe": "dancarino_das_sombras", "nome": "Dançarino das Sombras", "requisitos": {"nivel_minimo": 20, "classes_necessarias": ["assassino", "sombra"]}, "descricao_curta": "Um mestre da furtividade e do movimento, quase intocável."},
    {"id_classe": "kensei", "nome": "Kensei", "requisitos": {"nivel_minimo": 20, "classes_necessarias": ["mao_aberta", "guardiao"]}, "descricao_curta": "Um monge que canaliza seu chi através de uma arma escolhida, tratando-a como uma extensão de seu corpo."},
    {"id_classe": "juggernaut", "nome": "Juggernaut", "requisitos": {"nivel_minimo": 20, "classes_necessarias": ["berserker", "totemico"]}, "descricao_curta": "Uma força da natureza imparável, que ignora a dor e esmaga tudo em seu caminho."},

    # --- Combinações Mágicas Puras ---
    {"id_classe": "arquimago", "nome": "Arquimago", "requisitos": {"nivel_minimo": 20, "classes_necessarias": ["piromante", "criomante"]}, "descricao_curta": "Um mestre de todas as escolas de magia elemental e arcana."},
    {"id_classe": "teurgo_mistico", "nome": "Teurgo Místico", "requisitos": {"nivel_minimo": 20, "classes_necessarias": ["sacerdote", "pacto_do_tomo"]}, "descricao_curta": "Aquele que une o poder arcano e o divino em perfeita harmonia."},
    {"id_classe": "invocador_mestre", "nome": "Invocador Mestre", "requisitos": {"nivel_minimo": 20, "classes_necessarias": ["circulo_da_lua", "linhagem_draconica"]}, "descricao_curta": "Comanda as feras da terra e os ecos dos dragões."},
    {"id_classe": "arauto_da_tempestade", "nome": "Arauto da Tempestade", "requisitos": {"nivel_minimo": 20, "classes_necessarias": ["criomante", "sacerdote"]}, "descricao_curta": "Um clérigo do trovão e do relâmpago, que comanda a fúria dos céus."},

    # --- Combinações Híbridas (Gish - Lâmina e Magia) ---
    {"id_classe": "cavaleiro_arcano", "nome": "Cavaleiro Arcano", "requisitos": {"nivel_minimo": 20, "classes_necessarias": ["guardiao", "piromante"]}, "descricao_curta": "Guerreiro que imbui suas armas e armaduras com magia de batalha."},
    {"id_classe": "lamina_amaldicoada", "nome": "Lâmina Amaldiçoada", "requisitos": {"nivel_minimo": 20, "classes_necessarias": ["assassino", "pacto_da_lamina"]}, "descricao_curta": "Um assassino que usa magia de sangue e sombras para fortalecer seus golpes."},
    {"id_classe": "guardiao_runico", "nome": "Guardião Rúnico", "requisitos": {"nivel_minimo": 20, "classes_necessarias": ["guardiao"], "raca": ["anao_da_montanha"]}, "descricao_curta": "Um anão defensor que entalha runas mágicas em seu equipamento."},
    {"id_classe": "cantor_da_guerra", "nome": "Cantor da Guerra", "requisitos": {"nivel_minimo": 20, "classes_necessarias": ["colegio_da_valentia", "berserker"]}, "descricao_curta": "Um bardo cuja música se torna um grito de batalha, inspirando fúria e proeza marcial."},
    {"id_classe": "inquisidor_arcano", "nome": "Inquisidor Arcano", "requisitos": {"nivel_minimo": 20, "classes_necessarias": ["inquisidor", "trapaceiro"]}, "descricao_curta": "Caçador de magos hereges que usa os próprios truques do inimigo contra eles."},

    # --- Combinações Divinas/Naturais ---
    {"id_classe": "hierofante", "nome": "Hierofante", "requisitos": {"nivel_minimo": 20, "classes_necessarias": ["sacerdote", "circulo_da_terra"]}, "descricao_curta": "O elo supremo entre o mundo mortal e os planos da natureza e dos deuses."},
    {"id_classe": "vingador_sagrado", "nome": "Vingador Sagrado", "requisitos": {"nivel_minimo": 20, "classes_necessarias": ["juramento_da_vinganca", "inquisidor"]}, "descricao_curta": "Um paladino que abraçou completamente a fúria divina para caçar o mal."},
    {"id_classe": "xamã_espiritual", "nome": "Xamã Espiritual", "requisitos": {"nivel_minimo": 20, "classes_necessarias": ["totemico", "circulo_da_lua"]}, "descricao_curta": "Comunhão profunda com os espíritos, que lhe concedem poder sobre a vida e a morte."}
]

INDICE_CLASSES_AVANCADAS = {"by_id": {c["id_classe"]: c for c in CLASSES_AVANCADAS}}
