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
        "nome": "Ataque Poderoso",
        "tipo": "ativa",
        "descricao": "Um golpe pesado que sacrifica precisão por dano bruto.",
        "lore": "Uma técnica básica para qualquer combatente que prefere força sobre fineza. O objetivo é simples: colocar todo o peso do corpo e da arma em um único golpe esmagador.",
        "custo_tipo": "stamina",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {
                "tipo": "dano_fisico",
                "escala_com": "forca",
                "multiplicador_dano": 1.5,
                "penalidade_precisao": 0.2
            }
        ]
    },
    "grito_de_guerra": {
        "nome": "Grito de Guerra",
        "tipo": "ativa",
        "descricao": "Um grito poderoso que aumenta o ataque do guerreiro e pode assustar inimigos fracos.",
        "lore": "É o som do início da batalha, um desafio lançado aos inimigos e um juramento de vitória para os aliados.",
        "custo_tipo": "stamina",
        "custo_valor": 20,
        "tipo_alvo": "self",
        "efeitos": [
            {
                "tipo": "aplicar_efeito",
                "id_efeito": "buff_ataque_pequeno",
                "duracao": 3
            }
        ]
    },

    # --- HABILIDADES DE LADINO ---
    "ataque_furtivo": {
        "nome": "Ataque Furtivo",
        "tipo": "ativa",
        "descricao": "Um ataque preciso em um ponto vital. Causa dano massivo se o usuário não for o foco do alvo.",
        "lore": "A arte do assassino. Não se trata de força, mas de timing, posicionamento e conhecimento da anatomia do alvo. Um golpe bem-sucedido pode terminar uma luta antes que ela comece.",
        "custo_tipo": "stamina",
        "custo_valor": 25,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {
                "tipo": "dano_fisico_condicional",
                "condicao": "alvo_nao_focado_em_usuario",
                "escala_com": "destreza",
                "multiplicador_dano_bonus": 3.0,
                "multiplicador_dano_normal": 1.0
            }
        ]
    },
    "disparada": {
        "nome": "Disparada",
        "tipo": "ativa",
        "descricao": "Move-se rapidamente, tornando-se muito mais difícil de acertar por um curto período.",
        "lore": "Para um ladino, não ser atingido é tão importante quanto atacar. A disparada é uma explosão de velocidade para se reposicionar ou simplesmente evitar um golpe mortal.",
        "custo_tipo": "stamina",
        "custo_valor": 10,
        "tipo_alvo": "self",
        "efeitos": [
            {
                "tipo": "aplicar_efeito",
                "id_efeito": "buff_esquiva_grande",
                "duracao": 1
            }
        ]
    },
    "arremessar_adaga": {
        "nome": "Arremessar Adaga",
        "tipo": "ativa",
        "descricao": "Arremessa uma adaga com precisão. Um ataque à distância rápido e de baixo custo.",
        "lore": "Todo ladino carrega algumas facas extras, seja para o trabalho sujo de perto ou para acertar um inimigo em fuga.",
        "custo_tipo": "stamina",
        "custo_valor": 5,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {
                "tipo": "dano_fisico",
                "escala_com": "destreza",
                "multiplicador_dano": 0.8
            }
        ]
    },

    # --- HABILIDADES DE BÁRBARO ---
    "furia_selvagem": {
        "nome": "Fúria Selvagem",
        "tipo": "ativa",
        "descricao": "Entra em um estado de fúria, aumentando o dano causado e a resistência a dano, mas diminuindo a defesa.",
        "lore": "O bárbaro canaliza sua raiva primordial, ignorando a dor e se tornando uma força da natureza. A mente se vai, e apenas o instinto de lutar permanece.",
        "custo_tipo": "recurso_especial",
        "custo_valor": 50,
        "tipo_alvo": "self",
        "efeitos": [
            {
                "tipo": "aplicar_efeito",
                "id_efeito": "estado_furia_barbaro",
                "duracao": 5
            }
        ]
    },
    "golpe_brutal": {
        "nome": "Golpe Brutal",
        "tipo": "ativa",
        "descricao": "Um ataque devastador que ignora uma porção da armadura do inimigo.",
        "lore": "Não é um golpe de técnica, mas de pura força. O objetivo é quebrar não apenas a arma ou armadura do inimigo, mas seu espírito.",
        "custo_tipo": "stamina",
        "custo_valor": 20,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {
                "tipo": "dano_fisico",
                "escala_com": "forca",
                "multiplicador_dano": 1.2,
                "penetracao_armadura": 0.3
            }
        ]
    },

    # --- HABILIDADES DE RANGER ---
    "tiro_certeiro": {
        "nome": "Tiro Certeiro",
        "tipo": "ativa",
        "descricao": "Um disparo cuidadosamente mirado que causa dano extra e tem alta chance de acerto crítico.",
        "lore": "O ranger respira fundo, acalma o coração e se torna um com seu arco. O mundo desaparece, e apenas o alvo permanece. A flecha nunca erra.",
        "custo_tipo": "stamina",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {
                "tipo": "dano_fisico",
                "escala_com": "destreza",
                "multiplicador_dano": 1.3,
                "bonus_chance_critico": 0.25
            }
        ]
    },

    # --- HABILIDADES DE PALADINO ---
    "golpe_divino": {
        "nome": "Golpe Divino",
        "tipo": "ativa",
        "descricao": "Imbui sua arma com energia sagrada, causando dano físico e mágico extra no próximo ataque.",
        "lore": "Canalizando a força de seu juramento, o paladino transforma sua arma em um instrumento da vontade divina, capaz de punir os injustos com fogo sagrado.",
        "custo_tipo": "mp",
        "custo_valor": 20,
        "tipo_alvo": "self",
        "efeitos": [
            {
                "tipo": "aplicar_efeito",
                "id_efeito": "buff_golpe_divino",
                "duracao": 1
            }
        ]
    },

    # --- HABILIDADES FÍSICAS ADICIONAIS (NÍVEL 1-10) ---

    # --- Geral / Espadas ---
    "corte_transversal": {
        "nome": "Corte Transversal",
        "tipo": "ativa",
        "descricao": "Um rápido corte horizontal que pode atingir múltiplos inimigos próximos.",
        "lore": "Uma técnica fundamental para lidar com multidões, ensinada em todas as escolas de esgrima.",
        "custo_tipo": "stamina",
        "custo_valor": 20,
        "tipo_alvo": "inimigos_area",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 0.8}]
    },
    "aparar": {
        "nome": "Aparar",
        "tipo": "ativa",
        "descricao": "Antecipa um ataque corpo a corpo, bloqueando-o e criando uma abertura para um contra-ataque.",
        "lore": "Mais do que força, a esgrima é sobre tempo. Um mestre espadachim pode transformar a agressão de um inimigo em sua própria ruína.",
        "custo_tipo": "stamina",
        "custo_valor": 10,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_aparar", "duracao": 1}]
    },

    # --- Arcos ---
    "tiro_duplo": {
        "nome": "Tiro Duplo",
        "tipo": "ativa",
        "descricao": "Dispara duas flechas em rápida sucessão no mesmo alvo.",
        "lore": "Uma demonstração de velocidade e precisão, o tiro duplo é a marca de um arqueiro experiente.",
        "custo_tipo": "stamina",
        "custo_valor": 25,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 0.9},
            {"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 0.9}
        ]
    },
    "flecha_farpada": {
        "nome": "Flecha Farpada",
        "tipo": "ativa",
        "descricao": "Dispara uma flecha com farpas que causa dano de sangramento ao longo do tempo.",
        "lore": "Uma invenção cruel, mas eficaz. A flecha é projetada para ser mais difícil de remover do que de entrar, causando dor contínua.",
        "custo_tipo": "stamina",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 0.7},
            {"tipo": "aplicar_efeito", "id_efeito": "sangramento_fraco", "duracao": 3}
        ]
    },

    # --- Armas de Haste (Lanças) ---
    "estocada_perfurante": {
        "nome": "Estocada Perfurante",
        "tipo": "ativa",
        "descricao": "Uma estocada focada que visa as brechas na armadura do inimigo.",
        "lore": "A lança não tem o poder de corte de uma espada, mas sua ponta pode encontrar o menor dos vãos em uma armadura de placas.",
        "custo_tipo": "stamina",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.1, "penetracao_armadura": 0.4}]
    },

    # --- Armas de Impacto (Maças, Martelos) ---
    "quebra_ossos": {
        "nome": "Quebra-Ossos",
        "tipo": "ativa",
        "descricao": "Um golpe poderoso que visa as articulações, com chance de reduzir a capacidade de ataque do inimigo.",
        "lore": "Um golpe brutal que ensina ao inimigo uma lição dolorosa sobre o poder do impacto.",
        "custo_tipo": "stamina",
        "custo_valor": 20,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.3},
            {"tipo": "aplicar_efeito", "id_efeito": "debuff_ataque_pequeno", "chance": 0.3, "duracao": 3}
        ]
    },

    # --- Utilidade / Geral ---
    "intimidar": {
        "nome": "Intimidar",
        "tipo": "ativa",
        "descricao": "Usa sua presença física para intimidar um alvo, potencialmente o assustando.",
        "lore": "Às vezes, a melhor arma é a reputação e a aparência. Um olhar frio pode parar um inimigo antes mesmo que a luta comece.",
        "custo_tipo": "stamina",
        "custo_valor": 10,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "medo", "duracao": 2, "escala_com": "forca"}]
    },

    # =================================== HABILIDADES DE GLADIADOR ===================================
    "golpe_de_exibicao": {
        "nome": "Golpe de Exibição",
        "tipo": "ativa",
        "descricao": "Um ataque vistoso que causa menos dano, mas aumenta o carisma em combate, agradando a multidão.",
        "lore": "Para o gladiador, a batalha é um espetáculo. Cada movimento é calculado não apenas para ferir, mas para entreter.",
        "custo_tipo": "stamina",
        "custo_valor": 10,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 0.8},
            {"tipo": "aplicar_efeito", "id_efeito": "buff_carisma_pequeno", "duracao": 3, "alvo": "self"}
        ]
    },
    "rede_e_tridente": {
        "nome": "Rede e Tridente",
        "tipo": "ativa",
        "descricao": "Arremessa uma rede para prender o alvo, seguido por uma estocada com um tridente.",
        "lore": "Uma técnica clássica da arena, focada em controle e punição.",
        "custo_tipo": "stamina",
        "custo_valor": 25,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {"tipo": "aplicar_efeito", "id_efeito": "enraizado", "duracao": 2, "chance": 0.8},
            {"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 1.2}
        ]
    },

    # =================================== HABILIDADES DE CAÇADOR DE RECOMPENSAS ===================================
    "rastrear_alvo": {
        "nome": "Rastrear Alvo",
        "tipo": "ativa",
        "descricao": "Marca um inimigo, revelando suas fraquezas e aumentando o dano causado a ele por um tempo.",
        "lore": "Ninguém escapa de um caçador de recompensas determinado. Uma vez que ele tem seu cheiro, é apenas uma questão de tempo.",
        "custo_tipo": "mp",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "debuff_marcado_para_morrer", "duracao": 4}]
    },
    "disparo_debilitante": {
        "nome": "Disparo Debilitante",
        "tipo": "ativa",
        "descricao": "Um tiro preciso no joelho ou ombro do alvo, reduzindo sua capacidade de movimento ou ataque.",
        "lore": "Um alvo vivo vale mais do que um morto. Um tiro bem colocado pode incapacitar sem matar.",
        "custo_tipo": "stamina",
        "custo_valor": 20,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 0.9},
            {"tipo": "aplicar_efeito", "id_efeito": "debuff_destreza_pequeno", "duracao": 3, "chance": 0.7}
        ]
    },

    # =================================== HABILIDADES DE INQUISIDOR ===================================
    "julgamento": {
        "nome": "Julgamento",
        "tipo": "ativa",
        "descricao": "Condena um inimigo, fazendo com que ele receba dano extra de todas as fontes por um curto período.",
        "lore": "Pelo poder investido em mim, eu te declaro culpado. Que a sentença seja executada.",
        "custo_tipo": "mp",
        "custo_valor": 25,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "debuff_vulnerabilidade", "duracao": 2}]
    },

    # =================================== HABILIDADES DE MAGO DE BATALHA ===================================
    "golpe_arcano": {
        "nome": "Golpe Arcano",
        "tipo": "ativa",
        "descricao": "Canaliza energia mágica na arma, fazendo com que o próximo ataque corpo a corpo cause dano mágico adicional.",
        "lore": "A fusão perfeita de aço e feitiçaria. A lâmina corta e a magia queima.",
        "custo_tipo": "mp",
        "custo_valor": 10,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_golpe_arcano", "duracao": 1}]
    },

    # =================================== HABILIDADES DE MESTRE DAS FERAS ===================================
    "ataque_coordenado": {
        "nome": "Ataque Coordenado",
        "tipo": "ativa",
        "descricao": "Ordena que seu companheiro animal ataque o mesmo alvo, causando dano bônus.",
        "lore": "A ligação entre o mestre e a fera é tão forte que eles agem como um só.",
        "custo_tipo": "stamina",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "comando_animal", "comando": "atacar", "bonus_dano": 1.5}]
    },
    "vinculo_bestial": {
        "nome": "Vínculo Bestial",
        "tipo": "passiva",
        "descricao": "Sua conexão com seu companheiro animal aumenta seus atributos e os do animal.",
        "lore": "Duas almas, uma vontade. Onde um é fraco, o outro é forte.",
        "efeitos": [{"tipo": "bonus_passivo", "atributo": "constituicao", "valor": 2}, {"tipo": "bonus_passivo_companheiro", "atributo": "constituicao", "valor": 10}]
    },

    # =================================== HABILIDADES DE SAMURAI ===================================
    "golpe_iaijutsu": {
        "nome": "Golpe Iaijutsu",
        "tipo": "ativa",
        "descricao": "Um saque rápido e mortal com a katana que causa dano massivo no primeiro turno do combate.",
        "lore": "A batalha é vencida antes mesmo de começar. O golpe iaijutsu é a personificação da velocidade e precisão.",
        "custo_tipo": "stamina",
        "custo_valor": 30,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico_condicional", "condicao": "primeiro_turno", "escala_com": "destreza", "multiplicador_dano_bonus": 4.0, "multiplicador_dano_normal": 1.2}]
    },
    "postura_inabalavel": {
        "nome": "Postura Inabalável",
        "tipo": "ativa",
        "descricao": "Adota uma postura defensiva que aumenta a defesa e a resistência, mas impede o movimento.",
        "lore": "A mente clara e o corpo firme como uma montanha. O samurai se torna um pilar inamovível, pronto para qualquer ataque.",
        "custo_tipo": "stamina",
        "custo_valor": 10,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_postura_inabalavel", "duracao": 3}]
    },

    # =================================== HABILIDADES DE NINJA ===================================
    "bomba_de_fumaca": {
        "nome": "Bomba de Fumaça",
        "tipo": "ativa",
        "descricao": "Cria uma nuvem de fumaça densa, permitindo uma fuga garantida do combate ou aumentando a esquiva.",
        "lore": "A arte da dissimulação. O ninja desaparece como um fantasma, deixando apenas confusão para trás.",
        "custo_tipo": "stamina",
        "custo_valor": 20,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_esquiva_extremo", "duracao": 1}]
    },
    "substituicao": {
        "nome": "Substituição (Kawarimi)",
        "tipo": "passiva_reage_dano",
        "descricao": "Quando seria atingido por um ataque, o ninja se substitui por um tronco de madeira, negando o dano.",
        "lore": "Uma técnica clássica de engodo, que transforma um golpe mortal em uma oportunidade.",
        "chance": 0.2,
        "cooldown": 5,
        "efeitos": [{"tipo": "negar_dano"}]
    },

    # =================================== HABILIDADES DE CORSÁRIO ===================================
    "chute_baixo": {
        "nome": "Chute Baixo",
        "tipo": "ativa",
        "descricao": "Um chute sujo nos joelhos do oponente para desequilibrá-lo.",
        "lore": "No mar, não há regras de honra. Luta-se para vencer, não para parecer bonito.",
        "custo_tipo": "stamina",
        "custo_valor": 10,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 0.6}, {"tipo": "aplicar_efeito", "id_efeito": "debuff_esquiva_pequeno", "duracao": 2, "chance": 0.9}]
    },
    "tiro_de_pistola": {
        "nome": "Tiro de Pistola",
        "tipo": "ativa",
        "descricao": "Um disparo rápido e barulhento com uma pistola de pederneira.",
        "lore": "Uma arma de covardes para alguns, uma ferramenta pragmática para o corsário.",
        "custo_tipo": "stamina",
        "custo_valor": 20,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 1.8}]
    },

    # =================================== HABILIDADES DE DOMADOR ===================================
    "capturar_besta": {
        "nome": "Capturar Besta",
        "tipo": "ativa",
        "descricao": "Tenta capturar uma besta enfraquecida para torná-la sua companheira.",
        "lore": "O domador não busca matar, mas sim entender e dominar. Uma besta capturada é um aliado para a vida.",
        "custo_tipo": "mp",
        "custo_valor": 50,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "capturar", "condicao": "alvo_vida_abaixo_20_percent"}]
    },
    "ordem_de_ataque": {
        "nome": "Ordem de Ataque",
        "tipo": "ativa",
        "descricao": "Uma ordem clara e direta para seu companheiro atacar um alvo específico.",
        "lore": "Simples, direto e eficaz.",
        "custo_tipo": "stamina",
        "custo_valor": 5,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "comando_animal", "comando": "atacar"}]
    },

    # =================================== HABILIDADES DE DEFENSOR ===================================
    "bloqueio_com_escudo": {
        "nome": "Bloqueio com Escudo",
        "tipo": "ativa",
        "descricao": "Ergue o escudo para bloquear completamente o próximo ataque físico.",
        "lore": "O escudo do defensor é uma extensão de sua vontade. Nada passará.",
        "custo_tipo": "stamina",
        "custo_valor": 15,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_bloqueio_total", "duracao": 1}]
    },
    "intervir": {
        "nome": "Intervir",
        "tipo": "ativa",
        "descricao": "Corre para a frente de um aliado, recebendo o próximo ataque direcionado a ele.",
        "lore": "O sacrifício é a maior honra de um defensor.",
        "custo_tipo": "stamina",
        "custo_valor": 20,
        "tipo_alvo": "aliado_unico",
        "efeitos": [{"tipo": "aplicar_efeito_em_alvo", "id_efeito": "buff_intervir", "duracao": 1, "alvo": "self"}]
    },

    # =================================== HABILIDADES DE DUELISTA ===================================
    "aparar_e_ripostar": {
        "nome": "Aparar e Ripostar",
        "tipo": "ativa",
        "descricao": "Apara o ataque de um inimigo e contra-ataca com um golpe rápido.",
        "lore": "A dança da esgrima. Cada movimento do inimigo é uma oportunidade.",
        "custo_tipo": "stamina",
        "custo_valor": 20,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_ripostar", "duracao": 1}]
    },
    "estocada_precisa": {
        "nome": "Estocada Precisa",
        "tipo": "ativa",
        "descricao": "Uma estocada que ignora parte da armadura e tem alta chance de crítico.",
        "lore": "Não é sobre força, é sobre encontrar o lugar certo para atacar.",
        "custo_tipo": "stamina",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 1.2, "penetracao_armadura": 0.5, "bonus_chance_critico": 0.15}]
    },

    # =================================== HABILIDADES DE BERSERKER ===================================
    "furia_cega": {
        "nome": "Fúria Cega",
        "tipo": "ativa",
        "descricao": "Entra em um frenesi incontrolável, atacando aleatoriamente mas com poder devastador.",
        "lore": "A mente se apaga. Apenas a raiva permanece. Amigo e inimigo se tornam o mesmo.",
        "custo_tipo": "recurso_especial",
        "custo_valor": 100,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "estado_furia_cega", "duracao": 4}]
    },
    "ignorar_dor": {
        "nome": "Ignorar Dor",
        "tipo": "passiva",
        "descricao": "Quanto menos vida o berserker tem, mais dano ele causa.",
        "lore": "A dor é apenas um lembrete de que você ainda está vivo e pode lutar mais.",
        "efeitos": [{"tipo": "bonus_passivo_dinamico", "atributo": "forca", "escala_com": "percentual_vida_perdida"}]
    },

    # =================================== HABILIDADES DE PUGILISTA ===================================
    "soco_direto": {
        "nome": "Soco Direto",
        "tipo": "ativa",
        "descricao": "Um soco rápido e eficiente. Custa pouca stamina.",
        "lore": "O básico. Rápido, simples, eficaz.",
        "custo_tipo": "stamina",
        "custo_valor": 5,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 0.9}]
    },
    "queixo_de_granito": {
        "nome": "Queixo de Granito",
        "tipo": "passiva",
        "descricao": "Você é acostumado a levar socos. Aumenta a constituição.",
        "lore": "Depois de algumas centenas de brigas de taverna, sua cabeça fica um pouco mais dura.",
        "efeitos": [{"tipo": "bonus_passivo", "atributo": "constituicao", "valor": 5}]
    },

    # =================================== HABILIDADES DE CAÇADOR DE BRUXAS ===================================
    "disparo_de_ferro_frio": {
        "nome": "Disparo de Ferro Frio",
        "tipo": "ativa",
        "descricao": "Dispara um virote de ferro frio, que causa dano extra a criaturas mágicas e feéricas.",
        "lore": "A magia tem suas fraquezas. O ferro frio é uma delas.",
        "custo_tipo": "stamina",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico_condicional", "condicao": "alvo_tipo_magico", "escala_com": "destreza", "multiplicador_dano_bonus": 2.0, "multiplicador_dano_normal": 1.0}]
    },

    # =================================== HABILIDADES DE TEMPLÁRIO ===================================
    "arma_abençoada": {
        "nome": "Arma Abençoada",
        "tipo": "ativa",
        "descricao": "Imbui sua arma com poder sagrado, fazendo com que ela cause dano sagrado adicional.",
        "lore": "Que minha arma seja um canal para a fúria divina.",
        "custo_tipo": "mp",
        "custo_valor": 15,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_arma_abencoada", "duracao": 3}]
    },
    "escudo_da_fe": {
        "nome": "Escudo da Fé",
        "tipo": "ativa",
        "descricao": "Cria uma barreira sagrada que absorve uma quantidade de dano.",
        "lore": "Minha fé é meu escudo.",
        "custo_tipo": "mp",
        "custo_valor": 20,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "absorver_dano", "escala_com": "sabedoria", "multiplicador": 5}]
    },

    # =================================== HABILIDADES DE BARDO DA BRAVURA ===================================
    "cancao_de_batalha": {
        "nome": "Canção de Batalha",
        "tipo": "ativa",
        "descricao": "Toca uma canção marcial que aumenta o ataque de todos os aliados próximos.",
        "lore": "Uma melodia para acelerar o coração e firmar a mão.",
        "custo_tipo": "mp",
        "custo_valor": 30,
        "tipo_alvo": "aliados_area",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_ataque_pequeno", "duracao": 4}]
    },
    "golpe_inspirador": {
        "nome": "Golpe Inspirador",
        "tipo": "ativa",
        "descricao": "Um ataque corpo a corpo que também concede um pequeno bônus de ataque a um aliado próximo.",
        "lore": "Um ato de bravura inspira outros a seguirem o exemplo.",
        "custo_tipo": "stamina",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.0}, {"tipo": "buff_aliado_proximo", "id_efeito": "buff_ataque_minimo", "duracao": 2}]
    },

    # =================================== HABILIDADES DE PATRULHEIRO URBANO ===================================
    "movimento_de_telhado": {
        "nome": "Movimento de Telhado",
        "tipo": "passiva",
        "descricao": "Você se move com agilidade em ambientes urbanos, ganhando bônus de esquiva.",
        "lore": "A cidade é sua selva.",
        "efeitos": [{"tipo": "bonus_passivo", "atributo": "esquiva", "valor": 10}]
    },
    "tiro_rapido_de_besta": {
        "nome": "Tiro Rápido de Besta",
        "tipo": "ativa",
        "descricao": "Dispara um virote de besta de mão com incrível velocidade, embora com menos poder.",
        "lore": "Em uma viela apertada, a velocidade é mais importante que a força.",
        "custo_tipo": "stamina",
        "custo_valor": 5,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 0.7}]
    }
}
