# ==============================================================================
# ARQUIVO DE DADOS: CLASSES INICIAIS
# ==============================================================================
#
# Este arquivo contém as definições para todas as classes jogáveis iniciais.
# A estrutura é um dicionário onde a chave é o ID da classe e o valor é
# outro dicionário com os detalhes da classe.
#
# Cada entrada de classe será expandida com uma quantidade massiva de lore,
# filosofia, exemplos notáveis e guias de estilo de jogo para
# atingir a meta de linhas e profundidade do projeto.
#
# ==============================================================================

CLASSES_INICIAIS = {
    # =================================== GUERREIRO ===================================
    "guerreiro": {
        "nome": "Guerreiro",
        "descricao": "Mestre do combate corpo a corpo, treinado no uso de todas as armas e armaduras. Foca em força e resistência para proteger aliados e esmagar inimigos.",
        "lore": """
O caminho do guerreiro é um caminho de disciplina, aço e sangue. Eles são a espinha dorsal de todos os exércitos e grupos de aventureiros, a linha de frente que separa a civilização da selvageria. Um guerreiro não depende de truques mágicos ou subterfúgios; sua confiança está em sua força, em sua armadura e na lâmina de sua arma. Eles são os cavaleiros nobres que protegem os reinos, os mercenários brutais que lutam por ouro, e os soldados leais que morrem por seus comandantes. Onde quer que haja conflito, haverá guerreiros.

A filosofia do guerreiro é simples: preparação e prática levam à perfeição. Eles passam incontáveis horas treinando, dominando o manejo de espadas, machados, lanças e escudos. Eles aprendem a ler o fluxo da batalha, a antecipar o golpe de um inimigo e a encontrar a abertura perfeita na defesa de um oponente. Para um guerreiro, uma batalha não é um caos, mas uma dança mortal onde cada passo e cada golpe têm um propósito.
        """,
        "stats_primarios": ["forca", "constituicao"],
        "habilidades_iniciais": ["ataque_poderoso", "grito_de_guerra"],
        "equipamento_inicial": {"arma_principal": "espada_curta_ferro", "peitoral": "peitoral_de_couro_batido", "escudo": "escudo_de_madeira"}
    },

    # =================================== MAGO ===================================
    "mago": {
        "nome": "Mago",
        "descricao": "Um estudioso das artes arcanas, capaz de manipular as energias mágicas para devastar inimigos à distância, controlar o campo de batalha ou proteger aliados.",
        "lore": """
O mago é um cientista da realidade. Enquanto outros veem o mundo como ele é, o mago vê as leis fundamentais que o governam, as energias invisíveis que fluem através de todas as coisas. Eles dedicam suas vidas ao estudo de tomos antigos, à decifração de runas esquecidas e à experimentação com os próprios fios da magia. Para um mago, o poder não é um dom, mas um conhecimento que deve ser conquistado com anos de estudo e sacrifício.

Eles são frequentemente encontrados em torres isoladas, academias arcanas ou bibliotecas antigas, cercados por livros e artefatos. Um mago em um campo de batalha é uma força da natureza, capaz de invocar chuvas de fogo, erguer muralhas de gelo ou distorcer a mente de seus inimigos. No entanto, seu poder vem com um grande risco. Um feitiço mal calculado pode ter consequências desastrosas, não apenas para o mago, mas para todos ao seu redor.
        """,
        "stats_primarios": ["inteligencia", "sabedoria"],
        "habilidades_iniciais": ["bola_de_fogo", "barreira_de_gelo"],
        "equipamento_inicial": {"arma_principal": "cajado_de_aprendiz", "peitoral": "tunica_simples"}
    },

    # =================================== LADINO ===================================
    "ladino": {
        "nome": "Ladino",
        "descricao": "Um especialista em furtividade e subterfúgio, atacando das sombras, desarmando armadilhas e explorando as fraquezas do inimigo com precisão mortal.",
        "lore": """
Onde o guerreiro usa a força e o mago o poder, o ladino usa a astúcia. Criados nas vielas sombrias das grandes cidades ou como batedores em terras selvagens, eles são mestres da oportunidade. Um ladino sabe que uma adaga bem colocada nas costas é mais eficaz do que mil golpes de espada. Eles vivem nas sombras, movendo-se sem serem vistos, ouvindo conversas que não deveriam ouvir e encontrando tesouros que outros nem sabiam que existiam.

A vida de um ladino é uma de risco calculado. Eles são os ladrões que esvaziam os cofres dos nobres, os espiões que roubam segredos de estado e os assassinos que eliminam alvos sem deixar rastros. Mas nem todos os ladinos são criminosos. Muitos são caçadores de tesouros, exploradores de ruínas antigas, ou simplesmente aventureiros que preferem uma abordagem mais sutil para resolver problemas. Eles confiam em sua agilidade, em seus reflexos rápidos e em sua capacidade de pensar três passos à frente de seus oponentes.
        """,
        "stats_primarios": ["destreza", "carisma"],
        "habilidades_iniciais": ["ataque_furtivo", "disparada"],
        "equipamento_inicial": {"arma_principal": "adaga_de_ferro", "arma_secundaria": "adaga_de_ferro", "peitoral": "armadura_de_couro_leve"}
    },

    # =================================== CLÉRIGO ===================================
    "clerigo": {
        "nome": "Clérigo",
        "descricao": "Um servo devoto de uma divindade, que canaliza poder sagrado para curar os feridos, proteger os inocentes e punir os mortos-vivos e profanos.",
        "lore": """
A fé de um clérigo é sua arma e seu escudo. Eles são os emissários dos deuses no plano mortal, agindo como curandeiros, conselheiros e, quando necessário, guerreiros sagrados. Sua magia não vem do estudo de livros, mas da devoção e da comunhão com sua divindade. Eles são a luz na escuridão, a esperança em tempos de desespero.

Um clérigo pode ser um humilde curandeiro em uma pequena vila ou um inquisidor de armadura pesada em uma cruzada contra o mal. Seu poder é mais eficaz contra criaturas da escuridão, como mortos-vivos e demônios, que são anátemas para a ordem divina que eles servem. Em um grupo de aventureiros, um clérigo é muitas vezes o pilar moral e a diferença entre a vitória e a aniquilação, capaz de reverter ferimentos mortais e fortalecer o espírito de seus companheiros.
        """,
        "stats_primarios": ["sabedoria", "constituicao"],
        "habilidades_iniciais": ["cura_leve", "punicao_divina"],
        "equipamento_inicial": {"arma_principal": "maca_simples", "escudo": "escudo_de_madeira", "peitoral": "cota_de_malha"}
    },

    # =================================== BÁRBARO ===================================
    "barbaro": {
        "nome": "Bárbaro",
        "descricao": "Um guerreiro tribal das terras selvagens que canaliza uma fúria primordial em batalha, tornando-se uma tempestade imparável de destruição.",
        "lore": """
Longe das muralhas das cidades e dos exércitos disciplinados, vive o bárbaro. Criados em tribos selvagens onde a força é lei e a sobrevivência é uma luta diária, eles são a personificação da fúria da natureza. Um bárbaro não luta com técnica refinada; ele luta com instinto e poder avassalador. Em momentos de grande estresse ou raiva, ele pode entrar em uma fúria de batalha, um estado de transe onde a dor é ignorada e a força se multiplica.

Eles são um com a natureza, embora de uma forma diferente dos druidas. Eles não a servem; eles são parte dela, tão selvagens e indomáveis quanto uma tempestade ou um predador no topo da cadeia alimentar. Eles desprezam a 'fraqueza' da civilização, mas muitos encontram seu caminho para o mundo exterior como mercenários, guarda-costas ou aventureiros em busca de um desafio digno de sua força.
        """,
        "stats_primarios": ["forca", "constituicao"],
        "habilidades_iniciais": ["furia_selvagem", "golpe_brutal"],
        "equipamento_inicial": {"arma_principal": "machado_grande_de_duas_maos", "peitoral": "tanga_de_peles"}
    },

    # =================================== BARDO ===================================
    "bardo": {
        "nome": "Bardo",
        "descricao": "Um mestre da música, da palavra e do encanto. Usa sua arte para inspirar aliados, desmoralizar inimigos e manipular a própria magia do som.",
        "lore": """
O bardo sabe que as palavras podem ser mais afiadas que as espadas e que uma canção pode mudar o coração de um rei. Eles são os contadores de histórias, os músicos, os diplomatas e, por vezes, os espiões do mundo. Viajando de cidade em cidade, eles coletam conhecimento, espalham notícias e deixam um rastro de corações partidos e tavernas animadas.

Seu poder vem da crença de que a música é uma forma de magia, uma energia que pode influenciar as emoções e até mesmo a realidade. Com seu alaúde, flauta ou voz, um bardo pode tecer melodias que curam ferimentos, que enchem seus aliados de coragem ou que confundem a mente de seus oponentes. Eles são os 'faz-tudo', capazes de lutar, usar magia e se safar de problemas com seu carisma, tornando-os adições inestimáveis e imprevisíveis a qualquer grupo.
        """,
        "stats_primarios": ["carisma", "destreza"],
        "habilidades_iniciais": ["cancao_da_coragem", "nota_ dissonante"],
        "equipamento_inicial": {"arma_principal": "rapiera", "arma_secundaria": "alaude", "peitoral": "roupas_de_viajante"}
    },

    # =================================== DRUIDA ===================================
    "druida": {
        "nome": "Druida",
        "descricao": "Um guardião do equilíbrio natural, que extrai poder da própria essência da vida. Pode se transformar em animais selvagens e comandar as forças da natureza.",
        "lore": """
O druida é um sacerdote da natureza, um protetor do equilíbrio entre o crescimento e a decadência, a vida e a morte. Eles não servem a deuses do céu, mas à própria alma do mundo. Seus templos são bosques antigos, círculos de pedras e cavernas escondidas. Eles veem a civilização como uma ameaça a esse equilíbrio e lutam para proteger as terras selvagens da expansão das cidades.

O poder de um druida é tão antigo quanto o próprio mundo. Eles podem invocar o crescimento de plantas para prender seus inimigos, convocar enxames de insetos, chamar relâmpagos dos céus e, o mais notável de tudo, mudar sua própria forma física para a de um animal. Um druida pode lutar como um urso, correr como um lobo ou voar como uma águia. Eles são os guardiões silenciosos, os xamãs da floresta, e a fúria da natureza encarnada para aqueles que ousam perturbar seu domínio.
        """,
        "stats_primarios": ["sabedoria", "constituicao"],
        "habilidades_iniciais": ["forma_de_urso", "enraizar"],
        "equipamento_inicial": {"arma_principal": "cajado_de_galho_retorcido", "peitoral": "armadura_de_peles_e_folhas"}
    }
}
