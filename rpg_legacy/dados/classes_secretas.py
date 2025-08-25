# ==============================================================================
# ARQUIVO DE DADOS: CLASSES SECRETAS
# ==============================================================================
#
# Este arquivo contém as definições para as classes secretas.
# Estas classes não são encontradas através da progressão normal e exigem
# que o jogador complete feitos, encontre itens ou explore locais escondidos
# para serem desbloqueadas.
#
# ==============================================================================

CLASSES_SECRETAS = {
    # =================================== DANÇARINO DAS LÂMINAS ESPECTRAIS ===================================
    "dancarino_laminas_espectrais": {
        "nome": "Dançarino das Lâminas Espectrais",
        "descricao": "Um guerreiro que luta em uníssono com os espíritos de duelistas caídos, movendo-se com uma graça fantasmagórica e atacando com lâminas etéreas.",
        "lore": """
Existem lendas de espadachins tão dedicados à sua arte que suas almas se recusam a deixar o plano mortal, permanecendo ligadas às suas lâminas ou locais de sua última batalha. Um mortal que encontra tal local e prova seu valor em combate pode se harmonizar com esses espíritos. O Dançarino das Lâminas Espectrais não luta sozinho; ele é um com um coro de fantasmas guerreiros, seus movimentos são guiados por séculos de experiência de combate, e suas armas podem ferir tanto a alma quanto o corpo.
        """,
        "requisitos": {
            "evento": "completar_o_ritual_do_cemiterio_dos_herois",
            "item_necessario": "lamina_fantasma_partida"
        },
        "stats_primarios": ["destreza", "sabedoria"],
        "habilidades_planejadas": ["valsa_dos_espectros", "corte_da_alma", "forma_fantasma"]
    },

    # =================================== LADRÃO DE MEMÓRIAS ===================================
    "ladrao_de_memorias": {
        "nome": "Ladrão de Memórias",
        "descricao": "Um psíquico que se especializa em se infiltrar na mente dos outros, não para roubar segredos, mas para roubar memórias e habilidades.",
        "lore": """
O Ladrão de Memórias é o mais perigoso dos ladrões. Eles usam artefatos raros ou poderes psiônicos para entrar no cenário onírico de um alvo. Lá, eles navegam pelas memórias, emoções e conhecimentos da vítima. Um ladrão de memórias habilidoso pode 'aprender' uma habilidade de combate de um grande guerreiro ou 'roubar' o conhecimento de um feitiço da mente de um arquimago enquanto eles dormem. É uma arte perigosa, pois a mente pode ser um lugar traiçoeiro, e alguns sonhos se tornam pesadelos dos quais não há como escapar.
        """,
        "requisitos": {
            "evento": "sobreviver_a_uma_viagem_ao_plano_dos_sonhos",
            "stats": {"inteligencia": 25, "sabedoria": 25}
        },
        "stats_primarios": ["inteligencia", "carisma"],
        "habilidades_planejadas": ["roubar_habilidade", "invasao_onirica", "apagar_memoria"]
    },

    # =================================== CORAÇÃO DE GOLEM ===================================
    "coracao_de_golem": {
        "nome": "Coração de Golem",
        "descricao": "Um ser mortal que substituiu seu próprio coração por um núcleo de golem arcano, fundindo carne e pedra para se tornar um colosso vivo.",
        "lore": """
A busca pela imortalidade ou pelo poder leva a caminhos estranhos. O Coração de Golem é um indivíduo que, através de um ritual perigoso, implantou um núcleo de poder de um golem em seu próprio peito. Seu corpo se torna progressivamente mais parecido com pedra, e sua força e resistência atingem níveis sobre-humanos. Eles não sentem dor da mesma forma e podem reconstruir seus corpos a partir de danos terríveis. No entanto, eles correm o risco de perder sua humanidade, tornando-se mais máquina do que ser vivo.
        """,
        "requisitos": {
            "evento": "realizar_o_ritual_de_transfusao_do_nucleo",
            "raca_excluida": ["forjado", "automato"]
        },
        "stats_primarios": ["constituicao", "forca"],
        "habilidades_planejadas": ["punho_de_pedra", "regeneracao_do_construto", "sobrecarga_do_nucleo"]
    },

    # =================================== CANTOR DO VAZIO ===================================
    "cantor_do_vazio": {
        "nome": "Cantor do Vazio",
        "descricao": "Um conjurador que olhou para o abismo entre as estrelas e ouviu a canção do vazio. Agora, ele a canta para desfazer a realidade.",
        "lore": """
Existem espaços entre os mundos, um nada cheio de um potencial caótico e de uma música terrível. O Cantor do Vazio é um mortal que, intencionalmente ou não, ouviu essa música e sobreviveu com sua sanidade (quase) intacta. Ele aprendeu a imitar essa canção, usando sua voz para canalizar o poder do vazio. Seus feitiços não são de fogo ou gelo, mas de aniquilação, silêncio e entropia. Eles podem apagar o som, desintegrar matéria e invocar ecos das criaturas incompreensíveis que vivem no vazio.
        """,
        "requisitos": {
            "evento": "sobreviver_a_uma_exposicao_ao_plano_distante",
            "stats": {"carisma": 30}
        },
        "stats_primarios": ["carisma", "constituicao"],
        "habilidades_planejadas": ["cancao_da_entropia", "sopro_do_silencio", "invocar_horror"]
    },

    # =================================== CRONISTA ===================================
    "cronista": {
        "nome": "Cronista (Loremaster)",
        "descricao": "Um estudioso que transcendeu o mero conhecimento para alcançar uma compreensão fundamental da história e do destino do mundo.",
        "lore": """
O Cronista é um colecionador de histórias, um arquivista do passado, presente e futuro. Ao coletar artefatos, livros e histórias suficientes, ele começa a ver os padrões, as linhas do destino que conectam todos os eventos. Ele não apenas conhece a história; ele pode usar esse conhecimento como uma arma. Ele pode invocar o 'eco' de um herói antigo para lutar ao seu lado, recitar uma passagem de um texto proibido para banir um demônio, ou prever a próxima ação de um inimigo com base em seus padrões de comportamento.
        """,
        "requisitos": {
            "quests_concluidas": 100,
            "livros_unicos_lidos": 50
        },
        "stats_primarios": ["sabedoria", "inteligencia"],
        "habilidades_planejadas": ["invocar_eco_heroico", "palavra_da_verdade", "previsao_tatica"]
    },

    # =================================== VIAJANTE DO TEMPO ACIDENTAL ===================================
    "viajante_do_tempo_acidental": {
        "nome": "Viajante do Tempo Acidental",
        "descricao": "Alguém que foi jogado através do tempo por um acidente mágico e agora está instável no fluxo temporal, saltando aleatoriamente para o passado e o futuro.",
        "lore": "Esta pessoa não queria este poder. Um feitiço que deu errado, um artefato instável, e de repente eles se viram em sua própria infância, ou em um futuro em ruínas. Agora, eles não estão mais ancorados no tempo. Em momentos de estresse, eles podem saltar alguns segundos para o futuro para evitar um golpe, ou trazer uma versão futura de si mesmos para ajudar na batalha. É um poder incrivelmente desorientador e perigoso, e eles estão constantemente tentando encontrar o caminho de volta para sua própria linha do tempo.",
        "requisitos": { "evento": "ser_o_epicentro_de_um_paradoxo_temporal" },
        "stats_primarios": ["constituicao", "sabedoria"],
        "habilidades_planejadas": ["salto_temporal", "eco_do_futuro", "rebobinar_ferimento"]
    },

    # =================================== MESTRE DOS DESEJOS ===================================
    "mestre_dos_desejos": {
        "nome": "Mestre dos Desejos",
        "descricao": "Um ser que encontrou uma fonte de poder de desejos, como um gênio ou um artefato, e agora pode distorcer a realidade, mas sempre com um preço.",
        "lore": "O Mestre dos Desejos é um mortal que brinca com o poder dos deuses. Eles podem desejar que seus inimigos se transformem em pedra, que tesouros apareçam do nada, ou que seus ferimentos desapareçam. No entanto, a magia do desejo é uma força traiçoeira. Cada desejo tem uma consequência não intencional, uma 'pegadinha' cósmica. Desejar riqueza pode fazer chover ouro, mas também pode causar o colapso da economia. É o poder supremo, limitado apenas pela astúcia do usuário em formular seus desejos.",
        "requisitos": { "item_necessario": "lampada_do_genio_aprisionado", "evento": "libertar_o_genio_e_roubar_seu_poder" },
        "stats_primarios": ["carisma", "inteligencia"],
        "habilidades_planejadas": ["desejo_menor", "desejo_maior", "consequencia_imprevista"]
    },

    # =================================== DEVORADOR DE DEUSES ===================================
    "devorador_de_deuses": {
        "nome": "Devorador de Deuses",
        "descricao": "Uma criatura ou mortal que descobriu como matar seres divinos e absorver sua essência, crescendo em poder a cada divindade consumida.",
        "lore": "No início, era apenas um mortal. Mas então, ele matou um semideus. E ao fazê-lo, ele sentiu um poder imenso fluir para dentro de si. Agora, ele tem um novo apetite. O Devorador de Deuses caça ativamente os seres divinos, de avatares a deuses menores. Cada divindade que ele consome lhe concede uma porção de seus poderes e domínios. Ele é a heresia suprema, uma ameaça a todo o panteão.",
        "requisitos": { "evento": "matar_um_ser_divino_e_absorver_sua_essencia" },
        "stats_primarios": ["forca", "constituicao", "sabedoria"],
        "habilidades_planejadas": ["absorver_essencia_divina", "poder_roubado", "aura_deicida"]
    },

    # =================================== MÍMICO ===================================
    "mimico_classe": {
        "nome": "Mímico",
        "descricao": "Um ser que pode perfeitamente imitar a aparência, as habilidades e até mesmo o equipamento de qualquer pessoa que encontrar.",
        "lore": "Não se sabe se o Mímico é uma pessoa ou uma criatura que aprendeu a se parecer com uma. Eles são os mestres da imitação. Ao observar um guerreiro, eles podem replicar sua postura de combate e a força de seus golpes. Ao observar um mago, eles podem tecer os mesmos feitiços. Sua capacidade de se adaptar é sua maior força, mas eles não têm uma identidade própria, sendo apenas um reflexo daqueles ao seu redor.",
        "requisitos": { "raca": ["doppelganger", "changeling"], "evento": "absorver_a_essencia_de_100_humanoides_diferentes" },
        "stats_primarios": ["destreza", "inteligencia"],
        "habilidades_planejadas": ["copia_perfeita", "replicar_habilidade", "mudar_equipamento"]
    },

    # =================================== HOSPEDEIRO DA FÊNIX ===================================
    "hospedeiro_da_fenix": {
        "nome": "Hospedeiro da Fênix",
        "descricao": "Um mortal que se tornou o hospedeiro do espírito de uma Fênix, ganhando o poder do renascimento e do fogo purificador.",
        "lore": "A Fênix é um ser de renascimento eterno. Quando seu ciclo termina, ela deve encontrar um hospedeiro mortal para abrigar sua essência até que possa renascer. O Hospedeiro da Fênix ganha poderes incríveis sobre o fogo e a cura. E, o mais importante, se ele morrer, ele renascerá das próprias cinzas, assim como a Fênix. É um poder de imortalidade, mas o fogo da Fênix é uma força volátil e difícil de controlar.",
        "requisitos": { "evento": "ser_escolhido_pela_fenix_em_seu_ciclo_de_morte" },
        "stats_primarios": ["constituicao", "carisma"],
        "habilidades_planejadas": ["renascimento_flamejante", "fogo_purificador", "asas_de_cinza"]
    },

    # =================================== JARDINEIRO DE OSSOS ===================================
    "jardineiro_de_ossos": {
        "nome": "Jardineiro de Ossos",
        "descricao": "Um necromante que vê a beleza na morte, cultivando criaturas de ossos e plantas mortas-vivas em um jardim macabro.",
        "lore": "O Jardineiro de Ossos não é um necromante comum. Ele não busca poder ou dominação. Ele é um artista, e seu meio é a morte. Em seu jardim, ele cultiva flores que crescem de crânios, árvores feitas de espinhas e golens de ossos que cuidam de suas criações. Ele é um eremita, um filósofo da morte que vê o ciclo da vida e da decadência como a mais bela das artes.",
        "requisitos": { "evento": "cultivar_a_rosa_de_ébano_em_solo_assombrado" },
        "stats_primarios": ["sabedoria", "inteligencia"],
        "habilidades_planejadas": ["cultivar_golem_de_ossos", "colheita_macabra", "florescer_da_decadencia"]
    },

    # =================================== CAÇADOR DE ANOMALIAS ===================================
    "cacador_de_anomalias": {
        "nome": "Caçador de Anomalias",
        "descricao": "Um especialista em caçar e conter anomalias planares, paradoxos temporais e outras ameaças à realidade.",
        "lore": "O Caçador de Anomalias é o zelador da realidade. Quando um feitiço cria um paradoxo, quando uma criatura de uma realidade impossível vaza para o nosso mundo, ou quando as leis da física simplesmente param de funcionar em um local, ele é chamado. Equipado com dispositivos estranhos e um conhecimento profundo das leis cósmicas, ele caça e contém essas ameaças antes que elas possam desfazer o tecido da existência.",
        "requisitos": { "evento": "fechar_uma_fenda_realidade_com_as_proprias_maos" },
        "stats_primarios": ["inteligencia", "sabedoria"],
        "habilidades_planejadas": ["conter_anomalia", "arma_de_paradoxo", "sentir_distorcao"]
    },

    # =================================== CORAÇÃO DA TEMPESTADE ===================================
    "coracao_da_tempestade": {
        "nome": "Coração da Tempestade",
        "descricao": "Um ser que absorveu o coração de um elemental da tempestade, tornando-se uma tempestade ambulante de vento e raios.",
        "lore": "O Coração da Tempestade é um com a fúria dos céus. Após absorver o núcleo de um poderoso elemental da tempestade, seu corpo se tornou um condutor vivo para o poder do clima. Seus olhos crepitam com relâmpagos, sua voz é o trovão, e ele é cercado por um vendaval constante. Ele é a personificação da tempestade, um poder da natureza em forma humanóide.",
        "requisitos": { "evento": "absorver_o_nucleo_de_um_lorde_elemental_da_tempestade" },
        "stats_primarios": ["constituicao", "destreza"],
        "habilidades_planejadas": ["corpo_de_tempestade", "invocar_raio_mestre", "furacao"]
    },

    # =================================== TECELÃO DO DESTINO ===================================
    "tecelao_do_destino": {
        "nome": "Tecelão do Destino",
        "descricao": "Um ser que pode ver e manipular as linhas do destino que conectam todas as coisas, reescrevendo o futuro.",
        "lore": "O Tecelão do Destino vê o que poucos podem: os fios dourados do destino que guiam a vida de todos. Ele aprendeu a tocar nesses fios, a cortá-los, a amarrá-los e a tecê-los de novas maneiras. Ele pode garantir que um aliado encontre um amor perdido, que um inimigo sofra um acidente trágico, ou que uma nação caia em ruínas. Ele é um dos seres mais poderosos e temidos, pois joga com o próprio roteiro do universo.",
        "requisitos": { "item_necessario": "fuso_das_nornas", "evento": "tecer_uma_nova_linha_do_tempo" },
        "stats_primarios": ["sabedoria", "carisma"],
        "habilidades_planejadas": ["cortar_fio_do_destino", "tecer_futuro_brilhante", "ver_todas_as_possibilidades"]
    },

    # =================================== PACIFICADOR ===================================
    "pacificador": {
        "nome": "Pacificador",
        "descricao": "Um indivíduo com um carisma tão imenso e uma aura de paz tão poderosa que pode parar batalhas e acalmar os corações mais raivosos com sua mera presença.",
        "lore": "O Pacificador é uma anomalia em um mundo de guerra. Ele acredita que toda a violência é desnecessária. Sua aura é tão calmante, sua voz tão persuasiva, que exércitos inteiros baixaram suas armas em sua presença. Ele pode acalmar um dragão furioso, negociar a paz entre nações em guerra há séculos e redimir os vilões mais sombrios. Seu poder não é de combate, mas de compreensão e empatia absolutas.",
        "requisitos": { "evento": "terminar_uma_guerra_sem_derramar_uma_unica_gota_de_sangue" },
        "stats_primarios": ["carisma", "sabedoria"],
        "habilidades_planejadas": ["aura_de_paz", "palavra_de_serenidade", "redencao_do_inimigo"]
    },

    # =================================== LORDE DA PRAGA ===================================
    "lorde_da_praga": {
        "nome": "Lorde da Praga",
        "descricao": "Um conjurador que se tornou o mestre das doenças e das pestilências, comandando enxames e infecções.",
        "lore": "O Lorde da Praga é a personificação da doença. Ele é imune a todas as enfermidades e pode criá-las e controlá-las à vontade. Ele pode liberar uma praga que dizima uma cidade, invocar enxames de gafanhotos para destruir colheitas ou infectar um inimigo com uma doença que o consome por dentro. Ele é um dos cavaleiros do apocalipse, um arauto da decadência.",
        "requisitos": { "evento": "sobreviver_a_praga_divina_e_aprende-la_a_controlar" },
        "stats_primarios": ["constituicao", "inteligencia"],
        "habilidades_planejadas": ["invocar_praga", "enxame_devorador", "toque_da_decomposicao"]
    },

    # =================================== MESTRE DOS PORTAIS ===================================
    "mestre_dos_portais": {
        "nome": "Mestre dos Portais",
        "descricao": "Um mago que se especializou na arte de criar e controlar portais, usando-os para viajar, atacar e manipular o campo de batalha.",
        "lore": "O Mestre dos Portais vê o espaço como uma sugestão, não como uma regra. Ele pode criar portais para qualquer lugar que já tenha visto, ou até mesmo para outros planos. Em combate, ele é um pesadelo tático. Ele pode redirecionar o feitiço de um inimigo de volta para ele, teletransportar um aliado para fora do perigo, ou abrir um portal para o fundo do oceano acima da cabeça de seus inimigos. O campo de batalha é seu tabuleiro de xadrez.",
        "requisitos": { "item_necessario": "pedra_chave_planar", "evento": "visitar_10_planos_diferentes" },
        "stats_primarios": ["inteligencia", "destreza"],
        "habilidades_planejadas": ["labirinto_de_portais", "redirecionar_ataque", "invocar_exercito_instantaneo"]
    },

    # =================================== ECO DE BATALHA ===================================
    "eco_de_batalha": {
        "nome": "Eco de Batalha",
        "descricao": "Um guerreiro fantasmagórico que morreu em uma batalha cataclísmica e agora está preso em um eco dessa luta, revivendo-a e aperfeiçoando suas habilidades a cada repetição.",
        "lore": "O Eco de Batalha é um fantasma preso no tempo. Ele luta a mesma batalha de novo e de novo, o eco de um evento que moldou a história. A cada repetição, ele aprende, se adapta e se torna mais forte. Ele pode puxar outros para dentro de seu eco, forçando-os a lutar ao seu lado ou contra ele. Ele é um mestre do combate, pois teve uma eternidade para praticar.",
        "requisitos": { "evento": "morrer_em_uma_batalha_de_significancia_cosmica_e_ficar_preso_no_eco" },
        "stats_primarios": ["forca", "destreza", "sabedoria"],
        "habilidades_planejadas": ["puxar_para_o_eco", "golpe_aperfeicoado", "memoria_de_combate_eterno"]
    },

    # =================================== MESTRE CULINÁRIO ===================================
    "mestre_culinario": {
        "nome": "Mestre Culinário",
        "descricao": "Um chef cujas habilidades culinárias são tão grandes que sua comida pode conceder poderes mágicos, curar qualquer ferimento e até mesmo ressuscitar os mortos.",
        "lore": "O Mestre Culinário é o maior chef que já existiu. Ele viajou o mundo em busca dos ingredientes mais raros e exóticos: o ovo de um grifo, o leite de uma hidra, o sal do plano elemental da terra. Com esses ingredientes, ele pode criar pratos que são, literalmente, divinos. Sua comida pode conceder força de gigante, inteligência de dragão ou a capacidade de respirar fogo. Ele é um alquimista da cozinha, e seus banquetes são lendários.",
        "requisitos": { "item_necessario": "livro_de_receitas_dos_deuses", "evento": "cozinhar_um_banquete_para_uma_divindade" },
        "stats_primarios": ["constituicao", "sabedoria"],
        "habilidades_planejadas": ["banquete_dos_herois", "sopa_de_cura_total", "prato_da_ressurreicao"]
    },

    # =================================== APOSTADOR DO DESTINO ===================================
    "apostador_do_destino": {
        "nome": "Apostador do Destino",
        "descricao": "Um ser que fez uma aposta com uma entidade cósmica, ganhando o poder de manipular a sorte e a probabilidade em troca de um grande risco.",
        "lore": "O Apostador do Destino joga o jogo mais perigoso de todos. Ele fez uma aposta com o próprio destino, e agora ele pode manipular a sorte. Ele pode garantir que um evento de 1 em um milhão aconteça, ou que um evento certo falhe. Ele vive em um mundo de probabilidades, e sua vida é uma constante aposta. Se ele ganhar, ele pode se tornar um deus. Se ele perder, ele será apagado da existência.",
        "requisitos": { "evento": "ganhar_um_jogo_de_azar_contra_uma_personificacao_do_destino" },
        "stats_primarios": ["carisma", "destreza"],
        "habilidades_planejadas": ["aposta_total", "dado_viciado", "reverter_a_sorte"]
    }
}
