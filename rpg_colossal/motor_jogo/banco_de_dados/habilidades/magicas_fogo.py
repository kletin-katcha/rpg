# -*- coding: utf-8 -*-
"""
################################################################################################
##                                                                                            ##
##    ███╗   ███╗ █████╗  ██████╗ ██╗ ██████╗     █████╗      ██████╗  ██████╗  ██████╗          ##
##    ████╗ ████║██╔══██╗██╔════╝ ██║██╔═══██╗   ██╔══██╗    ██╔═══██╗██╔═══██╗██╔═══██╗         ##
##    ██╔████╔██║███████║██║  ███╗██║██║   ██║   ███████║    ██║   ██║██║   ██║██║   ██║         ##
##    ██║╚██╔╝██║██╔══██║██║   ██║██║██║   ██║   ██╔══██║    ██║   ██║██║   ██║██║   ██║         ##
##    ██║ ╚═╝ ██║██║  ██║╚██████╔╝██║╚██████╔╝   ██║  ██║    ╚██████╔╝╚██████╔╝╚██████╔╝         ##
##    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝ ╚═════╝    ╚═╝  ╚═╝     ╚═════╝  ╚═════╝  ╚═════╝          ##
##                                                                                            ##
################################################################################################
################################################################################################

================================================================================================
BANCO DE DADOS: HABILIDADES MÁGICAS - FOGO
================================================================================================
Este arquivo contém a definição de todas as habilidades da escola de magia do Fogo.
A Piromancia é uma arte arcana focada no poder bruto, destrutivo e caótico das chamas.
As habilidades aqui são caracterizadas por alto dano, efeitos de dano ao longo do
tempo (queimadura) e, por vezes, efeitos de área.

-------------------------
-- ESTRUTURA DE DADOS --
-------------------------
A estrutura de cada habilidade segue o padrão definido no grimório global, com
ênfase em campos como `custo` (mana), `efeitos` (queimadura) e `tags` (fogo, area).

- id, nome, tipo, categoria, custo, multiplicador, atributo_chave, precisao,
  critico_mult, cooldown, descricao, efeitos, requisitos, tags, placeholders_gui.

---------------------------------
-- EXEMPLO DE CONSUMO (COMBATE) --
---------------------------------
'''
# No CombatManager, ao resolver um feitiço de fogo
def resolver_magia_fogo(conjurador, alvos, magia):
    # Custo de Mana
    conjurador.stats['mana'] -= magia['custo']['mana']

    # Para cada alvo (magias de fogo são frequentemente em área)
    for alvo in alvos:
        # Teste de Resistência Mágica em vez de precisão física
        if random.random() < alvo.stats['resistencia_magica']:
            return f"{alvo.nome} resistiu à magia!"

        # Dano Mágico
        dano_base = conjurador.stats[magia['atributo_chave']] * magia['multiplicador']
        dano_final = dano_base * (1 - alvo.stats['resistencia_fogo'])

        # Aplicar Efeitos (ex: Queimadura)
        for efeito in magia['efeitos']:
            if efeito['tipo'] == 'dano_por_turno' and efeito['nome_efeito'] == 'Queimadura':
                alvo.aplicar_efeito(efeito)
'''
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import random
from typing import List, Dict, Any

# ==============================================================================================
# == SEÇÃO 2: HABILIDADES DE FOGO DE EXEMPLO ===================================================
# ==============================================================================================
HABILIDADES_FOGO_EXEMPLOS = [
    # --- Habilidades Simples ---
    {
        "id": "sk_mago_seta_de_fogo",
        "nome": "Seta de Fogo",
        "tipo": "ativa", "categoria": "magico",
        "custo": {"mana": 10, "stamina": 0},
        "multiplicador": 1.2, "atributo_chave": "inteligencia",
        "precisao": 1.0, "critico_mult": 1.5, "cooldown": 0,
        "descricao": {
            "lore": "O primeiro feitiço que todo acólito do fogo aprende. Uma simples manifestação de vontade arcana em forma de uma pequena chama teleguiada.",
            "mecanica": "Causa dano de fogo baixo a um único alvo. Custo de mana muito baixo."
        },
        "efeitos": [],
        "requisitos": {"classe": "mago"},
        "tags": ["fogo", "single-target"],
        "placeholders_gui": {"icone": "icons/skills/fire_bolt.png"}
    },
    {
        "id": "sk_piromante_bola_de_fogo",
        "nome": "Bola de Fogo",
        "tipo": "ativa", "categoria": "magico",
        "custo": {"mana": 40, "stamina": 0},
        "multiplicador": 2.0, "atributo_chave": "inteligencia",
        "precisao": 1.0, "critico_mult": 1.6, "cooldown": 3,
        "descricao": {
            "lore": "Um feitiço clássico e temido. O piromante condensa uma grande quantidade de energia ígnea em uma esfera instável e a arremessa, resultando em uma explosão devastadora.",
            "mecanica": "Causa alto dano de fogo a todos os inimigos em uma área. Chance de aplicar 'Queimadura'."
        },
        "efeitos": [
            {
                "tipo": "dano_por_turno",
                "valor": 0.2, "duracao": 2, "chance": 0.5,
                "nome_efeito": "Queimadura"
            }
        ],
        "requisitos": {"nivel": 10, "classe": "piromante"},
        "tags": ["fogo", "area", "dano_alto", "queimadura"],
        "placeholders_gui": {"icone": "icons/skills/fireball.png"}
    },
    # ... (mais 9 exemplos aqui)
    {
        "id": "sk_piromante_manto_de_chamas",
        "nome": "Manto de Chamas",
        "tipo": "ativa", "categoria": "magico",
        "custo": {"mana": 30, "stamina": 0},
        "multiplicador": 0, "atributo_chave": "inteligencia",
        "precisao": 1.0, "critico_mult": 1.0, "cooldown": 5,
        "descricao": {
            "lore": "O piromante se envolve em uma aura de fogo protetora, que queima qualquer um que ouse se aproximar.",
            "mecanica": "Cria um buff que dura 3 turnos. Aumenta a resistência a gelo e causa dano de fogo a qualquer inimigo que ataque o conjurador corpo a corpo."
        },
        "efeitos": [
            {
                "tipo": "buff",
                "valor": {"resistencia_gelo": 0.5, "dano_retorno": 0.5},
                "duracao": 3, "chance": 1.0,
                "nome_efeito": "Manto de Chamas"
            }
        ],
        "requisitos": {"nivel": 15, "classe": "piromante"},
        "tags": ["fogo", "buff", "defensivo", "dano_retorno"],
        "placeholders_gui": {"icone": "icons/skills/flame_cloak.png"}
    },
    # --- Habilidades Complexas ---
    {
        "id": "sk_piromante_chao_consagrado",
        "nome": "Chão Consagrado pelas Chamas",
        "tipo": "ativa", "categoria": "magico",
        "custo": {"mana": 50, "stamina": 0},
        "multiplicador": 0.5, "atributo_chave": "inteligencia",
        "precisao": 1.0, "critico_mult": 1.5, "cooldown": 6,
        "descricao": {
            "lore": "Uma técnica avançada onde o piromante não ataca os inimigos, mas o próprio chão sob seus pés, transformando a área em um inferno ardente por vários turnos.",
            "mecanica": "Causa dano de fogo baixo a todos os inimigos na área e cria um efeito de 'Chão em Chamas' por 3 turnos. Inimigos que começam seu turno na área recebem dano de fogo e têm sua resistência a fogo reduzida."
        },
        "efeitos": [
            {
                "tipo": "efeito_terreno",
                "valor": {"dano_por_turno": 0.4, "debuff_res_fogo": -0.25},
                "duracao": 3, "chance": 1.0,
                "nome_efeito": "Chão em Chamas"
            }
        ],
        "requisitos": {"nivel": 25, "classe": "piromante"},
        "tags": ["fogo", "area", "controle_terreno", "dano_por_turno", "debuff"],
        "placeholders_gui": {"icone": "icons/skills/consecrated_ground.png"}
    },
    {
        "id": "sk_piromante_combustao_espontanea",
        "nome": "Combustão Espontânea",
        "tipo": "ativa", "categoria": "magico",
        "custo": {"mana": 35, "stamina": 0},
        "multiplicador": 1.0, "atributo_chave": "inteligencia",
        "precisao": 0.9, "critico_mult": 2.0, "cooldown": 4,
        "descricao": {
            "lore": "O piromante foca em um alvo que já está queimando, intensificando as chamas existentes até que elas explodam de dentro para fora.",
            "mecanica": "Causa dano de fogo moderado. Se o alvo já estiver sob o efeito 'Queimadura', o efeito é consumido e o dano desta habilidade é dobrado. A explosão também aplica 'Queimadura' a alvos adjacentes."
        },
        "efeitos": [
            {
                "tipo": "dano_extra_condicional",
                "valor": 2.0, "duracao": 0, "chance": 1.0,
                "condicao": "alvo_queimando"
            },
            {
                "tipo": "aplicar_efeito_adjacente",
                "valor": {"tipo": "dano_por_turno", "valor": 0.2, "duracao": 2, "chance": 0.7, "nome_efeito": "Queimadura"},
                "duracao": 0, "chance": 1.0,
                "condicao": "alvo_queimando"
            }
        ],
        "requisitos": {"nivel": 30, "classe": "piromante"},
        "tags": ["fogo", "single-target", "condicional", "combo"],
        "placeholders_gui": {"icone": "icons/skills/spontaneous_combustion.png"}
    },
    # Adicionar mais 7 exemplos aqui
]

# ==============================================================================================
# == SEÇÃO 3: GERADOR DE PLACEHOLDERS ==========================================================
# ==============================================================================================
def gerar_placeholders_fogo(count: int = 50, prefixo: str = "ph_fogo_") -> list:
    """Gera uma lista de dicionários de habilidades de fogo placeholder."""
    placeholders = []
    for i in range(count):
        habilidade = {
            "id": f"{prefixo}{i+1:03d}",
            "nome": f"Magia de Fogo Placeholder #{i+1}",
            "tipo": "ativa", "categoria": "magico",
            "custo": {"mana": 10 + random.randint(0, 50), "stamina": 0},
            "multiplicador": 1.0 + random.random() * 2, "atributo_chave": "inteligencia",
            "precisao": 0.95, "critico_mult": 1.5, "cooldown": random.randint(0, 5),
            "descricao": {
                "lore": "Lore a ser definido para esta magia de fogo.",
                "mecanica": "Descrição mecânica a ser definida."
            },
            "efeitos": [], "requisitos": {}, "tags": ["placeholder", "fogo"],
            "placeholders_gui": {"icone": "icons/skills/placeholder_fire.png"}
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

HABILIDADES_FOGO = HABILIDADES_FOGO_EXEMPLOS + gerar_placeholders_fogo(count=100)
GRIMORIO_FOGO = construir_grimorio(HABILIDADES_FOGO)

# ==============================================================================================
# == SEÇÃO 5: OBSERVAÇÕES DE DESIGN E INTEGRAÇÃO ===============================================
# ==============================================================================================
"""
1.  **Resistências Elementais:** O motor de combate (`combate.py`) deve ter uma
    lógica para verificar a `resistencia_fogo` do alvo. O dano final seria
    calculado como `dano * (1 - alvo.resistencia_fogo)`. Uma resistência de 0.5
    reduz o dano pela metade, enquanto uma de -0.5 (vulnerabilidade) aumenta.

2.  **Interações de Efeitos:** Habilidades de gelo podem anular o efeito 'Queimadura',
    e vice-versa. O sistema de efeitos deve ter uma lógica para checar e remover
    efeitos opostos.

3.  **TO-DO para o Próximo Prompt:**
    - Povoar o grimório com centenas de magias de fogo, criando variações de dano,
      área de efeito, e efeitos secundários para as diversas classes que usam fogo.
    - Criar magias que interajam com o ambiente (ex: incendiar uma poça de óleo).
"""
