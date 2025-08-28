# ==============================================================================
# ARQUIVO DE DADOS: HABILIDADES MÁGICAS
# ==============================================================================
#
# Este arquivo contém as definições para habilidades baseadas em atributos
# mágicos como Inteligência e Sabedoria. A estrutura é idêntica à das
# habilidades físicas.
#
# ==============================================================================

HABILIDADES_MAGICAS = {
    # --- HABILIDADES DE MAGO ---
    "bola_de_fogo": {
        "nome": "Bola de Fogo", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 20,
        "descricao": "Lança uma esfera de fogo que explode no alvo.",
        "tipo_alvo": "inimigos_area", "efeitos": [{"tipo": "dano_magico", "escala_com": "inteligencia", "elemento": "fogo", "multiplicador_dano_principal": 1.4, "multiplicador_dano_area": 0.7}]
    },
    "raio_de_gelo": {
        "nome": "Raio de Gelo", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 12,
        "descricao": "Dispara um raio de energia congelante que causa dano e pode reduzir a velocidade do alvo.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "dano_magico", "escala_com": "inteligencia", "elemento": "gelo", "multiplicador_dano": 1.1}, {"tipo": "aplicar_efeito", "id_efeito": "debuff_velocidade_pequeno", "chance": 0.5, "duracao": 2}]
    },

    # --- HABILIDADES DE CLÉRIGO ---
    "punicao_divina": {
        "nome": "Punição Divina", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 15,
        "descricao": "Golpeia um inimigo com energia sagrada. Causa dano adicional a mortos-vivos e demônios.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "dano_magico_condicional", "condicao": ["alvo_familia_mortovivo", "alvo_familia_demonio"], "escala_com": "sabedoria", "elemento": "sagrado", "multiplicador_dano_bonus": 2.0, "multiplicador_dano_normal": 1.0}]
    },

    # --- HABILIDADES DE BARDO ---
    "nota_dissonante": {
        "nome": "Nota Dissonante", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 18,
        "descricao": "Toca uma nota musicalmente instável que ataca a mente de um inimigo, causando dano psíquico e potencialmente o confundindo.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "dano_magico", "escala_com": "carisma", "elemento": "psiquico", "multiplicador_dano": 1.5}, {"tipo": "aplicar_efeito", "id_efeito": "debuff_confusao", "chance": 0.25, "duracao": 2}]
    },

    # --- HABILIDADES DE DRUIDA ---
    "forma_de_urso": {
        "nome": "Forma de Urso", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 30,
        "descricao": "Assume a forma de um grande urso, trocando o uso de magias por força bruta e resistência.",
        "tipo_alvo": "self", "efeitos": [{"tipo": "transformacao", "id_forma": "urso_druida", "duracao": -1}]
    },
    "enraizar": {
        "nome": "Enraizar", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 15,
        "descricao": "Comanda raízes que brotam do chão para prender um inimigo no lugar.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "status_enraizado", "duracao": 3}]
    },

    # --- HABILIDADES DE FEITICEIRO ---
    "raio_do_caos": {
        "nome": "Raio do Caos", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 15,
        "descricao": "Dispara um raio de energia mágica imprevisível. O tipo de dano elemental é aleatório.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "dano_magico_aleatorio", "escala_com": "carisma", "elementos_possiveis": ["fogo", "gelo", "raio"], "multiplicador_dano": 1.8}]
    },
    "onda_de_forca": {
        "nome": "Onda de Força", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 20,
        "descricao": "Libera uma onda de força telecinética que empurra todos os inimigos próximos.",
        "tipo_alvo": "inimigos_area", "efeitos": [{"tipo": "empurrar", "distancia": 3}, {"tipo": "dano_magico", "escala_com": "carisma", "elemento": "forca", "multiplicador_dano": 0.5}]
    },

    # --- HABILIDADES DE BRUXO ---
    "explosao_mistica": {
        "nome": "Explosão Mística", "tipo": "ativa", "custo_tipo": "nenhum", "custo_valor": 0,
        "descricao": "Um raio de energia crepitante, a habilidade mais básica e confiável de um bruxo.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "dano_magico", "escala_com": "carisma", "elemento": "mistico", "multiplicador_dano": 1.6}]
    },

    # --- HABILIDADES DE NECROMANTE ---
    "toque_vampirico": {
        "nome": "Toque Vampírico", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 25,
        "descricao": "Drena a força vital de um inimigo, causando dano necrótico e curando o conjurador.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_magico", "escala_com": "inteligencia", "elemento": "necrotico", "multiplicador_dano": 1.5}, {"tipo": "roubo_de_vida", "porcentagem": 0.5}]
    },

    # --- CLASSES AVANÇADAS ---
    "chuva_de_meteoros": {
        "nome": "Chuva de Meteoros", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 80, "cooldown": 8,
        "descricao": "Invoca uma chuva de pequenos meteoros que bombardeiam uma área, causando dano massivo de fogo.",
        "tipo_alvo": "inimigos_area", "efeitos": [{"tipo": "dano_magico", "escala_com": "inteligencia", "elemento": "fogo", "multiplicador_dano": 3.5}]
    },
    "explosao_de_forca": {
        "nome": "Explosão de Força", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 35, "cooldown": 3,
        "descricao": "Libera uma onda de choque de pura força mágica, causando dano e empurrando todos os inimigos.",
        "tipo_alvo": "inimigos_area", "efeitos": [{"tipo": "dano_magico", "escala_com": "inteligencia", "elemento": "forca", "multiplicador_dano": 1.5}, {"tipo": "empurrar", "distancia": 4}]
    },
    "palavra_sagrada_punicao": {
        "nome": "Palavra Sagrada: Punição", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 50, "cooldown": 5,
        "descricao": "Profere uma palavra de poder divino que causa dano sagrado massivo a um único alvo.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "dano_magico", "escala_com": "sabedoria", "elemento": "sagrado", "multiplicador_dano": 3.0}]
    },
    "flecha_elemental": {
        "nome": "Flecha Elemental", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 20, "cooldown": 1,
        "descricao": "Imbui uma flecha com poder elemental aleatório (Fogo, Gelo ou Raio).",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "dano_magico_aleatorio", "escala_com": "inteligencia", "elementos_possiveis": ["fogo", "gelo", "raio"], "multiplicador_dano": 1.5}]
    },
    "disparo_enfraquecedor": {
        "nome": "Disparo Enfraquecedor", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 25, "cooldown": 3,
        "descricao": "Um disparo que visa os músculos do alvo, reduzindo seu poder de ataque.",
        "tipo_alvo": "inimigo_unico", "efeitos": [{"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 1.1}, {"tipo": "aplicar_efeito", "id_efeito": "debuff_ataque_medio", "duracao": 3}]
    },
    "balada_da_confusao": {
        "nome": "Balada da Confusão", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 40, "cooldown": 5,
        "descricao": "Uma melodia caótica que tem chance de deixar todos os inimigos confusos.",
        "tipo_alvo": "inimigos_area", "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "debuff_confusao", "chance": 0.4, "duracao": 2}]
    }
}
