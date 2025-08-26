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

    # --- HABILIDADES DE MAGO (Adicionais) ---
    "barreira_de_gelo": {
        "nome": "Barreira de Gelo",
        "tipo": "ativa",
        "descricao": "Cria uma barreira de gelo protetora que absorve uma quantidade de dano antes de quebrar.",
        "lore": "Uma aplicação defensiva da criomancia, transformando a umidade do ar em um escudo sólido e gelado.",
        "custo_tipo": "mp",
        "custo_valor": 15,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "absorver_dano", "escala_com": "inteligencia", "multiplicador": 4}]
    },

    # --- HABILIDADES DE CLÉRIGO (Adicionais) ---
    "cura_leve": {
        "nome": "Cura Leve",
        "tipo": "ativa",
        "descricao": "Uma prece simples que cura uma pequena quantidade de ferimentos.",
        "lore": "O primeiro dom concedido a muitos que seguem um caminho divino. É um toque de compaixão, um alívio para os feridos.",
        "custo_tipo": "mp",
        "custo_valor": 10,
        "tipo_alvo": "aliado_unico",
        "efeitos": [{"tipo": "cura", "escala_com": "sabedoria", "multiplicador_cura": 2.5}]
    },

    # --- HABILIDADES DE SACERDOTE DAS SOMBRAS ---
    "toque_vampirico": {
        "nome": "Toque Vampírico",
        "tipo": "ativa",
        "descricao": "Toca um inimigo, causando dano necrótico e curando o conjurador por uma parte do dano causado.",
        "lore": "Uma magia proibida que brinca com a transferência da força vital. A vida do inimigo alimenta a sua.",
        "custo_tipo": "mp",
        "custo_valor": 20,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "drenar_vida", "escala_com": "sabedoria", "multiplicador_dano": 1.2, "percentual_cura": 0.5}]
    },
    "palavra_de_dor": {
        "nome": "Palavra de Dor",
        "tipo": "ativa",
        "descricao": "Sussurra uma palavra de poder sombrio que causa dor excruciante e dano contínuo ao alvo.",
        "lore": "Existem palavras na língua das sombras que não foram feitas para serem ouvidas por mortais. Esta é uma delas.",
        "custo_tipo": "mp",
        "custo_valor": 18,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {"tipo": "dano_magico", "escala_com": "sabedoria", "elemento": "sombra", "multiplicador_dano": 0.8},
            {"tipo": "aplicar_efeito", "id_efeito": "debuff_palavra_de_dor", "duracao": 3}
        ]
    },

    # =================================== HABILIDADES DE INQUISIDOR (Mágicas) ===================================
    "fogo_purificador": {
        "nome": "Fogo Purificador",
        "tipo": "ativa",
        "descricao": "Chamas sagradas que queimam impurezas e causam dano contínuo a alvos malignos.",
        "lore": "O fogo que não apenas destrói, mas purifica. Uma ferramenta para expurgar a corrupção do mundo.",
        "custo_tipo": "mp",
        "custo_valor": 20,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "debuff_fogo_purificador", "duracao": 3}]
    },

    # =================================== HABILIDADES DE MAGO DE BATALHA (Mágicas) ===================================
    "armadura_de_mago": {
        "nome": "Armadura de Mago",
        "tipo": "ativa",
        "descricao": "Cria um campo de força arcano que aumenta a defesa do conjurador.",
        "lore": "Uma versão aprimorada da pele de pedra, que usa pura força mágica para desviar de golpes.",
        "custo_tipo": "mp",
        "custo_valor": 15,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_armadura_arcana", "duracao": 5}]
    },

    # =================================== HABILIDADES DE ILUSIONISTA ===================================
    "imagem_espelhada": {
        "nome": "Imagem Espelhada",
        "tipo": "ativa",
        "descricao": "Cria cópias ilusórias de si mesmo para confundir os inimigos.",
        "lore": "Por que lutar contra um inimigo quando você pode fazê-lo lutar contra sombras?",
        "custo_tipo": "mp",
        "custo_valor": 25,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "invocar_ilusao", "id_ilusao": "imagem_espelhada", "quantidade": 3}]
    },
    "medo_fantasmagorico": {
        "nome": "Medo Fantasmagórico",
        "tipo": "ativa",
        "descricao": "Cria uma ilusão do pior medo do alvo, potencialmente o aterrorizando.",
        "lore": "A mente é o verdadeiro campo de batalha. O ilusionista ataca as fundações da coragem de seu inimigo.",
        "custo_tipo": "mp",
        "custo_valor": 20,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "medo_severo", "duracao": 2, "chance": 0.5}]
    },

    # =================================== HABILIDADES DE PIROMANTE ===================================
    "seta_de_fogo": {
        "nome": "Seta de Fogo",
        "tipo": "ativa",
        "descricao": "Uma seta de fogo teleguiada que causa dano de fogo.",
        "lore": "Mais rápido que uma bola de fogo, mas com menos impacto. Uma ferramenta versátil no arsenal do piromante.",
        "custo_tipo": "mp",
        "custo_valor": 10,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_magico", "escala_com": "inteligencia", "elemento": "fogo", "multiplicador_dano": 1.2}]
    },
    "aura_flamejante": {
        "nome": "Aura Flamejante",
        "tipo": "ativa",
        "descricao": "Envolve o conjurador em uma aura de fogo que queima inimigos próximos a cada turno.",
        "lore": "O piromante se torna o próprio sol, uma presença que queima tudo ao seu redor.",
        "custo_tipo": "mp",
        "custo_valor": 30,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "aura_dano_fogo", "duracao": 4}]
    },

    # =================================== HABILIDADES DE CRIOMANTE ===================================
    "armadura_de_geada": {
        "nome": "Armadura de Geada",
        "tipo": "ativa",
        "descricao": "Cobre o conjurador com uma camada de gelo mágico que aumenta a defesa e pode congelar atacantes.",
        "lore": "Uma defesa que pune. O frio não apenas protege, ele retalia.",
        "custo_tipo": "mp",
        "custo_valor": 20,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_armadura_de_geada", "duracao": 5}]
    },

    # =================================== HABILIDADES DE GEOMANTE ===================================
    "arremessar_rocha": {
        "nome": "Arremessar Rocha",
        "tipo": "ativa",
        "descricao": "Arranca uma rocha do chão e a arremessa no inimigo.",
        "lore": "Simples, direto e doloroso. O geomante usa o próprio mundo como sua arma.",
        "custo_tipo": "mp",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "inteligencia", "multiplicador_dano": 1.8}]
    },

    # =================================== HABILIDADES DE AEROMANTE ===================================
    "rajada_de_vento": {
        "nome": "Rajada de Vento",
        "tipo": "ativa",
        "descricao": "Cria uma forte rajada de vento que empurra um inimigo para trás.",
        "lore": "O controle do ar é o controle do campo de batalha.",
        "custo_tipo": "mp",
        "custo_valor": 10,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "empurrar", "distancia": 4}]
    },
    "salto_do_vento": {
        "nome": "Salto do Vento",
        "tipo": "ativa",
        "descricao": "Usa uma corrente de ar para se impulsionar, aumentando drasticamente a esquiva por um turno.",
        "lore": "Por que desviar quando você pode simplesmente não estar lá?",
        "custo_tipo": "mp",
        "custo_valor": 15,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_esquiva_grande", "duracao": 1}]
    },

    # =================================== HABILIDADES DE ELETROMANTE ===================================
    "choque": {
        "nome": "Choque",
        "tipo": "ativa",
        "descricao": "Um pequeno choque elétrico que causa dano e tem uma chance de interromper a ação do inimigo.",
        "lore": "Uma picada de relâmpago para lembrar ao inimigo com quem ele está lidando.",
        "custo_tipo": "mp",
        "custo_valor": 8,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_magico", "escala_com": "inteligencia", "elemento": "raio", "multiplicador_dano": 0.9}, {"tipo": "interromper", "chance": 0.15}]
    },

    # =================================== HABILIDADES DE ALQUIMISTA ===================================
    "arremessar_bomba_de_fogo": {
        "nome": "Arremessar Bomba de Fogo",
        "tipo": "ativa",
        "descricao": "Arremessa um frasco com uma mistura volátil que explode em chamas.",
        "lore": "Ciência ou magia? Para o alquimista, não há diferença.",
        "custo_tipo": "stamina",
        "custo_valor": 20,
        "tipo_alvo": "inimigos_area",
        "efeitos": [{"tipo": "dano_magico", "escala_com": "inteligencia", "elemento": "fogo", "multiplicador_dano_principal": 1.2, "multiplicador_dano_area": 0.6}]
    },
    "criar_pocao_de_cura_rapida": {
        "nome": "Criar Poção de Cura Rápida",
        "tipo": "ativa",
        "descricao": "Mistura rapidamente alguns reagentes para criar uma poção de cura fraca no meio do combate.",
        "lore": "Um bom alquimista está sempre preparado.",
        "custo_tipo": "mp",
        "custo_valor": 25,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "adicionar_item_inventario", "id_item": "pocao_cura_fraca", "quantidade": 1}]
    },

    # =================================== HABILIDADES DE MESTRE CERVEJEIRO ===================================
    "estilo_do_bebado": {
        "nome": "Estilo do Bêbado",
        "tipo": "ativa",
        "descricao": "Adota uma postura de luta imprevisível, aumentando a esquiva e a chance de crítico.",
        "lore": "O oponente nunca sabe se o balanço é um erro ou um ataque. E, para ser honesto, às vezes nem o mestre cervejeiro sabe.",
        "custo_tipo": "recurso_especial",
        "custo_valor": 1,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_estilo_do_bebado", "duracao": 4}]
    },
    "baforada_de_fogo_alcoolico": {
        "nome": "Baforada de Fogo Alcoólico",
        "tipo": "ativa",
        "descricao": "Toma um gole de uma bebida forte e a cospe em uma chama.",
        "lore": "Uma técnica perigosa e impressionante, aprendida nas tavernas mais duvidosas.",
        "custo_tipo": "recurso_especial",
        "custo_valor": 2,
        "tipo_alvo": "inimigos_cone",
        "efeitos": [{"tipo": "dano_magico", "escala_com": "constituicao", "elemento": "fogo", "multiplicador_dano": 1.5}]
    },

    # =================================== HABILIDADES DE VIDENTE ===================================
    "premonicao": {
        "nome": "Premonição",
        "tipo": "ativa",
        "descricao": "O vidente vislumbra o futuro imediato, garantindo que o próximo ataque contra ele erre.",
        "lore": "O futuro é um rio com muitas correntes. O vidente aprende a navegar por elas.",
        "custo_tipo": "mp",
        "custo_valor": 20,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_esquiva_garantida", "duracao": 1}]
    },
    "maldição_do_azar": {
        "nome": "Maldição do Azar",
        "tipo": "ativa",
        "descricao": "Amaldiçoa um inimigo, diminuindo sua sorte e, consequentemente, sua chance de acerto crítico.",
        "lore": "O vidente torce os fios do destino, transformando a sorte de um campeão em pó.",
        "custo_tipo": "mp",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "debuff_azar", "duracao": 4}]
    },

    # =================================== HABILIDADES DE MAGO DO SANGUE ===================================
    "sacrificio_de_sangue": {
        "nome": "Sacrifício de Sangue",
        "tipo": "ativa",
        "descricao": "Sacrifica uma porção da própria vida para restaurar mana.",
        "lore": "A vida é poder. O mago do sangue entende esta verdade fundamental melhor do que ninguém.",
        "custo_tipo": "hp",
        "custo_valor": 50,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "restaurar_recurso", "recurso": "mp", "quantidade": 75}]
    },
    "lanca_de_sangue": {
        "nome": "Lança de Sangue",
        "tipo": "ativa",
        "descricao": "Cria uma lança de sangue solidificado e a arremessa no inimigo. Causa mais dano quanto menos vida o conjurador tiver.",
        "lore": "O poder do mago do sangue vem da beira da morte.",
        "custo_tipo": "hp",
        "custo_valor": 30,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_magico_dinamico", "escala_com": "percentual_vida_perdida", "elemento": "fisico", "multiplicador_dano_max": 3.0}]
    },

    # =================================== HABILIDADES DE ARCANISTA ===================================
    "analise_magica": {
        "nome": "Análise Mágica",
        "tipo": "ativa",
        "descricao": "Analisa as defesas mágicas de um alvo, identificando uma fraqueza elemental.",
        "lore": "Conhecimento é poder. O arcanista disseca a magia do inimigo para encontrar a rachadura em sua armadura.",
        "custo_tipo": "mp",
        "custo_valor": 10,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "revelar_fraqueza_elemental"}]
    },
    "runa_de_poder": {
        "nome": "Runa de Poder",
        "tipo": "ativa",
        "descricao": "Inscreve uma runa no chão que aumenta o poder de todas as magias conjuradas enquanto estiver sobre ela.",
        "lore": "O arcanista não apenas usa a magia, ele a escreve na própria realidade.",
        "custo_tipo": "mp",
        "custo_valor": 35,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "criar_area_efeito", "id_area": "runa_de_poder", "duracao": 4}]
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
