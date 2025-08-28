# ==============================================================================
# ARQUIVO DE DADOS: HABILIDADES FÍSICAS
# ==============================================================================
#
# Este arquivo contém as definições para habilidades baseadas em atributos
# físicos como Força e Destreza.
#
# ==============================================================================

HABILIDADES_FISICAS = {
    # --- HABILIDADES DE GUERREIRO ---
    "ataque_poderoso": {
        "nome": "Ataque Poderoso", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 15,
        "descricao": "Um golpe pesado que sacrifica precisão por dano bruto.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.5, "penalidade_precisao": 0.2}]
    },

    # --- HABILIDADES DE LADINO ---
    "ataque_furtivo": {
        "nome": "Ataque Furtivo", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 25,
        "descricao": "Um ataque preciso em um ponto vital. Causa dano massivo se o usuário não for o foco do alvo.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico_condicional", "condicao": "alvo_nao_focado_em_usuario", "escala_com": "destreza", "multiplicador_dano_bonus": 3.0, "multiplicador_dano_normal": 1.0}]
    },
    "disparada": {
        "nome": "Disparada", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 10,
        "descricao": "Move-se rapidamente, tornando-se muito mais difícil de acertar por um curto período.",
        "tipo_alvo": "self", "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_esquiva_grande", "duracao": 1}]
    },
    "arremessar_adaga": {
        "nome": "Arremessar Adaga", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 5,
        "descricao": "Arremessa uma adaga com precisão. Um ataque à distância rápido e de baixo custo.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 0.8}]
    },

    # --- HABILIDADES DE BÁRBARO ---
    "furia_selvagem": {
        "nome": "Fúria Selvagem", "tipo": "ativa", "custo_tipo": "recurso_especial", "custo_valor": 50,
        "descricao": "Entra em um estado de fúria, aumentando o dano causado e a resistência a dano, mas diminuindo a defesa.",
        "tipo_alvo": "self", "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "estado_furia_barbaro", "duracao": 5}]
    },
    "golpe_brutal": {
        "nome": "Golpe Brutal", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 20,
        "descricao": "Um ataque devastador que ignora uma porção da armadura do inimigo.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.2, "penetracao_armadura": 0.3}]
    },

    # --- HABILIDADES DE RANGER ---
    "tiro_certeiro": {
        "nome": "Tiro Certeiro", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 15,
        "descricao": "Um disparo cuidadosamente mirado que causa dano extra e tem alta chance de acerto crítico.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 1.3, "bonus_chance_critico": 0.25}]
    },

    # --- HABILIDADES DE PALADINO ---
    "golpe_divino": {
        "nome": "Golpe Divino", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 20,
        "descricao": "Imbui sua arma com energia sagrada, causando dano físico e mágico extra no próximo ataque.",
        "tipo_alvo": "self", "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_golpe_divino", "duracao": 1}]
    },

    # --- HABILIDADES FÍSICAS GERAIS ---
    "corte_transversal": {
        "nome": "Corte Transversal", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 20,
        "descricao": "Um rápido corte horizontal que pode atingir múltiplos inimigos próximos.",
        "tipo_alvo": "inimigos_area", "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 0.8}]
    },
    "aparar": {
        "nome": "Aparar", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 10,
        "descricao": "Antecipa um ataque corpo a corpo, bloqueando-o e criando uma abertura para um contra-ataque.",
        "tipo_alvo": "self", "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_aparar", "duracao": 1}]
    },
    "tiro_duplo": {
        "nome": "Tiro Duplo", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 25,
        "descricao": "Dispara duas flechas em rápida sucessão no mesmo alvo.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 0.9}, {"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 0.9}]
    },
    "flecha_farpada": {
        "nome": "Flecha Farpada", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 15,
        "descricao": "Dispara uma flecha com farpas que causa dano de sangramento ao longo do tempo.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 0.7}, {"tipo": "aplicar_efeito", "id_efeito": "sangramento_fraco", "duracao": 3}]
    },
    "estocada_perfurante": {
        "nome": "Estocada Perfurante", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 15,
        "descricao": "Uma estocada focada que visa as brechas na armadura do inimigo.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.1, "penetracao_armadura": 0.4}]
    },
    "quebra_ossos": {
        "nome": "Quebra-Ossos", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 20,
        "descricao": "Um golpe poderoso que visa as articulações, com chance de reduzir a capacidade de ataque do inimigo.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.3}, {"tipo": "aplicar_efeito", "id_efeito": "debuff_ataque_pequeno", "chance": 0.3, "duracao": 3}]
    },
    "intimidar": {
        "nome": "Intimidar", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 10,
        "descricao": "Usa sua presença física para intimidar um alvo, potencialmente o assustando.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "medo", "duracao": 2, "escala_com": "forca"}]
    },

    # --- HABILIDADES DE MONGE ---
    "rajada_de_golpes": {
        "nome": "Rajada de Golpes", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 20,
        "descricao": "Desfere uma sequência rápida de dois ataques desarmados.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 0.7}, {"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 0.7}]
    },
    "paciencia_defensiva": {
        "nome": "Paciência Defensiva", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 10,
        "descricao": "Assume uma postura que aumenta a esquiva e prepara para um contra-ataque.",
        "tipo_alvo": "self", "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_esquiva_grande", "duracao": 1}]
    },

    # --- HABILIDADES DE CAVALEIRO (KNIGHT) ---
    "provocar": {
        "nome": "Provocar", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 10,
        "descricao": "Chama a atenção de um inimigo, forçando-o a atacar você.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "status_provocado", "duracao": 2}]
    },
    "golpe_de_escudo": {
        "nome": "Golpe de Escudo", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 15,
        "descricao": "Ataca com o escudo, causando dano baixo mas com chance de atordoar.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 0.5}, {"tipo": "aplicar_efeito", "id_efeito": "atordoamento", "chance": 0.2, "duracao": 1}]
    },

    # --- HABILIDADES DE PISTOLEIRO (GUNSLINGER) ---
    "tiro_rapido": {
        "nome": "Tiro Rápido", "tipo": "ativa", "custo_tipo": "recurso_especial", "custo_valor": 1,
        "descricao": "Um disparo rápido da anca, menos preciso mas veloz.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 1.1, "penalidade_precisao": 0.15}]
    },
    "ricochete": {
        "nome": "Ricochete", "tipo": "ativa", "custo_tipo": "recurso_especial", "custo_valor": 2,
        "descricao": "Atira em uma superfície para que a bala ricocheteie e atinja um segundo inimigo.",
        "tipo_alvo": "inimigos_area", "efeitos": [{"tipo": "dano_fisico_em_cadeia", "escala_com": "destreza", "multiplicador_dano": 1.0, "max_saltos": 1}]
    },

    # --- CLASSES AVANÇADAS ---
    "postura_de_mestre": {
        "nome": "Postura de Mestre", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 20, "cooldown": 5,
        "descricao": "Assume uma postura de combate perfeita, aumentando drasticamente a precisão e o dano crítico por um tempo.",
        "tipo_alvo": "self", "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_postura_mestre", "duracao": 3}]
    },
    "golpe_mortal": {
        "nome": "Golpe Mortal", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 40, "cooldown": 4,
        "descricao": "Um único golpe devastador. Se o alvo estiver com menos de 25% de vida, o dano é massivamente aumentado.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "dano_fisico_condicional", "condicao": "alvo_hp_abaixo_25_porcento", "escala_com": "forca", "multiplicador_dano_bonus": 4.0, "multiplicador_dano_normal": 1.8}]
    },
    "golpe_imprudente": {
        "nome": "Golpe Imprudente", "tipo": "ativa", "custo_tipo": "hp", "custo_valor": 15, # Custa vida
        "descricao": "Um ataque selvagem que causa dano massivo tanto ao alvo quanto a si mesmo.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "dano_fisico_bruto", "dano": 100}] # Dano fixo, ignora defesa
    },
    "ataque_exposto": {
        "nome": "Ataque Exposto", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 25, "cooldown": 3,
        "descricao": "Explora uma fraqueza na defesa do inimigo, aplicando um debuff de defesa e causando dano.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 1.2}, {"tipo": "aplicar_efeito", "id_efeito": "debuff_defesa_media", "duracao": 3}]
    },
    "roubar_item": {
        "nome": "Roubar Item", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 30, "cooldown": 10,
        "descricao": "Tenta roubar um item do inventário do alvo durante o combate.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "roubar", "chance_base": 0.3, "escala_com": "destreza"}]
    },
    "golpe_temerario": {
        "nome": "Golpe Temerário", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 30, "cooldown": 2,
        "descricao": "Um ataque poderoso que ignora a defesa, mas deixa o usuário vulnerável.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 2.0, "penetracao_armadura": 1.0}, {"tipo": "aplicar_efeito_self", "id_efeito": "debuff_defesa_media", "duracao": 1}]
    },
    "danca_das_laminas": {
        "nome": "Dança das Lâminas", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 35, "cooldown": 4,
        "descricao": "Um rodopio gracioso que atinge todos os inimigos próximos.",
        "tipo_alvo": "inimigos_area", "efeitos": [{"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 1.2}]
    },
    "finta_ritmica": {
        "nome": "Finta Rítmica", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 15, "cooldown": 3,
        "descricao": "Aumenta a esquiva e, se bem-sucedido, permite um contra-ataque imediato.",
        "tipo_alvo": "self", "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_contra_ataque", "duracao": 1}]
    }
}
