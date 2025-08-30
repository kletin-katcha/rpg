# -*- coding: utf-8 -*-
"""
################################################################################################
##                                                                                            ##
##    ███╗   ███╗ ██████╗ ███╗   ██╗███████╗████████╗██████╗  ██████╗ ███████╗                  ##
##    ████╗ ████║██╔═══██╗████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗██╔════╝                  ##
##    ██╔████╔██║██║   ██║██╔██╗ ██║███████╗   ██║   ██████╔╝██║   ██║███████╗                  ##
##    ██║╚██╔╝██║██║   ██║██║╚██╗██║╚════██║   ██║   ██╔══██╗██║   ██║╚════██║                  ##
##    ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝███████║                  ##
##    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝                  ##
##                                                                                            ##
################################################################################################
################################################################################################

================================================================================================
BANCO DE DADOS: MONSTROS - ÁREA 1 (NÍVEIS 1-5)
================================================================================================
Este arquivo define os monstros encontrados nas áreas iniciais do jogo, como as
Planícies de Havenwood. São criaturas de baixo nível, projetadas para introduzir
o jogador às mecânicas de combate.

-------------------------
-- ESTRUTURA DE DADOS --
-------------------------
Cada monstro na lista `MONSTROS_AREA_1` é um dicionário com as seguintes chaves:

- `id` (str): Identificador único do monstro.
- `nome` (str): Nome do monstro.
- `nivel` (int): Nível base da criatura.
- `hp` (int): Pontos de vida base.
- `atributos` (dict): Atributos principais do monstro.
- `habilidades` (list): Lista de `id` de habilidades que o monstro pode usar.
- `drops` (list): Tabela de loot. Lista de dicionários com `item_id` e `chance`.
- `comportamento` (str): Define a IA básica ("agressivo", "defensivo", "fugidio").
- `descricao` (str): Descrição narrativa e de combate do monstro.
- `variante_campea` (dict, opcional): Se presente, o monstro tem uma chance de
                                      aparecer como uma versão mais forte.
  - `chance` (float): Chance de a variante aparecer (0.0 a 1.0).
  - `modificadores` (dict): Multiplicadores de HP, dano, etc.

---------------------------------
-- INTEGRAÇÃO COM O MOTOR --
---------------------------------
- **Sistema de Encontros:** O `EncounterManager` usará este arquivo para popular as áreas.
- **Sistema de Combate:** O `CombatManager` usará os `atributos` e `habilidades` para
  controlar o monstro em batalha, seguindo a lógica de `comportamento`.
- **Sistema de Loot:** Após a vitória, o `LootManager` usará a tabela `drops` para
  determinar as recompensas.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import random
from typing import List, Dict, Any

# ==============================================================================================
# == SEÇÃO 2: EXEMPLOS DETALHADOS DE MONSTROS (ÁREA 1) =========================================
# ==============================================================================================
MONSTROS_AREA_1_EXEMPLOS = [
    {
        "id": "goblin_batedor",
        "nome": "Goblin Batedor",
        "nivel": 1,
        "hp": 25,
        "atributos": {"forca": 8, "destreza": 12, "defesa": 5},
        "habilidades": ["sk_geral_ataque_basico"],
        "drops": [{"item_id": "moeda_de_cobre", "quantidade": "1d6", "chance": 0.8}],
        "comportamento": "agressivo",
        "descricao": "Pequeno e covarde, o batedor goblin ataca em grupos, usando sua agilidade para sobrepujar inimigos desavisados. Sozinho, ele tende a fugir.",
    },
    {
        "id": "lobo_jovem",
        "nome": "Lobo Jovem",
        "nivel": 2,
        "hp": 35,
        "atributos": {"forca": 10, "destreza": 14, "defesa": 6},
        "habilidades": ["sk_lobo_mordida_veloz"],
        "drops": [{"item_id": "pele_de_lobo", "quantidade": 1, "chance": 0.5}],
        "comportamento": "agressivo",
        "descricao": "Um lobo jovem, recentemente expulso da matilha para caçar por conta própria. É rápido e feroz, mas ainda inexperiente.",
        "variante_campea": {
            "chance": 0.1,
            "novo_nome": "Lobo Alfa Jovem",
            "modificadores": {"hp_mult": 1.5, "dano_mult": 1.3, "nivel_bonus": 1}
        }
    },
    {
        "id": "javali_selvagem",
        "nome": "Javali Selvagem",
        "nivel": 3,
        "hp": 50,
        "atributos": {"forca": 12, "destreza": 8, "defesa": 8},
        "habilidades": ["sk_javali_investida"],
        "drops": [{"item_id": "presa_de_javali", "quantidade": "1d2", "chance": 0.6}],
        "comportamento": "territorial",
        "descricao": "Um javali grande e mal-humorado que ataca qualquer um que invada seu território. Sua investida é poderosa, mas telegrafada.",
    },
    # ... Adicionar mais 7 monstros detalhados para a área 1
]

# ==============================================================================================
# == SEÇÃO 3: GERADOR DE PLACEHOLDERS ==========================================================
# ==============================================================================================
def gerar_placeholders_monstros(count: int, area_nivel_base: int, prefixo: str = "ph_monstro_") -> list:
    """Gera uma lista de dicionários de monstros placeholder."""
    placeholders = []
    tipos = ["Besta", "Humanoide", "Morto-vivo", "Elemental"]
    for i in range(count):
        nivel = area_nivel_base + random.randint(0, 4)
        monstro = {
            "id": f"{prefixo}{area_nivel_base}_{i+1:03d}",
            "nome": f"Monstro Placeholder #{i+1} ({random.choice(tipos)})",
            "nivel": nivel,
            "hp": 20 + nivel * 10,
            "atributos": {"forca": 5 + nivel, "destreza": 5 + nivel, "defesa": 2 + nivel},
            "habilidades": [], "drops": [],
            "comportamento": "agressivo",
            "descricao": "Descrição detalhada a ser adicionada para este monstro."
        }
        placeholders.append(monstro)
    return placeholders

# ==============================================================================================
# == SEÇÃO 4: CONSTRUÇÃO DO ÍNDICE DE MONSTROS =================================================
# ==============================================================================================
def construir_indice(lista_de_dados: List[Dict]) -> Dict:
    """Constrói um dicionário indexado por ID a partir de uma lista."""
    indice_por_id = {item["id"]: item for item in lista_de_dados}
    return {"by_id": indice_por_id, "lista_completa": lista_de_dados}

MONSTROS_AREA_1 = MONSTROS_AREA_1_EXEMPLOS + gerar_placeholders_monstros(count=20, area_nivel_base=1)
INDICE_MONSTROS_AREA_1 = construir_indice(MONSTROS_AREA_1)

# ==============================================================================================
# == SEÇÃO 5: OBSERVAÇÕES DE DESIGN E INTEGRAÇÃO ===============================================
# ==============================================================================================
"""
1.  **IA de Comportamento:** O `CombatManager` deve ter uma lógica que interpreta a string
    `comportamento`.
    - "agressivo": Foca em usar as habilidades de maior dano.
    - "defensivo": Usa habilidades de buff/defesa primeiro.
    - "fugidio": Tenta fugir se o HP estiver baixo.
    - "territorial": Só ataca se o jogador atacar primeiro.

2.  **Variantes Campeãs:** Quando um encontro é gerado, o `EncounterManager` deve rolar
    a `chance` da `variante_campea`. Se for bem-sucedido, ele cria uma cópia do
    monstro base e aplica os `modificadores` antes de iniciar o combate.

3.  **TO-DO para o Próximo Prompt:**
    - Povoar a lista de `habilidades` com os IDs correspondentes dos arquivos de
      habilidades que criamos.
    - Criar um sistema de loot mais robusto, com tabelas de loot separadas que podem
      ser referenciadas aqui.
"""
