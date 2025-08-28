# ==============================================================================
# ARQUIVO DE DADOS: HABILIDADES DE SUPORTE
# ==============================================================================
#
# Este arquivo contém as definições para habilidades de suporte, como curas,
# buffs, debuffs e outras utilidades.
#
# ==============================================================================

HABILIDADES_SUPORTE = {
    # --- HABILIDADES DE CLÉRIGO ---
    "cura_leve": {
        "nome": "Cura Leve",
        "tipo": "ativa",
        "custo_tipo": "mp",
        "custo_valor": 10,
        "descricao": "Cura uma pequena quantidade de ferimentos em um alvo.",
        "tipo_alvo": "aliado_unico",
        "efeitos": [
            {"tipo": "cura", "escala_com": "sabedoria", "multiplicador_cura": 1.5}
        ]
    },
    "cura_em_area": {
        "nome": "Cura em Área",
        "tipo": "ativa",
        "custo_tipo": "mp",
        "custo_valor": 40,
        "cooldown": 4,
        "descricao": "Invoca uma prece que cura todos os aliados próximos.",
        "tipo_alvo": "aliados_area",
        "efeitos": [
            {"tipo": "cura", "escala_com": "sabedoria", "multiplicador_cura": 1.2}
        ]
    },

    # --- HABILIDADES DE GUERREIRO ---
    "grito_de_guerra": {
        "nome": "Grito de Guerra",
        "tipo": "ativa",
        "custo_tipo": "stamina",
        "custo_valor": 15,
        "descricao": "Um grito poderoso que aumenta o ataque do grupo.",
        "tipo_alvo": "aliados_area",
        "efeitos": [
            {"tipo": "aplicar_efeito", "id_efeito": "buff_ataque_pequeno", "duracao": 3}
        ]
    },
    "furia_interminavel": {
        "nome": "Fúria Interminável",
        "tipo": "passiva",
        "descricao": "Sua fúria em batalha é tão intensa que você regenera vigor a cada turno.",
        "efeitos": [{"tipo": "modificador_regeneracao", "recurso": "stamina", "valor": 10}]
    },

    # --- HABILIDADES DE LADINO ---
    "veneno_debilitante": {
        "nome": "Veneno Debilitante",
        "tipo": "ativa",
        "custo_tipo": "stamina",
        "custo_valor": 20,
        "cooldown": 3,
        "descricao": "Aplica um veneno nas armas que reduz a força e a destreza do alvo.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "debuff_veneno_debilitante", "duracao": 3}]
    },
    "distracao": {
        "nome": "Distração",
        "tipo": "ativa",
        "custo_tipo": "stamina",
        "custo_valor": 15,
        "cooldown": 4,
        "descricao": "Cria uma distração que força um inimigo a perder seu próximo turno.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "status_confuso", "chance": 0.7, "duracao": 1}]
    }
}
