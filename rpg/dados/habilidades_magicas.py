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
        "nome": "Bola de Fogo",
        "descricao": "Lança uma esfera de fogo que explode no alvo, causando dano de fogo a um inimigo principal e dano reduzido a inimigos adjacentes.",
        "lore": "A primeira magia ofensiva que todo aprendiz sonha em dominar. É chamativa, barulhenta e inegavelmente eficaz para lidar com grupos de inimigos despreparados.",
        "custo_tipo": "mp",
        "custo_valor": 20,
        "tipo_alvo": "inimigos_area", # O sistema de combate interpretará isso como alvo principal + adjacentes
        "efeitos": [
            {
                "tipo": "dano_magico",
                "escala_com": "inteligencia",
                "elemento": "fogo",
                "multiplicador_dano_principal": 1.4,
                "multiplicador_dano_area": 0.7
            }
        ]
    },
    "raio_de_gelo": {
        "nome": "Raio de Gelo",
        "descricao": "Dispara um raio de energia congelante que causa dano e pode reduzir a velocidade do alvo.",
        "lore": "Uma magia que demonstra controle e precisão. Não se trata apenas de ferir, mas de controlar o ritmo da batalha, tornando a fuga ou o avanço do inimigo uma tarefa árdua.",
        "custo_tipo": "mp",
        "custo_valor": 12,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {
                "tipo": "dano_magico",
                "escala_com": "inteligencia",
                "elemento": "gelo",
                "multiplicador_dano": 1.1
            },
            {
                "tipo": "aplicar_efeito",
                "id_efeito": "debuff_velocidade_pequeno", # Debuff de -20% de esquiva/velocidade por 2 turnos
                "chance": 0.5, # 50% de chance de aplicar o efeito
                "duracao": 2
            }
        ]
    },

    # --- HABILIDADES DE CLÉRIGO ---
    "cura_leve": {
        "nome": "Cura Leve",
        "descricao": "Canaliza energia divina para restaurar os ferimentos de um alvo.",
        "lore": "Um milagre simples, mas talvez o mais importante de todos. A habilidade de fechar feridas e aliviar a dor é a marca de um verdadeiro servo dos deuses da vida e da luz.",
        "custo_tipo": "mp",
        "custo_valor": 10,
        "tipo_alvo": "aliado_unico",
        "efeitos": [
            {
                "tipo": "cura",
                "escala_com": "sabedoria",
                "multiplicador_cura": 2.5
            }
        ]
    },
    "punicao_divina": {
        "nome": "Punição Divina",
        "descricao": "Golpeia um inimigo com energia sagrada. Causa dano adicional a mortos-vivos e demônios.",
        "lore": "Uma oração transformada em arma. O clérigo invoca a ira de sua divindade para purgar aqueles que zombam da vida e da ordem natural.",
        "custo_tipo": "mp",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {
                "tipo": "dano_magico_condicional",
                "condicao": ["alvo_familia_mortovivo", "alvo_familia_demonio"],
                "escala_com": "sabedoria",
                "elemento": "sagrado",
                "multiplicador_dano_bonus": 2.0,
                "multiplicador_dano_normal": 1.0
            }
        ]
    },

    # --- HABILIDADES DE BARDO ---
    "cancao_da_coragem": {
        "nome": "Canção da Coragem",
        "descricao": "Uma melodia inspiradora que fortalece o espírito dos aliados, aumentando seu dano e precisão.",
        "lore": "Dizem que a primeira canção da coragem foi cantada na véspera de uma batalha impossível, e transformou camponeses assustados em heróis. A música lembra aos ouvintes pelo que eles lutam.",
        "custo_tipo": "mp",
        "custo_valor": 25,
        "tipo_alvo": "aliados_area",
        "efeitos": [
            {
                "tipo": "aplicar_efeito",
                "id_efeito": "buff_moral_bardo", # Aumenta ataque e precisão em 15%
                "duracao": 4
            }
        ]
    },
    "nota_dissonante": {
        "nome": "Nota Dissonante",
        "descricao": "Toca uma nota musicalmente instável que ataca a mente de um inimigo, causando dano psíquico e potencialmente o confundindo.",
        "lore": "Uma técnica secreta que explora as 'frequências erradas' da alma. A nota não fere os ouvidos, mas a própria sanidade, fazendo com que a realidade do alvo se desfaça por um momento.",
        "custo_tipo": "mp",
        "custo_valor": 18,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {
                "tipo": "dano_magico",
                "escala_com": "carisma",
                "elemento": "psiquico",
                "multiplicador_dano": 1.5
            },
            {
                "tipo": "aplicar_efeito",
                "id_efeito": "debuff_confusao", # Chance de atacar a si mesmo ou a um aliado
                "chance": 0.25,
                "duracao": 2
            }
        ]
    },

    # --- HABILIDADES DE DRUIDA ---
    "forma_de_urso": {
        "nome": "Forma de Urso",
        "descricao": "Assume a forma de um grande urso, trocando o uso de magias por força bruta, resistência e novas habilidades de combate corpo a corpo.",
        "lore": "O druida se conecta ao espírito do Grande Urso, um dos totens primordiais da floresta. Nesta forma, o druida se torna um protetor da natureza, com a fúria e a resistência da própria montanha.",
        "custo_tipo": "mp",
        "custo_valor": 30, # Custo para transformar
        "tipo_alvo": "self",
        "efeitos": [
            {
                "tipo": "transformacao",
                "id_forma": "urso_druida", # Altera stats, habilidades e aparência
                "duracao": -1 # Dura até ser cancelada
            }
        ]
    },
    "enraizar": {
        "nome": "Enraizar",
        "descricao": "Comanda raízes que brotam do chão para prender um inimigo no lugar, impedindo seu movimento.",
        "lore": "Um lembrete de que o chão sob os pés de todos está vivo e responde ao chamado do druida. As raízes se movem como serpentes para segurar aqueles que desrespeitam a ordem natural.",
        "custo_tipo": "mp",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {
                "tipo": "aplicar_efeito",
                "id_efeito": "status_enraizado", # Impede movimento e reduz esquiva
                "duracao": 3
            }
        ]
    }
}
