# -*- coding: utf-8 -*-
"""
################################################################################################
##                                                                                            ##
##    ██████╗ ██╗   ██╗███╗   ██╗ ██████╗ ███████╗ ██████╗ ███╗   ███╗███████╗                  ##
##    ██╔══██╗██║   ██║████╗  ██║██╔════╝ ██╔════╝██╔═══██╗████╗ ████║██╔════╝                  ##
##    ██║  ██║██║   ██║██╔██╗ ██║██║  ███╗█████╗  ██║   ██║██╔████╔██║███████╗                  ##
##    ██║  ██║██║   ██║██║╚██╗██║██║   ██║██╔══╝  ██║   ██║██║╚██╔╝██║╚════██║                  ##
##    ██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████╗╚██████╔╝██║ ╚═╝ ██║███████║                  ##
##    ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝                  ##
##                                                                                            ##
################################################################################################
################################################################################################

================================================================================================
BANCO DE DADOS: DUNGEONS
================================================================================================
Este arquivo define as dungeons, masmorras, ruínas e outros locais instanciados que
o jogador pode explorar. Dungeons são o pão e a manteiga da vida de um aventureiro,
repletas de monstros, armadilhas, quebra-cabeças e tesouros.

-------------------------
-- ESTRUTURA DE DADOS --
-------------------------
Cada dungeon na lista `DUNGEONS` é um dicionário com as seguintes chaves:

- `id` (str): Identificador único da dungeon (ex: "caverna_dos_goblins").
- `nome` (str): Nome da dungeon para exibição.
- `localizacao` (str): O `id` da área onde esta dungeon se encontra.
- `nivel_recomendado` (int): O nível de personagem ideal para explorar esta dungeon.
- `andares` (int): O número de "níveis" ou "andares" que a dungeon possui.
- `descricao` (str): Descrição narrativa da dungeon, sua história e perigos.
- `tipos_de_monstros` (list): Lista de `id` de monstros que habitam a dungeon.
- `armadilhas` (list): Lista de tipos de armadilhas presentes (ex: "fosso", "dardos").
- `boss` (str): O `id` do monstro chefe no final da dungeon.
- `loot_especial` (list): Lista de `id` de itens especiais ou únicos que só podem
                           ser encontrados nesta dungeon.

---------------------------------
-- INTEGRAÇÃO COM O MOTOR --
---------------------------------
- **Geração de Dungeons:** Um `DungeonManager` ou o `worldgen.py` usará este arquivo
  para gerar uma instância de uma dungeon quando o jogador entrar nela. O número de
  `andares`, `tipos_de_monstros` e `armadilhas` serão usados para criar o layout,
  possivelmente de forma procedural.
- **Sistema de Quests:** Muitas missões enviarão o jogador para explorar uma dungeon
  específica para recuperar um item ou derrotar um chefe.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import random
from typing import List, Dict, Any

# ==============================================================================================
# == SEÇÃO 2: EXEMPLOS DETALHADOS DE DUNGEONS ==================================================
# ==============================================================================================
DUNGEONS_EXEMPLOS = [
    {
        "id": "caverna_dos_goblins",
        "nome": "Caverna dos Goblins",
        "localizacao": "plains_de_havenwood",
        "nivel_recomendado": 3,
        "andares": 3,
        "descricao": "Uma caverna úmida e malcheirosa que serve de covil para a tribo de goblins Lança-Farpada. É um labirinto de túneis apertados, cheios de armadilhas grosseiras e guerreiros goblins.",
        "tipos_de_monstros": ["goblin_batedor", "goblin_guerreiro", "lobo_de_guerra_goblin"],
        "armadilhas": ["Armadilha de Laço", "Alarme de Ossos"],
        "boss": "chefe_goblin_grulnok",
        "loot_especial": ["item_adaga_farpada_de_grulnok"]
    },
    {
        "id": "templo_em_ruinas",
        "nome": "Templo em Ruínas",
        "localizacao": "floresta_do_silencio",
        "nivel_recomendado": 10,
        "andares": 5,
        "descricao": "Um antigo templo élfico, agora coberto por vinhas e musgo. A arquitetura outrora graciosa está em ruínas, e seus corredores silenciosos são agora o lar de feras da floresta e dos espíritos inquietos dos seus antigos guardiões.",
        "tipos_de_monstros": ["espirito_da_floresta", "golem_de_vinhas", "sombra_elfica"],
        "armadilhas": ["Armadilha de Raízes", "Glifo de Paralisia"],
        "boss": "espirito_guardiao_ancestral",
        "loot_especial": ["item_arco_longo_elfico"]
    },
    {
        "id": "fortaleza_anã_abandonada",
        "nome": "Fortaleza Anã Abandonada de Khaz-Mordin",
        "localizacao": "picos_congelados",
        "nivel_recomendado": 20,
        "andares": 10,
        "descricao": "Uma vasta cidade subterrânea anã, abandonada há séculos após uma catástrofe misteriosa. Seus grandes salões estão agora congelados e silenciosos, exceto pelo som de criaturas do gelo que fizeram da fortaleza seu lar e dos fantasmas dos anões que ali pereceram.",
        "tipos_de_monstros": ["espectro_anao", "elemental_de_gelo_maior", "troll_de_gelo"],
        "armadilhas": ["Armadilha de Congelamento Rúnico", "Machado Oscilante"],
        "boss": "rei_anao_fantasma_thrain",
        "loot_especial": ["item_martelo_de_guerra_runico", "item_esquema_armadura_de_placas_ana"]
    },
    {
        "id": "coracao_do_vulcao",
        "nome": "Coração do Vulcão",
        "localizacao": "deserto_das_cinzas",
        "nivel_recomendado": 38,
        "andares": 7,
        "descricao": "Uma rede de túneis de lava no interior do vulcão adormecido. O calor é quase insuportável, e rios de magma correm ao lado de caminhos precários. É o ninho de algumas das criaturas de fogo mais perigosas de Aetheria.",
        "tipos_de_monstros": ["salamandra_de_fogo_maior", "gigante_de_magma", "ifrit"],
        "armadilhas": ["Geiser de Lava", "Piso Quebradiço"],
        "boss": "lord_elemental_do_fogo_ignis",
        "loot_especial": ["item_fragmento_do_coracao_do_vulcao"]
    },
]

# ==============================================================================================
# == SEÇÃO 3: GERADOR DE PLACEHOLDERS ==========================================================
# ==============================================================================================
def gerar_placeholders_dungeons(count: int = 20, prefixo: str = "ph_dungeon_") -> list:
    """Gera uma lista de dicionários de dungeons placeholder."""
    placeholders = []
    tipos = ["Caverna", "Ruína", "Templo", "Forte", "Mina", "Cripta"]
    for i in range(count):
        nivel = i * 4 + 1
        dungeon = {
            "id": f"{prefixo}{i+1:03d}",
            "nome": f"{random.choice(tipos)} Placeholder #{i+1}",
            "localizacao": "ph_area_placeholder",
            "nivel_recomendado": nivel,
            "andares": random.randint(2, 8),
            "descricao": "Descrição detalhada a ser adicionada para esta dungeon.",
            "tipos_de_monstros": [],
            "armadilhas": [],
            "boss": "ph_boss_placeholder",
            "loot_especial": []
        }
        placeholders.append(dungeon)
    return placeholders

# ==============================================================================================
# == SEÇÃO 4: CONSTRUÇÃO DO ÍNDICE DE DUNGEONS =================================================
# ==============================================================================================
def construir_indice(lista_de_dados: List[Dict]) -> Dict:
    """Constrói um dicionário indexado por ID a partir de uma lista."""
    indice_por_id = {item["id"]: item for item in lista_de_dados}
    return {"by_id": indice_por_id, "lista_completa": lista_de_dados}

DUNGEONS = DUNGEONS_EXEMPLOS + gerar_placeholders_dungeons(count=50)
INDICE_DUNGEONS = construir_indice(DUNGEONS)

# ==============================================================================================
# == SEÇÃO 5: OBSERVAÇÕES DE DESIGN E INTEGRAÇÃO ===============================================
# ==============================================================================================
"""
1.  **Geração Procedural de Andares:** O `DungeonManager` pode usar o número de
    `andares` e as listas de `tipos_de_monstros` e `armadilhas` para gerar cada
    andar proceduralmente. A dificuldade e a frequência dos monstros podem aumentar
    à medida que o jogador desce mais fundo na dungeon.

2.  **Dungeons Dinâmicas:** A lista `eventos` de uma área pode incluir um evento que
    "cria" uma nova dungeon temporária no mapa, aumentando a rejogabilidade.

3.  **TO-DO para o Próximo Prompt:**
    - Povoar as listas `tipos_de_monstros`, `boss`, e `loot_especial` com os IDs
      correspondentes que serão criados nos próximos arquivos.
    - Criar um sistema de quebra-cabeças simples que possa ser adicionado a uma
      dungeon, como um evento especial em um dos andares.
"""
