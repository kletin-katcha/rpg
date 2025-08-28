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
        "nome": "Cura Leve", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 10,
        "descricao": "Cura uma pequena quantidade de ferimentos em um alvo.",
        "tipo_alvo": "aliado_unico", "efeitos": [{"tipo": "cura", "escala_com": "sabedoria", "multiplicador_cura": 1.5}]
    },
    "cura_em_area": {
        "nome": "Cura em Área", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 40, "cooldown": 4,
        "descricao": "Invoca uma prece que cura todos os aliados próximos.",
        "tipo_alvo": "aliados_area", "efeitos": [{"tipo": "cura", "escala_com": "sabedoria", "multiplicador_cura": 1.2}]
    },

    # --- HABILIDADES DE GUERREIRO ---
    "grito_de_guerra": {
        "nome": "Grito de Guerra", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 15,
        "descricao": "Um grito poderoso que aumenta o ataque do grupo.",
        "tipo_alvo": "aliados_area", "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_ataque_pequeno", "duracao": 3}]
    },

    # --- HABILIDADES DE LADINO ---
    "veneno_debilitante": {
        "nome": "Veneno Debilitante", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 20, "cooldown": 3,
        "descricao": "Aplica um veneno nas armas que reduz a força e a destreza do alvo.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "debuff_veneno_debilitante", "duracao": 3}]
    },
    "distracao": {
        "nome": "Distração", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 15, "cooldown": 4,
        "descricao": "Cria uma distração que força um inimigo a perder seu próximo turno.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "status_confuso", "chance": 0.7, "duracao": 1}]
    },

    # --- CLASSES AVANÇADAS ---
    "frenesi_de_batalha": {
        "nome": "Frenesi de Batalha", "tipo": "passiva",
        "descricao": "Passiva: Causa mais dano quanto menor for sua vida.",
        "efeitos": [{"tipo": "modificador_dano_dinamico", "atributo_base": "hp_percentual_restante", "max_bonus": 0.5, "inverter": True}] # 50% de dano extra com 0% de vida
    },
    "totem_de_protecao": {
        "nome": "Totem de Proteção", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 30, "cooldown": 6,
        "descricao": "Posiciona um totem que aumenta a defesa de todos os aliados por vários turnos.",
        "tipo_alvo": "self", # O totem é um efeito de área que se origina do jogador
        "efeitos": [{"tipo": "invocar_objeto", "id_objeto": "totem_defesa_pequeno", "duracao": 4}]
    },
    "espirito_do_urso": {
        "nome": "Espírito do Urso", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 40, "cooldown": 5,
        "descricao": "Invoca o espírito do urso, aumentando sua constituição e vida máxima temporariamente.",
        "tipo_alvo": "self", "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_espirito_urso", "duracao": 4}]
    },
    "ataque_coordenado_aprimorado": {
        "nome": "Ataque Coordenado Aprimorado", "tipo": "passiva",
        "descricao": "Passiva: Aumenta permanentemente o dano e a precisão do seu companheiro animal.",
        "efeitos": [{"tipo": "modificador_companheiro", "atributo": "dano", "valor": 10}, {"tipo": "modificador_companheiro", "atributo": "precisao", "valor": 15}]
    },
    "furia_bestial": {
        "nome": "Fúria Bestial", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 50, "cooldown": 6,
        "descricao": "Enfurece seu companheiro animal, aumentando drasticamente seu dano e velocidade por um curto período.",
        "tipo_alvo": "companheiro", "efeitos": [{"tipo": "aplicar_efeito_companheiro", "id_efeito": "buff_furia_bestial", "duracao": 3}]
    },
    "sonata_da_inspiracao": {
        "nome": "Sonata da Inspiração", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 50, "cooldown": 6,
        "descricao": "Uma canção magnífica que concede um grande bônus de ataque e defesa a um único aliado.",
        "tipo_alvo": "aliado_unico", "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_sonata_inspiracao", "duracao": 4}]
    }
}
