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
    },

    # =================================== RANGER ===================================
    "ranger": {
        "nome": "Ranger",
        "descricao": "Um caçador e rastreador mestre das terras selvagens. Combina o manejo de arco e lâminas com um conhecimento profundo da natureza e de seus habitantes.",
        "lore": """
O ranger é a ponte entre a civilização e a selva. Eles patrulham as fronteiras, protegem as estradas e caçam as bestas monstruosas que ameaçam as vilas. Diferente do bárbaro, que é parte da fúria da natureza, ou do druida, que é seu sacerdote, o ranger é seu estudante e guardião pragmático. Eles aprendem os segredos da floresta não por comunhão espiritual, mas por observação e experiência.

Um ranger pode rastrear uma presa por dias, ler os sinais no vento e na terra, e montar armadilhas mortais. Em combate, são adversários versáteis, igualmente proficientes com um arco à distância ou com duas lâminas em combate próximo. Muitos rangers formam laços profundos com companheiros animais, lutando lado a lado com lobos, ursos ou falcões que eles criaram e treinaram.
        """,
        "stats_primarios": ["destreza", "sabedoria"],
        "habilidades_iniciais": ["tiro_certeiro", "companheiro_animal_lobo"],
        "equipamento_inicial": {"arma_principal": "arco_longo", "arma_secundaria": "espada_curta_ferro", "peitoral": "armadura_de_couro"}
    },

    # =================================== PALADINO ===================================
    "paladino": {
        "nome": "Paladino",
        "descricao": "Um guerreiro sagrado vinculado por um juramento a uma causa maior. Combina proeza marcial com poder divino para proteger os inocentes e destruir o mal.",
        "lore": """
Um paladino é mais do que um guerreiro e mais do que um clérigo. É a encarnação de um juramento. Seja um juramento de devoção a um deus da justiça, um juramento de vingança contra as forças das trevas, ou um juramento de proteger a beleza e a vida, é esse voto que lhes concede poder. A força de um paladino não vem apenas de seus músculos, mas da força de sua convicção.

Eles são cavaleiros da retidão, vestidos em armaduras pesadas e empunhando armas que brilham com luz divina. Seu poder lhes permite curar os feridos, proteger seus aliados com auras sagradas e desferir golpes esmagadores que fazem os demônios recuarem. No entanto, o caminho do paladino é exigente. Quebrar seu juramento significa perder seus poderes, tornando-os o mais trágico dos heróis: um campeão caído.
        """,
        "stats_primarios": ["forca", "carisma"],
        "habilidades_iniciais": ["golpe_divino", "aura_de_protecao"],
        "equipamento_inicial": {"arma_principal": "espada_longa", "escudo": "escudo_de_aço", "peitoral": "armadura_de_placas"}
    },

    # =================================== FEITICEIRO ===================================
    "feiticeiro": {
        "nome": "Feiticeiro",
        "descricao": "Um conjurador que nasceu com magia em seu sangue. Sua magia é inata e poderosa, mas muitas vezes selvagem e difícil de controlar.",
        "lore": """
Enquanto o mago estuda a magia, o feiticeiro *é* a magia. O poder arcano flui em suas veias, um dom ou uma maldição de uma linhagem ancestral. Talvez um de seus ancestrais fosse um dragão, um anjo, ou talvez eles tenham nascido durante uma rara conjunção celestial. Seja qual for a origem, a magia de um feiticeiro é parte deles, uma expressão de sua própria alma.

Eles não precisam de livros de feitiços ou de gestos complexos. Eles simplesmente desejam que a realidade se dobre à sua vontade, e muitas vezes ela o faz, de maneiras espetaculares e imprevisíveis. Este poder bruto os torna incrivelmente potentes, mas também perigosos. Um jovem feiticeiro pode acidentalmente incendiar uma taverna com um espirro ou congelar um lago com uma birra. O desafio de um feiticeiro não é aprender a magia, mas aprender a controlá-la antes que ela os consuma.
        """,
        "stats_primarios": ["carisma", "constituicao"],
        "habilidades_iniciais": ["raio_do_caos", "onda_de_forca"],
        "equipamento_inicial": {"arma_principal": "adaga_ornamentada", "peitoral": "roupas_finas"}
    },

    # =================================== BRUXO ===================================
    "bruxo": {
        "nome": "Bruxo",
        "descricao": "Um conjurador que obtém seu poder através de um pacto com uma entidade de outro mundo. Sua magia é poderosa, mas sempre tem um preço.",
        "lore": """
O poder pode ser conquistado, pode ser herdado, ou pode ser... negociado. O bruxo escolhe o terceiro caminho. Em busca de conhecimento proibido ou poder para superar seus limites, eles fazem um pacto com um ser de poder imenso: um arquidemônio dos infernos, um grande ser antigo de além das estrelas, uma fada ardilosa ou um celestial enigmático.

Este patrono concede ao bruxo uma fração de seu poder, permitindo-lhes lançar feitiços estranhos e potentes que outros mortais não ousam tocar. No entanto, esse poder nunca é gratuito. O bruxo deve servir a seu patrono, cumprindo tarefas, coletando almas ou simplesmente agindo como seu agente no mundo mortal. A vida de um bruxo é um equilíbrio perigoso entre usar o poder que lhes foi dado e não se tornar um mero peão no jogo de seu mestre sobrenatural.
        """,
        "stats_primarios": ["carisma", "inteligencia"],
        "habilidades_iniciais": ["explosao_mistica", "maldição_do_patrono"],
        "equipamento_inicial": {"arma_principal": "grimorio_sombrio", "peitoral": "robe_escuro"}
    },

    # =================================== ARTÍFICE ===================================
    "artifice": {
        "nome": "Artífice",
        "descricao": "Um mestre da invenção, que funde magia e tecnologia para criar itens mágicos, autômatos e armas maravilhosas.",
        "lore": "O artífice vê a magia como um sistema complexo, esperando para ser decifrado e otimizado. Eles são engenheiros do arcano, capazes de infundir objetos mundanos com poder mágico. De torres de defesa automáticas a espadas que cospem fogo, suas criações são um testemunho da união entre a mente e a magia.",
        "stats_primarios": ["inteligencia", "destreza"],
        "habilidades_iniciais": ["infusao_magica", "construir_torreta"],
        "equipamento_inicial": {"arma_principal": "besta_leve", "peitoral": "avental_de_couro_reforcado"}
    },

    # =================================== CAVALEIRO ===================================
    "cavaleiro": {
        "nome": "Cavaleiro",
        "descricao": "Um guerreiro de armadura pesada focado na defesa, usando seu escudo e sua presença para proteger seus aliados e controlar o campo de batalha.",
        "lore": "O cavaleiro é a muralha inabalável. Treinados desde jovens na arte da defesa, eles aprendem que a melhor ofensa é uma defesa impenetrável. Eles são os guarda-costas da realeza, os protetores de relíquias sagradas e a âncora de qualquer formação de batalha.",
        "stats_primarios": ["constituicao", "forca"],
        "habilidades_iniciais": ["postura_defensiva", "provocacao_em_massa"],
        "equipamento_inicial": {"arma_principal": "espada_longa", "escudo": "escudo_torre", "peitoral": "armadura_de_placas_completa"}
    },

    # =================================== BATEDOR ===================================
    "batedor": {
        "nome": "Batedor",
        "descricao": "Especialista em reconhecimento e sobrevivência, usando conhecimento do terreno e ataques à distância para enfraquecer os inimigos antes que a batalha comece.",
        "lore": "Os olhos e ouvidos do exército. O batedor se move à frente do grupo, mapeando o terreno, identificando ameaças e preparando o campo de batalha. Eles são mestres em armadilhas e emboscadas, e sua paciência é sua maior arma.",
        "stats_primarios": ["destreza", "sabedoria"],
        "habilidades_iniciais": ["tiro_marcado", "montar_armadilha"],
        "equipamento_inicial": {"arma_principal": "arco_longo", "peitoral": "gibao_de_couro"}
    },

    # =================================== SACERDOTE DAS SOMBRAS ===================================
    "sacerdote_das_sombras": {
        "nome": "Sacerdote das Sombras",
        "descricao": "Um clérigo que acredita que o equilíbrio exige tanto a luz quanto a escuridão, usando magias de sombras para debilitar e atormentar a mente dos inimigos.",
        "lore": "Nem toda divindade é de luz. Alguns deuses residem no crepúsculo e no vazio. Seus sacerdotes não são maus, mas entendem que a dor e o medo são ferramentas tão válidas quanto a cura e a esperança. Eles usam o poder das sombras para proteger a luz, uma filosofia perigosa que muitas vezes os coloca em conflito com seus irmãos mais dogmáticos.",
        "stats_primarios": ["sabedoria", "inteligencia"],
        "habilidades_iniciais": ["toque_vampirico", "palavra_de_dor"],
        "equipamento_inicial": {"arma_principal": "adaga_ritualistica", "peitoral": "robe_negro"}
    },

    # =================================== ESPADACHIM ===================================
    "espadachim": {
        "nome": "Espadachim (Swashbuckler)",
        "descricao": "Um duelista carismático e audacioso, que luta com estilo e confiança, transformando o combate em uma performance.",
        "lore": "O espadachim vive por sua reputação e seu charme. Eles são duelistas elegantes, piratas galantes e heróis fanfarrões. Para eles, a batalha é um palco, e eles são os atores principais. Eles confiam em sua agilidade, em seus reflexos rápidos e em um sorriso atrevido para vencer seus oponentes, muitas vezes desmoralizando-os com um insulto espirituoso antes de desferir o golpe final.",
        "stats_primarios": ["destreza", "carisma"],
        "habilidades_iniciais": ["finta_audaciosa", "duelo_elegante"],
        "equipamento_inicial": {"arma_principal": "rapiera", "peitoral": "camisa_de_seda"}
    },

    # =================================== ATIRADOR ===================================
    "atirador": {
        "nome": "Atirador (Gunslinger)",
        "descricao": "Um pioneiro de uma nova forma de combate, usando armas de fogo primitivas, mas mortais. Uma mistura de inventor e soldado.",
        "lore": "Em um mundo de espadas e magia, o som de um tiro é o som do futuro. Os atiradores são engenheiros e guerreiros que dominaram a arte da pólvora negra. Suas armas são barulhentas, imprecisas e demoram para recarregar, mas um único tiro bem colocado pode perfurar a armadura mais forte e derrubar o monstro mais resistente. Eles são vistos com desconfiança por guerreiros tradicionais, mas seu poder de fogo é inegável.",
        "stats_primarios": ["destreza", "inteligencia"],
        "habilidades_iniciais": ["tiro_mirado", "consertar_arma"],
        "equipamento_inicial": {"arma_principal": "pistola_de_pederneira", "peitoral": "casaco_de_couro"}
    },

    # =================================== XAMÃ ===================================
    "xama": {
        "nome": "Xamã",
        "descricao": "Um guia espiritual que se comunica com os espíritos elementais e ancestrais, usando totens para canalizar seu poder.",
        "lore": "O xamã é a ponte entre o mundo físico e o mundo espiritual. Eles não comandam os elementos como um mago, nem servem a um deus como um clérigo. Em vez disso, eles negociam com os espíritos. Eles pedem ao espírito do fogo para queimar seus inimigos, ao espírito da terra para proteger seus aliados e aos espíritos de seus ancestrais por sabedoria. Seu poder é antigo, tribal e profundamente conectado ao mundo ao seu redor.",
        "stats_primarios": ["sabedoria", "constituicao"],
        "habilidades_iniciais": ["choque_flamejante", "totem_de_cura"],
        "equipamento_inicial": {"arma_principal": "clava_ritualistica", "peitoral": "vestes_tribais"}
    },

    # =================================== MONGE ===================================
    "monge": {
        "nome": "Monge",
        "descricao": "Um artista marcial disciplinado que transforma seu próprio corpo em uma arma. Usa energia espiritual, ou 'Ki', para realizar feitos sobre-humanos.",
        "lore": "Através de uma disciplina rigorosa e meditação, o monge alcança a perfeição do corpo e da mente. Eles não precisam de armas ou armaduras, pois seus punhos são tão duros quanto o aço e sua pele tão resistente quanto o couro. Eles canalizam uma energia interior chamada Ki, que lhes permite se mover mais rápido que o olho pode ver, desferir uma rajada de golpes em um piscar de olhos e pegar flechas no ar.",
        "stats_primarios": ["destreza", "sabedoria"],
        "habilidades_iniciais": ["rajada_de_golpes", "defesa_paciente"],
        "equipamento_inicial": {"arma_principal": "desarmado", "peitoral": "roupas_simples_de_monasterio"}
    },

    # =================================== NECROMANTE ===================================
    "necromante": {
        "nome": "Necromante",
        "descricao": "Um mago que estuda a tênue linha entre a vida e a morte, comandando os mortos e manipulando a energia vital.",
        "lore": "A necromancia é talvez a mais temida e incompreendida de todas as artes mágicas. Enquanto muitos a veem como puramente maligna, para o necromante, a morte não é o fim, mas sim uma outra forma de existência e uma fonte de poder. Eles podem reanimar esqueletos e zumbis para servi-los, drenar a força vital de seus inimigos e se comunicar com os espíritos dos mortos. Alguns buscam a imortalidade, tornando-se lichs, enquanto outros usam seu poder para entender os maiores mistérios da existência.",
        "stats_primarios": ["inteligencia", "constituicao"],
        "habilidades_iniciais": ["erguer_morto", "raio_doentio"],
        "equipamento_inicial": {"arma_principal": "adaga_de_osso", "peitoral": "robe_com_capuz"}
    },

    # =================================== GLADIADOR ===================================
    "gladiador": {
        "nome": "Gladiador",
        "descricao": "Um guerreiro focado em espetáculo e combate de arena. Mestre em múltiplas armas, luta para ganhar a glória e o favor da multidão.",
        "lore": "O gladiador não luta por um reino ou por uma causa, mas pela glória retumbante da arena. Cada movimento é tanto um ataque quanto uma performance. Eles são mestres em usar armas exóticas e em lutar em desvantagem, transformando o perigo em um espetáculo para a multidão delirante. Fora da arena, são mercenários formidáveis, cuja reputação os precede.",
        "stats_primarios": ["forca", "carisma"],
        "habilidades_iniciais": ["golpe_de_exibicao", "rede_e_tridente"],
        "equipamento_inicial": {"arma_principal": "gladio", "escudo":"parma", "peitoral": "armadura_de_gladiador"}
    },

    # =================================== CAÇADOR DE RECOMPENSAS ===================================
    "cacador_de_recompensas": {
        "nome": "Caçador de Recompensas",
        "descricao": "Um rastreador implacável que caça alvos por dinheiro. Utiliza uma mistura de habilidades de combate, rastreamento e investigação.",
        "lore": "O caçador de recompensas é a personificação da tenacidade. Seja caçando um fora-da-lei nas ruas de uma metrópole ou uma besta rara nas profundezas de uma floresta, eles não desistem até que o trabalho esteja feito. Eles são pragmáticos, usando qualquer ferramenta à sua disposição - de armadilhas a venenos, de bestas a bombas - para garantir que seu alvo seja capturado ou eliminado.",
        "stats_primarios": ["destreza", "inteligencia"],
        "habilidades_iniciais": ["rastrear_alvo", "disparo_debilitante"],
        "equipamento_inicial": {"arma_principal": "besta_pesada", "arma_secundaria": "machete", "peitoral": "sobretudo_de_couro"}
    },

    # =================================== INQUISIDOR ===================================
    "inquisidor": {
        "nome": "Inquisidor",
        "descricao": "Um caçador de hereges e feiticeiros, que combina fervor divino com táticas de investigação e combate. Implacável em sua busca pela verdade e purificação.",
        "lore": "Onde há suspeita de corrupção sombria, o Inquisidor é enviado. Eles são os detetives e executores das ordens sagradas, treinados para ver através de mentiras e ilusões. Um inquisidor é tanto temido quanto respeitado, pois seu julgamento é rápido e muitas vezes final. Eles usam magia divina para extrair confissões, detectar o mal e purificar a corrupção com fogo sagrado.",
        "stats_primarios": ["sabedoria", "forca"],
        "habilidades_iniciais": ["julgamento", "fogo_purificador"],
        "equipamento_inicial": {"arma_principal": "martelo_de_guerra", "peitoral": "armadura_de_placas_com_insignia"}
    },

    # =================================== MAGO DE BATALHA ===================================
    "mago_de_batalha": {
        "nome": "Mago de Batalha",
        "descricao": "Um mago que treina para o combate na linha de frente, fundindo magia arcana com proeza marcial. Usa armaduras e desfere feitiços de toque.",
        "lore": "O mago de batalha ri da ideia de se esconder atrás de seus companheiros. Eles treinam seus corpos assim como suas mentes, aprendendo a usar armaduras e a lutar corpo a corpo. Sua magia é canalisada através de suas armas, transformando uma lâmina comum em uma condutora de energia arcana. Eles são uma visão rara e aterrorizante no campo de batalha: uma tempestade de aço e feitiçaria.",
        "stats_primarios": ["inteligencia", "forca"],
        "habilidades_iniciais": ["golpe_arcano", "armadura_de_mago"],
        "equipamento_inicial": {"arma_principal": "espada_longa", "peitoral": "peitoral_de_aço", "luvas": "manoplas_de_batalha"}
    },

    # =================================== ILUSIONISTA ===================================
    "ilusionista": {
        "nome": "Ilusionista",
        "descricao": "Um mestre do engano e da manipulação mental. Cria imagens fantasmagóricas, confunde os sentidos e controla seus inimigos sem desferir um único golpe físico.",
        "lore": "Para o ilusionista, a percepção é a realidade. Por que invocar uma bola de fogo real quando uma ilusão de um dragão pode fazer o exército inimigo fugir de medo? Eles são artistas do engano, tecendo magias que enganam os olhos, ouvidos e mentes. Suas habilidades são usadas para distração, espionagem e para derrotar inimigos fazendo-os lutar contra seus próprios medos.",
        "stats_primarios": ["inteligencia", "carisma"],
        "habilidades_iniciais": ["imagem_espelhada", "medo_fantasmagorico"],
        "equipamento_inicial": {"arma_principal": "cajado_elegante", "peitoral": "robe_com_padroes_hipnoticos"}
    },

    # =================================== MESTRE DAS FERAS ===================================
    "mestre_das_feras": {
        "nome": "Mestre das Feras",
        "descricao": "Um guerreiro que luta em perfeita harmonia com um ou mais companheiros animais. Sua força vem da coordenação e do vínculo com suas feras.",
        "lore": "O Mestre das Feras e seu companheiro animal são duas metades de um todo. O vínculo deles é mais profundo do que o de um ranger; é uma conexão quase telepática forjada em anos de caça e sobrevivência juntos. Eles lutam como uma unidade, com o mestre criando aberturas para que a fera ataque, e a fera protegendo seu mestre de perigos. Um Mestre das Feras pode ser encontrado com uma variedade de companheiros, de lobos velozes a ursos esmagadores ou aves de rapina mortais.",
        "stats_primarios": ["forca", "destreza"],
        "habilidades_iniciais": ["ataque_coordenado", "vinculo_bestial"],
        "equipamento_inicial": {"arma_principal": "machadinha", "arma_secundaria": "chicote", "peitoral": "armadura_de_couro_reforcado"}
    },

    # =================================== PIROMANTE ===================================
    "piromante": {
        "nome": "Piromante",
        "descricao": "Um mago especializado na mais destrutiva das escolas elementais: o fogo. Suas magias queimam, explodem e incendeiam tudo em seu caminho.",
        "lore": "Alguns magos buscam conhecimento, outros buscam controle. O piromante busca a purificação através do fogo. Eles são fascinados pela chama, vendo nela tanto a beleza da criação quanto o poder da destruição total. Sua personalidade é muitas vezes tão volátil quanto sua magia, e eles são conhecidos por sua paixão e temperamento explosivo. Em batalha, eles são artilharia viva, lançando torrentes de chamas e bolas de fogo que deixam apenas cinzas para trás.",
        "stats_primarios": ["inteligencia", "constituicao"],
        "habilidades_iniciais": ["seta_de_fogo", "aura_flamejante"],
        "equipamento_inicial": {"arma_principal": "cajado_carbonizado", "peitoral": "robe_vermelho"}
    },

    # =================================== CRIOMANTE ===================================
    "criomante": {
        "nome": "Criomante",
        "descricao": "Um mago focado no controle do frio e do gelo. Congela inimigos, cria barreiras defensivas e retarda o campo de batalha.",
        "lore": "O oposto do piromante, o criomante encontra poder no zero absoluto. Sua magia é de controle e preservação. Eles são calculistas e pacientes, preferindo imobilizar e enfraquecer seus inimigos em vez de aniquilá-los diretamente. Eles podem congelar um rio para criar uma ponte, proteger seus aliados com escudos de gelo ou parar um inimigo em suas trilhas com um toque gelado. Sua presença pode esfriar o ar e o coração de seus oponentes.",
        "stats_primarios": ["inteligencia", "sabedoria"],
        "habilidades_iniciais": ["lanca_de_gelo", "armadura_de_geada"],
        "equipamento_inicial": {"arma_principal": "varinha_de_cristal", "peitoral": "robe_branco_e_azul"}
    },

    # =================================== GEOMANTE ===================================
    "geomante": {
        "nome": "Geomante",
        "descricao": "Um mago que extrai poder da terra, da pedra e das montanhas. Molda o terreno, invoca tremores e se protege com a força da rocha.",
        "lore": "O geomante é paciente, teimoso e inabalável como a montanha. Eles sentem o poder pulsando sob seus pés e podem moldá-lo à sua vontade. Eles não são chamativos, mas sua magia é fundamental e poderosa. Um geomante pode erguer uma muralha de pedra do chão, prender inimigos em areia movediça ou lançar pedregulhos do tamanho de casas. Eles são a base de qualquer grupo, oferecendo uma defesa sólida e um poder esmagador.",
        "stats_primarios": ["inteligencia", "constituicao"],
        "habilidades_iniciais": ["pele_de_pedra", "arremessar_rocha"],
        "equipamento_inicial": {"arma_principal": "martelo_de_pedra", "peitoral": "robe_marrom"}
    },

    # =================================== AEROMANTE ===================================
    "aeromante": {
        "nome": "Aeromante",
        "descricao": "Um mago que comanda os ventos e os céus. Usa o poder das tempestades para empurrar inimigos, criar vendavais e invocar relâmpagos.",
        "lore": "Livre e imprevisível como o vento, o aeromante é um mestre do ar. Eles veem o campo de batalha como um tabuleiro de xadrez, movendo as peças com rajadas de vento e controlando o espaço aéreo. Eles podem criar um silêncio mortal roubando o ar dos pulmões de um inimigo, ou um rugido ensurdecedor com um tornado localizado. Sua mobilidade é incomparável, pois podem usar o vento para se impulsionar ou até mesmo voar.",
        "stats_primarios": ["inteligencia", "destreza"],
        "habilidades_iniciais": ["rajada_de_vento", "salto_do_vento"],
        "equipamento_inicial": {"arma_principal": "cajado_leve", "peitoral": "roupas_esvoacantes"}
    },

    # =================================== ELETROMANTE ===================================
    "eletromante": {
        "nome": "Eletromante",
        "descricao": "Um mago que canaliza a energia bruta dos relâmpagos e da eletricidade. Sua magia é rápida, mortal e pode paralisar seus alvos.",
        "lore": "O eletromante lida com a energia pura e crepitante da tempestade. Sua magia não é sutil; é uma descarga instantânea de poder avassalador. Eles são frequentemente energéticos e de raciocínio rápido, refletindo a natureza de sua magia. Em combate, eles lançam raios em cadeia que saltam de um inimigo para outro, sobrecarregam autômatos e deixam seus oponentes convulsionando no chão, incapazes de se mover.",
        "stats_primarios": ["inteligencia", "destreza"],
        "habilidades_iniciais": ["choque", "raio_em_cadeia"],
        "equipamento_inicial": {"arma_principal": "haste_de_metal", "peitoral": "robe_com_fios_de_cobre"}
    },

    # =================================== ALQUIMISTA ===================================
    "alquimista": {
        "nome": "Alquimista",
        "descricao": "Um cientista que usa conhecimento de química e reagentes exóticos para criar poções, bombas e mutagênicos. Mestre da transmutação.",
        "lore": "Onde o artífice constrói, o alquimista mistura. Eles são os mestres das poções, dos venenos e das transformações. Um alquimista pode criar um elixir que concede força de gigante, uma bomba que dissolve aço ou um mutagênico que altera sua própria fisiologia para se adaptar a uma situação. Eles estão sempre em busca de ingredientes raros e do conhecimento para desbloquear os segredos da matéria.",
        "stats_primarios": ["inteligencia", "destreza"],
        "habilidades_iniciais": ["arremessar_bomba_de_fogo", "criar_pocao_de_cura_rapida"],
        "equipamento_inicial": {"arma_principal": "adaga_reforcada", "peitoral": "avental_de_alquimista", "acessorio": "bolsa_de_reagentes"}
    },

    # =================================== MESTRE CERVEJEIRO ===================================
    "mestre_cervejeiro": {
        "nome": "Mestre Cervejeiro",
        "descricao": "Um monge ou guerreiro que encontra poder em bebidas alcoólicas especialmente preparadas. Luta em um estilo de luta aparentemente bêbado, mas altamente eficaz.",
        "lore": "O Mestre Cervejeiro é uma figura subestimada. Muitos o veem como um mero bêbado, mas seus movimentos desajeitados escondem um estilo de luta fluido e imprevisível. Eles preparam infusões místicas que, quando consumidas, lhes concedem agilidade, resistência ou até mesmo a capacidade de cuspir fogo. Para o Mestre Cervejeiro, a taverna não é apenas um lugar para relaxar, é um templo e um laboratório.",
        "stats_primarios": ["constituicao", "forca"],
        "habilidades_iniciais": ["estilo_do_bebado", "baforada_de_fogo_alcoolico"],
        "equipamento_inicial": {"arma_principal": "barril_pequeno_nas_costas", "peitoral": "roupas_rusticas"}
    },

    # =================================== VIDENTE ===================================
    "vidente": {
        "nome": "Vidente",
        "descricao": "Um conjurador que perscruta o passado, o presente e o futuro. Usa seu conhecimento para prever os movimentos do inimigo e alterar o destino.",
        "lore": "O vidente carrega o fardo de ver o que foi, o que é e o que poderia ser. Eles leem os presságios nas estrelas, nas entranhas de um sacrifício ou no fundo de uma poça d'água. Em batalha, seu poder não é destrutivo, mas sim de controle absoluto. Eles podem prever o golpe de um inimigo antes que ele seja dado, identificar uma fraqueza que ainda não foi explorada ou vislumbrar o caminho para a vitória. No entanto, o conhecimento do futuro é uma faca de dois gumes, e muitos videntes enlouquecem com as possibilidades que veem.",
        "stats_primarios": ["sabedoria", "inteligencia"],
        "habilidades_iniciais": ["premonicao", "maldição_do_azar"],
        "equipamento_inicial": {"arma_principal": "orbe_de_cristal", "peitoral": "mantos_de_oraculo"}
    },

    # =================================== SAMURAI ===================================
    "samurai": {
        "nome": "Samurai",
        "descricao": "Um guerreiro de uma terra distante, ligado por um código de honra estrito. Mestre da katana, sua velocidade e precisão são incomparáveis.",
        "lore": "O samurai é um guerreiro de elite, cuja vida é dedicada ao bushido, o caminho do guerreiro. Sua lealdade a seu senhor é absoluta, e sua honra é mais valiosa que sua própria vida. Em combate, eles são poetas da morte. Usando sua katana, eles podem cortar um oponente em dois com um único golpe relâmpago. Sua armadura, embora pareça ornamentada, é funcional e permite uma grande mobilidade. Um samurai errante, um ronin, é um guerreiro perigoso em busca de um novo propósito ou de uma morte honrada.",
        "stats_primarios": ["forca", "destreza"],
        "habilidades_iniciais": ["golpe_iaijutsu", "postura_inabalavel"],
        "equipamento_inicial": {"arma_principal": "katana", "arma_secundaria": "wakizashi", "peitoral": "armadura_o-yoroi"}
    },

    # =================================== NINJA ===================================
    "ninja": {
        "nome": "Ninja",
        "descricao": "Um agente de furtividade e espionagem de uma terra distante. Usa táticas de guerrilha, ferramentas exóticas e artes marciais para eliminar seus alvos.",
        "lore": "O ninja opera nas sombras, um fantasma no meio da noite. Eles são os espiões e assassinos de aluguel, mestres do ninjutsu. Sua arte não é a do combate honrado, mas da vitória a qualquer custo. Eles usam bombas de fumaça para desaparecer, shurikens para distrair e sua ninjatō para desferir golpes mortais. Um ninja pode se infiltrar na fortaleza mais segura, roubar o segredo mais bem guardado e desaparecer sem deixar vestígios.",
        "stats_primarios": ["destreza", "inteligencia"],
        "habilidades_iniciais": ["bomba_de_fumaca", "substituicao"],
        "equipamento_inicial": {"arma_principal": "ninjato", "acessorio": "shurikens", "peitoral": "traje_shinobi"}
    },

    # =================================== CORSÁRIO ===================================
    "corsario": {
        "nome": "Corsário",
        "descricao": "Um marinheiro e guerreiro dos mares. Luta com uma mistura de esgrima e táticas sujas, e é um mestre da navegação e do combate a bordo.",
        "lore": "A vida do corsário é o mar. Eles são os piratas, os comerciantes e os exploradores dos oceanos. Eles são tão confortáveis no convés de um navio balançando quanto um guerreiro em terra firme. Em combate, são pragmáticos e impiedosos, usando pistolas, cimitarras e qualquer coisa que possam pegar para ganhar vantagem. Eles vivem por seu próprio código, leais apenas à sua tripulação e ao seu capitão.",
        "stats_primarios": ["destreza", "forca"],
        "habilidades_iniciais": ["chute_baixo", "tiro_de_pistola"],
        "equipamento_inicial": {"arma_principal": "cimitarra", "arma_secundaria": "pistola_de_pederneira", "peitoral": "casaco_de_capitao"}
    },

    # =================================== DOMADOR ===================================
    "domador": {
        "nome": "Domador",
        "descricao": "Um especialista em capturar, treinar e lutar ao lado de monstros e bestas. Seu poder está na variedade e força de suas criaturas.",
        "lore": "Enquanto o Mestre das Feras forma um vínculo profundo com um único companheiro, o Domador vê o mundo como um zoológico de potencial. Eles são colecionadores, sempre em busca de novas criaturas para adicionar à sua coleção. Eles usam iscas, armadilhas e, por vezes, força bruta para capturar monstros, e então os treinam para lutar em arenas ou ao seu lado em aventuras. O poder de um domador é diretamente proporcional à força e variedade de seu estábulo de monstros.",
        "stats_primarios": ["carisma", "sabedoria"],
        "habilidades_iniciais": ["capturar_besta", "ordem_de_ataque"],
        "equipamento_inicial": {"arma_principal": "chicote", "peitoral": "roupas_reforcadas"}
    },

    # =================================== MAGO DO SANGUE ===================================
    "mago_do_sangue": {
        "nome": "Mago do Sangue",
        "descricao": "Um conjurador que usa a própria força vital - a sua e a dos outros - como combustível para sua magia. Uma arte poderosa, mas proibida.",
        "lore": "A magia do sangue é uma das artes mais antigas e temidas. O mago do sangue entende que o sangue é poder, a própria essência da vida. Eles podem sacrificar sua própria vitalidade para lançar feitiços de poder incrível ou podem extrair a força vital de seus inimigos para se curar e fortalecer. É um caminho perigoso, que corrompe tanto o corpo quanto a alma, e aqueles que o praticam são caçados como os piores dos monstros.",
        "stats_primarios": ["constituicao", "inteligencia"],
        "habilidades_iniciais": ["sacrificio_de_sangue", "lanca_de_sangue"],
        "equipamento_inicial": {"arma_principal": "adaga_sacrificial", "peitoral": "robe_manchado_de_sangue"}
    },

    # =================================== DEFENSOR ===================================
    "defensor": {
        "nome": "Defensor",
        "descricao": "Um especialista em proteção. Usa armadura pesada e um escudo para se interpor entre seus aliados e o perigo, absorvendo danos e resistindo a golpes.",
        "lore": "O Defensor é a âncora de qualquer grupo. Enquanto outros se concentram em causar dano, o único propósito do Defensor é sobreviver e proteger. Eles são mestres em usar seu escudo não apenas para bloquear, mas também para desarmar e atordoar. Sua determinação é sua maior arma, permitindo-lhes suportar punições que derrubariam qualquer outro guerreiro.",
        "stats_primarios": ["constituicao", "forca"],
        "habilidades_iniciais": ["bloqueio_com_escudo", "intervir"],
        "equipamento_inicial": {"arma_principal": "espada_curta_ferro", "escudo": "escudo_de_torre", "peitoral": "armadura_de_placas_completa"}
    },

    # =================================== DUELISTA ===================================
    "duelista": {
        "nome": "Duelista",
        "descricao": "Um guerreiro focado no combate um-a-um. Mestre da esgrima, usa velocidade, precisão e contra-ataques para derrotar seus oponentes.",
        "lore": "Para o duelista, o campo de batalha é uma série de confrontos individuais. Eles se destacam em isolar um único oponente e desmantelar sua defesa com uma série de ataques precisos. Eles não usam armaduras pesadas, preferindo a mobilidade para se esquivar e aparar. Um duelista é um artista da lâmina, e seu estilo de luta é uma dança mortal de fintas, estocadas e ripostas.",
        "stats_primarios": ["destreza", "forca"],
        "habilidades_iniciais": ["aparar_e_ripostar", "estocada_precisa"],
        "equipamento_inicial": {"arma_principal": "florete", "peitoral": "jaqueta_de_couro"}
    },

    # =================================== BERSERKER ===================================
    "berserker": {
        "nome": "Berserker",
        "descricao": "Um guerreiro que entra em um estado de fúria cega em batalha, ignorando a dor e lutando com ferocidade animal. Mais selvagem e incontrolável que um Bárbaro.",
        "lore": "Se o Bárbaro canaliza a fúria, o Berserker é consumido por ela. Sua raiva não é uma ferramenta; é uma maldição. Em batalha, eles perdem todo o senso de si mesmos, tornando-se máquinas de matar que não distinguem amigo de inimigo. Eles ignoram ferimentos que seriam mortais para outros, lutando até que seus corpos finalmente cedam. Fora da batalha, são muitas vezes indivíduos atormentados, temerosos do monstro que vive dentro deles.",
        "stats_primarios": ["forca", "constituicao"],
        "habilidades_iniciais": ["furia_cega", "ignorar_dor"],
        "equipamento_inicial": {"arma_principal": "machado_duplo", "peitoral": "peito_nu_com_pinturas_de_guerra"}
    },

    # =================================== ACÓLITO ===================================
    "acolito": {
        "nome": "Acólito",
        "descricao": "Um aprendiz de uma ordem religiosa ou culto. Focado em apoiar seus superiores, aprender os dogmas e realizar rituais menores.",
        "lore": "O acólito está no primeiro degrau de uma longa escada para o poder divino ou profano. Eles passam seus dias estudando textos sagrados, limpando o templo e auxiliando os clérigos e sacerdotes em seus deveres. Sua magia ainda é fraca, mas sua fé é forte e pura. Eles são os futuros líderes, profetas ou mártires de sua fé.",
        "stats_primarios": ["sabedoria", "carisma"],
        "habilidades_iniciais": ["bencao_menor", "assistencia_ritualistica"],
        "equipamento_inicial": {"arma_principal": "maça_leve", "peitoral": "tunica_de_acolito"}
    },

    # =================================== ANDARILHO ESPIRITUAL ===================================
    "andarilho_espiritual": {
        "nome": "Andarilho Espiritual",
        "descricao": "Um indivíduo que pode projetar sua consciência para fora de seu corpo, viajando como um fantasma para espionar, explorar ou interagir com outros espíritos.",
        "lore": "O andarilho espiritual vive com um pé em dois mundos. Seu corpo físico pode estar em um lugar, mas sua mente está livre para vagar. Eles podem atravessar paredes, espionar conversas e ver as almas dos vivos e dos mortos. É uma habilidade perigosa; se seu corpo for morto enquanto seu espírito está fora, eles se tornam um fantasma para sempre. Eles são frequentemente consultados como médiuns, espiões ou guias para locais assombrados.",
        "stats_primarios": ["sabedoria", "constituicao"],
        "habilidades_iniciais": ["projecao_astral", "toque_etereo"],
        "equipamento_inicial": {"arma_principal": "desarmado", "peitoral": "roupas_simples"}
    },

    # =================================== CAÇADOR DE BRUXAS ===================================
    "cacador_de_bruxas": {
        "nome": "Caçador de Bruxas",
        "descricao": "Um guerreiro especializado em caçar e matar usuários de magia corrompida. Resistente à magia e treinado para explorar as fraquezas dos conjuradores.",
        "lore": "Onde a magia floresce, também floresce a corrupção. O Caçador de Bruxas é a resposta a essa ameaça. Eles são céticos, pragmáticos e muitas vezes brutais. Eles não confiam em magia e são treinados para resistir a seus efeitos. Com bestas de repetição, armadilhas anti-magia e um conhecimento profundo das artes sombrias, eles são o pesadelo de todo bruxo e necromante.",
        "stats_primarios": ["sabedoria", "destreza"],
        "habilidades_iniciais": ["resistencia_a_magia", "disparo_de_ferro_frio"],
        "equipamento_inicial": {"arma_principal": "besta_de_repeticao", "arma_secundaria": "espada_curta_prateada", "peitoral": "sobretudo_de_couro_escuro"}
    },

    # =================================== TEMPLÁRIO ===================================
    "templario": {
        "nome": "Templário",
        "descricao": "Um guerreiro de uma ordem sagrada, que combina a disciplina de um soldado com o zelo de um clérigo. Protege os locais sagrados e caça os inimigos de sua fé.",
        "lore": "O Templário é o braço armado de uma igreja. Eles são mais disciplinados que um paladino e mais marciais que um clérigo. Eles são os guardiões de templos, as escoltas de peregrinos e a linha de frente em guerras santas. Sua fé lhes concede poder para abençoar suas armas e resistir à corrupção, mas seu foco principal é a proeza marcial a serviço de sua divindade.",
        "stats_primarios": ["forca", "sabedoria"],
        "habilidades_iniciais": ["arma_abençoada", "escudo_da_fe"],
        "equipamento_inicial": {"arma_principal": "espada_longa", "escudo": "escudo_com_simbolo_sagrado", "peitoral": "armadura_de_placas_ornamentada"}
    },

    # =================================== ARCANISTA ===================================
    "arcanista": {
        "nome": "Arcanista",
        "descricao": "Um estudioso que busca o conhecimento arcano por si só. Um teórico da magia, focado em metamecanica mágica e feitiços complexos.",
        "lore": "Se o mago é o cientista, o arcanista é o filósofo. Eles não estão interessados apenas em como a magia funciona, mas por que ela funciona. Eles estudam a origem da magia, a natureza dos planos e as leis que governam a própria realidade. Seu poder não está em lançar a bola de fogo mais rápida, mas em tecer feitiços de complexidade e sutileza incríveis, capazes de reescrever as regras do combate.",
        "stats_primarios": ["inteligencia", "sabedoria"],
        "habilidades_iniciais": ["analise_magica", "runa_de_poder"],
        "equipamento_inicial": {"arma_principal": "tomo_arcano", "peitoral": "robe_de_erudito"}
    },

    # =================================== BARDO DA BRAVURA ===================================
    "bardo_da_bravura": {
        "nome": "Bardo da Bravura",
        "descricao": "Um bardo que inspira coragem e heroísmo no campo de batalha. Luta na linha de frente, e suas canções são gritos de guerra.",
        "lore": "O Bardo da Bravura conta as histórias de heróis, e aspira a se tornar um. Eles não se contentam em ficar na retaguarda, cantando canções de apoio. Eles mergulham no coração da batalha, com um instrumento em uma mão e uma arma na outra. Suas canções são tão poderosas quanto os golpes de seus machados, incitando seus aliados a feitos de coragem sobre-humana.",
        "stats_primarios": ["carisma", "forca"],
        "habilidades_iniciais": ["cancao_de_batalha", "golpe_inspirador"],
        "equipamento_inicial": {"arma_principal": "machadinha", "arma_secundaria": "tambor_de_guerra", "peitoral": "cota_de_malha"}
    },

    # =================================== PATRULHEIRO URBANO ===================================
    "patrulheiro_urbano": {
        "nome": "Patrulheiro Urbano",
        "descricao": "Um ranger que adaptou suas habilidades para a selva de pedra. Mestre em se mover pelos telhados, rastrear em multidões e combate em espaços confinados.",
        "lore": "Para o Patrulheiro Urbano, as vielas são desfiladeiros e os telhados são as copas das árvores. Eles são os guardiões silenciosos das cidades, caçando criminosos e monstros que se escondem nas sombras urbanas. Eles conhecem cada atalho, cada esconderijo e cada informante. São mestres do parkour, da besta de mão e da lâmina curta, perfeitamente adaptados para a guerra nas ruas.",
        "stats_primarios": ["destreza", "sabedoria"],
        "habilidades_iniciais": ["movimento_de_telhado", "tiro_rapido_de_besta"],
        "equipamento_inicial": {"arma_principal": "besta_de_mao", "arma_secundaria": "espada_curta_ferro", "peitoral": "capuz_e_manto_escuro"}
    },

    # =================================== PUGILISTA ===================================
    "pugilista": {
        "nome": "Pugilista",
        "descricao": "Um lutador de rua que confia em seus punhos e em sua resistência. Não tem a disciplina do monge, mas compensa com força bruta e determinação.",
        "lore": "O pugilista aprendeu a lutar nas tavernas e nas docas, onde as regras são poucas e a sobrevivência é tudo. Eles não usam 'Ki'; eles usam socos, ganchos e cabeçadas. Sua técnica é crua, mas eficaz. Eles são incrivelmente resistentes, capazes de levar uma surra e continuar de pé, esperando a oportunidade de desferir um único golpe nocauteador que pode encerrar qualquer luta.",
        "stats_primarios": ["forca", "constituicao"],
        "habilidades_iniciais": ["soco_direto", "queixo_de_granito"],
        "equipamento_inicial": {"arma_principal": "soqueiras_de_bronze", "peitoral": "camisa_rasgada"}
    }
}
