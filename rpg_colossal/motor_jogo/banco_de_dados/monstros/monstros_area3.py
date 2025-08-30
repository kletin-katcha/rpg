# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: MONSTROS - ÁREA 3 (NÍVEIS 15-25)
================================================================================================
Este arquivo define os monstros encontrados em áreas de nível mais elevado, como os
Picos Congelados. Estas criaturas são perigosas e possuem habilidades que podem
rapidamente sobrepujar um aventureiro despreparado.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import random
from typing import List, Dict, Any

# Reutilização das funções do primeiro arquivo de monstros.
from .monstros_area1 import gerar_placeholders_monstros, construir_indice

# ==============================================================================================
# == SEÇÃO 2: EXEMPLOS DETALHADOS DE MONSTROS (ÁREA 3) =========================================
# ==============================================================================================
MONSTROS_AREA_3_EXEMPLOS = [
    {
        "id": "gigante_do_gelo",
        "nome": "Gigante do Gelo",
        "nivel": 18,
        "hp": 350,
        "atributos": {"forca": 22, "destreza": 9, "defesa": 20, "resistencia_gelo": 0.75},
        "habilidades": ["sk_gigante_pancada_esmagadora", "sk_gigante_arremessar_rocha"],
        "drops": [
            {"item_id": "coracao_congelado_de_gigante", "quantidade": 1, "chance": 0.2},
            {"item_id": "pele_grossa", "quantidade": "1d4", "chance": 0.8}
        ],
        "comportamento": "agressivo",
        "descricao": "Um gigante imenso e lento, cuja pele é tão fria e dura quanto o gelo das montanhas. Seus golpes são capazes de esmagar armaduras e ossos com facilidade.",
    },
    {
        "id": "yeti",
        "nome": "Yeti",
        "nivel": 16,
        "hp": 280,
        "atributos": {"forca": 18, "destreza": 15, "defesa": 15},
        "habilidades": ["sk_yeti_furia_gelada", "sk_yeti_sopro_congelante"],
        "drops": [{"item_id": "pele_de_yeti_imaculada", "quantidade": 1, "chance": 0.4}],
        "comportamento": "territorial",
        "descricao": "Uma besta peluda e poderosa que vive nas cavernas dos Picos Congelados. É extremamente territorial e ataca com uma fúria selvagem, usando tanto suas garras quanto o frio ao seu redor.",
    },
    {
        "id": "elemental_de_gelo_maior",
        "nome": "Elemental de Gelo Maior",
        "nivel": 20,
        "hp": 250,
        "atributos": {"forca": 10, "destreza": 18, "defesa": 18, "resistencia_gelo": 1.0, "vulnerabilidade_fogo": 0.5},
        "habilidades": ["sk_elemental_lanca_de_gelo_tripla", "sk_elemental_nova_congelante"],
        "drops": [{"item_id": "nucleo_elemental_de_gelo", "quantidade": 1, "chance": 0.9}],
        "comportamento": "defensivo",
        "descricao": "Uma manifestação pura e consciente do frio eterno. Não possui corpo físico, sendo uma forma humanoide feita de gelo mágico. Ataca à distância com precisão mortal e pode congelar inimigos em seu lugar.",
    },
    # ... Adicionar mais 7 monstros detalhados para a área 3
]

# ==============================================================================================
# == SEÇÃO 3: CONSTRUÇÃO DO GRIMÓRIO INDEXADO ==================================================
# ==============================================================================================
MONSTROS_AREA_3 = MONSTROS_AREA_3_EXEMPLOS + gerar_placeholders_monstros(count=30, area_nivel_base=15, prefixo="ph_monstro_a3_")
INDICE_MONSTROS_AREA_3 = construir_indice(MONSTROS_AREA_3)

# ==============================================================================================
# == SEÇÃO 4: OBSERVAÇÕES DE DESIGN E INTEGRAÇÃO ===============================================
# ==============================================================================================
"""
1.  **Resistências e Vulnerabilidades:** Monstros nesta faixa de nível começam a ter
    resistências e vulnerabilidades elementais significativas. O `CombatManager`
    precisará de uma matriz ou função para calcular o modificador de dano final
    baseado no tipo de dano da habilidade e nas resistências do monstro.

2.  **Habilidades de Chefes:** As habilidades dos monstros aqui (`nova_congelante`,
    `pancada_esmagadora`) podem ser versões mais fracas de habilidades usadas por
    chefes, ensinando ao jogador as mecânicas antes da luta principal.

3.  **TO-DO para o Próximo Prompt:**
    - Criar os arquivos de dados para os chefes, que terão as habilidades mais
      complexas e únicas do jogo.
    - Começar a povoar as listas de `habilidades` dos monstros com os IDs reais
      do Grimório de Habilidades.
"""
