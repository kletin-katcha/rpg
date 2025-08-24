# ==============================================================================
# ARQUIVO DE DADOS: CLASSES RACIAIS
# ==============================================================================
#
# Este arquivo contém as definições para classes que são exclusivas para
# uma ou mais raças específicas, refletindo suas culturas e habilidades únicas.
#
# ==============================================================================

CLASSES_RACIAIS = {
    # =================================== FERREIRO DE BATALHA ANÃO ===================================
    "ferreiro_de_batalha_anao": {
        "nome": "Ferreiro de Batalha Anão",
        "descricao": "Um mestre artesão que leva sua forja para o campo de batalha, usando autômatos, runas e armas experimentais.",
        "lore": """
Para um Ferreiro de Batalha, a distinção entre a oficina e a guerra não existe. Sua armadura é uma obra-prima de engenharia, seu martelo é tanto uma ferramenta de criação quanto de destruição, e ele é muitas vezes acompanhado por um golem rúnico de sua própria criação. Eles são os pináculos da tradição anã de artesanato e guerra, capazes de consertar a armadura de um aliado no meio do combate ou de implantar uma torreta de defesa para proteger uma posição.
        """,
        "requisitos": {
            "nivel_total": 15,
            "raca": ["anao"]
        },
        "stats_primarios": ["forca", "constituicao", "inteligencia"],
        "habilidades_planejadas": ["invocar_golem_de_runas", "martelo_da_forja", "reparo_de_combate"]
    },

    # =================================== CANTOR DA LÂMINA ÉLFICO ===================================
    "cantor_da_lamina_elfico": {
        "nome": "Cantor da Lâmina",
        "descricao": "Uma tradição élfica que mistura a dança da espada com a magia arcana, transformando o combate em uma arte mortal.",
        "lore": """
A Canção da Lâmina é uma arte antiga e secreta, passada de mestre para aluno entre os elfos. O Cantor da Lâmina entra em um transe de batalha, onde seus movimentos se tornam uma dança fluida e hipnótica. Sua espada canta no ar, e cada corte é acompanhado por um feitiço. Eles são incrivelmente ágeis, usando magia para se proteger em vez de armaduras pesadas, e são capazes de lutar contra múltiplos inimigos com uma graça que desafia a compreensão.
        """,
        "requisitos": {
            "nivel_total": 20,
            "raca": ["elfo", "meio-elfo"]
        },
        "stats_primarios": ["destreza", "inteligencia"],
        "habilidades_planejadas": ["cancao_da_lamina", "golpe_cantado", "passo_arcano"]
    },

    # =================================== CHEFE DE GUERRA ORC ===================================
    "chefe_de_guerra_orc": {
        "nome": "Chefe de Guerra Orc",
        "descricao": "Um líder brutal e carismático, que inspira seus aliados com sua ferocidade e comanda o campo de batalha com táticas implacáveis.",
        "lore": """
Um Chefe de Guerra é o coração de um clã orc. Ele não lidera pelo direito de primogenitura, mas pela força bruta e respeito conquistado. Ele é o primeiro a entrar na batalha e o último a sair. Sua presença é tão inspiradora para os orcs que eles lutarão com o dobro de sua força normal. Ele não é apenas um bárbaro, mas um estrategista astuto, usando o terreno e a ferocidade de seu povo para esmagar inimigos mais numerosos e mais bem equipados.
        """,
        "requisitos": {
            "nivel_total": 20,
            "raca": ["orc", "meio-orc"]
        },
        "stats_primarios": ["forca", "carisma"],
        "habilidades_planejadas": ["pela_horda", "desafio_do_chefe", "furia_estrategica"]
    },

    # =================================== ANDARILHO DAS SOMBRAS KHAJIIT ===================================
    "andarilho_das_sombras_khajiit": {
        "nome": "Andarilho das Sombras",
        "descricao": "Um mestre da furtividade e da magia lunar, que usa as sombras e a agilidade felina para se tornar um predador perfeito.",
        "lore": """
Os Andarilhos das Sombras são uma ordem secreta de Khajiit que adoram as luas escuras. Eles aprendem a manipular as sombras, a se mover sem som e a usar a magia da lua para confundir e enganar. Eles são os espiões e assassinos mais eficazes do mundo, capazes de se infiltrar em qualquer lugar e desaparecer sem deixar vestígios. Para eles, a escuridão não é algo a ser temido, mas um manto que os protege e lhes dá poder.
        """,
        "requisitos": {
            "nivel_total": 15,
            "raca": ["khajiit", "tabaxi"]
        },
        "stats_primarios": ["destreza", "carisma"],
        "habilidades_planejadas": ["manto_de_sombras", "ataque_lunar", "passos_silenciosos"]
    },

    # =================================== XAMÃ DO PÂNTANO ARGONIANO ===================================
    "xama_do_pantano_argoniano": {
        "nome": "Xamã do Pântano",
        "descricao": "Um Argoniano que mergulhou fundo nos segredos do Hist e do pântano, usando venenos, doenças e a própria terra como armas.",
        "lore": """
O Xamã do Pântano é a voz do Hist e a fúria de Black Marsh. Eles não usam a magia da mesma forma que as outras raças; eles a comandam através de rituais primordiais. Eles podem cuspir veneno, invocar nuvens de insetos doentios e fazer com que o próprio pântano se levante para engolir seus inimigos. Eles são os protetores de seu povo e uma personificação da natureza perigosa e implacável de sua terra natal.
        """,
        "requisitos": {
            "nivel_total": 15,
            "raca": ["argoniano", "povo_lagarto"]
        },
        "stats_primarios": ["sabedoria", "constituicao"],
        "habilidades_planejadas": ["sopro_pestilento", "pele_de_espinho", "invocar_lodo_do_pantano"]
    },

    # =================================== GOLEMITA (WARFORGED) ===================================
    "golemita": {
        "nome": "Golemita",
        "descricao": "Um construto que integra novas tecnologias e armas em seu próprio corpo, tornando-se uma fortaleza ambulante.",
        "lore": "O Golemita é o ápice da engenharia dos Forjados Bélicos. Eles não apenas usam armas; eles se tornam as armas. Seu corpo é um chassi em constante evolução, integrando canhões, lâminas retráteis e escudos de energia. Eles são a fusão definitiva de ser vivo e máquina de guerra, uma visão aterrorizante para qualquer exército tradicional.",
        "requisitos": { "nivel_total": 20, "raca": ["forjado_belico"] },
        "stats_primarios": ["constituicao", "forca"],
        "habilidades_planejadas": ["integrar_arma", "chassi_reforcado", "canhao_de_ombro"]
    },

    # =================================== DEFENSOR DE PEDRA (GOLIATH) ===================================
    "defensor_de_pedra": {
        "nome": "Defensor de Pedra",
        "descricao": "Um Golias que personifica a força e a resiliência da montanha, usando seu tamanho e poder para proteger seu povo.",
        "lore": "O Defensor de Pedra é a rocha sobre a qual a tribo Golias se apoia. Eles são guerreiros de poder imenso, cuja pele pode se tornar tão dura quanto granito. Eles se especializam em lutar em terrenos montanhosos, usando o ambiente a seu favor para criar avalanches ou bloquear passagens. São a muralha inabalável que protege seu povo dos perigos da montanha.",
        "requisitos": { "nivel_total": 15, "raca": ["golias"] },
        "stats_primarios": ["forca", "constituicao"],
        "habilidades_planejadas": ["pele_de_granito", "arremesso_de_rocha", "presenca_da_montanha"]
    },

    # =================================== MESTRE CERVEJEIRO (PANDAREN) ===================================
    "mestre_cervejeiro_pandaren": {
        "nome": "Mestre Cervejeiro",
        "descricao": "A personificação da tradição pandaren, um lutador que combina artes marciais fluidas com o poder de infusões místicas.",
        "lore": "Para o Mestre Cervejeiro, a cerveja não é apenas uma bebida; é uma filosofia. Cada infusão é uma forma de meditação e uma fonte de poder. Eles lutam com um estilo de luta aparentemente desequilibrado e caótico, mas que esconde uma precisão mortal. Eles podem cuspir fogo, curar-se com um gole de sua bebida ou criar uma névoa que confunde seus inimigos.",
        "requisitos": { "nivel_total": 20, "raca": ["pandaren"] },
        "stats_primarios": ["constituicao", "destreza"],
        "habilidades_planejadas": ["baforada_de_fogo", "infusao_vigorosa", "estilo_do_bebado"]
    },

    # =================================== PORTADOR DO VAZIO (TIEFLING) ===================================
    "portador_do_vazio": {
        "nome": "Portador do Vazio",
        "descricao": "Um Tiefling que abraçou sua herança infernal, usando magia das sombras e do fogo do inferno para corromper e destruir.",
        "lore": "Enquanto alguns Tieflings lutam contra sua linhagem, o Portador do Vazio a abraça. Ele extrai poder diretamente dos planos inferiores, tornando-se um canal para a energia do vazio e do fogo do inferno. Suas sombras dançam com malícia, e seu toque pode drenar a vida ou inflamar a alma. Eles são a prova de que a herança de alguém pode ser uma arma poderosa.",
        "requisitos": { "nivel_total": 20, "raca": ["tiefling"] },
        "stats_primarios": ["carisma", "inteligencia"],
        "habilidades_planejadas": ["tentaculos_do_vazio", "chamas_infernais", "drenar_alma"]
    },

    # =================================== LÂMINA SOLAR (AASIMAR) ===================================
    "lamina_solar": {
        "nome": "Lâmina Solar",
        "descricao": "Um Aasimar que canaliza sua herança celestial em sua arma, criando uma lâmina de pura luz solar para purificar o mal.",
        "lore": "A Lâmina Solar é a justiça dos céus encarnada. Eles são guerreiros celestiais cuja fé e poder se manifestam como uma espada de luz. Esta lâmina queima mortos-vivos e demônios com um toque e pode cegar os inimigos com seu brilho. Eles são os campeões da luz, enviados para lutar nas batalhas mais sombrias.",
        "requisitos": { "nivel_total": 20, "raca": ["aasimar"] },
        "stats_primarios": ["forca", "carisma"],
        "habilidades_planejadas": ["espada_de_luz_solar", "golpe_purificador", "aura_ofuscante"]
    },

    # =================================== TECELÃO DE AREIA (HUMANO DO DESERTO) ===================================
    "tecelao_de_areia": {
        "nome": "Tecelão de Areia",
        "descricao": "Um mago do deserto que comanda a areia para criar construtos, tempestades e proteger seus aliados.",
        "lore": "O deserto é um lugar de poder, e o Tecelão de Areia é seu mestre. Eles podem sentir cada grão de areia e moldá-los à sua vontade. Eles podem criar soldados de areia para lutar por eles, invocar tempestades de areia que cegam e esfolam seus inimigos, e se transformar em areia para se mover sem serem detectados. São os guardiões dos segredos do deserto.",
        "requisitos": { "nivel_total": 15, "raca": ["humano"] },
        "stats_primarios": ["inteligencia", "sabedoria"],
        "habilidades_planejadas": ["invocar_elemental_de_areia", "tempestade_de_areia", "forma_de_areia"]
    },

    # =================================== VIDENTE DAS PROFUNDEZAS (TRITÃO) ===================================
    "vidente_das_profundezas": {
        "nome": "Vidente das Profundezas",
        "descricao": "Um Tritão que usa a pressão e os segredos do oceano para esmagar e enlouquecer seus inimigos.",
        "lore": "O Vidente das Profundezas ouviu os sussurros do oceano profundo, e isso mudou sua mente. Ele comanda a pressão esmagadora das fossas abissais, pode invocar a tinta de lulas gigantes para cegar seus inimigos e compartilhar os segredos enlouquecedores que aprendeu com as criaturas das profundezas. Ele é o guardião dos mistérios do oceano.",
        "requisitos": { "nivel_total": 20, "raca": ["tritao", "elfo_do_mar"] },
        "stats_primarios": ["sabedoria", "inteligencia"],
        "habilidades_planejadas": ["esmagamento_abissal", "sussurros_enlouquecedores", "invocar_kraken_juvenil"]
    },

    # =================================== CAVALEIRO DE GRIFO (HUMANO/ELFO) ===================================
    "cavaleiro_de_grifo": {
        "nome": "Cavaleiro de Grifo",
        "descricao": "Um guerreiro de elite que luta montado em um grifo, dominando os céus e atacando de cima.",
        "lore": "Os Cavaleiros de Grifo são a cavalaria dos céus. O vínculo entre cavaleiro e grifo é forjado ao longo de anos de treinamento, tornando-os uma unidade de combate perfeita. Do alto, eles podem atacar as linhas inimigas, destruir máquinas de cerco e fornecer reconhecimento. São um símbolo de esperança e poder aéreo.",
        "requisitos": { "nivel_total": 20, "raca": ["humano", "elfo"] },
        "stats_primarios": ["destreza", "forca"],
        "habilidades_planejadas": ["ataque_em_mergulho", "grito_do_grifo", "maestria_aerea"]
    },

    # =================================== SENHOR DAS FERAS (CENTAURO) ===================================
    "senhor_das_feras_centauro": {
        "nome": "Senhor das Feras",
        "descricao": "Um centauro que lidera não apenas seu povo, mas também as criaturas selvagens da floresta.",
        "lore": "O Senhor das Feras é um com a natureza. Ele não apenas lidera sua tribo de centauros, mas também os lobos, os ursos e os javalis da floresta. Em batalha, ele é uma força da natureza, liderando uma carga de cascos, garras e presas que pode atropelar qualquer exército. Ele é o guardião supremo da floresta.",
        "requisitos": { "nivel_total": 25, "raca": ["centauro"] },
        "stats_primarios": ["forca", "sabedoria"],
        "habilidades_planejadas": ["carga_da_floresta", "invocar_matilha", "espiritos_da_natureza"]
    },

    # =================================== VINGADOR DE ASAS (KENKU) ===================================
    "vingador_de_asas": {
        "nome": "Vingador de Asas",
        "descricao": "Um Kenku que, através de um pacto ou magia, recuperou a capacidade de voar e agora busca vingança contra aqueles que amaldiçoaram sua raça.",
        "lore": "A maldição dos Kenku os impede de voar. O Vingador de Asas é aquele que quebrou essa maldição. Com asas recém-adquiridas, ele se tornou um anjo da vingança para seu povo. Ele é um mestre do combate aéreo, usando sua agilidade e conhecimento de sons para imitar os ataques de seus inimigos e se vingar daqueles que os oprimiram.",
        "requisitos": { "nivel_total": 25, "raca": ["kenku", "aarakocra"] },
        "stats_primarios": ["destreza", "carisma"],
        "habilidades_planejadas": ["voo_da_vinganca", "mimetismo_de_combate", "grito_perfurante"]
    },

    # =================================== MESTRE DAS RUNAS GIGANTES ===================================
    "mestre_das_runas_gigantes": {
        "nome": "Mestre das Runas Gigantes",
        "descricao": "Um gigante que dominou a antiga arte da magia rúnica dos gigantes, infundindo seu corpo e armas com poder elemental.",
        "lore": "A magia rúnica dos gigantes é uma das formas mais antigas e poderosas de magia. O Mestre das Runas inscreve esses símbolos em sua pele, em suas armas e na própria terra. Cada runa lhe concede o poder de um aspecto dos gigantes: a força do gigante da colina, o fogo do gigante do fogo, o gelo do gigante do gelo. Ele é um arquivo vivo da história e do poder de sua raça.",
        "requisitos": { "nivel_total": 30, "raca": ["gigante", "golias"] },
        "stats_primarios": ["forca", "constituicao", "sabedoria"],
        "habilidades_planejadas": ["runa_do_fogo_de_surtur", "runa_do_gelo_de_thrym", "runa_da_terra_de_skofnung"]
    },

    # =================================== ESPINHO DO SUBTERRÂNEO (GNOMO) ===================================
    "espinho_do_subterraneo": {
        "nome": "Espinho do Subterrâneo",
        "descricao": "Um gnomo que usa sua inteligência e conhecimento do subterrâneo para criar armadilhas mortais e emboscadas.",
        "lore": "O Espinho do Subterrâneo é o protetor das cidades gnômicas. Ele conhece cada túnel, cada caverna e cada fenda. Ele é um mestre da guerra de guerrilha, usando armadilhas complexas, ilusões e conhecimento do terreno para derrotar invasores muito mais fortes. Para os inimigos dos gnomos, cada túnel escuro pode esconder uma morte engenhosa.",
        "requisitos": { "nivel_total": 15, "raca": ["gnomo"] },
        "stats_primarios": ["inteligencia", "destreza"],
        "habilidades_planejadas": ["mestre_das_armadilhas", "emboscada_subterranea", "ilusao_de_terreno"]
    },

    # =================================== CAMPEÃO DRACONATO (DRAGONBORN) ===================================
    "campeao_draconato": {
        "nome": "Campeão Draconato",
        "descricao": "Um Dragonborn que abraçou plenamente sua herança dracônica, manifestando asas, uma presença aterrorizante e um sopro devastador.",
        "lore": "O Campeão Draconato é o mais próximo que um mortal pode chegar de ser um dragão. Sua herança dracônica se manifesta plenamente, dando-lhe asas para voar, escamas tão duras quanto metal e um sopro que pode derreter pedra. Ele é o líder de seu clã, um guerreiro reverenciado e temido, a personificação do poder dos dragões.",
        "requisitos": { "nivel_total": 25, "raca": ["draconato"] },
        "stats_primarios": ["forca", "constituicao"],
        "habilidades_planejadas": ["voo_draconico", "sopro_cataclismico", "presenca_de_dragao"]
    },

    # =================================== MESTRE DAS ILUSÕES (FADA) ===================================
    "mestre_das_ilusoes_fada": {
        "nome": "Mestre das Ilusões",
        "descricao": "Uma fada cujo domínio sobre a magia de ilusão é tão grande que ela pode criar realidades temporárias e prender seus inimigos em seus próprios sonhos.",
        "lore": "Para o Mestre das Ilusões, a linha entre o real e o falso é um brinquedo. Eles são os tecelões de sonhos e pesadelos, capazes de criar paisagens inteiras do nada ou prender um inimigo em um loop de seus piores medos. Sua magia é sutil, mas aterrorizante, e poucos podem dizer que já viram a verdadeira forma de um desses mestres.",
        "requisitos": { "nivel_total": 20, "raca": ["fada", "changeling"] },
        "stats_primarios": ["carisma", "inteligencia"],
        "habilidades_planejadas": ["criar_semiplano_ilusorio", "pesadelo_lucido", "dobrar_a_realidade"]
    },

    # =================================== PASTOR DE ÁRVORES (ENT/SYLVAN) ===================================
    "pastor_de_arvores": {
        "nome": "Pastor de Árvores",
        "descricao": "Um Ent ou Silvano que pode despertar as árvores da floresta para lutar ao seu lado, comandando um exército de madeira e folhas.",
        "lore": "O Pastor de Árvores é o guardião da floresta antiga. Ele pode falar com as árvores, e as árvores respondem. Em tempos de necessidade, ele pode despertar seus irmãos adormecidos, criando um exército de Ents e Treants que pode esmagar qualquer exército que ouse invadir seu domínio. Ele é a vontade da floresta, lenta para a fúria, mas imparável uma vez despertada.",
        "requisitos": { "nivel_total": 30, "raca": ["ent", "silvano"] },
        "stats_primarios": ["sabedoria", "forca"],
        "habilidades_planejadas": ["despertar_floresta", "comandar_treants", "pele_de_casca_de_ferro"]
    },

    # =================================== CAMINHANTE DOS SONHOS (KITSUNE) ===================================
    "caminhante_dos_sonhos": {
        "nome": "Caminhante dos Sonhos",
        "descricao": "Um Kitsune que dominou a arte de entrar e manipular os sonhos dos outros, usando-os para obter informações ou enlouquecer seus inimigos.",
        "lore": "O Caminhante dos Sonhos é um mestre do subconsciente. Eles podem entrar nos sonhos de qualquer ser, roubar seus segredos mais profundos, plantar ideias ou criar pesadelos tão vívidos que causam dano físico. Eles são os espiões e manipuladores perfeitos, capazes de derrubar um império sem nunca dar um passo em seu território.",
        "requisitos": { "nivel_total": 20, "raca": ["kitsune"] },
        "stats_primarios": ["carisma", "sabedoria"],
        "habilidades_planejadas": ["invasao_de_sonhos", "roubar_segredos", "ataque_psiquico"]
    },

    # =================================== LADRÃO DE SORTE (HALFLING) ===================================
    "ladrao_de_sorte": {
        "nome": "Ladrão de Sorte",
        "descricao": "Um Halfling que pode literalmente manipular a sorte, roubando a boa sorte de seus inimigos e dando-a a seus aliados.",
        "lore": "Os Halflings são naturalmente sortudos, mas o Ladrão de Sorte transformou isso em uma arma. Com um toque ou um sussurro, ele pode fazer com que o golpe de um inimigo erre, que uma armadilha falhe ou que um feitiço saia pela culatra. Ao mesmo tempo, ele pode garantir que o ataque de seu amigo seja um acerto crítico ou que ele encontre um item valioso. Ele é o mestre das probabilidades, um fator de caos que pode virar qualquer batalha.",
        "requisitos": { "nivel_total": 20, "raca": ["halfling"] },
        "stats_primarios": ["destreza", "carisma"],
        "habilidades_planejadas": ["roubar_sorte", "dar_boa_sorte", "manipular_probabilidades"]
    },

    # =================================== CANTOR DOS ECOS (SIREN/HARPIA) ===================================
    "cantor_dos_ecos": {
        "nome": "Cantor dos Ecos",
        "descricao": "Uma Sirene ou Harpia cuja canção pode manipular o som e o espaço, criando ecos que confundem, atacam e encantam.",
        "lore": "O Cantor dos Ecos é um mestre da acústica e da magia sônica. Sua voz pode quebrar pedra, encantar exércitos inteiros ou criar ecos fantasmagóricos que fazem um único guerreiro parecer um exército. Eles são os bardos da natureza, cuja música é tão bela quanto mortal.",
        "requisitos": { "nivel_total": 15, "raca": ["sirene", "harpia"] },
        "stats_primarios": ["carisma", "constituicao"],
        "habilidades_planejadas": ["grito_sonico", "ecos_confusos", "cancao_irresistivel"]
    },

    # =================================== LORDE DAS PROFUNDEZAS (ANÃO DAS PROFUNDEZAS) ===================================
    "lorde_das_profundezas": {
        "nome": "Lorde das Profundezas",
        "descricao": "Um Anão das Profundezas que se tornou um mestre do Subterrâneo, comandando as criaturas e os segredos da escuridão.",
        "lore": "O Lorde das Profundezas é o rei do mundo subterrâneo. Ele conhece cada túnel, cada cidade escondida e cada monstro que vive na escuridão. Ele pode convocar enxames de aranhas gigantes, negociar com devoradores de mentes e encontrar os veios mais ricos de mithril e adamantina. Ele é o mestre indiscutível das profundezas.",
        "requisitos": { "nivel_total": 25, "raca": ["anao_das_profundezas", "drow"] },
        "stats_primarios": ["sabedoria", "constituicao"],
        "habilidades_planejadas": ["comandar_criaturas_subterraneas", "terremoto_localizado", "mestre_mineiro"]
    },

    # =================================== CAVALEIRO CELESTIAL (ANJO) ===================================
    "cavaleiro_celestial": {
        "nome": "Cavaleiro Celestial",
        "descricao": "Um anjo guerreiro que cavalga um pégaso ou outra montaria celestial, liderando as hostes do bem contra as forças das trevas.",
        "lore": "O Cavaleiro Celestial é a vanguarda dos exércitos celestiais. Montado em um corcel de pura luz, ele mergulha na batalha, sua lança brilhando com poder divino. Ele é um farol de esperança para os justos e um terror para os demônios e mortos-vivos. Sua carga pode quebrar as linhas de qualquer exército infernal.",
        "requisitos": { "nivel_total": 30, "raca": ["anjo", "aasimar"] },
        "stats_primarios": ["forca", "carisma"],
        "habilidades_planejadas": ["carga_celestial", "lanca_de_luz", "montaria_divina"]
    },

    # =================================== MESTRE DAS MARÉS (ELFO DO MAR) ===================================
    "mestre_das_mares": {
        "nome": "Mestre das Marés",
        "descricao": "Um Elfo do Mar que pode controlar as marés, invocar tsunamis e comandar as correntes do oceano.",
        "lore": "O Mestre das Marés é um com o oceano. Ele pode sentir o puxão da lua e o fluxo das correntes. Com um gesto, ele pode criar ondas gigantes para esmagar navios, ou acalmar uma tempestade para salvar uma frota. Ele é o poder do oceano encarnado, um aliado inestimável para qualquer nação marítima e um inimigo temível para qualquer um que ouse desafiá-lo em seu domínio.",
        "requisitos": { "nivel_total": 20, "raca": ["elfo_do_mar", "tritao"] },
        "stats_primarios": ["sabedoria", "carisma"],
        "habilidades_planejadas": ["invocar_tsunami", "controlar_correntes", "respiracao_aquatica_em_massa"]
    },

    # =================================== PROFETA DA MONTANHA (AARAKOCRA) ===================================
    "profeta_da_montanha": {
        "nome": "Profeta da Montanha",
        "descricao": "Um Aarakocra que vive nos picos mais altos, meditando sobre os ventos e as estrelas para prever o futuro.",
        "lore": "O Profeta da Montanha vive mais perto das estrelas do que qualquer outro mortal. Ele lê o futuro nos padrões do vento e nas constelações. Reis e imperadores fazem peregrinações para ouvir suas profecias. Ele é um guardião do conhecimento, um observador do destino, e sua sabedoria é tão vasta quanto os céus que ele habita.",
        "requisitos": { "nivel_total": 25, "raca": ["aarakocra"] },
        "stats_primarios": ["sabedoria", "inteligencia"],
        "habilidades_planejadas": ["profecia_do_vento", "comunhao_com_as_estrelas", "voo_meditativo"]
    },

    # =================================== GUARDIÃO DO VÉU (CHANGELING) ===================================
    "guardiao_do_veu": {
        "nome": "Guardião do Véu",
        "descricao": "Um Changeling que protege o equilíbrio entre o mundo mortal e o reino das fadas, usando sua habilidade de mudar de forma para policiar ambos os lados.",
        "lore": "O Guardião do Véu vive na fronteira entre dois mundos. Ele é um diplomata, um espião e, quando necessário, um executor. Ele garante que as fadas não causem muito caos no mundo mortal e que os mortais não explorem o reino das fadas. Com mil faces e mil vozes, ele é o guardião invisível que mantém a paz entre duas realidades.",
        "requisitos": { "nivel_total": 15, "raca": ["changeling", "doppelganger"] },
        "stats_primarios": ["carisma", "destreza"],
        "habilidades_planejadas": ["mestre_da_transformacao", "passagem_feérica", "impor_acordo"]
    },

    # =================================== LÂMINA DA DUNA (YUAN-TI) ===================================
    "lamina_da_duna": {
        "nome": "Lâmina da Duna",
        "descricao": "Um Yuan-ti que combina a furtividade da serpente com a magia do deserto, um assassino que ataca das areias.",
        "lore": "A Lâmina da Duna é o predador perfeito do deserto. Ele se move sob a areia como uma serpente, emergindo apenas para dar o bote. Ele usa venenos potentes e magias de areia para incapacitar suas presas antes de desferir o golpe final. Ele é o medo sussurrado nas caravanas, o fantasma das dunas que caça sob o sol escaldante.",
        "requisitos": { "nivel_total": 20, "raca": ["yuan-ti_puro-sangue"] },
        "stats_primarios": ["destreza", "constituicao"],
        "habilidades_planejadas": ["bote_da_areia", "veneno_debilitante", "pele_de_serpente"]
    },

    # =================================== CORAÇÃO DA FORJA (ANÃO DE FOGO) ===================================
    "coracao_da_forja": {
        "nome": "Coração da Forja",
        "descricao": "Um Anão de Fogo que se tornou um com o magma e a forja, seu corpo irradiando calor e seu toque moldando o metal.",
        "lore": "O Coração da Forja é a alma viva da grande forja de sua cidade. Seu corpo é tão quente que a água ferve ao seu redor, e ele pode moldar o aço com as próprias mãos. Ele é o maior dos ferreiros, capaz de criar armas lendárias infundidas com o poder do próprio magma. Ele é a personificação da paixão e da habilidade dos anões de fogo.",
        "requisitos": { "nivel_total": 25, "raca": ["anao_de_fogo"] },
        "stats_primarios": ["constituicao", "forca"],
        "habilidades_planejadas": ["corpo_de_magma", "moldar_metal", "arma_da_forja_eterna"]
    }
}
