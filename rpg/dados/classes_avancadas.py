# ==============================================================================
# ARQUIVO DE DADOS: CLASSES AVANÇADAS
# ==============================================================================
#
# Este arquivo contém as definições para as classes avançadas, o auge
# das especializações de um personagem. Elas exigem um alto nível e
# maestria em classes intermediárias.
#
# ==============================================================================

CLASSES_AVANCADAS = {
    # =================================== LORDE DA GUERRA ===================================
    "lorde_da_guerra": {
        "nome": "Lorde da Guerra",
        "descricao": "Um mestre estrategista e um guerreiro incomparável, cuja presença no campo de batalha pode virar o rumo da guerra.",
        "lore": """
O Lorde da Guerra é mais do que um soldado; ele é o próprio coração da batalha. Ele entende a sinfonia do caos, o fluxo e refluxo do combate, e comanda seus aliados com uma precisão e carisma que beiram o sobrenatural. Sua voz pode inspirar um exército inteiro a lutar além de seus limites, e suas táticas podem desmantelar as forças inimigas antes mesmo que o primeiro golpe seja desferido. Eles são os generais, os campeões e os líderes que forjam impérios.
        """,
        "requisitos": {
            "nivel_total": 50,
            "classes": [{"id_classe": "gladiador", "nivel": 20}, {"id_classe": "cavaleiro", "nivel": 20}]
        },
        "stats_primarios": ["forca", "carisma", "inteligencia"],
        "habilidades_planejadas": ["comandar_aliados", "taticas_de_mestre", "presenca_inspiradora"]
    },

    # =================================== ARQUIMAGO DO TEMPO ===================================
    "arquimago_do_tempo": {
        "nome": "Arquimago do Tempo",
        "descricao": "Um arquimago que se aprofundou na mais proibida e perigosa de todas as escolas de magia: a cronomancia.",
        "lore": """
Manipular o tempo é brincar com o tecido da existência, um ato que os deuses proíbem e que a própria realidade resiste. O Arquimago do Tempo é um estudioso que ignorou esses avisos em sua busca por poder absoluto. Ele pode acelerar seus próprios movimentos para se tornar um borrão, retardar seus inimigos até que fiquem imóveis, e até mesmo vislumbrar futuros possíveis ou reverter pequenos eventos. No entanto, cada feitiço temporal cria ondulações no fluxo do tempo, com consequências muitas vezes imprevisíveis e catastróficas.
        """,
        "requisitos": {
            "nivel_total": 60,
            "classes": [{"id_classe": "arquimago", "nivel": 25}]
        },
        "stats_primarios": ["inteligencia", "sabedoria"],
        "habilidades_planejadas": ["paralisia_temporal", "aceleracao", "rebobinar"]
    },

    # =================================== MESTRE DAS SOMBRAS ===================================
    "mestre_das_sombras": {
        "nome": "Mestre das Sombras",
        "descricao": "O ápice do caminho do assassino. Um ser que se tornou um com a escuridão, capaz de se mover e atacar sem ser detectado.",
        "lore": """
O Mestre das Sombras não se esconde mais na escuridão; ele *é* a escuridão. Eles são lendas, mitos usados para assustar crianças e tiranos. Dizem que podem viajar através das sombras, criar duplicatas sombrias de si mesmos e matar um alvo em uma sala trancada sem deixar vestígios. Sua existência é um segredo bem guardado, e sua lealdade é apenas para si mesmos ou para a antiga entidade sombria que lhes concedeu tal poder.
        """,
        "requisitos": {
            "nivel_total": 50,
            "classes": [{"id_classe": "assassino", "nivel": 20}, {"id_classe": "trapaceiro_arcano", "nivel": 15}]
        },
        "stats_primarios": ["destreza", "inteligencia"],
        "habilidades_planejadas": ["passo_sombrio", "clone_de_sombras", "execucao_silenciosa"]
    },

    # =================================== HIEROFANTE ===================================
    "hierofante": {
        "nome": "Hierofante",
        "descricao": "Um canal direto para o poder divino ou primordial, um ser que personifica a vontade de seu deus ou da própria natureza.",
        "lore": """
O Hierofante é o mais alto dos sacerdotes. Eles não mais pedem por poder; eles o comandam. Sua fé é tão absoluta, sua conexão tão pura, que eles se tornam avatares de sua fonte de poder. Um Hierofante da natureza pode convocar florestas inteiras para a batalha, enquanto um Hierofante de um deus da luz pode invocar anjos para lutar ao seu lado. Eles são os líderes espirituais de seus credos, e suas palavras são consideradas a própria voz do divino.
        """,
        "requisitos": {
            "nivel_total": 55,
            "classes": [{"id_classe": "clerigo", "nivel": 25}, {"id_classe": "druida", "nivel": 25}]
        },
        "stats_primarios": ["sabedoria", "carisma"],
        "habilidades_planejadas": ["intervencao_divina", "palavra_de_poder", "um_com_o_mundo"]
    },

    # =================================== LÂMINA ARCANA ===================================
    "lamina_arcana": {
        "nome": "Lâmina Arcana (Spellblade)",
        "descricao": "A fusão perfeita entre a arte da espada e a magia arcana. Cada golpe de sua lâmina é um feitiço, e cada feitiço é tão afiado quanto sua lâmina.",
        "lore": """
O Lâmina Arcana alcançou o que a maioria dos magos de batalha apenas sonha: a harmonia perfeita. Não há mais separação entre o combate físico e o mágico. Seus movimentos são um fluxo contínuo de aço e energia. Eles podem aparar um golpe de machado com uma muralha de força, contra-atacar com uma lâmina envolta em raios e terminar a luta com uma explosão de fogo que emana de sua própria espada. Eles são os guerreiros mais versáteis e imprevisíveis do mundo.
        """,
        "requisitos": {
            "nivel_total": 45,
            "classes": [{"id_classe": "mago_de_batalha", "nivel": 20}]
        },
        "stats_primarios": ["forca", "destreza", "inteligencia"],
        "habilidades_planejadas": ["corte_elemental", "danca_do_feitico", "escudo_de_lamina"]
    },

    # =================================== AVATAR DA FÚRIA ===================================
    "avatar_da_furia": {
        "nome": "Avatar da Fúria",
        "descricao": "Um bárbaro que transcendeu a raiva, tornando-se a personificação viva da fúria primordial.",
        "lore": "O Avatar da Fúria não sente mais raiva; ele é a raiva. Sua fúria é tão potente que se manifesta fisicamente, criando uma aura de poder destrutivo que desintegra inimigos menores. Em seu auge, diz-se que podem crescer em tamanho, tornando-se gigantes de músculos e cicatrizes, cuja força pode abalar montanhas. Eles são desastres naturais ambulantes.",
        "requisitos": {
            "nivel_total": 50,
            "classes": [{"id_classe": "berserker", "nivel": 20}, {"id_classe": "protetor_ancestral", "nivel": 15}]
        },
        "stats_primarios": ["forca", "constituicao"],
        "habilidades_planejadas": ["furia_imortal", "aura_destrutiva", "golpe_quebra-mundo"]
    },

    # =================================== LENDA VIVA ===================================
    "lenda_viva": {
        "nome": "Lenda Viva",
        "descricao": "Um bardo cujas histórias e canções se tornaram tão poderosas que podem alterar a realidade e reescrever o destino.",
        "lore": "A Lenda Viva é um bardo que compreendeu a verdade final: a realidade é apenas uma história sendo contada. E se é uma história, ela pode ser reescrita. Suas canções não inspiram mais; elas comandam. Eles podem cantar uma canção de heroísmo e tornar um camponês em um campeão, ou cantar uma canção de tragédia e fazer um rei cair em desgraça. São os narradores do mundo, e sua voz é a pena do destino.",
        "requisitos": {
            "nivel_total": 50,
            "classes": [{"id_classe": "bardo_do_conhecimento", "nivel": 20}, {"id_classe": "bardo_da_bravura", "nivel": 20}]
        },
        "stats_primarios": ["carisma", "sabedoria"],
        "habilidades_planejadas": ["canção_da_criação", "reescrever_o_destino", "palavra_final"]
    },

    # =================================== ANDARILHO DOS PLANOS ===================================
    "andarilho_dos_planos": {
        "nome": "Andarilho dos Planos",
        "descricao": "Um mestre das viagens planares, que considera os diferentes planos de existência como seu playground pessoal.",
        "lore": "O Andarilho dos Planos não apenas viaja entre os mundos; ele os domina. Ele pode abrir portais para qualquer lugar que possa imaginar, convocar exércitos de criaturas de diferentes realidades e até mesmo criar seus próprios semi-planos. Eles são os exploradores supremos, os cartógrafos do multiverso, e seu conhecimento das diferentes realidades os torna uma das entidades mais poderosas e imprevisíveis da existência.",
        "requisitos": {
            "nivel_total": 55,
            "classes": [{"id_classe": "andarilho_do_horizonte", "nivel": 20}, {"id_classe": "invocador", "nivel": 20}]
        },
        "stats_primarios": ["sabedoria", "inteligencia"],
        "habilidades_planejadas": ["caminho_planar", "convocar_exercito_planar", "criar_semiplano"]
    },

    # =================================== GRÃO-MESTRE MONGE ===================================
    "grao-mestre_monge": {
        "nome": "Grão-Mestre Monge",
        "descricao": "Um monge que alcançou a iluminação, transcendendo as limitações do corpo físico e se tornando um com o fluxo do universo.",
        "lore": "O Grão-Mestre Monge não precisa mais de punhos de ferro ou de técnicas bêbadas. Ele alcançou um estado de perfeita harmonia com o universo. Seus movimentos não são mais seus; são os movimentos do vento e da água. Ele pode desferir golpes que atingem a alma do oponente, se mover mais rápido que o pensamento e se tornar intangível, pois seu corpo é apenas uma ilusão. Ele é a personificação da paz e do poder que vêm da verdadeira iluminação.",
        "requisitos": {
            "nivel_total": 60,
            "classes": [{"id_classe": "monge_do_punho_de_ferro", "nivel": 25}, {"id_classe": "mestre_bebado", "nivel": 25}]
        },
        "stats_primarios": ["sabedoria", "destreza"],
        "habilidades_planejadas": ["transcendencia_fisica", "golpe_na_alma", "unidade_com_o_todo"]
    },

    # =================================== LICH ===================================
    "lich": {
        "nome": "Lich",
        "descricao": "Um necromante que alcançou a imortalidade ao aprisionar sua alma em um objeto, tornando-se um mestre morto-vivo da magia.",
        "lore": "O Lich é o ápice da ambição necromântica. Através de um ritual profano, ele arrancou sua própria alma e a escondeu em um filactério. Enquanto o filactério existir, o Lich não pode ser verdadeiramente destruído. Livres do medo da morte, eles têm eras para acumular conhecimento e poder. São os tiranos de reinos de mortos-vivos, os mestres de exércitos de esqueletos e os magos mais temidos da história.",
        "requisitos": {
            "nivel_total": 60,
            "classes": [{"id_classe": "ceifador", "nivel": 25}]
        },
        "stats_primarios": ["inteligencia", "constituicao"],
        "habilidades_planejadas": ["filacterio", "invocar_legiao_de_mortos", "toque_paralisante_de_lich"]
    },

    # =================================== DEUS DA MORTE ===================================
    "deus_da_morte": {
        "nome": "Deus da Morte",
        "descricao": "Uma entidade que usurpou o poder de um deus da morte ou alcançou a divindade através da maestria sobre a vida e a morte.",
        "lore": "Há um poder no fim de todas as coisas, e o Deus da Morte o comanda. Seja por matar o deus da morte anterior ou por acumular tantas almas que sua própria essência se tornou divina, esta entidade agora governa o ciclo da vida e da morte. Eles podem matar com um pensamento, reanimar qualquer ser, e sua palavra é lei no pós-vida. Eles são o fim inevitável, a conclusão de todas as histórias.",
        "requisitos": {
            "nivel_total": 70,
            "classes": [{"id_classe": "lich", "nivel": 30}, {"id_classe": "ceifador", "nivel": 30}]
        },
        "stats_primarios": ["inteligencia", "sabedoria", "carisma"],
        "habilidades_planejadas": ["decreto_da_morte", "controle_sobre_o_pos-vida", "colheita_global"]
    },

    # =================================== FORJADOR DE MUNDOS ===================================
    "forjador_de_mundos": {
        "nome": "Forjador de Mundos",
        "descricao": "Um artífice de poder divino, capaz de construir não apenas autômatos, mas paisagens inteiras e semi-planos.",
        "lore": "O Forjador de Mundos vê a realidade como argila em suas mãos. Sua compreensão da matemática, da magia e da física é tão profunda que eles podem criar matéria do nada. Eles são os arquitetos dos deuses, construindo cidades flutuantes, forjando montanhas e criando mundos de bolso para seus mestres ou para si mesmos. Seu poder não é de destruição, mas de criação em uma escala inimaginável.",
        "requisitos": {
            "nivel_total": 60,
            "classes": [{"id_classe": "geometra_sagrado", "nivel": 25}, {"id_classe": "mestre_alquimista", "nivel": 25}]
        },
        "stats_primarios": ["inteligencia", "sabedoria"],
        "habilidades_planejadas": ["genesis", "moldar_terreno_em_massa", "criar_semiplano_permanente"]
    },

    # =================================== REI DOS LADRÕES ===================================
    "rei_dos_ladroes": {
        "nome": "Rei dos Ladrões",
        "descricao": "O mestre de todos os ladrões, um gênio do crime cuja rede de informações e influência se estende por todo o mundo.",
        "lore": "O Rei dos Ladrões não precisa mais roubar pessoalmente. Ele comanda uma guilda de ladrões, assassinos e espiões que abrange continentes. Ele sabe de todos os segredos, de todas as fraquezas e de todos os tesouros. Com uma palavra, ele pode derrubar um nobre, roubar uma relíquia de um cofre impenetrável ou iniciar uma guerra. Seu maior tesouro não é ouro, mas informação, e ele é a pessoa mais rica do mundo.",
        "requisitos": {
            "nivel_total": 50,
            "classes": [{"id_classe": "ladrao_de_almas", "nivel": 20}, {"id_classe": "assassino", "nivel": 20}]
        },
        "stats_primarios": ["destreza", "carisma", "inteligencia"],
        "habilidades_planejadas": ["comandar_guilda", "roubo_impossivel", "mestre_do_disfarce_absoluto"]
    },

    # =================================== TITÃ ===================================
    "tita": {
        "nome": "Titã",
        "descricao": "Um mortal que, através de força ou magia, alcançou o tamanho e o poder de um gigante, tornando-se uma força da natureza.",
        "lore": "O Titã é um mortal que se recusou a aceitar seus limites. Seja através de um ritual antigo, de um artefato poderoso ou de pura força de vontade, ele cresceu em tamanho e poder, rivalizando com os gigantes e dragões de antigamente. Sua força pode mover montanhas, e seus passos podem causar terremotos. Eles são a prova de que a determinação de um mortal pode elevá-lo ao nível dos monstros.",
        "requisitos": {
            "nivel_total": 60,
            "classes": [{"id_classe": "avatar_da_furia", "nivel": 25}, {"id_classe": "defensor_runico", "nivel": 25}]
        },
        "stats_primarios": ["forca", "constituicao"],
        "habilidades_planejadas": ["crescimento_titanico", "golpe_sismico", "pele_de_pedra_viva"]
    },

    # =================================== LORDE ELEMENTAL ===================================
    "lorde_elemental": {
        "nome": "Lorde Elemental",
        "descricao": "Um conjurador que não mais convoca elementais, mas os governa, tornando-se o mestre de um dos planos elementais.",
        "lore": "O Lorde Elemental alcançou o domínio supremo sobre um elemento. O Lorde do Fogo vive em um palácio de magma, o Lorde da Terra comanda montanhas vivas, o Lorde da Água governa os oceanos e o Lorde do Ar cavalga os ventos. Eles não são mais meros mortais, mas reis de seus próprios domínios planares, com exércitos de elementais à sua disposição.",
        "requisitos": {
            "nivel_total": 60,
            "classes": [{"id_classe": "xama_elemental", "nivel": 30}]
        },
        "stats_primarios": ["sabedoria", "constituicao", "carisma"],
        "habilidades_planejadas": ["comandar_plano_elemental", "corpo_elemental_permanente", "invocar_tsunami_de_fogo_terra_etc"]
    },

    # =================================== PESADELO ENCARNADO ===================================
    "pesadelo_encarnado": {
        "nome": "Pesadelo Encarnado",
        "descricao": "Um ser de puro terror, que se alimenta do medo e pode manifestar os piores pesadelos de uma pessoa na realidade.",
        "lore": "O Pesadelo Encarnado é o que acontece quando um Lorde do Medo transcende. Ele não precisa mais se esconder nas sombras; ele é a própria sombra. Ele é uma entidade que se alimenta do terror, e sua presença pode enlouquecer cidades inteiras. Ele pode arrastar suas vítimas para um reino de pesadelo pessoal, onde ele é um deus e elas são meros brinquedos. A única saída de seu reino é a loucura ou a morte.",
        "requisitos": {
            "nivel_total": 55,
            "classes": [{"id_classe": "lorde_do_medo", "nivel": 25}]
        },
        "stats_primarios": ["carisma", "inteligencia"],
        "habilidades_planejadas": ["criar_reino_de_pesadelo", "manifestar_medo_primordial", "devorar_sanidade"]
    },

    # =================================== MESTRE DAS RUNAS ===================================
    "mestre_das_runas": {
        "nome": "Mestre das Runas",
        "descricao": "Um estudioso que decifrou a linguagem da criação, capaz de inscrever runas que alteram as leis da física e da magia.",
        "lore": "O Mestre das Runas descobriu o segredo por trás do universo: tudo é código. As runas são a linguagem de programação da realidade. Ele pode inscrever uma runa em uma flecha para que ela nunca erre o alvo, uma runa em uma armadura para torná-la indestrutível, ou uma runa no ar para criar uma zona de silêncio mágico. Seu poder é sutil, mas absoluto.",
        "requisitos": {
            "nivel_total": 55,
            "classes": [{"id_classe": "defensor_runico", "nivel": 25}, {"id_classe": "arcanista", "nivel": 20}]
        },
        "stats_primarios": ["inteligencia", "sabedoria"],
        "habilidades_planejadas": ["runa_da_realidade", "selo_inquebravel", "palavra_de_comando_runica"]
    },

    # =================================== QUIMERA ===================================
    "quimera": {
        "nome": "Quimera",
        "descricao": "Um metamorfo que perdeu o controle sobre suas transformações, tornando-se uma amálgama de diferentes criaturas, mas ganhando um poder instável e imenso.",
        "lore": "A Quimera é o resultado trágico e poderoso da arte do metamorfo. Em sua busca por poder, ele tentou absorver muitas formas ao mesmo tempo, e seu corpo se quebrou. Agora, ele é uma mistura instável de diferentes criaturas: asas de dragão, braços de golem, cauda de escorpião. Ele é um monstro, mas um monstro de poder inimaginável, capaz de usar as habilidades de todas as criaturas que compõem seu corpo... se ele conseguir manter o controle.",
        "requisitos": {
            "nivel_total": 50,
            "classes": [{"id_classe": "metamorfo", "nivel": 25}]
        },
        "stats_primarios": ["constituicao", "forca", "destreza"],
        "habilidades_planejadas": ["forma_instavel", "ataque_multifacetado", "adaptacao_genetica_rapida"]
    },

    # =================================== ARAUTO DA TEMPESTADE ===================================
    "arauto_da_tempestade": {
        "nome": "Arauto da Tempestade",
        "descricao": "A personificação da fúria dos céus, um conjurador que comanda ventos, relâmpagos e trovões em uma escala massiva.",
        "lore": "O Arauto da Tempestade não invoca uma tempestade; ele *é* a tempestade. Onde quer que ele vá, os céus escurecem e os ventos uivam. Ele pode invocar furacões, criar tempestades de raios que duram dias e seu grito é o próprio trovão. Ele é um com o caos dos céus, um poder elemental bruto que varre tudo em seu caminho.",
        "requisitos": {
            "nivel_total": 50,
            "classes": [{"id_classe": "aeromante", "nivel": 20}, {"id_classe": "eletromante", "nivel": 20}, {"id_classe": "druida", "nivel": 10}]
        },
        "stats_primarios": ["inteligencia", "destreza"],
        "habilidades_planejadas": ["invocar_furacao", "tempestade_eterna", "corpo_de_raio"]
    },

    # =================================== INQUISIDOR-MOR ===================================
    "inquisidor-mor": {
        "nome": "Inquisidor-Mor",
        "descricao": "O líder de todos os inquisidores, um caçador de bruxas cuja fé e determinação o tornaram imune a quase toda magia.",
        "lore": "O Inquisidor-Mor viu a pior corrupção que a magia pode criar e sobreviveu. Sua vontade é de ferro, e sua fé é seu escudo. Ele é treinado para ser o caçador supremo de usuários de magia, imune a ilusões, encantamentos e maldições. Sua presença anula a magia ao seu redor, e suas armas são forjadas para destruir a própria essência de um conjurador. Para os magos do mundo, ele é o diabo.",
        "requisitos": {
            "nivel_total": 55,
            "classes": [{"id_classe": "inquisidor", "nivel": 25}, {"id_classe": "cacador_de_bruxas", "nivel": 20}]
        },
        "stats_primarios": ["sabedoria", "constituicao"],
        "habilidades_planejadas": ["vontade_de_ferro", "aura_de_anulacao_magica", "julgamento_final"]
    },

    # =================================== CAMPEÃO ETERNO ===================================
    "campeao_eterno": {
        "nome": "Campeão Eterno",
        "descricao": "Um guerreiro que, através de um ritual, bênção ou maldição, está destinado a reencarnar para sempre para lutar em batalhas cruciais.",
        "lore": "A alma do Campeão Eterno está ligada ao destino do mundo. Sempre que uma grande ameaça surge, ele renasce, muitas vezes sem memória de suas vidas passadas, mas com uma habilidade de combate inata. Ele é o herói que sempre aparece quando o mundo mais precisa, destinado a lutar, morrer e renascer em um ciclo sem fim. Sua habilidade vem de mil vidas de experiência de combate, gravadas em sua alma.",
        "requisitos": {
            "nivel_total": 60,
            "classes": [{"id_classe": "lorde_da_guerra", "nivel": 25}, {"id_classe": "vingador", "nivel": 25}]
        },
        "stats_primarios": ["forca", "destreza", "constituicao"],
        "habilidades_planejadas": ["memoria_da_alma", "golpe_do_destino", "renascimento_do_heroi"]
    },

    # =================================== MESTRE DAS FERAS LENDÁRIO ===================================
    "mestre_das_feras_lendario": {
        "nome": "Mestre das Feras Lendário",
        "descricao": "Um domador que capturou e treinou as criaturas mais raras e poderosas do mundo, as bestas lendárias.",
        "lore": "Enquanto outros domadores se contentam com lobos e ursos, o Mestre das Feras Lendário caça mitos. Ele rastreou e domou grifos, hidras, quimeras e talvez até mesmo um dragão. Sua equipe não é uma matilha; é uma coleção de lendas vivas. Comandar tais criaturas requer uma força de vontade imensa e um conhecimento profundo da natureza do mundo.",
        "requisitos": {
            "nivel_total": 55,
            "classes": [{"id_classe": "mestre_das_feras", "nivel": 25}, {"id_classe": "domador", "nivel": 20}]
        },
        "stats_primarios": ["carisma", "sabedoria"],
        "habilidades_planejadas": ["invocar_grifo", "comando_de_hidra", "vinculo_lendario"]
    },

    # =================================== ARCANISTA DO VAZIO ===================================
    "arcanista_do_vazio": {
        "nome": "Arcanista do Vazio",
        "descricao": "Um estudioso que voltou sua atenção para o nada entre as estrelas, extraindo poder do vazio e da anti-magia.",
        "lore": "O Arcanista do Vazio encontrou poder não na magia, mas em sua ausência. Ele estuda o vazio, o silêncio entre os planos, e aprendeu a invocá-lo. Ele pode criar esferas de aniquilação que apagam a matéria e a magia, silenciar conjuradores e até mesmo banir seres para o nada eterno. Seu poder é temido por todos, pois representa o fim de tudo.",
        "requisitos": {
            "nivel_total": 60,
            "classes": [{"id_classe": "arcanista", "nivel": 30}]
        },
        "stats_primarios": ["inteligencia", "sabedoria"],
        "habilidades_planejadas": ["esfera_de_aniquilacao", "silencio_absoluto", "invocar_o_vazio"]
    },

    # =================================== LORDE PIRATA ===================================
    "lorde_pirata": {
        "nome": "Lorde Pirata",
        "descricao": "Um corsário que uniu as frotas piratas sob sua bandeira, tornando-se o rei indiscutível dos mares.",
        "lore": "O Lorde Pirata é o pirata mais temido e respeitado dos sete mares. Através de carisma, brutalidade e uma habilidade de navegação incomparável, ele forjou uma nação flutuante de navios piratas. Sua palavra é lei nos oceanos, e sua frota pode desafiar as marinhas das maiores nações. Ele é a lenda que todo marinheiro teme encontrar no horizonte.",
        "requisitos": {
            "nivel_total": 50,
            "classes": [{"id_classe": "corsario", "nivel": 25}, {"id_classe": "atirador_de_elite", "nivel": 15}]
        },
        "stats_primarios": ["destreza", "carisma"],
        "habilidades_planejadas": ["comandar_frota_pirata", "abordagem_em_massa", "rei_dos_mares"]
    },

    # =================================== MENTE SUPREMA ===================================
    "mente_suprema": {
        "nome": "Mente Suprema",
        "descricao": "Um psíquico de poder incalculável, capaz de controlar mentes, mover objetos com o pensamento e criar mundos dentro de sua própria consciência.",
        "lore": "A Mente Suprema é o ápice do poder mental. Seu cérebro evoluiu para se tornar um computador quântico de carne. Eles podem ler os pensamentos de uma cidade inteira, controlar exércitos com sua vontade, e criar paisagens mentais tão reais quanto o mundo físico. Eles são os mestres da intriga e da manipulação, muitas vezes controlando impérios inteiros sem que ninguém saiba de sua existência.",
        "requisitos": {
            "nivel_total": 60,
            "classes": [{"id_classe": "vidente", "nivel": 30}, {"id_classe": "ilusionista", "nivel": 30}]
        },
        "stats_primarios": ["inteligencia", "sabedoria", "carisma"],
        "habilidades_planejadas": ["controle_mental_em_massa", "telecinese_massiva", "criar_paisagem_mental"]
    },

    # =================================== MESTRE DO BUSHIDO ===================================
    "mestre_do_bushido": {
        "nome": "Mestre do Bushido",
        "descricao": "Um samurai que personifica perfeitamente o código do guerreiro, alcançando um estado de clareza e precisão que beira o sobre-humano.",
        "lore": "O Mestre do Bushido vive e respira o código. Honra, coragem, compaixão, respeito - não são ideais, são as leis que governam sua existência. Essa devoção absoluta lhe confere uma clareza mental e uma força de vontade inabaláveis. Em combate, ele é imparável, pois não tem medo, não tem dúvida e não tem hesitação. Seu corte é o corte da própria justiça.",
        "requisitos": {
            "nivel_total": 60,
            "classes": [{"id_classe": "mestre_samurai", "nivel": 30}]
        },
        "stats_primarios": ["destreza", "forca", "sabedoria"],
        "habilidades_planejadas": ["corte_da_honra", "mente_inabalavel", "personificacao_do_bushido"]
    },

    # =================================== LORDE DEMÔNIO ===================================
    "lorde_demonio": {
        "nome": "Lorde Demônio",
        "descricao": "Um mortal que subiu na hierarquia dos infernos, tornando-se um governante de demônios e um lorde de seu próprio círculo infernal.",
        "lore": "O Lorde Demônio é a história de sucesso do inferno. Começando como um mero cultista ou bruxo, ele traiu, assassinou e conspirou seu caminho até o topo. Agora, ele governa uma legião de demônios, comanda um dos círculos do inferno e tem o poder de corromper o mundo mortal. Ele é a ambição e a crueldade encarnadas.",
        "requisitos": {
            "nivel_total": 65,
            "classes": [{"id_classe": "lorde_bruxo", "nivel": 30}]
        },
        "stats_primarios": ["carisma", "inteligencia"],
        "habilidades_planejadas": ["comandar_legiao_infernal", "corromper_terra", "invocar_principe_demonio"]
    },

    # =================================== SERAFIM ===================================
    "serafim": {
        "nome": "Serafim",
        "descricao": "Um mortal que ascendeu à divindade, tornando-se um anjo de poder imenso, a mão direita de um deus da luz.",
        "lore": "O Serafim é a prova de que a mortalidade pode ser superada pela virtude. Através de atos de sacrifício e fé inabalável, este mortal foi elevado pelos deuses, transformando-se em um ser de pura luz e poder. Com seis asas de fogo e uma espada que canta a canção da criação, o Serafim é a personificação da justiça divina e da esperança em um mundo escuro.",
        "requisitos": {
            "nivel_total": 65,
            "classes": [{"id_classe": "campeao_divino", "nivel": 30}]
        },
        "stats_primarios": ["carisma", "sabedoria", "forca"],
        "habilidades_planejadas": ["ascensao_angelical", "espada_de_fogo_divino", "julgamento_celestial"]
    },

    # =================================== ASPECTO DA NATUREZA ===================================
    "aspecto_da_natureza": {
        "nome": "Aspecto da Natureza",
        "descricao": "Um druida que se fundiu com a própria essência do mundo natural, tornando-se um guardião semi-divino do equilíbrio.",
        "lore": "O Aspecto da Natureza não serve mais à natureza; ele *é* a natureza. Ele se fundiu com a alma do mundo, e seu corpo é uma manifestação dessa união - feito de madeira, pedra e folhas. Ele pode sentir cada árvore cortada, cada rio poluído, e pode comandar a fúria do mundo natural para punir aqueles que perturbam o equilíbrio. Ele é a vontade viva de Gaia.",
        "requisitos": {
            "nivel_total": 60,
            "classes": [{"id_classe": "hierofante", "nivel": 30, "especializacao": "natureza"}]
        },
        "stats_primarios": ["sabedoria", "constituicao"],
        "habilidades_planejadas": ["um_com_a_terra", "furia_de_gaia", "canto_da_vida_e_morte"]
    },

    # =================================== IMPERADOR ===================================
    "imperador": {
        "nome": "Imperador",
        "descricao": "O governante supremo, um líder que uniu nações através da conquista, diplomacia ou poder absoluto, e cujo governo molda o destino do mundo.",
        "lore": "O Imperador é o ápice do poder mortal. Ele não é necessariamente o mais forte ou o mago mais poderoso, mas é o líder mais eficaz. Ele comanda exércitos, controla economias e sua vontade é lei para milhões. Ele alcançou o que todos os reis sonham: um império sobre o qual o sol nunca se põe. Seu legado será escrito nos livros de história para sempre.",
        "requisitos": {
            "nivel_total": 60,
            "classes": [{"id_classe": "lorde_da_guerra", "nivel": 30}, {"id_classe": "rei_dos_ladroes", "nivel": 25}]
        },
        "stats_primarios": ["carisma", "inteligencia"],
        "habilidades_planejadas": ["decreto_imperial", "comandar_imperio", "legado_eterno"]
    }
}
