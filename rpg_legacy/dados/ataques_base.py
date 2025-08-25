# ==============================================================================
# ARQUIVO DE DADOS: TIPOS DE ATAQUES BÁSICOS
# ==============================================================================
#
# Este arquivo define diferentes estilos de ataque básico que as classes
# podem usar. Isso adiciona uma camada de escolha tática ao combate básico.
#
# Estrutura de cada Ataque:
# --------------------------
# "nome": (str) O nome do tipo de ataque.
# "descricao": (str) Uma breve descrição da escolha tática.
# "multiplicador_dano": (float) Multiplicador aplicado ao dano base do personagem.
# "mod_precisao": (float) Bônus ou penalidade na chance de acertar (ex: 1.1 para +10%).
# "custo_stamina": (int) Custo de vigor para usar este tipo de ataque.
# "tipo_dano": (str) "fisico" ou "magico".
#
# ==============================================================================

ATAQUES_BASE = {
    # --- Ataques Humanoides Padrão ---
    "soco": {
        "nome": "Soco",
        "descricao": "Um golpe rápido e direto. Custo baixo, dano baixo.",
        "multiplicador_dano": 0.8,
        "mod_precisao": 1.1, # +10% precisão
        "custo_stamina": 5,
        "tipo_dano": "fisico"
    },
    "chute": {
        "nome": "Chute",
        "descricao": "Um golpe mais forte que um soco, mas que consome mais vigor.",
        "multiplicador_dano": 1.0,
        "mod_precisao": 1.0,
        "custo_stamina": 10,
        "tipo_dano": "fisico"
    },

    # --- Ataques de Bestas ---
    "mordida": {
        "nome": "Mordida",
        "descricao": "Uma mordida poderosa que causa dano significativo.",
        "multiplicador_dano": 1.2,
        "mod_precisao": 0.95, # -5% precisão
        "custo_stamina": 12,
        "tipo_dano": "fisico"
    },
    "garra": {
        "nome": "Garra",
        "descricao": "Um ataque rápido com garras afiadas. Preciso e eficaz.",
        "multiplicador_dano": 0.9,
        "mod_precisao": 1.15, # +15% precisão
        "custo_stamina": 8,
        "tipo_dano": "fisico"
    },
    "cabeçada": {
        "nome": "Cabeçada",
        "descricao": "Um ataque bruto e desesperado. Alto dano, baixa precisão.",
        "multiplicador_dano": 1.4,
        "mod_precisao": 0.8, # -20% precisão
        "custo_stamina": 15,
        "tipo_dano": "fisico"
    },
    "picada": {
        "nome": "Picada",
        "descricao": "Um ataque perfurante quase impossível de errar, mas de dano baixo.",
        "multiplicador_dano": 0.6,
        "mod_precisao": 1.3, # +30% precisão
        "custo_stamina": 4,
        "tipo_dano": "fisico"
    },
    "bicada": {
        "nome": "Bicada",
        "descricao": "Um ataque focado em um ponto vital. Bom dano e precisão.",
        "multiplicador_dano": 1.1,
        "mod_precisao": 1.1, # +10% precisão
        "custo_stamina": 10,
        "tipo_dano": "fisico"
    },

    # --- Ataques de Força Bruta ---
    "pancada": {
        "nome": "Pancada",
        "descricao": "Um golpe esmagador e lento. Dano massivo, mas fácil de desviar.",
        "multiplicador_dano": 1.6,
        "mod_precisao": 0.75, # -25% precisão
        "custo_stamina": 20,
        "tipo_dano": "fisico"
    },
    "patada": {
        "nome": "Patada",
        "descricao": "Um golpe pesado com uma pata. Bom dano e custo moderado.",
        "multiplicador_dano": 1.3,
        "mod_precisao": 0.9, # -10% precisão
        "custo_stamina": 15,
        "tipo_dano": "fisico"
    }
}
