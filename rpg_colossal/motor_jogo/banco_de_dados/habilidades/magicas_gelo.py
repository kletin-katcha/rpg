# -*- coding: utf-8 -*-
"""
################################################################################################
##                                                                                            ##
##    ███╗   ███╗ █████╗  ██████╗ ██╗ ██████╗     █████╗      ██████╗  ██████╗  ██████╗          ##
##    ████╗ ████║██╔══██╗██╔════╝ ██║██╔═══██╗   ██╔══██╗    ██╔════╝ ██████╗ ██╗  ██╗          ##
##    ██╔████╔██║███████║██║  ███╗██║██║   ██║   ███████║    ██║  ███╗██╔═══██╗██║  ██║          ##
##    ██║╚██╔╝██║██╔══██║██║   ██║██║██║   ██║   ██╔══██║    ██║   ██║██║   ██║██║  ██║          ##
##    ██║ ╚═╝ ██║██║  ██║╚██████╔╝██║╚██████╔╝   ██║  ██║    ╚██████╔╝██║  ██║╚██████╔╝          ##
##    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝ ╚═════╝    ╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝           ##
##                                                                                            ##
################################################################################################
################################################################################################

================================================================================================
BANCO DE DADOS: HABILIDADES MÁGICAS - GELO
================================================================================================
Este arquivo contém a definição de todas as habilidades da escola de magia do Gelo.
A Criomancia é uma arte arcana focada no controle, na defesa e na debilitação de
inimigos através do frio extremo. Em contraste com o poder bruto do fogo, o gelo
é uma força de precisão e paciência.

-------------------------
-- ESTRUTURA DE DADOS --
-------------------------
A estrutura de cada habilidade segue o padrão definido no grimório global, com
ênfase em `efeitos` que causam `debuff` (como Lentidão e Congelamento) e `tags`
que refletem essa natureza de controle.

- id, nome, tipo, categoria, custo, multiplicador, atributo_chave, precisao,
  critico_mult, cooldown, descricao, efeitos, requisitos, tags, placeholders_gui.

---------------------------------
-- EXEMPLO DE CONSUMO (COMBATE) --
---------------------------------
'''
# No CombatManager, ao resolver um debuff de gelo
def aplicar_lentidao(alvo, efeito):
    if not alvo.tem_efeito('Congelado'): # Evita redundância
        alvo.stats['velocidade'] *= (1 - efeito['valor']) # Reduz a velocidade
        alvo.aplicar_efeito(efeito)
        narrar(f"{alvo.nome} está mais lento! [gelo]")
'''
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import random
from typing import List, Dict, Any

# ==============================================================================================
# == SEÇÃO 2: HABILIDADES DE GELO DE EXEMPLO ===================================================
# ==============================================================================================
HABILIDADES_GELO_EXEMPLOS = [
    # --- Habilidades Simples ---
    {
        "id": "sk_mago_lanca_de_gelo",
        "nome": "Lança de Gelo",
        "tipo": "ativa", "categoria": "magico",
        "custo": {"mana": 15, "stamina": 0},
        "multiplicador": 1.1, "atributo_chave": "inteligencia",
        "precisao": 0.98, "critico_mult": 1.5, "cooldown": 0,
        "descricao": {
            "lore": "Um fragmento de gelo mágico, afiado e frio como o inverno, é arremessado contra o inimigo.",
            "mecanica": "Causa dano de gelo baixo a um único alvo. Chance de aplicar 'Lentidão'."
        },
        "efeitos": [
            {
                "tipo": "debuff",
                "valor": {"velocidade": -0.1}, # Reduz a velocidade em 10%
                "duracao": 2,
                "chance": 0.3,
                "nome_efeito": "Lentidão"
            }
        ],
        "requisitos": {"classe": "mago"},
        "tags": ["gelo", "single-target", "lentidao"],
        "placeholders_gui": {"icone": "icons/skills/ice_lance.png"}
    },
    {
        "id": "sk_criomante_armadura_de_gelo",
        "nome": "Armadura de Gelo",
        "tipo": "ativa", "categoria": "magico",
        "custo": {"mana": 25, "stamina": 0},
        "multiplicador": 0, "atributo_chave": "inteligencia",
        "precisao": 1.0, "critico_mult": 1.0, "cooldown": 5,
        "descricao": {
            "lore": "O criomante envolve seu corpo em uma camada de gelo místico, que o protege de danos e retalia contra atacantes.",
            "mecanica": "Cria um buff que aumenta a defesa física e mágica por 3 turnos. Inimigos que atacam corpo a corpo têm chance de receber 'Lentidão'."
        },
        "efeitos": [
            {
                "tipo": "buff",
                "valor": {"defesa_fisica": 0.2, "defesa_magica": 0.2},
                "duracao": 3, "chance": 1.0,
                "nome_efeito": "Armadura de Gelo"
            }
        ],
        "requisitos": {"nivel": 10, "classe": "criomante"},
        "tags": ["gelo", "buff", "defensivo"],
        "placeholders_gui": {"icone": "icons/skills/ice_armor.png"}
    },
    # ... (mais 9 exemplos aqui)
    # --- Habilidades Complexas ---
    {
        "id": "sk_criomante_nevasca",
        "nome": "Nevasca",
        "tipo": "ativa", "categoria": "magico",
        "custo": {"mana": 60, "stamina": 0},
        "multiplicador": 1.5, "atributo_chave": "inteligencia",
        "precisao": 1.0, "critico_mult": 1.5, "cooldown": 7,
        "descricao": {
            "lore": "O criomante invoca o poder de uma tempestade de inverno, criando uma nevasca cortante em uma vasta área que pune qualquer um que se mova.",
            "mecanica": "Causa dano de gelo baixo a todos os inimigos na área por 3 turnos. Inimigos na área têm sua velocidade drasticamente reduzida. Se um inimigo tentar usar uma habilidade de movimento, recebe dano extra."
        },
        "efeitos": [
            {
                "tipo": "efeito_terreno",
                "valor": {"dano_por_turno": 0.3, "debuff_velocidade": -0.4, "dano_em_movimento": 1.0},
                "duracao": 3, "chance": 1.0,
                "nome_efeito": "Nevasca"
            }
        ],
        "requisitos": {"nivel": 28, "classe": "criomante"},
        "tags": ["gelo", "area", "controle_terreno", "dano_por_turno", "debuff", "lentidao"],
        "placeholders_gui": {"icone": "icons/skills/blizzard.png"}
    },
    {
        "id": "sk_criomante_prisao_gelida",
        "nome": "Prisão Gélida",
        "tipo": "ativa", "categoria": "magico",
        "custo": {"mana": 45, "stamina": 0},
        "multiplicador": 0.8, "atributo_chave": "inteligencia",
        "precisao": 0.9, "critico_mult": 1.5, "cooldown": 5,
        "descricao": {
            "lore": "Uma magia de controle suprema, onde o criomante aprisiona um inimigo em um caixão de gelo sólido, paralisando-o e tornando-o vulnerável.",
            "mecanica": "Causa dano de gelo baixo e tem alta chance de aplicar o efeito 'Congelado' por 2 turnos. Um alvo 'Congelado' não pode agir. O primeiro ataque físico contra um alvo 'Congelado' o quebra, causando dano crítico garantido."
        },
        "efeitos": [
            {
                "tipo": "debuff",
                "valor": {"status": "Congelado", "vulnerabilidade_fisica_crit": 1.0},
                "duracao": 2, "chance": 0.85,
                "nome_efeito": "Congelado"
            }
        ],
        "requisitos": {"nivel": 35, "classe": "criomante"},
        "tags": ["gelo", "single-target", "controle", "congelamento", "vulnerabilidade"],
        "placeholders_gui": {"icone": "icons/skills/icy_prison.png"}
    },
    # Adicionar mais 8 exemplos aqui
]

# ==============================================================================================
# == SEÇÃO 3: GERADOR DE PLACEHOLDERS ==========================================================
# ==============================================================================================
def gerar_placeholders_gelo(count: int = 50, prefixo: str = "ph_gelo_") -> list:
    """Gera uma lista de dicionários de habilidades de gelo placeholder."""
    placeholders = []
    for i in range(count):
        habilidade = {
            "id": f"{prefixo}{i+1:03d}",
            "nome": f"Magia de Gelo Placeholder #{i+1}",
            "tipo": "ativa", "categoria": "magico",
            "custo": {"mana": 10 + random.randint(0, 50), "stamina": 0},
            "multiplicador": 1.0 + random.random() * 1.5, "atributo_chave": "inteligencia",
            "precisao": 0.98, "critico_mult": 1.5, "cooldown": random.randint(0, 5),
            "descricao": {
                "lore": "Lore a ser definido para esta magia de gelo.",
                "mecanica": "Descrição mecânica a ser definida."
            },
            "efeitos": [], "requisitos": {}, "tags": ["placeholder", "gelo"],
            "placeholders_gui": {"icone": "icons/skills/placeholder_ice.png"}
        }
        placeholders.append(habilidade)
    return placeholders

# ==============================================================================================
# == SEÇÃO 4: CONSTRUÇÃO DO GRIMÓRIO INDEXADO ==================================================
# ==============================================================================================
def construir_grimorio(lista_habilidades: List[Dict]) -> Dict:
    """Constrói um dicionário indexado a partir de uma lista de habilidades."""
    grimorio_por_id = {h["id"]: h for h in lista_habilidades}
    return {"by_id": grimorio_por_id, "lista_completa": lista_habilidades}

HABILIDADES_GELO = HABILIDADES_GELO_EXEMPLOS + gerar_placeholders_gelo(count=100)
GRIMORIO_GELO = construir_grimorio(HABILIDADES_GELO)

# ==============================================================================================
# == SEÇÃO 5: OBSERVAÇÕES DE DESIGN E INTEGRAÇÃO ===============================================
# ==============================================================================================
"""
1.  **Interações Elementais:** O motor de combate deve tratar a interação entre fogo e
    gelo. Por exemplo, usar uma magia de fogo em um alvo 'Congelado' pode causar o
    efeito 'Evaporação', causando dano extra mas removendo ambos os status. Usar gelo
    em um alvo 'Queimando' pode simplesmente anular os dois efeitos.

2.  **Diminishing Returns:** Para habilidades de controle como 'Congelado' e 'Lentidão',
    seria interessante implementar um sistema de 'diminishing returns', onde cada
    aplicação consecutiva do mesmo tipo de controle em um alvo tem uma duração ou
    eficácia menor, para evitar que um chefe seja permanentemente paralisado.

3.  **TO-DO para o Próximo Prompt:**
    - Povoar o grimório com centenas de magias de gelo, criando variações de controle,
      dano e buffs defensivos para as diversas classes que usam gelo.
    - Criar magias que interajam com o ambiente (ex: congelar um rio para criar uma ponte).
"""
