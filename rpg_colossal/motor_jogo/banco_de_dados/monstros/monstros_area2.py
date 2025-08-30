# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: MONSTROS - ÁREA 2 (NÍVEIS 5-15)
================================================================================================
Este arquivo define os monstros encontrados em áreas de nível intermediário, como a
Floresta do Silêncio ou as Colinas Assombradas. As criaturas aqui apresentam
mecânicas mais complexas do que as da Área 1, exigindo mais tática do jogador.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import random
from typing import List, Dict, Any

# Importa o gerador e o construtor de índice do arquivo da área 1 para reutilização.
# Isso é uma boa prática para não duplicar código.
from .monstros_area1 import gerar_placeholders_monstros, construir_indice

# ==============================================================================================
# == SEÇÃO 2: EXEMPLOS DETALHADOS DE MONSTROS (ÁREA 2) =========================================
# ==============================================================================================
MONSTROS_AREA_2_EXEMPLOS = [
    {
        "id": "lobo_atroz",
        "nome": "Lobo Atroz",
        "nivel": 6,
        "hp": 80,
        "atributos": {"forca": 15, "destreza": 16, "defesa": 10},
        "habilidades": ["sk_lobo_mordida_feroz", "sk_lobo_uivo_amedrontador"],
        "drops": [
            {"item_id": "pele_de_lobo_atroz", "quantidade": 1, "chance": 0.6},
            {"item_id": "presa_de_lobo_atroz", "quantidade": "1d2", "chance": 0.3}
        ],
        "comportamento": "matilha",
        "descricao": "Maior, mais forte e mais astuto que um lobo comum. Lobos Atrozes caçam em matilhas coordenadas e são conhecidos por cercar suas presas.",
    },
    {
        "id": "aranha_gigante",
        "nome": "Aranha Gigante",
        "nivel": 7,
        "hp": 70,
        "atributos": {"forca": 12, "destreza": 18, "defesa": 12},
        "habilidades": ["sk_aranha_picada_venenosa", "sk_aranha_teia_pegajosa"],
        "drops": [{"item_id": "glandula_de_veneno", "quantidade": 1, "chance": 0.7}],
        "comportamento": "emboscada",
        "descricao": "Uma caçadora paciente que tece teias enormes e quase invisíveis para capturar suas vítimas. Sua picada pode injetar um veneno paralisante.",
    },
    {
        "id": "espirito_da_floresta",
        "nome": "Espírito da Floresta",
        "nivel": 8,
        "hp": 90,
        "atributos": {"forca": 10, "destreza": 15, "defesa": 15, "resistencia_magica": 0.3},
        "habilidades": ["sk_espirito_toque_drenante", "sk_espirito_forma_eterea"],
        "drops": [{"item_id": "essencia_espiritual", "quantidade": "1d3", "chance": 0.5}],
        "comportamento": "guardião",
        "descricao": "Um espírito antigo ligado à floresta. Normalmente pacífico, ataca com fúria qualquer um que profane seu domínio, usando a própria natureza como arma.",
    },
    # ... Adicionar mais 7 monstros detalhados para a área 2
]

# ==============================================================================================
# == SEÇÃO 3: CONSTRUÇÃO DO GRIMÓRIO INDEXADO ==================================================
# ==============================================================================================
MONSTROS_AREA_2 = MONSTROS_AREA_2_EXEMPLOS + gerar_placeholders_monstros(count=30, area_nivel_base=5, prefixo="ph_monstro_a2_")
INDICE_MONSTROS_AREA_2 = construir_indice(MONSTROS_AREA_2)

# ==============================================================================================
# == SEÇÃO 4: OBSERVAÇÕES DE DESIGN E INTEGRAÇÃO ===============================================
# ==============================================================================================
"""
1.  **Comportamento de Matilha:** A IA para o comportamento "matilha" deve fazer com que
    os monstros foquem no mesmo alvo que o "líder" da matilha (o monstro de nível
    mais alto no encontro).

2.  **Comportamento de Emboscada:** A IA para "emboscada" pode dar ao monstro um turno
    de preparação ou um bônus de dano no primeiro ataque se o jogador falhar em um
    teste de percepção ao entrar na sala.

3.  **TO-DO para o Próximo Prompt:**
    - Povoar a lista de `habilidades` com IDs do grimório.
    - Criar monstros para a Área 3, com mecânicas ainda mais complexas, como
      resistências elementais e habilidades de invocação.
"""
