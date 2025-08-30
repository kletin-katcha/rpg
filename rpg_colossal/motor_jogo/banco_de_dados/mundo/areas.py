# -*- coding: utf-8 -*-
"""
################################################################################################
##                                                                                            ##
##     █████╗ ██████╗ ███████╗ █████╗ ███████╗    ███╗   ███╗██╗   ██╗███╗   ██╗██████╗  ██████╗  ##
##    ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝    ████╗ ████║██║   ██║████╗  ██║██╔══██╗██╔═══██╗ ##
##    ███████║██████╔╝█████╗  ███████║███████╗    ██╔████╔██║██║   ██║██╔██╗ ██║██║  ██║██║   ██║ ##
##    ██╔══██║██╔══██╗██╔══╝  ██╔══██║╚════██║    ██║╚██╔╝██║██║   ██║██║╚██╗██║██║  ██║██║   ██║ ##
##    ██║  ██║██║  ██║███████╗██║  ██║███████║    ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██████╔╝╚██████╔╝ ##
##    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝  ╚═════╝  ##
##                                                                                            ##
################################################################################################
################################################################################################

================================================================================================
BANCO DE DADOS: ÁREAS DO MUNDO
================================================================================================
Este arquivo define as diversas áreas, regiões e biomas que compõem o mundo de Aetheria.
Cada área é um "nó" no mapa-múndi, contendo informações sobre seu ambiente, os perigos
que abriga e os pontos de interesse que o jogador pode encontrar.

-------------------------
-- ESTRUTURA DE DADOS --
-------------------------
Cada área na lista `AREAS` é um dicionário com as seguintes chaves:

- `id` (str): Identificador único da área (ex: "floresta_ancia").
- `nome` (str): Nome da área para exibição.
- `bioma` (str): Tipo de ambiente (ex: "Floresta", "Deserto", "Pântano").
- `nivel_min` (int): Nível mínimo recomendado para entrar na área.
- `nivel_max` (int): Nível máximo em que a área ainda oferece desafio.
- `descricao` (str): Descrição narrativa da área, evocando sua atmosfera.
- `monstros` (list): Lista de `id` de monstros que podem ser encontrados aqui.
- `eventos` (list): Lista de `id` de eventos aleatórios ou fixos que podem ocorrer.
- `cidades_proximas` (list): Lista de `id` de cidades nesta área ou adjacentes.
- `dungeons` (list): Lista de `id` de dungeons localizadas nesta área.
- `recursos` (list): Lista de recursos coletáveis (ex: "Erva Curativa", "Minério de Ferro").

---------------------------------
-- INTEGRAÇÃO COM O MOTOR --
---------------------------------
- **Geração de Mundo:** O `sistemas/worldgen.py` pode usar este arquivo para construir
  o mapa do mundo, conectando as áreas e seus pontos de interesse.
- **Sistema de Encontros:** Ao viajar por uma área, o motor usará a lista `monstros`
  e `eventos` para gerar encontros aleatórios para o jogador.
- **Navegação:** O jogador se moverá de uma área para outra, e a descrição de cada
  área será exibida para criar imersão.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import random
from typing import List, Dict, Any

# ==============================================================================================
# == SEÇÃO 2: EXEMPLOS DETALHADOS DE ÁREAS =====================================================
# ==============================================================================================
AREAS_EXEMPLOS = [
    {
        "id": "plains_de_havenwood",
        "nome": "Planícies de Havenwood",
        "bioma": "Planície",
        "nivel_min": 1,
        "nivel_max": 5,
        "descricao": "Vastas planícies verdejantes que se estendem a partir dos portões da cidade de Havenwood. É uma terra relativamente segura, patrulhada por guardas, mas goblins e lobos selvagens ainda espreitam nos limites da civilização.",
        "monstros": ["goblin_batedor", "lobo_jovem", "javali_selvagem"],
        "eventos": ["mercador_viajante", "ataque_goblin_a_caravana"],
        "cidades_proximas": ["havenwood"],
        "dungeons": ["caverna_dos_goblins"],
        "recursos": ["Erva Simples", "Couro de Lobo"]
    },
    {
        "id": "floresta_do_silencio",
        "nome": "Floresta do Silêncio",
        "bioma": "Floresta",
        "nivel_min": 5,
        "nivel_max": 12,
        "descricao": "Uma floresta antiga e densa, onde a luz do sol mal penetra as copas das árvores. O ar é pesado e um silêncio sobrenatural paira sobre o local, quebrado apenas pelo estalar de galhos sob pés invisíveis. Dizem que a floresta é guardada por espíritos antigos.",
        "monstros": ["lobo_atroz", "aranha_gigante", "espirito_da_floresta", "troll_da_floresta"],
        "eventos": ["altar_esquecido", "cacador_perdido"],
        "cidades_proximas": [],
        "dungeons": ["templo_em_ruinas"],
        "recursos": ["Madeira Ancestral", "Veneno de Aranha", "Essência Espiritual"]
    },
    {
        "id": "picos_congelados",
        "nome": "Picos Congelados",
        "bioma": "Montanha de Neve",
        "nivel_min": 15,
        "nivel_max": 25,
        "descricao": "As imponentes montanhas que marcam a fronteira norte do reino. O frio é implacável e as tempestades de neve são constantes. Apenas os mais resistentes sobrevivem aqui, entre gigantes do gelo e feras adaptadas ao clima extremo.",
        "monstros": ["gigante_do_gelo", "yeti", "elemental_de_gelo", "urso_da_neve"],
        "eventos": ["avalanche", "caverna_de_gelo_oculta"],
        "cidades_proximas": ["forja_branca"],
        "dungeons": ["fortaleza_anã_abandonada"],
        "recursos": ["Minério de Gelo Eterno", "Pele de Yeti"]
    },
    {
        "id": "pantano_das_almas_perdidas",
        "nome": "Pântano das Almas Perdidas",
        "bioma": "Pântano",
        "nivel_min": 20,
        "nivel_max": 30,
        "descricao": "Um pântano fétido e enevoado, onde almas de guerreiros caídos em uma antiga batalha ainda vagam, incapazes de encontrar o descanso. A água escura esconde criaturas peçonhentas e os mortos-vivos se erguem da lama ao anoitecer.",
        "monstros": ["espectro", "zumbi_do_lodo", "hidra_pequena", "crocodilo_gigante"],
        "eventos": ["visão_fantasmagorica", "barco_afundado"],
        "cidades_proximas": [],
        "dungeons": ["cripta_do_general_caido"],
        "recursos": ["Lótus Negra", "Ectoplasma", "Escama de Hidra"]
    },
    {
        "id": "deserto_das_cinzas",
        "nome": "Deserto das Cinzas",
        "bioma": "Deserto Vulcânico",
        "nivel_min": 30,
        "nivel_max": 40,
        "descricao": "Uma vasta extensão de areia negra e rocha vulcânica, resultado de uma catástrofe arcana eras atrás. O ar é quente e seco, e a paisagem é dominada por um vulcão adormecido. Salamandras de fogo e escorpiões de obsidiana são os reis deste domínio inóspito.",
        "monstros": ["salamandra_de_fogo", "escorpiao_de_obsidiana", "elemental_de_magma", "verme_da_areia"],
        "eventos": ["miragem_arcana", "geiser_de_lava"],
        "cidades_proximas": [],
        "dungeons": ["coracao_do_vulcao"],
        "recursos": ["Obsidiana", "Coracao_de_Magma"]
    },
    {
        "id": "terras_profanas",
        "nome": "Terras Profanas",
        "bioma": "Terra Devastada",
        "nivel_min": 45,
        "nivel_max": 50,
        "descricao": "A região que circunda a fortaleza do Rei dos Demônios. O céu é perpetuamente vermelho, o chão é rachado e corrupto, e a própria realidade parece se desfazer. Apenas os demônios mais poderosos e seus servos mortais ousam caminhar aqui.",
        "monstros": ["demonio_menor", "cavaleiro_do_caos", "diabrete", "cao_infernal"],
        "eventos": ["fenda_para_o_abismo", "alma_atormentada"],
        "cidades_proximas": [],
        "dungeons": ["portao_do_inferno"],
        "recursos": ["Pedra Infernal", "Enxofre"]
    },
]

# ==============================================================================================
# == SEÇÃO 3: GERADOR DE PLACEHOLDERS ==========================================================
# ==============================================================================================
def gerar_placeholders_areas(count: int = 20, prefixo: str = "ph_area_") -> list:
    """Gera uma lista de dicionários de áreas placeholder."""
    placeholders = []
    biomas = ["Floresta", "Planície", "Montanha", "Deserto", "Pântano", "Costa"]
    for i in range(count):
        nivel = i * 5 + 1
        area = {
            "id": f"{prefixo}{i+1:03d}",
            "nome": f"Área Placeholder #{i+1} ({random.choice(biomas)})",
            "bioma": random.choice(biomas),
            "nivel_min": nivel,
            "nivel_max": nivel + 4,
            "descricao": "Descrição detalhada a ser adicionada para esta área.",
            "monstros": [], "eventos": [], "cidades_proximas": [], "dungeons": [], "recursos": []
        }
        placeholders.append(area)
    return placeholders

# ==============================================================================================
# == SEÇÃO 4: CONSTRUÇÃO DO ÍNDICE DE ÁREAS ====================================================
# ==============================================================================================
def construir_indice(lista_de_dados: List[Dict]) -> Dict:
    """Constrói um dicionário indexado por ID a partir de uma lista."""
    indice_por_id = {item["id"]: item for item in lista_de_dados}
    return {"by_id": indice_por_id, "lista_completa": lista_de_dados}

AREAS = AREAS_EXEMPLOS + gerar_placeholders_areas(count=50)
INDICE_AREAS = construir_indice(AREAS)

# ==============================================================================================
# == SEÇÃO 5: OBSERVAÇÕES DE DESIGN E INTEGRAÇÃO ===============================================
# ==============================================================================================
"""
1.  **Geração Procedural de Mapas:** O sistema `worldgen.py` pode usar este arquivo
    como um 'catálogo' de nós. Ele pode pegar várias áreas e conectá-las de forma
    procedural, garantindo que as conexões façam sentido (ex: não conectar um
    Pico Congelado diretamente a um Deserto Vulcânico sem uma área de transição).

2.  **Tabelas de Encontro:** O `CombatManager` ou um `EncounterManager` usaria a
    lista `monstros` de uma área para criar uma tabela de encontros ponderada.
    Monstros mais fracos (como goblins) teriam uma chance maior de aparecer do que
    monstros mais fortes (como trolls).

3.  **TO-DO para o Próximo Prompt:**
    - Povoar a lista de `monstros`, `eventos`, `cidades_proximas` e `dungeons`
      nos placeholders gerados com os IDs correspondentes que serão criados nos
      próximos arquivos.
    - Detalhar o sistema de `eventos`, criando um arquivo `eventos.py`.
"""
