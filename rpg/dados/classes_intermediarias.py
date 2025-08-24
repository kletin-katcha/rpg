# ==============================================================================
# ARQUIVO DE DADOS: CLASSES INTERMEDIÁRIAS
# ==============================================================================
#
# Este arquivo contém as definições para as classes intermediárias.
# Estas classes representam uma especialização ou evolução das classes
# iniciais e exigem o cumprimento de certos pré-requisitos.
#
# Estrutura de cada Classe:
# -------------------------
# "nome": (str) Nome da classe.
# "descricao": (str) Descrição do estilo de jogo.
# "lore": (str) História da classe no mundo.
# "requisitos": (dict) Condições para desbloquear a classe.
#   - "nivel": (int) Nível total do personagem.
#   - "classes": (list) Lista de classes iniciais e seus níveis mínimos.
#     Ex: [{"id_classe": "guerreiro", "nivel": 10}]
# "stats_primarios": (list) Atributos principais.
# "habilidades_planejadas": (list) Nomes de habilidades que serão definidas.
#
# ==============================================================================

CLASSES_INTERMEDIARIAS = {
    # =================================== GLADIADOR ===================================
    "gladiador": {
        "nome": "Gladiador",
        "descricao": "Um mestre do combate de arena, focado em ataques chamativos e controle de multidão para agradar o público e massacrar oponentes.",
        "lore": """
O gladiador é um artista da violência. Nascido nas arenas sangrentas das grandes cidades, ele aprendeu a lutar não apenas para sobreviver, mas para entreter. Cada golpe, cada esquiva, é uma parte de uma performance mortal. Eles são especialistas em usar armas exóticas e em lutar contra múltiplos oponentes ao mesmo tempo, usando sua presença de palco para intimidar inimigos e inspirar a torcida. Fora da arena, sua habilidade de combate os torna mercenários de elite ou guarda-costas temíveis.
        """,
        "requisitos": {
            "nivel_total": 20,
            "classes": [{"id_classe": "guerreiro", "nivel": 10}, {"id_classe": "barbaro", "nivel": 5}]
        },
        "stats_primarios": ["forca", "carisma"],
        "habilidades_planejadas": ["golpe_do_showman", "rede_e_tridente", "provocacao_da_arena"]
    },

    # =================================== MESTRE DAS LÂMINAS ===================================
    "mestre_das_laminas": {
        "nome": "Mestre das Lâminas",
        "descricao": "Um duelista que dedicou sua vida ao domínio de um único tipo de lâmina, alcançando uma velocidade e precisão sobre-humanas.",
        "lore": """
Para o Mestre das Lâminas, a espada não é uma ferramenta, mas uma extensão de sua alma. Através de décadas de treinamento implacável, ele aprendeu cada nuance de sua arma escolhida. Seus movimentos são um borrão de aço, seus golpes são perfeitamente precisos, visando as menores aberturas na defesa do inimigo. Eles são conhecidos por sua capacidade de cortar uma flecha no ar ou de desarmar um oponente com um único movimento fluido. Lutar contra um Mestre das Lâminas é como lutar contra um redemoinho de aço.
        """,
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "guerreiro", "nivel": 15}, {"id_classe": "espadachim", "nivel": 10}]
        },
        "stats_primarios": ["destreza", "forca"],
        "habilidades_planejadas": ["postura_da_garca", "mil_cortes", "lamina_fantasma"]
    },

    # =================================== ARQUIMAGO ===================================
    "arquimago": {
        "nome": "Arquimago",
        "descricao": "Um mago que alcançou um novo patamar de compreensão arcana, especializando-se profundamente em uma escola de magia.",
        "lore": """
O título de Arquimago não é concedido, é conquistado. Representa uma vida de estudo que beira a obsessão, um poder que pode rivalizar com o dos dragões. Um Arquimago transcendeu os feitiços básicos; eles começam a manipular a própria estrutura da magia. Um piromante pode criar um sol em miniatura, um criomante pode congelar um lago com um pensamento, e um ilusionista pode criar uma cidade inteira do nada. Eles são os diretores de academias arcanas, os conselheiros de reis, e muitas vezes, as maiores ameaças ao mundo.
        """,
        "requisitos": {
            "nivel_total": 30,
            "classes": [{"id_classe": "mago", "nivel": 20}]
        },
        "stats_primarios": ["inteligencia", "sabedoria"],
        "habilidades_planejadas": ["chuva_de_meteoros", "parar_o_tempo", "invocar_elemental_maior"]
    },

    # =================================== ASSASSINO ===================================
    "assassino": {
        "nome": "Assassino",
        "descricao": "A evolução letal do ladino, um mestre da morte que usa venenos, disfarces e ataques surpresa para eliminar seus alvos sem deixar rastros.",
        "lore": """
O assassino é um fantasma, uma lenda sussurrada em tavernas e cortes reais. Eles são os agentes de guildas secretas, de reis e de cultos sombrios. Sua arte não é o combate, mas a morte. Eles estudam seus alvos, aprendem suas rotinas e fraquezas, e atacam no momento perfeito. Um assassino pode passar semanas se infiltrando em um castelo, disfarçado de servo, esperando pela oportunidade de colocar uma gota de veneno em um copo de vinho ou uma adaga entre as costelas de um rei.
        """,
        "requisitos": {
            "nivel_total": 20,
            "classes": [{"id_classe": "ladino", "nivel": 15}]
        },
        "stats_primarios": ["destreza", "inteligencia"],
        "habilidades_planejadas": ["golpe_mortal", "mestre_dos_venenos", "desaparecer_nas_sombras"]
    },

    # =================================== TEMPLÁRIO ===================================
    "templario": {
        "nome": "Templário",
        "descricao": "Um caçador de magos e demônios, treinado para resistir e dissipar magia enquanto protege os inocentes com sua fé e aço.",
        "lore": """
Onde há poder, há aqueles que abusam dele. Os Templários existem para caçar esses indivíduos. Eles são uma ordem de cavaleiros sagrados que se especializam em combater usuários de magia corrompida e criaturas de outros planos. Eles aprendem a anular feitiços, a quebrar encantamentos e a resistir à manipulação mental. Com suas armaduras pesadas inscritas com runas de proteção e suas armas imbuídas de poder sagrado, um Templário é o pior pesadelo de um bruxo ou necromante.
        """,
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "paladino", "nivel": 15}, {"id_classe": "clerigo", "nivel": 10}]
        },
        "stats_primarios": ["sabedoria", "forca"],
        "habilidades_planejadas": ["circulo_antimagia", "golpe_dissipador", "julgamento"]
    },

    # =================================== MAGO DE BATALHA ===================================
    "mago_de_batalha": {
        "nome": "Mago de Batalha",
        "descricao": "Um guerreiro que complementa sua proeza marcial com feitiços arcanos, usando magia para fortalecer suas armas e defesas.",
        "lore": "O Mago de Batalha rejeita a noção de que se deve escolher entre a espada e o feitiço. Eles treinam seus corpos e mentes em igual medida, tornando-se uma força versátil no campo de batalha. Eles podem encantar suas próprias lâminas com fogo, proteger-se com escudos de força e se teleportar para flanquear o inimigo. Eles são a fusão perfeita de poder e intelecto.",
        "requisitos": {
            "nivel_total": 20,
            "classes": [{"id_classe": "guerreiro", "nivel": 10}, {"id_classe": "mago", "nivel": 10}]
        },
        "stats_primarios": ["forca", "inteligencia"],
        "habilidades_planejadas": ["lamina_arcana", "armadura_de_mago", "passo_bruxo"]
    },

    # =================================== TRAPACEIRO ARCANO ===================================
    "trapaceiro_arcano": {
        "nome": "Trapaceiro Arcano",
        "descricao": "Um ladino que descobriu a magia e a usa para aprimorar suas habilidades de furto, engano e infiltração.",
        "lore": "Para o Trapaceiro Arcano, a magia é a melhor ferramenta de um ladrão. Por que arrombar uma fechadura quando você pode abri-la com um feitiço? Por que se esgueirar pelas sombras quando você pode ficar invisível? Eles usam magias de ilusão e encantamento para confundir os guardas, criar distrações e realizar os roubos mais impossíveis. Eles são a prova de que um pouco de magia pode tornar um bom ladrão em um ladrão lendário.",
        "requisitos": {
            "nivel_total": 20,
            "classes": [{"id_classe": "ladino", "nivel": 10}, {"id_classe": "mago", "nivel": 5}]
        },
        "stats_primarios": ["destreza", "inteligencia"],
        "habilidades_planejadas": ["mao_magica_versatil", "emboscada_invisivel", "encantar_pessoa"]
    },

    # =================================== INQUISIDOR ===================================
    "inquisidor": {
        "nome": "Inquisidor",
        "descricao": "Um caçador implacável de hereges e monstros, que usa conhecimento, fé e táticas de guerrilha para purgar o mal.",
        "lore": "O Inquisidor opera nas sombras, longe dos holofotes dos paladinos. Eles são os detetives, os caçadores e os executores das ordens sagradas. Eles entendem que para lutar contra monstros, é preciso entender como eles pensam. Eles usam furtividade, venenos e conhecimento proibido, combinando-os com o poder de sua fé para caçar e destruir seus alvos com uma eficiência assustadora.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "clerigo", "nivel": 10}, {"id_classe": "ladino", "nivel": 10}, {"id_classe": "ranger", "nivel": 5}]
        },
        "stats_primarios": ["sabedoria", "destreza"],
        "habilidades_planejadas": ["julgamento_do_cacador", "fogo_purificador", "conhecimento_proibido"]
    },

    # =================================== GUARDIÃO ===================================
    "guardiao": {
        "nome": "Guardião (Warden)",
        "descricao": "Um defensor da natureza que usa a força da terra e dos animais para proteger seus aliados e seu território.",
        "lore": "O Guardião é a vontade defensiva da natureza. Enquanto o druida é um com a natureza, o guardião é seu escudo. Eles se transformam em formas bestiais não para caçar, mas para proteger, tornando-se ursos ou tartarugas gigantes para absorver dano. Eles podem comandar a terra para criar barreiras e curar seus aliados com o poder da própria vida.",
        "requisitos": {
            "nivel_total": 20,
            "classes": [{"id_classe": "druida", "nivel": 10}, {"id_classe": "cavaleiro", "nivel": 5}]
        },
        "stats_primarios": ["constituicao", "sabedoria"],
        "habilidades_planejadas": ["forma_do_guardiao_urso", "abraco_da_terra", "espiritos_curativos"]
    },

    # =================================== MESTRE DAS FERAS ===================================
    "mestre_das_feras": {
        "nome": "Mestre das Feras",
        "descricao": "Um ranger que aprofundou seu vínculo com o mundo animal, capaz de lutar em perfeita harmonia com múltiplos companheiros.",
        "lore": "Para o Mestre das Feras, seus companheiros animais não são animais de estimação; são família. Eles compartilham um vínculo que transcende as palavras, permitindo-lhes lutar como uma única unidade. O Mestre das Feras e seus companheiros podem flanquear inimigos, combinar seus ataques e se proteger mutuamente. Eles são a personificação da matilha, uma força de dentes, garras e aço.",
        "requisitos": {
            "nivel_total": 20,
            "classes": [{"id_classe": "ranger", "nivel": 15}]
        },
        "stats_primarios": ["destreza", "sabedoria"],
        "habilidades_planejadas": ["matilha_de_um", "vinculo_primordial", "ataque_coordenado"]
    },

    # =================================== CAVALEIRO ARCANO ===================================
    "cavaleiro_arcano": {
        "nome": "Cavaleiro Arcano",
        "descricao": "Um guerreiro que se liga a uma arma, permitindo-lhe conjurar sua arma do nada e usar magias de proteção e mobilidade.",
        "lore": "O Cavaleiro Arcano forja um vínculo místico com sua arma. Ela se torna parte dele, e ele pode conjurá-la à sua mão a qualquer momento. Este vínculo lhe permite canalizar magia através da arma, não para atacar, mas para se defender e se mover pelo campo de batalha. Eles podem se teleportar, criar escudos de força e contra-atacar feitiços, tornando-os guerreiros altamente móveis e resilientes.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "guerreiro", "nivel": 15}, {"id_classe": "mago", "nivel": 5}]
        },
        "stats_primarios": ["forca", "inteligencia"],
        "habilidades_planejadas": ["arma_vinculada", "salto_arcano", "defesa_magica"]
    },

    # =================================== CAMPEÃO DIVINO ===================================
    "campeao_divino": {
        "nome": "Campeão Divino",
        "descricao": "O braço direito de um deus, um paladino que se tornou a personificação viva da vontade de sua divindade.",
        "lore": "O Campeão Divino é escolhido por um deus para ser seu avatar no mundo mortal. Eles são infundidos com uma porção do poder de sua divindade, tornando-se mais do que meros mortais. Sua presença inspira fervor nos fiéis e terror nos inimigos de sua fé. Eles podem canalizar a energia divina pura, transformando-se em avatares de luz ou escuridão, dependendo de seu patrono.",
        "requisitos": {
            "nivel_total": 30,
            "classes": [{"id_classe": "paladino", "nivel": 20}]
        },
        "stats_primarios": ["forca", "carisma"],
        "habilidades_planejadas": ["transformacao_divina", "palavra_de_poder", "aura_dominante"]
    },

    # =================================== SOMBRA DANÇARINA ===================================
    "sombra_dancarina": {
        "nome": "Sombra Dançarina",
        "descricao": "Um mestre da furtividade que pode literalmente saltar entre as sombras, tornando-se um fantasma intangível no campo de batalha.",
        "lore": "A Sombra Dançarina aprendeu um segredo antigo: que as sombras não são apenas ausência de luz, mas um plano próprio. Eles podem entrar em uma sombra e sair de outra a quilômetros de distância. Em combate, eles são quase impossíveis de acertar, desaparecendo na sombra de um inimigo para reaparecer em suas costas. Eles são os espiões e assassinos perfeitos, capazes de se infiltrar em qualquer lugar onde uma sombra possa cair.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "ladino", "nivel": 15}, {"id_classe": "monge", "nivel": 5}]
        },
        "stats_primarios": ["destreza", "sabedoria"],
        "habilidades_planejadas": ["salto_sombrio", "ataque_das_sombras", "forma_sombria"]
    },

    # =================================== ATIRADOR DE ELITE ===================================
    "atirador_de_elite": {
        "nome": "Atirador de Elite",
        "descricao": "Um mestre do arco ou da arma de fogo, capaz de acertar alvos a distâncias incríveis com uma precisão mortal.",
        "lore": "O Atirador de Elite é um artista da morte à distância. Eles podem calcular a trajetória de um projétil levando em conta o vento, a umidade e a rotação do planeta. Seus olhos são como os de uma águia, capazes de ver detalhes a quilômetros de distância. Eles são os assassinos pacientes, capazes de esperar por dias na posição perfeita para o tiro perfeito, aquele que pode mudar o curso de uma batalha ou de uma guerra.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "ranger", "nivel": 15}, {"id_classe": "atirador", "nivel": 10}]
        },
        "stats_primarios": ["destreza", "sabedoria"],
        "habilidades_planejadas": ["tiro_mortal", "olho_de_aguia", "respiracao_controlada"]
    },

    # =================================== LORDE BRUXO ===================================
    "lorde_bruxo": {
        "nome": "Lorde Bruxo",
        "descricao": "Um bruxo que dominou seu patrono ou roubou uma parte significativa de seu poder, tornando-se uma entidade poderosa por direito próprio.",
        "lore": "O pacto de um bruxo é um jogo perigoso, mas o Lorde Bruxo é aquele que venceu. Através de astúcia, poder ou pura força de vontade, ele virou o jogo contra seu patrono. Ele não pede mais por poder; ele o toma. Eles se tornam figuras de poder quase divino, comandando demônios menores, distorcendo a realidade e continuando a acumular poder de fontes proibidas. Eles são a prova de que mesmo um mortal pode desafiar os deuses... e vencer.",
        "requisitos": {
            "nivel_total": 30,
            "classes": [{"id_classe": "bruxo", "nivel": 20}]
        },
        "stats_primarios": ["carisma", "inteligencia"],
        "habilidades_planejadas": ["roubar_poder_do_patrono", "invocar_servos_maiores", "realidade_distorcida"]
    },

    # =================================== METAMORFO ===================================
    "metamorfo": {
        "nome": "Metamorfo",
        "descricao": "Um mestre da transformação, capaz de alterar sua forma para a de qualquer criatura que já tenha visto, ganhando suas habilidades.",
        "lore": "Se o druida pode se transformar em animais, o Metamorfo pode se transformar em *qualquer coisa*. Eles estudam a anatomia e a essência das criaturas, aprendendo a replicar sua forma. Eles podem se tornar um dragão para voar sobre uma montanha, um golem para atravessar uma parede ou até mesmo um rato para se esgueirar por uma fresta. Sua versatilidade é inigualável, mas eles correm o risco de perder sua forma original e sua identidade no processo.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "druida", "nivel": 15}, {"id_classe": "mago", "nivel": 10}]
        },
        "stats_primarios": ["sabedoria", "constituicao"],
        "habilidades_planejadas": ["forma_de_dragao", "forma_de_golem", "memoria_genetica"]
    },

    # =================================== BARDO DO CONHECIMENTO ===================================
    "bardo_do_conhecimento": {
        "nome": "Bardo do Conhecimento",
        "descricao": "Um bardo que viajou o mundo coletando histórias e segredos. Seu poder vem de saber quase tudo sobre qualquer coisa.",
        "lore": "O Bardo do Conhecimento é a maior biblioteca do mundo, contida em uma única mente. Eles sabem a fraqueza secreta de um demônio, a linhagem esquecida de um rei e a localização de uma ruína perdida. Em combate, eles usam seu conhecimento para explorar as vulnerabilidades de seus inimigos, desmoralizá-los com verdades inconvenientes e até mesmo roubar os feitiços de outros conjuradores, tecendo-os em suas próprias canções.",
        "requisitos": {
            "nivel_total": 20,
            "classes": [{"id_classe": "bardo", "nivel": 15}]
        },
        "stats_primarios": ["carisma", "inteligencia"],
        "habilidades_planejadas": ["segredos_comerciais", "palavras_cortantes", "roubar_magia"]
    },

    # =================================== XAMÃ ELEMENTAL ===================================
    "xama_elemental": {
        "nome": "Xamã Elemental",
        "descricao": "Um xamã que se tornou um canal para os próprios elementos, capaz de invocar fúria elemental e se transformar em avatares de fogo, terra, ar ou água.",
        "lore": "O Xamã Elemental não apenas fala com os espíritos; ele os convida a habitar seu corpo. Eles se tornam um com os elementos, capazes de transformar sua pele em pedra, seus braços em ciclones ou seu corpo em uma chama viva. Eles são a personificação da fúria da natureza, uma força de destruição primordial que protege o equilíbrio do mundo.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "xama", "nivel": 15}, {"id_classe": "druida", "nivel": 10}]
        },
        "stats_primarios": ["sabedoria", "constituicao"],
        "habilidades_planejadas": ["avatar_do_fogo", "avatar_da_terra", "furia_dos_elementos"]
    },

    # =================================== MONGE DO PUNHO DE FERRO ===================================
    "monge_do_punho_de_ferro": {
        "nome": "Monge do Punho de Ferro",
        "descricao": "Um monge que focou seu Ki para tornar seus golpes tão duros e destrutivos quanto o aço forjado.",
        "lore": "O Monge do Punho de Ferro acredita que a melhor defesa é um ataque que quebra a arma do inimigo. Eles condicionam seus corpos a um nível sobre-humano, e seu Ki lhes permite endurecer seus punhos e pés a ponto de poderem quebrar pedras e amassar aço. Seus golpes não são apenas rápidos; são devastadores, capazes de quebrar ossos e armaduras com a mesma facilidade.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "monge", "nivel": 15}, {"id_classe": "guerreiro", "nivel": 5}]
        },
        "stats_primarios": ["destreza", "forca"],
        "habilidades_planejadas": ["punho_de_ferro", "golpe_vibratorio", "quebrar_arma"]
    },

    # =================================== CEIFADOR ===================================
    "ceifador": {
        "nome": "Ceifador",
        "descricao": "Um mestre da necromancia que se concentra em colher as almas dos mortos e usar a energia da morte para alimentar seus feitiços.",
        "lore": "O Ceifador anda na linha tênue entre a vida e a morte. Eles não apenas comandam os mortos; eles colhem as almas dos que estão morrendo. Com sua foice, eles podem cortar a conexão de uma alma com seu corpo, armazenando-a para usar como combustível para magias terríveis. Eles são temidos por todos, pois representam o fim inevitável.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "necromante", "nivel": 15}, {"id_classe": "clerigo", "nivel": 5}]
        },
        "stats_primarios": ["inteligencia", "sabedoria"],
        "habilidades_planejadas": ["colher_alma", "foice_da_morte", "prisao_de_almas"]
    },

    # =================================== CAVALEIRO DA MORTE ===================================
    "cavaleiro_da_morte": {
        "nome": "Cavaleiro da Morte",
        "descricao": "Um guerreiro morto-vivo de poder imenso, que usa uma combinação de proeza marcial e magia profana. Geralmente criado por um necromante poderoso.",
        "lore": "O Cavaleiro da Morte é o que acontece quando um grande guerreiro cai e é reanimado com magia necromântica. Eles mantêm suas habilidades marciais, mas agora são infundidos com o poder do gelo e da praga. Eles são generais de exércitos de mortos-vivos, cavalgando em corcéis esqueléticos e congelando o chão por onde passam. São uma paródia profana dos paladinos, impulsionados por uma fome insaciável de vida.",
        "requisitos": {
            "nivel_total": 30,
            "classes": [{"id_classe": "guerreiro", "nivel": 15}, {"id_classe": "necromante", "nivel": 15}]
        },
        "stats_primarios": ["forca", "inteligencia"],
        "habilidades_planejadas": ["golpe_gelido", "presenca_pestilenta", "erguer_servo_morto-vivo"]
    },

    # =================================== DEFENSOR RÚNICO ===================================
    "defensor_runico": {
        "nome": "Defensor Rúnico",
        "descricao": "Um guerreiro que inscreve runas mágicas em sua armadura, escudo e corpo para obter poder e proteção.",
        "lore": "O Defensor Rúnico é um estudioso e um guerreiro. Eles aprenderam a antiga arte de inscrever runas, símbolos de poder que podem armazenar e liberar magia. Sua armadura não é apenas metal; é uma tapeçaria de encantamentos. Eles podem ativar runas para criar escudos de fogo, para curar seus ferimentos ou para liberar uma onda de choque que derruba os inimigos. Eles são fortalezas ambulantes de magia e aço.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "cavaleiro", "nivel": 15}, {"id_classe": "artifice", "nivel": 10}]
        },
        "stats_primarios": ["constituicao", "inteligencia"],
        "habilidades_planejadas": ["runa_da_protecao", "runa_da_explosao", "ativar_todas_as_runas"]
    },

    # =================================== MESTRE ALQUIMISTA ===================================
    "mestre_alquimista": {
        "nome": "Mestre Alquimista",
        "descricao": "Um alquimista que transcendeu a criação de poções, aprendendo a transmutar a matéria e até mesmo a criar vida.",
        "lore": "O Mestre Alquimista busca o segredo final: a Pedra Filosofal. Eles podem transformar chumbo em ouro, criar homúnculos (servos artificiais) a partir de argila e sangue, e preparar elixires que podem curar qualquer doença ou conceder vida eterna. Seu laboratório é um lugar de maravilhas e horrores, e seu conhecimento da composição da realidade rivaliza com o dos magos mais poderosos.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "alquimista", "nivel": 15}, {"id_classe": "artifice", "nivel": 10}]
        },
        "stats_primarios": ["inteligencia", "destreza"],
        "habilidades_planejadas": ["transmutar_chumbo_em_ouro", "criar_homunculo", "pedra_filosofal"]
    },

    # =================================== ANDARILHO DO HORIZONTE ===================================
    "andarilho_do_horizonte": {
        "nome": "Andarilho do Horizonte",
        "descricao": "Um ranger que protege o mundo das ameaças de outros planos de existência. Mestre em viagens planares e em caçar criaturas extraplanares.",
        "lore": "O Andarilho do Horizonte guarda as fronteiras não entre nações, mas entre realidades. Eles caçam as criaturas que vazam de outros planos - demônios, aberrações, anjos caídos. Eles aprendem a sentir portais, a viajar através deles e a banir criaturas de volta para suas dimensões de origem. Eles são os guardiões silenciosos que protegem o mundo de horrores que a maioria das pessoas nem sabe que existem.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "ranger", "nivel": 15}, {"id_classe": "bruxo", "nivel": 5}]
        },
        "stats_primarios": ["destreza", "sabedoria"],
        "habilidades_planejadas": ["detectar_portal", "golpe_planar", "banimento"]
    },

    # =================================== MESTRE SAMURAI (KENSEI) ===================================
    "mestre_samurai": {
        "nome": "Mestre Samurai (Kensei)",
        "descricao": "Um samurai que alcançou a união perfeita com sua lâmina, tratando-a como uma extensão de sua alma e infundindo-a com seu próprio espírito.",
        "lore": "O Kensei, ou 'Santo da Espada', é um samurai que transcendeu a técnica marcial e entrou no reino da filosofia espiritual. Para eles, a katana não é apenas uma arma; é um objeto de meditação e um canal para seu Ki. Eles podem infundir sua lâmina com sua própria força vital, tornando-a inquebrável e capaz de cortar através de magia. Um duelo com um Kensei não é uma luta; é uma lição sobre a natureza da perfeição.",
        "requisitos": {
            "nivel_total": 30,
            "classes": [{"id_classe": "samurai", "nivel": 20}, {"id_classe": "monge", "nivel": 5}]
        },
        "stats_primarios": ["destreza", "sabedoria"],
        "habilidades_planejadas": ["lamina_espiritual", "corte_perfeito", "mente_vazia"]
    },

    # =================================== MAGO VERMELHO ===================================
    "mago_vermelho": {
        "nome": "Mago Vermelho",
        "descricao": "Um polímata que combina magia branca e negra com esgrima, buscando o equilíbrio entre os extremos.",
        "lore": "O Mago Vermelho caminha no fio da navalha entre a cura e a destruição, a criação e a aniquilação. Eles acreditam que a verdadeira maestria mágica vem do equilíbrio, não da especialização. Em um momento, eles podem curar um ferimento com magia branca; no outro, podem lançar uma bola de fogo com magia negra. Sua versatilidade é sua maior força, complementada por uma esgrima elegante que os torna perigosos a qualquer distância.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "mago", "nivel": 10}, {"id_classe": "clerigo", "nivel": 10}, {"id_classe": "espadachim", "nivel": 5}]
        },
        "stats_primarios": ["inteligencia", "destreza"],
        "habilidades_planejadas": ["golpe_duplo_magico", "equilibrio_arcano", "vermelho_final"]
    },

    # =================================== ESPADACHIM ARCANO ===================================
    "espadachim_arcano": {
        "nome": "Espadachim Arcano",
        "descricao": "Um duelista que infunde sua lâmina com feitiços, desferindo ataques que são tanto físicos quanto mágicos.",
        "lore": "O Espadachim Arcano vê sua espada não apenas como uma arma, mas como um canal para a magia. Eles tecem feitiços em seus ataques, criando lâminas de gelo, fogo ou eletricidade. Seus movimentos são uma dança hipnótica de aço e energia, confundindo e sobrecarregando seus oponentes. Eles são os herdeiros de uma tradição que busca a união perfeita da arte da espada e da arte arcana.",
        "requisitos": {
            "nivel_total": 20,
            "classes": [{"id_classe": "espadachim", "nivel": 10}, {"id_classe": "feiticeiro", "nivel": 10}]
        },
        "stats_primarios": ["destreza", "carisma"],
        "habilidades_planejadas": ["lamina_elemental", "defesa_magica_fluida", "estocada_bruxa"]
    },

    # =================================== FEITICEIRO DRACÔNICO ===================================
    "feiticeiro_draconico": {
        "nome": "Feiticeiro Dracônico",
        "descricao": "Um feiticeiro cuja linhagem dracônica se manifestou, concedendo-lhe escamas, asas e o poder de um dragão.",
        "lore": "O sangue de dragão corre forte nas veias deste feiticeiro. Com o tempo, sua herança se manifesta fisicamente: sua pele se torna resistente como escamas, asas de couro brotam de suas costas e sua magia assume a forma do sopro de seu ancestral dracônico - seja fogo, gelo, ácido ou relâmpago. Eles são a personificação do poder dracônico em forma humanóide, inspirando admiração e medo.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "feiticeiro", "nivel": 20}]
        },
        "stats_primarios": ["carisma", "constituicao"],
        "habilidades_planejadas": ["sopro_de_dragao", "asas_draconicas", "presenca_aterrorizante"]
    },

    # =================================== HIEROFANTE ===================================
    "hierofante": {
        "nome": "Hierofante",
        "descricao": "Um clérigo que se tornou um canal direto para o divino, capaz de realizar milagres e manifestar a vontade de seu deus na terra.",
        "lore": "O Hierofante não apenas serve a um deus; ele fala por ele. Eles alcançaram um nível de comunhão tão profundo que a linha entre sua vontade e a de sua divindade se torna tênue. Eles podem realizar milagres que desafiam a lógica, curar doenças incuráveis, abençoar exércitos inteiros ou invocar a ira de seu deus para punir os infiéis. Eles são os líderes supremos de suas religiões, reverenciados como santos vivos.",
        "requisitos": {
            "nivel_total": 30,
            "classes": [{"id_classe": "clerigo", "nivel": 20}]
        },
        "stats_primarios": ["sabedoria", "carisma"],
        "habilidades_planejadas": ["milagre", "intervencao_divina", "palavra_sagrada"]
    },

    # =================================== VINGADOR ===================================
    "vingador": {
        "nome": "Vingador",
        "descricao": "Um paladino que fez um juramento de vingança. Caça seus inimigos jurados com uma fúria divina implacável.",
        "lore": "Algo terrível aconteceu ao Vingador. Sua ordem foi destruída, seu mestre foi assassinado, ou seu povo foi massacrado. Em sua dor, eles fizeram um juramento de vingança, e seu deus respondeu. Eles não protegem mais os inocentes; eles caçam os culpados. Sua magia divina é focada na perseguição e na destruição, permitindo-lhes rastrear seus alvos incansavelmente e desferir golpes de retribuição divina.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "paladino", "nivel": 15}, {"id_classe": "ranger", "nivel": 5}]
        },
        "stats_primarios": ["forca", "constituicao"],
        "habilidades_planejadas": ["juramento_de_inimizade", "perseguicao_implacavel", "golpe_vingativo"]
    },

    # =================================== MESTRE DAS ARMAS ===================================
    "mestre_das_armas": {
        "nome": "Mestre das Armas",
        "descricao": "Um guerreiro que dominou o uso de todas as formas de armamento. Capaz de pegar qualquer arma e usá-la com uma eficácia mortal.",
        "lore": "O Mestre das Armas acredita que a especialização é uma fraqueza. Por que dominar apenas a espada quando se pode dominar a lança, o machado, o arco e a maça? Eles viajam o mundo, aprendendo com diferentes mestres e colecionando armas exóticas. Em batalha, são imprevisíveis, trocando de arma e de estilo de luta para se adaptar a qualquer situação e explorar qualquer fraqueza.",
        "requisitos": {
            "nivel_total": 30,
            "classes": [{"id_classe": "guerreiro", "nivel": 20}, {"id_classe": "bardo", "nivel": 5}]
        },
        "stats_primarios": ["forca", "destreza"],
        "habilidades_planejadas": ["maestria_adaptavel", "arsenal_do_mestre", "postura_de_combate_universal"]
    },

    # =================================== LADRÃO DE ALMAS ===================================
    "ladrao_de_almas": {
        "nome": "Ladrão de Almas",
        "descricao": "Um trapaceiro que aprendeu a roubar não apenas bens materiais, mas a própria essência vital de seus inimigos.",
        "lore": "O Ladrão de Almas descobriu um segredo sombrio: que a alma é o bem mais precioso. Usando uma combinação de magia das sombras e técnicas de assassinato, eles podem arrancar fragmentos da alma de um alvo, deixando-os enfraquecidos e vazios. Eles usam essa energia roubada para se fortalecer, curar seus ferimentos ou alimentar habilidades sobrenaturais. São parasitas do espírito, temidos até mesmo por outros ladrões.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "ladino", "nivel": 15}, {"id_classe": "bruxo", "nivel": 10}]
        },
        "stats_primarios": ["destreza", "carisma"],
        "habilidades_planejadas": ["roubar_vitalidade", "prisao_de_alma_fragmentada", "passo_fantasma"]
    },

    # =================================== PROTETOR ANCESTRAL ===================================
    "protetor_ancestral": {
        "nome": "Protetor Ancestral",
        "descricao": "Um bárbaro que pode invocar os espíritos de seus ancestrais para proteger seus aliados e guiá-lo em batalha.",
        "lore": "Quando um Protetor Ancestral entra em fúria, ele não luta sozinho. Os espíritos de gerações de guerreiros de sua tribo se erguem ao seu redor, formando uma barreira espiritual que protege seus companheiros. Esses espíritos podem desviar golpes, distrair inimigos e oferecer conselhos táticos sussurrados na mente do bárbaro. Ele é um guardião de seu povo, tanto dos vivos quanto dos mortos.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "barbaro", "nivel": 15}, {"id_classe": "xama", "nivel": 5}]
        },
        "stats_primarios": ["forca", "constituicao"],
        "habilidades_planejadas": ["furia_ancestral", "escudo_espiritual", "guia_dos_ancestrais"]
    },

    # =================================== MESTRE DOS VENENOS ===================================
    "mestre_dos_venenos": {
        "nome": "Mestre dos Venenos",
        "descricao": "Um alquimista ou assassino que se especializou na arte da toxicologia, criando e aplicando os venenos mais mortais e exóticos.",
        "lore": "O Mestre dos Venenos é um artista cujo meio é a morte em um frasco. Eles conhecem cada toxina, cada veneno e cada antídoto. Eles podem criar um veneno que mata em segundos, um que paralisa, um que causa alucinações ou um que não deixa vestígios. Eles são os assassinos mais sutis, capazes de matar um alvo a quilômetros de distância com uma única gota em sua comida ou bebida.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "alquimista", "nivel": 15}, {"id_classe": "ladino", "nivel": 10}]
        },
        "stats_primarios": ["inteligencia", "destreza"],
        "habilidades_planejadas": ["veneno_perfeito", "imunidade_a_toxinas", "nuvem_toxica"]
    },

    # =================================== CAÇADOR DE SOMBRAS ===================================
    "cacador_de_sombras": {
        "nome": "Caçador de Sombras",
        "descricao": "Um ranger que se especializou em caçar mortos-vivos, demônios e outras criaturas da escuridão.",
        "lore": "O Caçador de Sombras dedica sua vida a lutar contra a noite. Eles são especialistas em caçar as criaturas que a maioria das pessoas teme. Eles aprendem os pontos fracos de vampiros, lobisomens, fantasmas e demônios. Eles usam armas de prata, água benta e magias sagradas para explorar essas fraquezas. São a linha de defesa solitária entre a humanidade e as coisas que se escondem na escuridão.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "ranger", "nivel": 15}, {"id_classe": "clerigo", "nivel": 5}]
        },
        "stats_primarios": ["destreza", "sabedoria"],
        "habilidades_planejadas": ["inimigo_predileto_morto-vivo", "flecha_de_prata", "ver_o_invisivel"]
    },

    # =================================== INVOCADOR ===================================
    "invocador": {
        "nome": "Invocador",
        "descricao": "Um mago que se especializou em conjurar criaturas de outros planos para lutar por ele.",
        "lore": "O Invocador é um mestre dos pactos e dos portais. Eles não lutam suas próprias batalhas; eles convocam outros para lutar por eles. Com círculos de poder e nomes verdadeiros, eles podem arrastar demônios dos infernos, elementais dos planos elementais ou anjos dos céus para servi-los. O poder de um invocador é medido pela força das criaturas que ele pode controlar.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "mago", "nivel": 15}, {"id_classe": "bruxo", "nivel": 10}]
        },
        "stats_primarios": ["inteligencia", "carisma"],
        "habilidades_planejadas": ["invocar_demonio_maior", "pacto_elemental", "elo_com_o_invocado"]
    },

    # =================================== GEÔMETRA SAGRADO ===================================
    "geometra_sagrado": {
        "nome": "Geômetra Sagrado",
        "descricao": "Um artífice que usa geometria divina e matemática para criar construções e selos de poder.",
        "lore": "O Geômetra Sagrado acredita que Deus é um matemático. Eles veem a geometria divina em tudo, desde a forma de uma folha até a órbita de um planeta. Usando esse conhecimento, eles podem criar selos que prendem demônios, construir autômatos com inteligência quase divina e criar armas que disparam raios de pura ordem matemática. Eles são os arquitetos do sagrado.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "artifice", "nivel": 15}, {"id_classe": "clerigo", "nivel": 10}]
        },
        "stats_primarios": ["inteligencia", "sabedoria"],
        "habilidades_planejadas": ["selo_de_salomao", "construir_anjo_mecanico", "equacao_da_criacao"]
    },

    # =================================== CRONOMANTE ===================================
    "cronomante": {
        "nome": "Cronomante",
        "descricao": "Um mago que ousa manipular a mais perigosa de todas as forças: o tempo.",
        "lore": "O Cronomante brinca com o fogo dos deuses. Eles podem acelerar seus próprios movimentos para se tornarem um borrão, retardar seus inimigos até que fiquem quase parados, ou até mesmo vislumbrar o futuro para evitar o perigo. É uma arte incrivelmente poderosa e perigosa. Um único erro pode criar um paradoxo que desfaz a própria realidade ou apaga o mago da existência.",
        "requisitos": {
            "nivel_total": 30,
            "classes": [{"id_classe": "mago", "nivel": 20}, {"id_classe": "vidente", "nivel": 10}]
        },
        "stats_primarios": ["inteligencia", "sabedoria"],
        "habilidades_planejadas": ["acelerar", "parar_o_tempo_localizado", "visao_do_futuro"]
    },

    # =================================== MESTRE BÊBADO ===================================
    "mestre_bebado": {
        "nome": "Mestre Bêbado",
        "descricao": "Um monge que alcançou a maestria em seu estilo de luta imprevisível, tornando-se quase impossível de acertar.",
        "lore": "O Mestre Bêbado transformou sua aparente fraqueza em sua maior força. Seus movimentos são tão caóticos e imprevisíveis que nem mesmo ele sabe qual será seu próximo passo. Ele tropeça para se esquivar de um golpe, balança para desferir um soco e cai para aplicar uma rasteira. Lutar contra ele é como lutar contra o próprio caos, uma experiência frustrante e muitas vezes dolorosa para seus oponentes.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "monge", "nivel": 15}, {"id_classe": "mestre_cervejeiro", "nivel": 10}]
        },
        "stats_primarios": ["destreza", "constituicao"],
        "habilidades_planejadas": ["passo_cambaleante", "rolamento_imprevisivel", "soco_do_bebado_furioso"]
    },

    # =================================== LORDE DO MEDO ===================================
    "lorde_do_medo": {
        "nome": "Lorde do Medo",
        "descricao": "Um especialista em magia de ilusão e sombras que se alimenta do medo de suas vítimas, tornando-se um pesadelo vivo.",
        "lore": "O Lorde do Medo é um boogeyman, um monstro que se esconde debaixo da cama. Eles não matam com a lâmina ou com o feitiço; eles matam com o terror. Eles podem assumir a forma do maior medo de uma pessoa, criar pesadelos vívidos que assombram seus inimigos acordados e se alimentar de sua crescente paranoia. Para suas vítimas, é impossível saber o que é real e o que é uma ilusão, até que seus corações simplesmente desistam.",
        "requisitos": {
            "nivel_total": 25,
            "classes": [{"id_classe": "ilusionista", "nivel": 15}, {"id_classe": "sacerdote_das_sombras", "nivel": 10}]
        },
        "stats_primarios": ["carisma", "inteligencia"],
        "habilidades_planejadas": ["personificacao_do_medo", "colheita_de_terror", "paisagem_de_pesadelo"]
    }
}
