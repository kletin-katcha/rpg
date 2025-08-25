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
        "tipo": "ativa",
        "descricao": "Lança uma esfera de fogo que explode no alvo, causando dano de fogo a um inimigo principal e dano reduzido a inimigos adjacentes.",
        "lore": "A primeira magia ofensiva que todo aprendiz sonha em dominar. É chamativa, barulhenta e inegavelmente eficaz para lidar com grupos de inimigos despreparados.",
        "custo_tipo": "mp",
        "custo_valor": 20,
        "tipo_alvo": "inimigos_area",
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
        "tipo": "ativa",
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
                "id_efeito": "debuff_velocidade_pequeno",
                "chance": 0.5,
                "duracao": 2
            }
        ]
    },

    # --- HABILIDADES DE CLÉRIGO ---
    "punicao_divina": {
        "nome": "Punição Divina",
        "tipo": "ativa",
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
        "tipo": "ativa",
        "descricao": "Uma melodia inspiradora que fortalece o espírito dos aliados, aumentando seu dano e precisão.",
        "lore": "Dizem que a primeira canção da coragem foi cantada na véspera de uma batalha impossível, e transformou camponeses assustados em heróis. A música lembra aos ouvintes pelo que eles lutam.",
        "custo_tipo": "mp",
        "custo_valor": 25,
        "tipo_alvo": "aliados_area",
        "efeitos": [
            {
                "tipo": "aplicar_efeito",
                "id_efeito": "buff_moral_bardo",
                "duracao": 4
            }
        ]
    },
    "nota_dissonante": {
        "nome": "Nota Dissonante",
        "tipo": "ativa",
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
                "id_efeito": "debuff_confusao",
                "chance": 0.25,
                "duracao": 2
            }
        ]
    },

    # --- HABILIDADES DE DRUIDA ---
    "forma_de_urso": {
        "nome": "Forma de Urso",
        "tipo": "ativa",
        "descricao": "Assume a forma de um grande urso, trocando o uso de magias por força bruta, resistência e novas habilidades de combate corpo a corpo.",
        "lore": "O druida se conecta ao espírito do Grande Urso, um dos totens primordiais da floresta. Nesta forma, o druida se torna um protetor da natureza, com a fúria e a resistência da própria montanha.",
        "custo_tipo": "mp",
        "custo_valor": 30,
        "tipo_alvo": "self",
        "efeitos": [
            {
                "tipo": "transformacao",
                "id_forma": "urso_druida",
                "duracao": -1
            }
        ]
    },
    "enraizar": {
        "nome": "Enraizar",
        "tipo": "ativa",
        "descricao": "Comanda raízes que brotam do chão para prender um inimigo no lugar, impedindo seu movimento.",
        "lore": "Um lembrete de que o chão sob os pés de todos está vivo e responde ao chamado do druida. As raízes se movem como serpentes para segurar aqueles que desrespeitam a ordem natural.",
        "custo_tipo": "mp",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {
                "tipo": "aplicar_efeito",
                "id_efeito": "status_enraizado",
                "duracao": 3
            }
        ]
    },

    # --- HABILIDADES DE PALADINO ---
    "aura_de_protecao": {
        "nome": "Aura de Proteção",
        "tipo": "ativa",
        "descricao": "Emite uma aura divina que concede resistência a dano para o paladino e aliados próximos.",
        "lore": "A fé do paladino se manifesta como um escudo de luz visível, protegendo aqueles que se abrigam perto dele.",
        "custo_tipo": "mp",
        "custo_valor": 30,
        "tipo_alvo": "aliados_area",
        "efeitos": [
            {"tipo": "aplicar_efeito", "id_efeito": "buff_aura_protecao", "duracao": 5}
        ]
    },

    # --- HABILIDADES DE FEITICEIRO ---
    "raio_do_caos": {
        "nome": "Raio do Caos",
        "tipo": "ativa",
        "descricao": "Dispara um raio de energia mágica imprevisível. O tipo de dano elemental é aleatório a cada uso.",
        "lore": "A magia selvagem do feiticeiro se recusa a ser contida. Este feitiço é um reflexo direto de sua natureza, poderoso mas inconstante.",
        "custo_tipo": "mp",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {"tipo": "dano_magico_aleatorio", "escala_com": "carisma", "elementos_possiveis": ["fogo", "gelo", "raio"], "multiplicador_dano": 1.8}
        ]
    },
    "onda_de_forca": {
        "nome": "Onda de Força",
        "tipo": "ativa",
        "descricao": "Libera uma onda de força telecinética que empurra todos os inimigos próximos para trás.",
        "lore": "Uma manifestação bruta do poder do feiticeiro, uma explosão de pura força de vontade que afeta o mundo físico.",
        "custo_tipo": "mp",
        "custo_valor": 20,
        "tipo_alvo": "inimigos_area",
        "efeitos": [
            {"tipo": "empurrar", "distancia": 3},
            {"tipo": "dano_magico", "escala_com": "carisma", "elemento": "forca", "multiplicador_dano": 0.5}
        ]
    },

    # --- HABILIDADES DE BRUXO ---
    "explosao_mistica": {
        "nome": "Explosão Mística",
        "tipo": "ativa",
        "descricao": "Um raio de energia crepitante, a habilidade mais básica e confiável de um bruxo.",
        "lore": "Um presente direto do patrono, esta habilidade é a assinatura de um bruxo. Pode não ser a mais chamativa, mas é uma fonte constante de poder que pode ser moldada e aprimorada de inúmeras maneiras.",
        "custo_tipo": "nenhum",
        "custo_valor": 0,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {"tipo": "dano_magico", "escala_com": "carisma", "elemento": "mistico", "multiplicador_dano": 1.6}
        ]
    },
    "maldição_do_patrono": {
        "nome": "Maldição do Patrono",
        "tipo": "ativa",
        "descricao": "Amaldiçoa um alvo, tornando-o mais vulnerável ao seu dano e concedendo um benefício ao bruxo quando o alvo morre.",
        "lore": "O bruxo marca uma alma para seu patrono. A entidade sombria volta sua atenção para o amaldiçoado, enfraquecendo suas defesas e aguardando para reclamar sua essência.",
        "custo_tipo": "mp",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {"tipo": "aplicar_efeito", "id_efeito": "debuff_maldicao_bruxo", "duracao": -1}
        ]
    },

    # --- HABILIDADES MÁGICAS ADICIONAIS (NÍVEL 1-10) ---

    # --- Buffs / Debuffs ---
    "pele_de_pedra": {
        "nome": "Pele de Pedra",
        "tipo": "ativa",
        "descricao": "A pele do alvo se torna dura como pedra, aumentando sua defesa física.",
        "lore": "Uma magia de transmutação simples que imbui a carne com as propriedades da terra.",
        "custo_tipo": "mp",
        "custo_valor": 15,
        "tipo_alvo": "aliado_unico",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_defesa_media", "duracao": 5}]
    },
    "lentidao": {
        "nome": "Lentidão",
        "tipo": "ativa",
        "descricao": "Altera o fluxo do tempo ao redor de um inimigo, tornando seus movimentos lentos e desajeitados.",
        "lore": "Uma manipulação temporal básica, mas eficaz. O alvo se sente como se estivesse se movendo através de melaço.",
        "custo_tipo": "mp",
        "custo_valor": 10,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "debuff_velocidade_grande", "duracao": 3}]
    },
    "forca_do_touro": {
        "nome": "Força do Touro",
        "tipo": "ativa",
        "descricao": "Concede a um aliado a força de um touro enfurecido.",
        "lore": "Invocando o espírito do touro primordial, esta magia enche os músculos do alvo com poder bruto.",
        "custo_tipo": "mp",
        "custo_valor": 20,
        "tipo_alvo": "aliado_unico",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_forca_medio", "duracao": 4}]
    },

    # --- Ataques Elementais ---
    "lanca_de_gelo": {
        "nome": "Lança de Gelo",
        "tipo": "ativa",
        "descricao": "Cria e lança uma lança de gelo sólido que perfura o alvo.",
        "lore": "Uma versão mais focada e letal do Raio de Gelo, projetada para perfurar armaduras e congelar o sangue nas veias.",
        "custo_tipo": "mp",
        "custo_valor": 25,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {"tipo": "dano_magico", "escala_com": "inteligencia", "elemento": "gelo", "multiplicador_dano": 2.2}
        ]
    },
    "corrente_de_raios": {
        "nome": "Corrente de Raios",
        "tipo": "ativa",
        "descricao": "Um raio que atinge um alvo e salta para outros inimigos próximos.",
        "lore": "O conjurador se torna um conduíte para a fúria da tempestade, liberando uma energia que anseia por encontrar um caminho para a terra, saltando de corpo em corpo.",
        "custo_tipo": "mp",
        "custo_valor": 35,
        "tipo_alvo": "inimigos_area",
        "efeitos": [
            {"tipo": "dano_magico_em_cadeia", "escala_com": "inteligencia", "elemento": "raio", "multiplicador_dano": 1.5, "max_saltos": 3, "reducao_por_salto": 0.3}
        ]
    },

    # --- Invocações ---
    "invocar_familiar_imp": {
        "nome": "Invocar Familiar: Imp",
        "tipo": "ativa",
        "descricao": "Invoca um diabrete (Imp) do plano infernal para ajudar em combate.",
        "lore": "Uma invocação simples, muitas vezes o primeiro passo para um conjurador que se aprofunda na arte de chamar criaturas de outros planos.",
        "custo_tipo": "mp",
        "custo_valor": 40,
        "tipo_alvo": "self",
        "efeitos": [
            {"tipo": "invocar_criatura", "id_criatura": "familiar_imp", "duracao": -1}
        ]
    }
}
