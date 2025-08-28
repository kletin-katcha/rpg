# ==============================================================================
# ARQUIVO DE DADOS: HABILIDADES DE MONSTROS
# ==============================================================================
#
# Este arquivo contém as definições para habilidades exclusivas de monstros.
#
# ==============================================================================

HABILIDADES_MONSTROS = {
    # --- HABILIDADES DE CONSTRUTOS (RUÍNAS DE AL'KHEM) ---
    "golpe_pesado": {
        "nome": "Golpe Pesado", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 20,
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.6}]
    },
    "raio_arcano": {
        "nome": "Raio Arcano", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 15, "cooldown": 2, "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_magico", "escala_com": "inteligencia", "elemento": "arcano", "multiplicador_dano": 1.5}]
    },
    "barreira_de_forca": {
        "nome": "Barreira de Força", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 25, "cooldown": 4, "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_defesa_grande", "duracao": 2}]
    },
    "pisao_devastador": {
        "nome": "Pisão Devastador", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 35, "cooldown": 4, "tipo_alvo": "inimigos_area",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.2}, {"tipo": "aplicar_efeito", "id_efeito": "atordoamento", "chance": 0.4, "duracao": 1}]
    },
    "raio_ocular": {
        "nome": "Raio Ocular", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 50, "cooldown": 3, "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_magico", "escala_com": "inteligencia", "elemento": "fogo", "multiplicador_dano": 2.8, "penetracao_armadura": 0.2}]
    },

    # --- HABILIDADES DE MONSTROS LEGACY ---
    "mordida_feroz": {
        "nome": "Mordida Feroz", "custo_tipo": "stamina", "custo_valor": 10, "cooldown": 3,
        "descricao": "Uma mordida selvagem.", "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.2}]
    },
    "arremessar_pedra": {
        "nome": "Arremessar Pedra", "custo_tipo": "stamina", "custo_valor": 5, "tipo": "ativa",
        "descricao": "Um goblin arremessa uma pedra com pontaria surpreendente.", "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 0.8}]
    },
    "golpe_baixo": {
        "nome": "Golpe Baixo", "custo_tipo": "stamina", "custo_valor": 15, "tipo": "ativa",
        "descricao": "Um ataque sujo que visa as pernas do alvo.", "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.0}]
    },
    "investida_imprudente": {
        "nome": "Investida Imprudente", "custo_tipo": "stamina", "custo_valor": 20, "tipo": "ativa",
        "descricao": "O javali avança com fúria total, causando dano massivo mas ficando vulnerável.", "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.8},
            {"tipo": "aplicar_efeito_self", "id_efeito": "debuff_defesa_grande"}
        ]
    },
    "ferroada_venenosa": {
        "nome": "Ferroada Venenosa", "custo_tipo": "stamina", "custo_valor": 10, "tipo": "ativa",
        "descricao": "Uma ferroada rápida que tem chance de envenenar o alvo.", "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 0.5},
            {"tipo": "aplicar_efeito", "id_efeito": "veneno_fraco", "chance": 0.3, "duracao": 3}
        ]
    },
    "cuspe_acido": {
        "nome": "Cuspe Ácido", "custo_tipo": "stamina", "custo_valor": 10, "tipo": "ativa",
        "descricao": "Cospe uma gosma ácida que causa dano e reduz a defesa.", "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {"tipo": "dano_magico", "escala_com": "constituicao", "elemento": "acido", "multiplicador_dano": 0.6},
            {"tipo": "aplicar_efeito", "id_efeito": "debuff_defesa_pequeno", "chance": 1.0, "duracao": 2}
        ]
    },
    "uivo_de_comando": {
        "nome": "Uivo de Comando", "custo_tipo": "mp", "custo_valor": 15, "tipo": "ativa",
        "descricao": "Um uivo que inspira a matilha, aumentando o dano de todos os lobos aliados na batalha.", "tipo_alvo": "aliados_area",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_dano_matilha", "duracao": 3}]
    },
    "seta_de_veneno": {
        "nome": "Seta de Veneno", "custo_tipo": "mp", "custo_valor": 10, "tipo": "ativa",
        "descricao": "Dispara uma pequena seta embebida em veneno de aranha.", "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_magico", "escala_com": "inteligencia", "multiplicador_dano": 0.8}, {"tipo": "aplicar_efeito", "id_efeito": "veneno_fraco", "chance": 0.8, "duracao": 3}]
    },
    "cura_primitiva": {
        "nome": "Cura Primitiva", "custo_tipo": "mp", "custo_valor": 20, "tipo": "ativa",
        "descricao": "Um cântico gutural que invoca espíritos para curar um aliado ferido.", "tipo_alvo": "aliado_unico",
        "efeitos": [{"tipo": "cura", "escala_com": "sabedoria", "multiplicador_cura": 2.0}]
    },
    "patada_esmagadora": {
        "nome": "Patada Esmagadora", "custo_tipo": "stamina", "custo_valor": 25, "tipo": "ativa",
        "descricao": "Um golpe poderoso com as garras de urso que pode atordoar o alvo.", "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.6}, {"tipo": "aplicar_efeito", "id_efeito": "atordoamento", "chance": 0.2, "duracao": 1}]
    },
    "bico_perfurante": {
        "nome": "Bico Perfurante", "custo_tipo": "stamina", "custo_valor": 15, "tipo": "ativa",
        "descricao": "Uma bicada focada que perfura a armadura.", "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.1, "penetracao_armadura": 0.5}]
    },
    "grito_aterrorizante": {
        "nome": "Grito Aterrorizante", "custo_tipo": "mp", "custo_valor": 20, "tipo": "ativa",
        "descricao": "Emite um grito sobrenatural que pode causar medo nos inimigos.", "tipo_alvo": "inimigos_area",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "medo", "duracao": 2}]
    },
    "golpe_com_escudo": {
        "nome": "Golpe com Escudo", "custo_tipo": "stamina", "custo_valor": 15, "tipo": "ativa",
        "descricao": "Usa o escudo para atacar e desequilibrar o oponente.", "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 0.5}, {"tipo": "aplicar_efeito", "id_efeito": "debuff_defesa_pequeno", "chance": 0.7, "duracao": 2}]
    },
    "pancada_de_galho": {
        "nome": "Pancada de Galho", "custo_tipo": "stamina", "custo_valor": 20, "tipo": "ativa",
        "descricao": "Um golpe lento mas poderoso com um galho do tamanho de uma clava.", "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.9}]
    },
    "casca_reforçada": {
        "nome": "Casca Reforçada", "custo_tipo": "mp", "custo_valor": 15, "tipo": "ativa",
        "descricao": "A casca do treant se enrijece, aumentando drasticamente sua defesa por um tempo.", "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_defesa_grande", "duracao": 3}]
    }
}
