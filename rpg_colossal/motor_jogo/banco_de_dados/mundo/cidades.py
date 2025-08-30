# -*- coding: utf-8 -*-
"""
################################################################################################
##                                                                                            ##
##     ██████╗██╗██████╗ █████╗ ██████╗ ███████╗███████╗     ██████╗ ██████╗  █████╗ ███████╗   ##
##    ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝   ##
##    ██║     ██║██║  ██║███████║██║  ██║█████╗  ███████╗    ██║     ██║   ██║███████║███████╗   ##
##    ██║     ██║██║  ██║██╔══██║██║  ██║██╔══╝  ╚════██║    ██║     ██║   ██║██╔══██║╚════██║   ##
##    ╚██████╗██║██████╔╝██║  ██║██████╔╝███████╗███████║    ╚██████╗╚██████╔╝██║  ██║███████║   ##
##     ╚═════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝   ##
##                                                                                            ##
################################################################################################
################################################################################################

================================================================================================
BANCO DE DADOS: CIDADES
================================================================================================
Este arquivo define as cidades, vilas e outros assentamentos civilizados do mundo de
Aetheria. Cidades são os principais centros de interação social, comércio, missões
e descanso para o jogador.

-------------------------
-- ESTRUTURA DE DADOS --
-------------------------
Cada cidade na lista `CIDADES` é um dicionário com as seguintes chaves:

- `id` (str): Identificador único da cidade (ex: "havenwood").
- `nome` (str): Nome da cidade.
- `populacao` (int): Número aproximado de habitantes.
- `descricao` (str): Descrição narrativa da cidade, sua arquitetura e atmosfera.
- `governante` (str): Nome ou título do líder da cidade.
- `faccoes_presentes` (list): Lista de `id` de facções que operam na cidade.
- `servicos` (dict): Dicionário com os serviços disponíveis.
  - `lojas` (list): Lista de `id` de lojas (ferreiro, alquimista, etc.).
  - `guildas` (list): Lista de `id` de guildas (guerreiros, magos, etc.).
  - `taverna` (bool): Se há uma taverna para descanso e obtenção de rumores.
  - `templo` (bool): Se há um templo para cura e serviços divinos.
- `cultura` (str): Breve descrição dos costumes e principal atividade econômica.

---------------------------------
-- INTEGRAÇÃO COM O MOTOR --
---------------------------------
- **Interação:** Quando o jogador entra em uma cidade, o `main.py` ou um `InteractionManager`
  usará os dados deste arquivo para apresentar um menu de opções com os `servicos`
  disponíveis.
- **Sistema de Facções:** O `FactionManager` usará a lista `faccoes_presentes` para
  determinar quais missões e NPCs de facção estão disponíveis na cidade.
- **Economia:** Os tipos de lojas e a `cultura` da cidade podem influenciar o sistema
  econômico do jogo (ex: preços de mercadorias).
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import random
from typing import List, Dict, Any

# ==============================================================================================
# == SEÇÃO 2: EXEMPLOS DETALHADOS DE CIDADES ===================================================
# ==============================================================================================
CIDADES_EXEMPLOS = [
    {
        "id": "havenwood",
        "nome": "Havenwood",
        "populacao": 2500,
        "descricao": "Uma cidade murada próspera, conhecida como o 'Portão do Reino'. Havenwood é um centro de comércio movimentado, com uma população diversa e uma forte guarnição militar. Suas ruas de paralelepípedos estão sempre cheias de mercadores, aventureiros e cidadãos comuns.",
        "governante": "Lorde Valerius",
        "faccoes_presentes": ["guilda_dos_aventureiros", "alianca_mercante"],
        "servicos": {
            "lojas": ["ferreiro_braco_de_aco", "alquimista_caldeirao_borbulhante"],
            "guildas": ["guilda_dos_aventureiros_local"],
            "taverna": True,
            "templo": True,
        },
        "cultura": "Comércio e militarismo. A economia de Havenwood gira em torno do comércio de bens manufaturados e da proteção de rotas comerciais."
    },
    {
        "id": "forja_branca",
        "nome": "Forja Branca",
        "populacao": 800,
        "descricao": "Esculpida na encosta da montanha, Forja Branca é um assentamento anão robusto e barulhento. O ar é preenchido com a fumaça das forjas e o som constante de martelos batendo em bigornas. É o melhor lugar no reino para encontrar armas e armaduras de qualidade excepcional.",
        "governante": "Thorek, Mestre da Forja",
        "faccoes_presentes": ["clã_barba_de_pedra"],
        "servicos": {
            "lojas": ["forja_de_thorek", "taverna_martelo_e_caneca"],
            "guildas": [],
            "taverna": True,
            "templo": False, # Anões confiam mais em seu aço do que nos deuses dos homens.
        },
        "cultura": "Mineração e forja. A vida em Forja Branca é dura e focada no trabalho árduo e na criação dos melhores equipamentos de metal de toda Aetheria."
    },
    {
        "id": "sussurro_da_folha",
        "nome": "Sussurro da Folha",
        "populacao": 500,
        "descricao": "Uma vila élfica escondida no coração da Floresta do Silêncio, construída em harmonia com a natureza. As casas são esculpidas em árvores vivas e pontes de corda conectam as plataformas. É um lugar de tranquilidade, magia e segredos antigos.",
        "governante": "Anciã Lyra",
        "faccoes_presentes": ["circulo_dos_druidas"],
        "servicos": {
            "lojas": ["arcos_de_lyra", "herbolaria_elfica"],
            "guildas": [],
            "taverna": False, # Elfos preferem reuniões tranquilas a tavernas barulhentas.
            "templo": True, # Um templo dedicado aos espíritos da natureza.
        },
        "cultura": "Guardiões da natureza e estudiosos da magia. A cultura é focada na preservação da floresta e no estudo das artes arcanas e druídicas."
    },
]

# ==============================================================================================
# == SEÇÃO 3: GERADOR DE PLACEHOLDERS ==========================================================
# ==============================================================================================
def gerar_placeholders_cidades(count: int = 10, prefixo: str = "ph_cidade_") -> list:
    """Gera uma lista de dicionários de cidades placeholder."""
    placeholders = []
    tipos = ["Vila", "Aldeia", "Forte", "Posto Avançado", "Metrópole"]
    for i in range(count):
        cidade = {
            "id": f"{prefixo}{i+1:03d}",
            "nome": f"{random.choice(tipos)} Placeholder #{i+1}",
            "populacao": random.randint(100, 5000),
            "descricao": "Descrição detalhada a ser adicionada para esta cidade.",
            "governante": "Nome a definir",
            "faccoes_presentes": [],
            "servicos": {"lojas": [], "guildas": [], "taverna": random.choice([True, False]), "templo": random.choice([True, False])},
            "cultura": "Cultura a ser definida."
        }
        placeholders.append(cidade)
    return placeholders

# ==============================================================================================
# == SEÇÃO 4: CONSTRUÇÃO DO ÍNDICE DE CIDADES ==================================================
# ==============================================================================================
def construir_indice(lista_de_dados: List[Dict]) -> Dict:
    """Constrói um dicionário indexado por ID a partir de uma lista."""
    indice_por_id = {item["id"]: item for item in lista_de_dados}
    return {"by_id": indice_por_id, "lista_completa": lista_de_dados}

CIDADES = CIDADES_EXEMPLOS + gerar_placeholders_cidades(count=20)
INDICE_CIDADES = construir_indice(CIDADES)

# ==============================================================================================
# == SEÇÃO 5: OBSERVAÇÕES DE DESIGN E INTEGRAÇÃO ===============================================
# ==============================================================================================
"""
1.  **Serviços como Entidades:** As lojas e guildas listadas em `servicos` devem ter seus
    próprios arquivos de dados (ex: `lojas.py`, `guildas.py`), onde os `id`s seriam
    definidos com seus inventários, missões, etc.

2.  **Cidades Dinâmicas:** O estado de uma cidade pode mudar com base nas ações do
    jogador ou eventos mundiais. Por exemplo, completar uma missão pode desbloquear
    uma nova loja ou mudar o governante. O `GameState` precisará rastrear o estado
    atual de cada cidade.

3.  **TO-DO para o Próximo Prompt:**
    - Criar os arquivos de dados para `lojas.py` e `guildas.py`.
    - Conectar os `id`s de facções, lojas e guildas às suas definições detalhadas.
"""
