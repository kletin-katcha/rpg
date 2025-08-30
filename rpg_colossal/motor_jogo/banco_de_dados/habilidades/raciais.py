# -*- coding: utf-8 -*-
"""
################################################################################################
##                                                                                            ##
##    ██████╗  █████╗  ██████╗██╗ █████╗ ██╗     █████╗ ██╗     ███████╗                         ##
##    ██╔══██╗██╔══██╗██╔════╝██║██╔══██╗██║    ██╔══██╗██║     ██╔════╝                         ##
##    ██████╔╝███████║██║     ██║███████║██║    ███████║██║     ███████╗                         ##
##    ██╔══██╗██╔══██║██║     ██║██╔══██║██║    ██╔══██║██║     ╚════██║                         ##
##    ██║  ██║██║  ██║╚██████╗██║██║  ██║███████╗██║  ██║███████╗███████║                         ##
##    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝                         ##
##                                                                                            ##
################################################################################################
################################################################################################

================================================================================================
BANCO DE DADOS: HABILIDADES RACIAIS
================================================================================================
Este arquivo define as habilidades únicas e inatas de cada raça em Aetheria. Essas
habilidades refletem a biologia, cultura e afinidades naturais de uma raça e estão
disponíveis para o personagem desde o nível 1, independentemente de sua classe.

-------------------------
-- ESTRUTURA DE DADOS --
-------------------------
A estrutura segue o padrão global, com a `categoria` sempre sendo "racial". Os
requisitos aqui são geralmente vazios, pois a habilidade é concedida pela raça.

- id (str): Convenção: "sk_raca_<nome_slug>".
- nome, tipo, categoria, custo, multiplicador, atributo_chave, precisao,
  critico_mult, cooldown, descricao, efeitos, requisitos, tags, placeholders_gui.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import random
from typing import List, Dict, Any

# ==============================================================================================
# == SEÇÃO 2: HABILIDADES RACIAIS DE EXEMPLO ===================================================
# ==============================================================================================
HABILIDADES_RACIAIS_EXEMPLOS = [
    # --- Habilidades Humanas ---
    {
        "id": "sk_humano_diplomacia",
        "nome": "Diplomacia Humana",
        "tipo": "passiva", "categoria": "racial",
        "custo": {"mana": 0, "stamina": 0},
        "multiplicador": 0.1, "atributo_chave": "carisma",
        "precisao": 1.0, "critico_mult": 1.0, "cooldown": 0,
        "descricao": {
            "lore": "A capacidade humana de se adaptar e se conectar com outras culturas lhes concede uma vantagem natural em situações sociais.",
            "mecanica": "Aumenta passivamente os ganhos de reputação em 10% e melhora as chances de sucesso em testes de persuasão."
        },
        "efeitos": [{"tipo": "buff_passivo", "valor": {"ganho_reputacao": 0.1}}],
        "requisitos": {"raca": "humano"},
        "tags": ["social", "passiva"],
        "placeholders_gui": {"icone": "icons/skills/human_diplomacy.png"}
    },
    {
        "id": "sk_humano_vontade_de_ferro",
        "nome": "Vontade de Ferro",
        "tipo": "ativa", "categoria": "racial",
        "custo": {"mana": 0, "stamina": 30},
        "multiplicador": 0, "atributo_chave": "constituicao",
        "precisao": 1.0, "critico_mult": 1.0, "cooldown": 10,
        "descricao": {
            "lore": "Em face do perigo, o espírito humano pode se tornar inquebrável, ignorando o medo e a dor.",
            "mecanica": "Remove efeitos de Medo e concede imunidade a Medo por 3 turnos."
        },
        "efeitos": [
            {"tipo": "limpar_debuff", "valor": "Medo", "duracao": 0, "chance": 1.0},
            {"tipo": "buff", "valor": {"imunidade_status": "Medo"}, "duracao": 3, "chance": 1.0, "nome_efeito": "Vontade de Ferro"}
        ],
        "requisitos": {"raca": "humano"},
        "tags": ["defensivo", "mental", "buff"],
        "placeholders_gui": {"icone": "icons/skills/iron_will.png"}
    },
    # --- Habilidades Élficas ---
    {
        "id": "sk_elfo_passo_silencioso",
        "nome": "Passo Silencioso",
        "tipo": "passiva", "categoria": "racial",
        "custo": {"mana": 0, "stamina": 0},
        "multiplicador": 0.15, "atributo_chave": "destreza",
        "precisao": 1.0, "critico_mult": 1.0, "cooldown": 0,
        "descricao": {
            "lore": "A graça natural dos elfos permite que eles se movam através de terrenos naturais sem fazer som.",
            "mecanica": "Aumenta a eficácia da furtividade em 15% em ambientes de floresta ou planície."
        },
        "efeitos": [{"tipo": "buff_passivo_condicional", "condicao": "terreno_floresta", "valor": {"furtividade": 0.15}}],
        "requisitos": {"raca": "elfo"},
        "tags": ["furtividade", "passiva", "condicional"],
        "placeholders_gui": {"icone": "icons/skills/silent_step.png"}
    },
    # --- Habilidades Anãs ---
    {
        "id": "sk_anao_pele_de_pedra",
        "nome": "Pele de Pedra",
        "tipo": "ativa", "categoria": "racial",
        "custo": {"mana": 0, "stamina": 25},
        "multiplicador": 0.5, "atributo_chave": "constituicao",
        "precisao": 1.0, "critico_mult": 1.0, "cooldown": 8,
        "descricao": {
            "lore": "A pele de um anão, já naturalmente resistente, pode se enrijecer misticamente para se assemelhar à rocha da montanha de onde vieram.",
            "mecanica": "Aumenta a defesa física em 50% por 3 turnos."
        },
        "efeitos": [
            {"tipo": "buff", "valor": {"defesa_fisica": 0.5}, "duracao": 3, "chance": 1.0, "nome_efeito": "Pele de Pedra"}
        ],
        "requisitos": {"raca": "anao"},
        "tags": ["defensivo", "buff", "fisico"],
        "placeholders_gui": {"icone": "icons/skills/stoneform.png"}
    },
]

# ==============================================================================================
# == SEÇÃO 3: GERADOR DE PLACEHOLDERS ==========================================================
# ==============================================================================================
def gerar_placeholders_raciais(count: int = 20, prefixo: str = "ph_racial_") -> list:
    """Gera uma lista de dicionários de habilidades raciais placeholder."""
    placeholders = []
    for i in range(count):
        habilidade = {
            "id": f"{prefixo}{i+1:03d}",
            "nome": f"Habilidade Racial Placeholder #{i+1}",
            "tipo": random.choice(["ativa", "passiva"]), "categoria": "racial",
            "custo": {"mana": 0, "stamina": random.randint(0, 20)},
            "multiplicador": random.random(), "atributo_chave": "constituicao",
            "precisao": 1.0, "critico_mult": 1.0, "cooldown": random.randint(0, 10),
            "descricao": {
                "lore": "Lore a ser definido para esta habilidade racial.",
                "mecanica": "Descrição mecânica a ser definida."
            },
            "efeitos": [], "requisitos": {"raca": "placeholder"}, "tags": ["placeholder", "racial"],
            "placeholders_gui": {"icone": "icons/skills/placeholder_racial.png"}
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

HABILIDADES_RACIAIS = HABILIDADES_RACIAIS_EXEMPLOS + gerar_placeholders_raciais(count=50)
GRIMORIO_RACIAL = construir_grimorio(HABILIDADES_RACIAIS)

# ==============================================================================================
# == SEÇÃO 5: OBSERVAÇÕES DE DESIGN E INTEGRAÇÃO ===============================================
# ==============================================================================================
"""
1.  **Atribuição na Criação:** O `motor_jogo/entidades/personagem.py` deve, ao criar um
    personagem, iterar sobre este arquivo e adicionar os IDs de todas as habilidades
    que correspondem à raça escolhida para a lista de `habilidades_conhecidas` do
    personagem.

2.  **Habilidades de Evolução:** Habilidades de raças evoluídas (como 'Humano Abençoado')
    também serão armazenadas aqui. Seus `requisitos` conterão a `id_raca` da forma
    evoluída. O `gerenciador_evolucoes` será responsável por conceder essas
    habilidades ao personagem no momento da evolução.

3.  **TO-DO para o Próximo Prompt:**
    - Povoar o grimório com as habilidades raciais para todas as raças base e
      evoluções planejadas.
    - Criar habilidades raciais mais complexas, talvez algumas que mudem
      dependendo da hora do dia no jogo ou do ambiente.
"""
