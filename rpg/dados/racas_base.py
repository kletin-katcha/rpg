# ==============================================================================
# ARQUIVO DE DADOS: RAÇAS BASE
# ==============================================================================
#
# Este arquivo contém as definições para todas as raças jogáveis iniciais.
# A estrutura é um dicionário onde a chave é o ID da raça (em minúsculas,
# sem espaços) e o valor é outro dicionário com os detalhes da raça.
#
# Cada entrada de raça será expandida com uma quantidade massiva de lore,
# detalhes culturais, variações, diálogos e possíveis evoluções para
# atingir a meta de linhas e profundidade do projeto.
#
# ==============================================================================

RACAS = {
    # =================================== HUMANO ===================================
    "humano": {
        "nome": "Humano",
        "descricao": "Versáteis e adaptáveis, os humanos podem ser encontrados em quase todas as profissões e terras, impulsionados por sua ambição e resiliência.",
        "lore": """
Os humanos são a raça mais jovem, prolífica e, talvez, a mais paradoxal do mundo conhecido. Sua história não está gravada em runas antigas de milênios, mas sim escrita a cada dia em tinta e sangue, em tratados e declarações de guerra. Onde as outras raças veem o tempo como um rio lento e profundo, os humanos o veem como uma tempestade furiosa, e eles são os navios que ousam navegá-la.

Sua curta vida útil, uma mera fração da de um elfo ou anão, é tanto sua maior fraqueza quanto sua maior força. Ela os imbui de uma urgência inigualável, uma necessidade de deixar uma marca, de construir impérios, de alcançar a imortalidade através de feitos e descendentes. Essa ambição desenfreada os levou a explorar os cantos mais remotos do mundo, a dominar terras que outras raças consideravam inóspitas e a desenvolver sociedades complexas e dinâmicas.

A adaptabilidade humana é lendária. Eles não possuem a força inata de um orc, a graça de um elfo ou a resiliência de um anão, mas podem aspirar a ser qualquer um deles. Um humano pode treinar para se tornar um guerreiro tão forte quanto um orc, um mago tão sábio quanto um elfo ou um artesão tão habilidoso quanto um anão. Essa flexibilidade é a chave para sua sobrevivência e domínio. Suas nações são diversas, desde reinos feudais e teocracias rígidas até repúblicas mercantis e tribos nômades.

No entanto, essa mesma ambição muitas vezes se transforma em ganância, e sua diversidade leva a conflitos internos. As guerras civis humanas são tão comuns quanto as guerras contra outras raças. Sua capacidade de grande bondade é igualada apenas por sua capacidade de crueldade indescritível. Para cada herói humano que salva o mundo, há um tirano que busca escravizá-lo. Eles são um espelho do próprio mundo: cheios de potencial, beleza, caos e contradição.
        """,
        "detalhes_culturais": """
**Sociedade e Governo:** A estrutura social humana é a mais variada de todas. Reinos, impérios, cidades-estado, repúblicas e tribos coexistem, muitas vezes em conflito. A lealdade pode ser ao rei, ao deus, ao dinheiro ou à família, dependendo da cultura. A mobilidade social é possível, mas muitas vezes difícil, alimentando a ambição de muitos.
**Religião:** Os humanos adoram um panteão vasto e diversificado de deuses, desde divindades do sol e da colheita até deuses da guerra e da morte. Sua fé é muitas vezes fervorosa e serve como uma grande força unificadora ou como uma desculpa para a guerra santa.
**Arquitetura:** A arquitetura humana é prática e funcional, mas também pode ser grandiosa e imponente. Seus castelos de pedra são fortalezas formidáveis, suas catedrais alcançam os céus e suas cidades são um labirinto de ruas de paralelepípedos, mercados movimentados e bairros pobres.
        """,
        "modificadores_stats": {"forca": 1, "destreza": 1, "constituicao": 1, "inteligencia": 1, "sabedoria": 1, "carisma": 1},
        "habilidades_raciais": ["esforco_heroico"],
        "variacoes": [
            {"nome": "Imperial", "descricao": "Criados no coração do império, são conhecidos por sua disciplina, educação e habilidade em diplomacia.", "modificadores_stats": {"carisma": 1}},
            {"nome": "Nórdico", "descricao": "Vindos das terras geladas do norte, são robustos, resistentes ao frio e guerreiros natos.", "modificadores_stats": {"constituicao": 1}},
            {"nome": "Habitante do Deserto", "descricao": "Adaptados ao sol escaldante, são ágeis e resistentes ao fogo e à fadiga.", "modificadores_stats": {"destreza": 1}}
        ],
        "dialogo_racial": ["Pelo Império!", "Que os deuses guiem seu caminho.", "Precisa de ajuda, forasteiro?", "O tempo é dinheiro, amigo."],
        "nomes_sugeridos": {"masculino": ["Marcus", "Gareth", "Elian", "Kael"], "feminino": ["Anabelle", "Seraphina", "Isolde", "Lia"], "familia": ["Stonewell", "Blackwood", "Goldhand"]},
        "relacionamento_racas": {
            "elfo": "Respeito Cauteloso - 'Eles são sábios, mas arrogantes. Vivem no passado.'",
            "anao": "Amigável - 'São parceiros comerciais confiáveis e excelentes artesãos, desde que você não os ofenda.'",
            "orc": "Desconfiança - 'Fortes, mas selvagens. É melhor manter distância de suas fortalezas.'"
        },
        "arvore_evolucao": {"semideus": {"nome": "Semideus", "requisitos": "Nível 60, favor de uma divindade maior.", "descricao": "Um mortal que transcendeu suas limitações, tocado pelo poder divino."}}
    },

    # =================================== ELFO ===================================
    "elfo": {
        "nome": "Elfo",
        "descricao": "Uma raça antiga e graciosa, com uma afinidade natural para a magia e uma profunda conexão com a natureza e as artes.",
        "lore": """
Os elfos, ou 'Eldar' como se autodenominam, são os ecos vivos de um mundo que já passou. Nascidos da magia primordial da própria terra, suas vidas se estendem por séculos, dando-lhes uma perspectiva que poucas outras raças podem compreender. Para um elfo, um reino humano pode parecer um flash momentâneo, uma flor que desabrocha e murcha em um piscar de olhos.

Esta longevidade molda todos os aspectos de sua psique. Eles são pacientes, meticulosos e deliberados em suas ações, o que muitas vezes é mal interpretado como preguiça ou indiferença por raças de vida mais curta. A verdade é que um elfo prefere observar e compreender uma situação por completo antes de agir. Sua arte, música e arquitetura refletem essa filosofia, sendo complexas, belas e construídas para durar eras. Suas cidades, muitas vezes escondidas em florestas profundas ou vales isolados, são maravilhas de design orgânico, onde a natureza e a construção se fundem em perfeita harmonia.

Sua conexão com a magia é inata. Eles não apenas a estudam; eles a sentem. A mana flui através deles como o sangue em suas veias, tornando-os naturalmente proficientes em todas as formas de feitiçaria. Da mesma forma, sua ligação com a natureza lhes confere uma agilidade e sentidos sobre-humanos, tornando-os arqueiros e batedores incomparáveis.

No entanto, sua longa vida também pode ser uma maldição. Eles sentem o peso do tempo e da perda mais profundamente do que qualquer outra raça. A memória de amores perdidos, de florestas derrubadas e de eras de ouro que se foram pode levar um elfo à melancolia e a um isolamento profundo. Eles guardam ressentimentos por séculos e lutam para perdoar as transgressões das raças mais jovens, que veem como impetuosas e destrutivas.
        """,
        "detalhes_culturais": """
**Sociedade e Governo:** A sociedade élfica é governada por conselhos de anciãos e monarcas cuja linhagem remonta a milhares de anos. A tradição e o precedente são extremamente importantes. A honra é medida não por atos de bravura impulsiva, mas por sabedoria, arte e domínio de uma habilidade ao longo de décadas.
**Religião:** Os elfos veneram os deuses da natureza e da magia, muitas vezes vendo-os como ancestrais divinos em vez de mestres distantes. Seus rituais estão ligados aos ciclos das estações e das luas.
**Arte:** Para os elfos, a arte é vida. Poesia, música, escultura e magia são vistas como facetas da mesma busca pela beleza e pela perfeição. Cada objeto que um elfo cria, de uma simples tigela a uma espada encantada, é uma obra de arte.
        """,
        "modificadores_stats": {"destreza": 2, "inteligencia": 1, "constituicao": -1},
        "habilidades_raciais": ["visao_no_escuro", "afinidade_arcana"],
        "variacoes": [
            {"nome": "Alto Elfo", "descricao": "Focados no estudo da magia, vivem em cidades magníficas e se consideram a elite da raça élfica.", "modificadores_stats": {"inteligencia": 1}},
            {"nome": "Elfo da Floresta", "descricao": "Reclusos e selvagens, são mestres da caça e da furtividade, vivendo em total harmonia com a natureza.", "modificadores_stats": {"destreza": 1}},
            {"nome": "Elfo Negro (Drow)", "descricao": "Exilados no subterrâneo há eras, são uma sociedade matriarcal cruel, conhecida por sua maestria com venenos e magia sombria.", "modificadores_stats": {"sabedoria": 1, "carisma": -1}}
        ],
        "dialogo_racial": ["Que as estrelas guiem seu caminho.", "O que a pressa lhe trará além de um túmulo precoce?", "Sinta a magia no ar.", "Nossas memórias são mais longas que a história do seu povo."],
        "nomes_sugeridos": {"masculino": ["Aelar", "Laeron", "Erevan", "Faelar"], "feminino": ["Lyra", "Aranel", "Galadrielle", "Naivara"], "familia": ["Moonshadow", "Starfall", "Whisperwind"]},
        "relacionamento_racas": {
            "humano": "Paternalista - 'Eles queimam tão intensamente, mas por tão pouco tempo. Uma pena.'",
            "anao": "Neutro - 'Eles destroem a beleza da pedra para fazer suas caixas. Mas seu artesanato é... durável.'",
            "orc": "Inimizade - 'Uma zombaria da forma élfica. Uma raça quebrada que só entende a força.'"
        },
        "arvore_evolucao": {"elfo_eterno": {"nome": "Elfo Eterno", "requisitos": "Nível 70, beber da 'Fonte das Eras'.", "descricao": "Um elfo que transcendeu o ciclo da vida, tornando-se um com a magia do mundo."}}
    },

    # =================================== ANÃO ===================================
    "anao": {
        "nome": "Anão",
        "descricao": "Mestres artesãos e guerreiros robustos que habitam vastas cidades subterrâneas, conhecidos por sua honra, teimosia e amor por ouro e cerveja.",
        "lore": """
'Das profundezas da terra nós viemos, e para a terra nós retornamos.' Este é um antigo provérbio anão que encapsula sua existência. Os anões são um povo nascido da pedra, moldado pelo calor da forja e temperado pela pressão das montanhas. Suas cidades são monumentos de engenharia e alvenaria, escavadas nas raízes do mundo, com salões tão vastos que poderiam conter cidades humanas inteiras.

A sociedade anã é construída sobre três pilares: o clã, a forja e a honra. A lealdade a um clã é absoluta, e a palavra de um anão é seu bem mais precioso. Quebrar um juramento é o pior crime imaginável. Eles são teimosos como a montanha que habitam, uma característica que os torna guerreiros formidáveis e negociadores frustrantes.

Seu amor pelo ouro e pedras preciosas não é mera ganância. Para um anão, esses materiais representam a beleza pura e duradoura do coração da terra. Eles veem a si mesmos como os guardiões desses tesouros, e seu maior talento é transformá-los em objetos de poder e beleza incomparáveis. Um machado anão não é apenas uma arma; é o legado de uma geração de ferreiros.

Em combate, os anões são a infantaria pesada por excelência. Lentos, mas implacáveis, eles formam uma parede de escudos que poucas forças podem quebrar. Preferem machados pesados, martelos de guerra e armaduras de placas completas. Embora desconfiem da maioria das formas de 'magia élfica', eles são mestres da runa, uma forma de encantamento que ligam diretamente ao metal e à pedra.

Um anão pode parecer rude e taciturno para um estranho, mas por baixo dessa fachada rochosa há um coração leal e um amigo para toda a vida, especialmente se você compartilhar uma caneca de sua melhor cerveja com ele.
        """,
        "detalhes_culturais": """
**Sociedade e Governo:** Governados por reis que herdam o trono, mas que devem constantemente provar seu valor, os anões vivem em clãs que muitas vezes se especializam em um ofício (mineração, ferraria, joalheria). As disputas são resolvidas através de conselhos de anciãos ou, em casos extremos, em duelos de honra.
**Religião:** Os anões veneram seus ancestrais e o deus-ferreiro que, segundo a lenda, forjou a própria raça anã. Eles acreditam que as almas de seus maiores heróis residem nas veias de minério mais puro no coração da montanha.
**Tradição:** A tradição é tudo. Os anões mantêm livros de rancores, registrando cada ofensa feita ao seu clã, não importa quão pequena. Um rancor só é removido quando a dívida, muitas vezes em sangue ou ouro, é paga.
        """,
        "modificadores_stats": {"constituicao": 2, "forca": 1, "destreza": -1},
        "habilidades_raciais": ["resistencia_a_veneno", "artesao_de_pedra"],
        "variacoes": [
            {"nome": "Anão da Montanha", "descricao": "Os anões mais comuns, conhecidos por sua força e habilidade como guerreiros.", "modificadores_stats": {"forca": 1}},
            {"nome": "Anão das Colinas", "descricao": "Vivendo mais perto da superfície, são um pouco menos robustos, mas com sentidos mais aguçados.", "modificadores_stats": {"sabedoria": 1}},
            {"nome": "Anão das Profundezas", "descricao": "Uma sub-raça rara que vive nas profundezas mais perigosas, são pálidos, resistentes à magia e desconfiados de todos.", "modificadores_stats": {"constituicao": 1, "resistencia_magica": 0.1}}
        ],
        "dialogo_racial": ["Pela minha barba!", "Mantenha seus pés no chão.", "Nada como o som de um martelo na bigorna.", "Ouro de tolo não enche a barriga."],
        "nomes_sugeridos": {"masculino": ["Thorin", "Balin", "Gimli", "Durin"], "feminino": ["Helga", "Bruna", "Astrid", "Inga"], "familia": ["Ironhand", "Stonebeard", "Deepdelver"]},
        "relacionamento_racas": {
            "humano": "Amigável - 'Eles são bons clientes e, para uma raça de vida curta, alguns têm honra.'",
            "elfo": "Desconfiança - 'Eles dançam nas folhas enquanto nós trabalhamos. Magia e palavras bonitas não constroem uma fortaleza.'",
            "orc": "Ódio - 'Bestas imundas que roubam nossas minas. Não há honra neles.'"
        },
        "arvore_evolucao": {"senhor_da_runa": {"nome": "Senhor da Runa", "requisitos": "Nível 60, forjar uma 'Arma Ancestral'.", "descricao": "Um mestre artesão que aprendeu os segredos para ligar a magia primordial às suas criações."}}
    },

    # =================================== ORC ===================================
    "orc": {
        "nome": "Orc",
        "descricao": "Uma raça guerreira e tribal, forjada na dureza das terras selvagens, que valoriza a força e a honra em combate acima de tudo.",
        "lore": """
Os Orcs, ou 'Orsimer' em sua própria língua gutural, não são uma criação do mal, como as lendas dos homens e elfos costumam pregar. Eles são os filhos de Malacath, o Príncipe Daédrico da Ostracização e dos Votos Quebrados. Sua história é uma de traição e exílio. Antigamente, eram um povo élfico conhecido como Aldmer, liderados pelo seu deus-herói Trinimac. Quando o Príncipe Daédrico Boethiah enganou e devorou Trinimac, ele o excretou como uma versão corrompida de si mesmo. Os seguidores de Trinimac que testemunharam isso foram transformados junto com seu deus, sua pele dourada se tornando verde e cinza, suas feições se tornando bestiais e poderosas. Eles se tornaram os Orsimer, o 'Povo Pária'.

Expulsos de suas terras ancestrais, os orcs foram forçados a viver em fortalezas nas montanras mais inóspitas, lutando constantemente por sobrevivência. Essa luta constante moldou sua cultura. A sociedade orc é centrada na força. O chefe da fortaleza é sempre o mais forte, e qualquer um pode desafiá-lo pela liderança em um combate mortal. Suas leis são simples e brutais, conhecidas como o 'Código de Malacath'. Honra, força e união do clã são os pilares deste código.

Apesar de sua aparência intimidadora, os orcs são conhecidos por serem os melhores ferreiros de todo o continente, rivalizando e até superando os anões em sua arte. O aço orc é lendário por sua resistência e durabilidade. Eles também são mineiros incomparáveis, extraindo minérios raros das profundezas de suas montanhas.

Um orc pode parecer um bárbaro selvagem para um forasteiro, mas dentro de sua fortaleza, ele é parte de uma comunidade unida e disciplinada, com um profundo senso de honra e lealdade para com seu povo. Eles não são maus por natureza, mas são ferozes e implacáveis com aqueles que os ameaçam ou desrespeitam seu código.
        """,
        "detalhes_culturais": """
**Sociedade:** A vida orc gira em torno da fortaleza do clã. A estrutura é rigidamente hierárquica, com o chefe no topo, seguido por seus guerreiros, caçadores e ferreiros. A família é a unidade central, mas a lealdade ao clã supera os laços de sangue.
**Religião:** A vasta maioria dos orcs venera Malacath, a quem veem não como um demônio, mas como um pai severo que os testa para torná-los mais fortes. Os xamãs da fortaleza se comunicam com Malacath e os espíritos dos ancestrais.
**Metalurgia:** A forja é o coração de cada fortaleza orc. É um lugar sagrado. Um jovem orc aprende a lutar e a forjar quase ao mesmo tempo. Eles acreditam que um pedaço de si mesmos é imbuído em cada arma ou armadura que criam.
        """,
        "modificadores_stats": {"forca": 2, "constituicao": 1, "inteligencia": -1, "carisma": -1},
        "habilidades_raciais": ["furor_de_batalha"],
        "variacoes": [
            {"nome": "Orc Cinzento", "descricao": "Descendentes dos clãs mais antigos, sua pele é da cor da cinza e são conhecidos por sua fúria incontrolável.", "modificadores_stats": {"forca": 1}},
            {"nome": "Orc da Montanha", "descricao": "Adaptados às altas altitudes, são mais robustos e resistentes que seus primos.", "modificadores_stats": {"constituicao": 1}}
        ],
        "dialogo_racial": ["Sangue e trovão!", "Pela honra do clã!", "O que um forasteiro quer aqui?", "Nossas forjas queimam mais quente que o seu sol.", "A força resolve tudo."],
        "nomes_sugeridos": {"masculino": ["Grom", "Tharg", "Uruk", "Borgakh", "Durg"], "feminino": ["Ghorza", "Urzoga", "Bagra", "Sharn", "Lash"], "clã": ["-gro-Khash", "-gra-Urm", "-gro-Stonetooth"]},
        "relacionamento_racas": {
            "humano": "Neutro - 'Eles são fracos, mas numerosos. Úteis para o comércio.'",
            "elfo": "Hostil - 'Os elfos nos traíram. Nunca confie em um.'",
            "anao": "Respeito Relutante - 'Eles conhecem a pedra e o aço, como nós. Mas são teimosos.'",
            "orc": "Lealdade - 'Um orc é um irmão. O resto do mundo é nosso inimigo.'"
        },
        "arvore_evolucao": {"senhor_da_guerra": {"nome": "Senhor da Guerra Orc", "requisitos": "Nível 50, completar a 'Prova de Malacath'.", "descricao": "Um orc que se provou o mais forte de seu tempo, um avatar da vontade de Malacath."}}
    },

    # =================================== KHAJIIT ===================================
    "khajiit": {
        "nome": "Khajiit",
        "descricao": "Uma raça felina de andarilhos e comerciantes, conhecidos por sua agilidade natural, furtividade e sotaque característico.",
        "lore": """
Os Khajiit são um povo de extremos, tão mutáveis quanto as duas luas, Jone e Joda, que governam suas vidas. Vindos das terras áridas e açucaradas de Elsweyr, sua própria forma física é ditada pelas fases das luas no momento de seu nascimento, resultando em uma variedade de 'peles' que vão desde seres quase élficos até grandes felinos de caça. Esta natureza lunar os torna inerentemente adaptáveis e imprevisíveis.

A sociedade Khajiit é em grande parte nômade, organizada em caravanas que viajam pelo mundo vendendo suas mercadorias exóticas, principalmente o açúcar lunar, uma substância cristalina que é a base de sua cultura e culinária. Para um Khajiit, o comércio é uma forma de arte, e eles são negociadores astutos e perspicazes. No entanto, essa mesma astúcia, combinada com sua agilidade natural, lhes rendeu uma reputação, muitas vezes injusta, de serem ladrões e traficantes de Skooma, uma perigosa droga derivada do açúcar lunar.

Eles falam com um sotaque único, muitas vezes se referindo a si mesmos na terceira pessoa. Para um Khajiit, a vida é uma jornada cheia de histórias para contar, de tesouros para encontrar e de cochilos quentes ao sol. Eles valorizam a agilidade, a inteligência e a capacidade de sair de situações difíceis com um sorriso malicioso. Embora possam parecer despreocupados, são ferozmente leais às suas caravanas e ao seu povo, e um inimigo que subestima um Khajiit muitas vezes se encontra com uma bolsa mais leve e uma adaga nas costas.
        """,
        "detalhes_culturais": """
**As Luas:** A religião e biologia Khajiit são inseparáveis das luas. Eles acreditam que suas almas foram dadas a eles pelos deuses para proteger o mundo, e as luas ditam seu caminho. Cada fase lunar tem um significado profundo em sua cultura.
**Caravanas:** A caravana é a unidade social e política mais importante. Liderada por um chefe de caravana, ela funciona como uma cidade em movimento, com suas próprias leis, guerreiros e comerciantes. A lealdade à caravana é suprema.
**Skooma:** Embora o açúcar lunar seja uma parte benigna de sua cultura, o Skooma é sua versão corrupta e viciante. O tráfico de Skooma é uma mancha na reputação dos Khajiit, embora muitos o condenem.
        """,
        "modificadores_stats": {"destreza": 2, "carisma": 1, "forca": -1},
        "habilidades_raciais": ["garras_afiadas", "visao_noturna_superior"],
        "variacoes": [
            {"nome": "Cathay", "descricao": "A forma mais comum de Khajiit, de tamanho e forma semelhantes a um humano.", "modificadores_stats": {"destreza": 1}},
            {"nome": "Suthay-raht", "descricao": "Menores e mais ágeis que os Cathay, conhecidos por sua habilidade como ladrões.", "modificadores_stats": {"agilidade": 2, "forca": -1}},
            {"nome": "Alfiq", "descricao": "Khajiit que se assemelham a gatos domésticos, mas possuem inteligência e a capacidade de usar magia.", "modificadores_stats": {"inteligencia": 2, "constituicao": -2}}
        ],
        "dialogo_racial": ["Que seus caminhos sejam quentes.", "Este tem moedas, se aquele tiver mercadorias.", "Que as luas o guiem.", "Cuidado com o Skooma, amigo."],
        "nomes_sugeridos": {"masculino": ["J'zargo", "Ra'virr", "Dro'shan"], "feminino": ["Shavari", "Ahjara", "Ziss'r"], "prefixo": ["'J", "'Dro", "'Ra"]},
        "relacionamento_racas": {
            "argoniano": "Amigável - 'Eles conhecem os segredos do pântano, nós conhecemos os do deserto. Há respeito.'",
            "humano": "Cauteloso - 'Eles têm muito ouro, mas pouca paciência. Bons para negócios, mas mantenha sua bolsa perto.'",
            "elfo": "Desconfiança - 'Eles se acham muito importantes. Acham que sua magia é melhor que o açúcar da lua. Tolos.'"
        },
        "arvore_evolucao": {"mestre_das_caravanas": {"nome": "Mestre das Caravanas", "requisitos": "Nível 50, completar a 'Rota do Comerciante Lendário'.", "descricao": "Um Khajiit que se tornou uma lenda viva entre os comerciantes, capaz de encontrar os melhores negócios em qualquer lugar do mundo."}}
    },

    # =================================== ARGONIANO ===================================
    "argoniano": {
        "nome": "Argoniano",
        "descricao": "Uma raça reptiliana enigmática dos pântanos de Black Marsh, imunes a doenças e venenos e capazes de respirar debaixo d'água.",
        "lore": """
Os Argonianos, ou Saxhleel em sua língua nativa, são talvez a raça mais incompreendida e alienígena de todas. Nascidos dos pântanos de Black Marsh, um ambiente hostil e venenoso para a maioria das outras raças, eles são um povo moldado pela adversidade e pela resiliência. Sua fisiologia única lhes concede imunidade natural a quase todos os venenos e doenças, e a capacidade de respirar debaixo d'água lhes dá domínio total sobre seu ambiente aquático.

Sua cultura é profundamente ligada ao Hist, uma rede de árvores sencientes que funcionam como uma consciência coletiva para os Argonianos. Um Argoniano nascido longe do Hist se sente incompleto, desconectado. O Hist guia seu povo, concede-lhes visões e os chama para defender Black Marsh de invasores, algo que eles fizeram com sucesso brutal por eras. Exércitos que marcharam para seus pântanos nunca mais foram vistos.

Argonianos são mestres da guerrilha. Eles usam o ambiente a seu favor, atacando das águas turvas, usando dardos envenenados e desaparecendo na vegetação densa. Sua mentalidade é muitas vezes difícil para os forasteiros entenderem. Eles podem parecer frios e sem emoção, mas possuem um complexo sistema de lealdades tribais e um profundo respeito pela natureza e pelo ciclo da vida e da morte. Eles não constroem grandes monumentos de pedra; suas cidades são vivas, feitas de lama, juncos e da própria madeira do Hist. Eles não veem o passado ou o futuro da mesma forma que as outras raças, mas sim o presente, o agora, como a única realidade que importa.
        """,
        "detalhes_culturais": """
**O Hist:** O centro de tudo. O Hist não é um deus, mas a própria alma da raça Argoniana. Eles se comunicam com o Hist através de rituais envolvendo a seiva da árvore, que lhes dá uma conexão com todos os outros Argonianos.
**Sociedade Tribal:** Embora unidos pelo Hist, os Argonianos vivem em numerosas tribos, cada uma com seus próprios costumes e tradições. A sobrevivência da tribo é a principal prioridade.
**Guerra Silenciosa:** Os Argonianos não travam guerras de conquista. Eles travam guerras de defesa. Sua história é marcada pela resistência contra a escravidão e a invasão, tornando-os desconfiados de forasteiros.
        """,
        "modificadores_stats": {"constituicao": 2, "sabedoria": 1, "carisma": -1},
        "habilidades_raciais": ["respirar_agua", "imunidade_a_doenca_veneno", "pele_hist"],
        "variacoes": [
            {"nome": "Naga", "descricao": "Uma variação com corpos mais serpentinos, conhecidos por sua letalidade em combate.", "modificadores_stats": {"forca": 1, "destreza": 1}},
            {"nome": "Paatru", "descricao": "Argonianos com aparência de sapo, mais lentos mas incrivelmente robustos e com uma forte conexão com o Hist.", "modificadores_stats": {"constituicao": 2, "sabedoria": -1}},
        ],
        "dialogo_racial": ["O pântano provê.", "O Hist sussurra em meus pensamentos.", "Sua pele seca parece... frágil.", "O que a maré trouxe hoje?"],
        "nomes_sugeridos": {"masculino": ["Tejei", "Meer-Zish", "Deekus"], "feminino": ["Shaleez", "Kee-Ava", "Wujeeta"], "sem_familia": True},
        "relacionamento_racas": {
            "humano": "Desconfiança - 'Eles tentaram nos escravizar por séculos. Suas ambições não conhecem limites.'",
            "elfo_negro": "Ódio Profundo - 'Eles são os caçadores de escravos. Nenhum Argoniano os perdoará.'",
            "khajiit": "Neutro - 'Eles entendem o que é ser um pária. Mas seu açúcar é uma fraqueza.'"
        },
        "arvore_evolucao": {"xamã_do_hist": {"nome": "Xamã do Hist", "requisitos": "Nível 60, sobreviver ao 'Ritual da Seiva Negra'.", "descricao": "Um Argoniano que se fundiu tão completamente com o Hist que pode canalizar a vontade da floresta."}}
    },

    # =================================== GNOMO ===================================
    "gnomo": {
        "nome": "Gnomo",
        "descricao": "Uma raça pequena e incrivelmente inteligente de inventores, ilusionistas e engenheiros, obcecados com mecanismos complexos e conhecimento.",
        "lore": """
Se os anões são os mestres da matéria, os gnomos são os mestres do mecanismo e da mente. Esta raça de seres diminutos possui um intelecto que supera em muito o de qualquer outra raça. Para um gnomo, o mundo não é uma coleção de objetos, mas sim um sistema gigante e interligado, uma máquina complexa que pode ser estudada, desmontada e, com sorte, melhorada.

Eles vivem em cidades-toca escavadas em colinas e florestas, mas suas casas não são simples buracos no chão. São labirintos de engrenagens, alavancas, autômatos de relojoaria e passagens secretas, onde cada casa é uma invenção em si. A sociedade gnômica é uma meritocracia barulhenta e caótica, onde o status é ganho não por linhagem ou força, mas pela engenhosidade de suas invenções e pela profundidade de seu conhecimento.

Gnomos são curiosos por natureza, uma curiosidade que muitas vezes beira a imprudência. Eles são conhecidos por desmontar artefatos mágicos perigosos apenas para ver como funcionam, ou por testar novas poções em si mesmos com resultados... explosivos. Além de sua afinidade com a engenharia, eles são mestres natos da magia de ilusão. Eles a usam não apenas para defesa, mas para entretenimento, pregar peças e para o puro prazer de dobrar a percepção da realidade.

Apesar de seu tamanho pequeno, um gnomo nunca deve ser subestimado. Um inimigo que os ataca pode se ver preso em uma armadilha de engrenagens, enganado por um exército de clones ilusórios ou enfrentando um golem de relojoaria do tamanho de um ogro. Eles são a prova de que o cérebro, e não os músculos, é a arma mais poderosa de todas.
        """,
        "detalhes_culturais": """
**Invenção como Religião:** Os gnomos veneram Garl Glittergold, o deus da astúcia e da invenção. Para eles, criar uma nova invenção ou resolver um quebra-cabeça complexo é uma forma de oração.
**Rivalidade Amistosa (e Nem Tanto):** Gnomos mantêm uma rivalidade secular com os goblins sobre quem são os melhores inventores, embora as invenções gnômicas tendam a funcionar com mais frequência. Eles também competem com os anões para ver quem cria os melhores autômatos.
**Conhecimento Acima de Tudo:** Um gnomo pode arriscar a vida e a integridade física por uma nova peça de informação ou por um vislumbre de um mecanismo antigo e esquecido.
        """,
        "modificadores_stats": {"inteligencia": 2, "destreza": 1, "forca": -2},
        "habilidades_raciais": ["mente_mecanica", "afinidade_com_ilusao"],
        "variacoes": [
            {"nome": "Gnomo das Rochas", "descricao": "Focados na engenharia e na criação de autômatos, são os mais robustos de sua raça.", "modificadores_stats": {"constituicao": 1}},
            {"nome": "Gnomo da Floresta", "descricao": "Mestres da ilusão e da furtividade, vivem em harmonia com os animais da floresta, que muitas vezes se tornam parte de suas geringonças.", "modificadores_stats": {"carisma": 1}}
        ],
        "dialogo_racial": ["Fascinante! Como você acha que isso funciona?", "Espere, eu tenho uma ideia!", "Precisa de uma mãozinha? Ou talvez uma mão de relógio?", "Cuidado onde pisa, meu laboratório está por toda parte."],
        "nomes_sugeridos": {"masculino": ["Zook", "Boddynock", "Glim", "Wobble"], "feminino": ["Ellywick", "Nissa", "Loopmottin"], "familia": ["Cogspinner", "Fiddlewick", "Tinkerfoot"]},
        "relacionamento_racas": {
            "anao": "Amigável - 'Eles fazem coisas grandes e fortes! Nós as fazemos pequenas e inteligentes. Podemos aprender um com o outro.'",
            "humano": "Curiosidade - 'Eles constroem coisas tão rápido! Pena que quebram com a mesma velocidade.'",
            "goblin": "Rivalidade - 'Ladrões de ideias! E suas invenções sempre explodem. Quase sempre.'"
        },
        "arvore_evolucao": {"mestre_artifice": {"nome": "Mestre Artífice", "requisitos": "Nível 60, construir o 'Autômato Supremo'.", "descricao": "Um gnomo cuja mente se tornou uma com a própria arte da criação, capaz de construir maravilhas mecânicas."}}
    },

    # =================================== AASIMAR ===================================
    "aasimar": {
        "nome": "Aasimar",
        "descricao": "Seres humanos com uma herança celestial, destinados a serem campeões do bem e da ordem, possuindo uma luz interior que pode inspirar ou purificar.",
        "lore": """
Os Aasimar são os 'tocados pelos céus'. Em algum ponto de sua linhagem, um de seus ancestrais teve um encontro com um ser celestial - um anjo, um arconte ou outra criatura do bem. Essa herança divina permanece adormecida por gerações, até que se manifesta em um recém-nascido, que carrega as marcas de sua ascendência: olhos que brilham como ouro líquido, cabelos com um brilho metálico ou uma aura de paz quase palpável.

Criados entre os mortais, os Aasimar muitas vezes se sentem como estranhos. Eles são guiados por um senso inato de justiça e compaixão, e muitas vezes recebem visões e sussurros de seus guias celestiais, que os impelem a lutar contra o mal. Eles são faróis de esperança em um mundo sombrio, destinados a grandes feitos. No entanto, esse destino é um fardo pesado. A pressão para serem perfeitos, para sempre fazerem a coisa certa, pode levar um Aasimar a uma profunda angústia ou a uma rebelião severa contra a própria natureza que os define.
        """,
        "detalhes_culturais": """
**O Guia Celestial:** Cada Aasimar tem um guia celestial que se comunica com eles, geralmente em sonhos. Este guia atua como um mentor e uma consciência, mas sua orientação nem sempre é clara.
**O Fardo da Virtude:** A sociedade muitas vezes espera que os Aasimar sejam santos perfeitos, uma expectativa impossível que pode causar grande sofrimento psicológico.
**Conflito Interno:** Um Aasimar que se desvia do caminho da retidão sente um conflito interno profundo, pois sua própria alma anseia pelo bem.
        """,
        "modificadores_stats": {"sabedoria": 2, "carisma": 1},
        "habilidades_raciais": ["resistencia_celestial", "toque_curativo"],
        "variacoes": [
            {"nome": "Aasimar Protetor", "descricao": "Destinados a serem os guardiões dos fracos, podem manifestar asas de luz.", "modificadores_stats": {"forca": 1}},
            {"nome": "Aasimar Flagelado", "descricao": "Carregam uma energia celestial tão poderosa que ela vaza, causando dano a si mesmos e aos outros.", "modificadores_stats": {"constituicao": 1}},
            {"nome": "Aasimar Caído", "descricao": "Um Aasimar que se voltou para as trevas, transformando sua luz interior em uma chama necrótica.", "modificadores_stats": {"inteligencia": 1}}
        ],
        "dialogo_racial": ["Que a luz guie suas ações.", "Eu sinto uma grande escuridão neste lugar.", "Não teste minha paciência, criatura do mal.", "Todos merecem uma chance de redenção."],
        "nomes_sugeridos": {"masculino": ["Valerius", "Seraphiel", "Mikael"], "feminino": ["Celestia", "Sariel", "Laila"], "familia": ["Lightbringer", "Sunstrider"]},
        "relacionamento_racas": {
            "tiefling": "Piedade e Rivalidade - 'Eles são o espelho sombrio de nós mesmos. Uma alma para ser salva ou um mal a ser purgado.'",
            "humano": "Protetorado - 'Eles são o rebanho que devemos guiar e proteger.'",
            "clerigo": "Afinidade - 'Nós compartilhamos um propósito, se não a mesma fonte de poder.'"
        },
        "arvore_evolucao": {"anjo_encarnado": {"nome": "Anjo Encarnado", "requisitos": "Nível 70, completar a 'Ascensão Celestial'.", "descricao": "Um Aasimar que abraçou completamente sua herança, tornando-se um mortal com o poder de um anjo."}}
    },

    # =================================== TIEFLING ===================================
    "tiefling": {
        "nome": "Tiefling",
        "descricao": "Seres humanos com uma herança infernal, marcados por traços demoníacos e uma afinidade com o fogo e as sombras. Lutam para encontrar seu lugar em um mundo que os teme.",
        "lore": """
Onde os Aasimar são tocados pelos céus, os Tieflings são manchados pelos infernos. Em algum ponto de seu passado, um de seus ancestrais fez um pacto com um demônio, e essa mácula infernal ecoa através das gerações. Um Tiefling nasce parecendo humano, mas logo desenvolve as marcas de sua herança: pequenos chifres, uma cauda preênsil, olhos de fogo ou uma pele de cor anormal.

A sociedade os vê com medo e desconfiança. Eles são frequentemente confundidos com adoradores de demônios ou monstros, e são forçados a viver nas margens da sociedade, em guetos ou como párias. Essa desconfiança constante molda sua personalidade. Tieflings tendem a ser cínicos, sarcásticos e autossuficientes. Eles não confiam em ninguém, porque o mundo nunca lhes deu uma razão para confiar.

Apesar de sua herança, os Tieflings não são inerentemente maus. O sangue infernal lhes dá poder sobre o fogo e as trevas, mas a escolha de como usar esse poder é inteiramente deles. Muitos lutam contra sua própria natureza e contra os preconceitos do mundo para se tornarem heróis, talvez os mais improváveis de todos. Outros abraçam a escuridão, tornando-se os monstros que o mundo sempre disse que eles eram. A jornada de um Tiefling é uma de autodefinição, uma luta constante para provar que eles são mais do que o sangue que corre em suas veias.
        """,
        "detalhes_culturais": """
**A Mácula:** A aparência de um Tiefling varia muito, dependendo do demônio específico em sua linhagem. Alguns podem ter traços sutis, enquanto outros são abertamente monstruosos.
**Autossuficiência:** Forçados a se virar sozinhos, os Tieflings são mestres da sobrevivência urbana, muitas vezes se tornando ladrões, espiões ou mercenários.
**Nomes Virtuosos:** Muitos Tieflings adotam nomes que representam uma virtude (Esperança, Glória, Tormento) como um lembrete de sua luta pessoal ou como um ato de desafio contra o mundo.
        """,
        "modificadores_stats": {"inteligencia": 1, "carisma": 2},
        "habilidades_raciais": ["resistencia_infernal", "magia_das_sombras"],
        "variacoes": [
            {"nome": "Tiefling de Asmodeus", "descricao": "Descendentes do arquidemônio da tirania, são mestres da manipulação e do fogo.", "modificadores_stats": {"inteligencia": 1}},
            {"nome": "Tiefling de Zariel", "descricao": "Com sangue de um anjo caído, são guerreiros formidáveis com poder sobre o fogo divino e infernal.", "modificadores_stats": {"forca": 1}},
            {"nome": "Tiefling de Dispater", "descricao": "Descendentes do lorde do engano, são espiões e infiltradores natos, com poder sobre as sombras.", "modificadores_stats": {"destreza": 1}}
        ],
        "dialogo_racial": ["O que você está olhando?", "Confiança é para os tolos.", "O inferno está vazio e todos os demônios estão aqui.", "Eu faço meu próprio destino."],
        "nomes_sugeridos": {"masculino": ["Akmenos", "Damakos", "Kairon"], "feminino": ["Akta", "Rieta", "Kallista"], "virtude": ["Esperança", "Tormento", "Desafio"]},
        "relacionamento_racas": {
            "aasimar": "Inveja e Desdém - 'Eles não sabem o que é lutar. A vida lhes foi dada em uma bandeja de prata.'",
            "humano": "Ressentimento - 'Eles nos temem e nos odeiam, mas são rápidos em pedir nossa ajuda quando a escuridão chega.'",
            "demonio": "Medo e Ódio - 'Eu sou mais do que meu sangue. Eu nunca serei como eles.'"
        },
        "arvore_evolucao": {"lorde_demonio_renegado": {"nome": "Lorde Demônio Renegado", "requisitos": "Nível 70, derrotar seu ancestral demoníaco.", "descricao": "Um Tiefling que dominou sua herança infernal, roubando o poder de seu ancestral para si mesmo."}}
    },

    # =================================== GOLIATH ===================================
    "goliath": {
        "nome": "Goliath",
        "descricao": "Uma raça nômade de humanoides gigantescos que vivem nos picos das montanhas mais altas, valorizando a competição e a autossuficiência.",
        "lore": """
Os Golias são um povo esculpido pelo vento e pelo gelo dos picos das montanhas. Eles vivem em uma sociedade tribal onde a competição justa é o alicerce de tudo. Para um Golias, a vida é uma grande competição, e eles se esforçam para superar não apenas seus rivais, mas a si mesmos, todos os dias. Eles veem a derrota como uma lição para se tornarem mais fortes, e a vitória como uma prova temporária de seu valor.

Sua fisiologia é adaptada à vida em grandes altitudes. Eles são altos e musculosos, com uma resistência incrível ao frio e ao ar rarefeito. A pele deles é muitas vezes cinzenta e manchada, coberta de litografias - tatuagens que contam a história de seus feitos e de sua família.

Os Golias são um povo justo, mas direto. Eles não têm paciência para enganos ou diplomacia complicada. Eles dizem o que pensam e esperam o mesmo dos outros. Sua obsessão com a competição se estende a tudo, desde beber e contar histórias até caçar e lutar. Eles são aliados poderosos e confiáveis, desde que você possa provar seu valor para eles.
        """,
        "detalhes_culturais": """
**A Competição:** Tudo é uma competição. Manter um placar de seus feitos é uma obsessão nacional.
**Autossuficiência:** Cada membro da tribo deve ser capaz de contribuir para a sobrevivência do grupo. A fraqueza não é tolerada.
**Hospitalidade da Montanha:** Apesar de sua natureza competitiva, eles são hospitaleiros com aqueles que enfrentam os perigos de suas casas nas montanhas, pois respeitam a força necessária para chegar até eles.
        """,
        "modificadores_stats": {"forca": 2, "constituicao": 1},
        "habilidades_raciais": ["resistencia_da_montanha", "forca_do_gigante"],
        "variacoes": [],
        "dialogo_racial": ["Você é forte o suficiente para esta montanha?", "Prove seu valor!", "Hoje é um bom dia para um desafio.", "O eco é a única testemunha de nossas batalhas."],
        "nomes_sugeridos": {"masculino": ["Keothi", "Numea", "Thotham"], "feminino": ["Gae-Al", "Kuori", "Manneo"], "clã": ["Akannathi", "Gathakanathi"]},
        "relacionamento_racas": {
            "anao": "Respeito - 'Eles conhecem a montanha. Eles são fortes. Bons competidores.'",
            "gnomo": "Confusão - 'Pequenos e fracos, mas suas geringonças são... intrigantes. Uma competição estranha.'",
            "humano": "Neutro - 'Eles sobem nossas montanhas em busca de glória. Poucos são dignos.'"
        },
        "arvore_evolucao": {"avatar_da_montanha": {"nome": "Avatar da Montanha", "requisitos": "Nível 60, sobreviver à 'Avalanche Eterna'.", "descricao": "Um Golias que se tornou um com o espírito da montanha, sua pele tão dura quanto a rocha."}}
    },

    # =================================== HALFLING ===================================
    "halfling": {
        "nome": "Halfling",
        "descricao": "Um povo pequeno e alegre que valoriza os confortos do lar, uma boa refeição e a companhia de amigos. Surpreendentemente corajosos e sortudos.",
        "lore": """
Os Halflings são o coração caloroso do mundo. Eles não buscam poder, glória ou riqueza. Em vez disso, encontram alegria nas coisas simples da vida: um jardim bem cuidado, uma despensa cheia, uma canção alegre e um cachimbo para fumar ao lado da lareira. Suas casas são tocas aconchegantes e confortáveis, construídas nas encostas de colinas verdejantes.

Apesar de sua aversão ao perigo e ao desconforto, os Halflings possuem uma coragem surpreendente quando seus lares e entes queridos estão ameaçados. Eles também são abençoados com uma sorte inexplicável, muitas vezes escapando de perigos mortais por um triz. Embora prefiram uma vida pacífica, o espírito de aventura ocasionalmente chama um Halfling para o mundo, onde sua sorte, furtividade e otimismo inabalável os tornam companheiros valiosos.
        """,
        "detalhes_culturais": """
**Comunidade:** A vida Halfling é centrada na comunidade. Famílias inteiras vivem juntas em vilarejos unidos, onde todos se conhecem e se ajudam.
**Conforto:** O conforto é a maior virtude. Uma cama macia, uma refeição quente e um bom livro são as maiores ambições de um Halfling.
**Sorte Inata:** Os Halflings têm uma habilidade sobrenatural de evitar o perigo, uma sorte que eles mesmos não entendem, mas da qual dependem.
        """,
        "modificadores_stats": {"destreza": 2, "carisma": 1, "forca": -2},
        "habilidades_raciais": ["sorte_dos_pequenos", "furtividade_natural"],
        "variacoes": [
            {"nome": "Pés Leves", "descricao": "Especialmente adeptos a se esconder, até mesmo atrás de outras criaturas.", "modificadores_stats": {"carisma": 1}},
            {"nome": "Robustos", "descricao": "Descendentes de Halflings que tiveram contato com anões, são mais resistentes a venenos.", "modificadores_stats": {"constituicao": 1}}
        ],
        "dialogo_racial": ["Hora do segundo café da manhã!", "Uma aventura? Parece desconfortável.", "Cuidado para não pisar nas minhas flores!", "Vamos resolver isso com uma boa torta."],
        "nomes_sugeridos": {"masculino": ["Pippin", "Merry", "Samwise"], "feminino": ["Rosie", "Belladonna", "Ruby"], "familia": ["Goodbarrel", "Took", "Brandybuck"]},
        "relacionamento_racas": {
            "anao": "Amigável - 'Eles fazem ótimas cervejas e contam boas histórias, embora sejam um pouco barulhentos.'",
            "humano": "Amigável - 'São tão grandes e apressados, mas têm bom coração.'",
            "elfo": "Respeito - 'Eles fazem lindas músicas, mas não comem o suficiente.'"
        },
        "arvore_evolucao": {}
    },

    # =================================== MEIO-ELFO ===================================
    "meio_elfo": {
        "nome": "Meio-Elfo",
        "descricao": "Presos entre dois mundos, os Meio-Elfos combinam a curiosidade humana com a graça élfica, mas muitas vezes não se sentem pertencentes a nenhum dos dois.",
        "lore": """
Os Meio-Elfos são o resultado da união, muitas vezes rara e transitória, entre um humano e um elfo. Eles herdam a beleza e os sentidos aguçados de sua herança élfica e a ambição e adaptabilidade de sua herança humana. No entanto, esta dualidade é tanto uma bênção quanto uma maldição.

Eles vivem mais que os humanos, mas muito menos que os elfos. Para os humanos, eles são um lembrete da passagem do tempo, vendo amigos e familiares envelhecerem e morrerem. Para os elfos, eles são impetuosos e impacientes, um flash na longa existência élfica. Como resultado, muitos Meio-Elfos se sentem como párias, nunca totalmente aceitos em nenhuma das duas sociedades. Isso os torna excelentes diplomatas, mediadores e viajantes, pois aprendem desde cedo a navegar entre diferentes culturas e pontos de vista.
        """,
        "modificadores_stats": {"carisma": 2, "destreza": 1, "inteligencia": 1},
        "habilidades_raciais": ["heranca_feerica", "habilidade_versatil"],
        "variacoes": [],
        "dialogo_racial": ["Eu vejo o mundo com os olhos de dois povos.", "Não pertenço a lugar nenhum, então pertenço a todos os lugares.", "A beleza da vida está em sua transitoriedade."],
        "nomes_sugeridos": {"masculino": ["Alaric", "Faelan", "Tanner"], "feminino": ["Lyra", "Seraphina", "Elara"], "familia": []},
        "relacionamento_racas": {
            "humano": "Compreensão e Melancolia - 'Eu os amo, mas vê-los partir é uma dor constante.'",
            "elfo": "Anseio e Frustração - 'Eu admiro sua graça, mas sua indiferença ao mundo que muda me irrita.'"
        },
        "arvore_evolucao": {}
    },

    # =================================== MEIO-ORC ===================================
    "meio_orc": {
        "nome": "Meio-Orc",
        "descricao": "Combinando a força física dos orcs com a ambição humana, os Meio-Orcs são guerreiros poderosos que vivem para provar seu valor.",
        "lore": """
Nascidos da união, raramente feliz, entre humanos e orcs, os Meio-Orcs são muitas vezes párias de ambas as sociedades. Para os humanos, eles são monstros. Para os orcs, são fracos. Essa rejeição os força a desenvolver uma força interior e uma determinação feroz. Eles vivem para provar que são mais do que a soma de suas partes.

Um Meio-Orc é impulsionado por uma necessidade de aceitação, seja através de feitos de força incríveis, de uma lealdade inabalável a seus companheiros ou de uma liderança brutal. Eles canalizam a fúria de seu sangue orc com a disciplina que aprendem no mundo dos homens, tornando-se guerreiros e bárbaros temíveis em batalha.
        """,
        "modificadores_stats": {"forca": 2, "constituicao": 1},
        "habilidades_raciais": ["ataques_selvagens", "resistencia_implacavel"],
        "variacoes": [],
        "dialogo_racial": ["Eu vou te mostrar o que é força!", "Meu sangue ferve para a batalha.", "Não sou nem um nem outro. Eu sou eu mesmo."],
        "nomes_sugeridos": {"masculino": ["Thokk", "Grol", "Murg"], "feminino": ["Bree", "Yevelda", "Shautha"], "familia": []},
        "relacionamento_racas": {
            "humano": "Desconfiança - 'Eles me julgam pela minha aparência antes de conhecerem meu coração.'",
            "orc": "Desprezo e Anseio - 'Eu nunca serei forte o suficiente para eles, mas vou tentar mesmo assim.'"
        },
        "arvore_evolucao": {}
    },

    # =================================== DRACONATO ===================================
    "draconato": {
        "nome": "Draconato",
        "descricao": "Uma raça de humanoides dracônicos que valorizam a honra e a maestria de seu sopro elemental, um legado de seus ancestrais dragões.",
        "lore": """
Os Draconatos nasceram dos ovos dos dragões, moldados pelos deuses para combinar as melhores qualidades dos dragões e dos humanoides. Eles são uma raça orgulhosa, que vive em clãs que valorizam a honra acima de tudo. Quebrar um juramento é a maior desonra imaginável.

Cada Draconato carrega dentro de si o poder elemental de seu ancestral dracônico - seja fogo, gelo, ácido, veneno ou raio. Essa energia se manifesta em uma arma de sopro devastadora. Eles são guerreiros e feiticeiros naturais, e sua lealdade a seus companheiros é lendária.
        """,
        "modificadores_stats": {"forca": 2, "carisma": 1},
        "habilidades_raciais": ["arma_de_sopro", "resistencia_draconica"],
        "variacoes": [
            {"nome": "Draconato Vermelho (Fogo)", "descricao": "Descendentes de dragões vermelhos, são orgulhosos e seu sopro é de fogo.", "modificadores_stats": {}},
            {"nome": "Draconato Azul (Raio)", "descricao": "Descendentes de dragões azuis, são estratégicos e seu sopro é de raio.", "modificadores_stats": {}},
            {"nome": "Draconato Branco (Gelo)", "descricao": "Descendentes de dragões brancos, são caçadores solitários e seu sopro é de gelo.", "modificadores_stats": {}}
        ],
        "dialogo_racial": ["Pela honra do meu clã!", "Sinta a fúria dos dragões!", "Minha palavra é meu vínculo."],
        "nomes_sugeridos": {"masculino": ["Arjhan", "Balasar", "Torinn"], "feminino": ["Akra", "Harann", "Sora"], "clã": ["Clethtinthiallor", "Kerrhylon"]},
        "relacionamento_racas": {
            "humano": "Neutro - 'Sua ambição é interessante, mas sua falta de honra é decepcionante.'",
            "elfo": "Respeito - 'Eles são antigos e sábios, como nossos ancestrais.'"
        },
        "arvore_evolucao": {}
    },

    # =================================== GENASI ===================================
    "genasi": {
        "nome": "Genasi",
        "descricao": "Descendentes de gênios dos planos elementais, os Genasi são manifestações físicas dos elementos, como fogo, água, terra ou ar.",
        "lore": """
Os Genasi são raros, resultado da união de um mortal com um gênio. Eles não são uma raça unificada, mas sim indivíduos espalhados pelo mundo, cada um uma manifestação de seu elemento parental. Um Genasi do Fogo pode ter cabelo que dança como chamas, enquanto um Genasi da Água pode ter pele que brilha com umidade.

Eles são tão variados em personalidade quanto os elementos que representam. Genasi do Fogo são passionais e impetuosos. Genasi da Água são calmos e flexíveis. Genasi da Terra são estoicos e resilientes. Genasi do Ar são livres e distantes. Eles são a personificação do poder elemental bruto, lutando para equilibrar sua natureza mortal com a energia caótica que flui dentro deles.
        """,
        "modificadores_stats": {"constituicao": 2},
        "habilidades_raciais": ["poder_elemental"],
        "variacoes": [
            {"nome": "Genasi do Fogo", "descricao": "Impacientes e orgulhosos, com afinidade com o fogo.", "modificadores_stats": {"inteligencia": 1}},
            {"nome": "Genasi da Água", "descricao": "Calmos e perceptivos, com afinidade com a água.", "modificadores_stats": {"sabedoria": 1}},
            {"nome": "Genasi da Terra", "descricao": "Fortes e determinados, com afinidade com a terra.", "modificadores_stats": {"forca": 1}},
            {"nome": "Genasi do Ar", "descricao": "Livres e astutos, com afinidade com o ar.", "modificadores_stats": {"destreza": 1}}
        ],
        "dialogo_racial": ["Sinta o poder da tempestade!", "Eu sou um com o fogo.", "A terra me dá força."],
        "nomes_sugeridos": {"masculino": ["Ignis", "Aero", "Triton"], "feminino": ["Terra", "Aqua", "Cinder"], "familia": []},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== POVO-LAGARTO ===================================
    "povo_lagarto": {
        "nome": "Povo-Lagarto",
        "descricao": "Uma raça reptiliana primitiva e pragmática que vive em pântanos e pântanos. Eles veem o mundo através de uma lente de sobrevivência e necessidade.",
        "lore": """
Diferente de seus primos mais misticamente inclinados, os Argonianos, o Povo-Lagarto é um estudo em pragmatismo reptiliano. Sua cultura é antiga, mas não avançada. Eles não constroem cidades; eles formam ninhos. Eles não forjam aço; eles usam ossos, pedras e obsidiana para criar suas ferramentas e armas. Sua mentalidade é desprovida de emoção como as outras raças a entendem. Para eles, um companheiro caído não é uma fonte de tristeza, mas uma fonte de alimento. Um inimigo não é odiado, mas visto como uma ameaça ou uma oportunidade.

Eles são caçadores e sobreviventes natos. Sua pele escamosa lhes oferece uma armadura natural, e eles podem prender a respiração por longos períodos. Eles são mestres em usar o ambiente a seu favor, criando armadilhas e emboscadas com uma paciência que só um predador de sangue frio pode possuir.
        """,
        "detalhes_culturais": """
**Sobrevivência Acima de Tudo:** A única lei é a da natureza. O forte sobrevive, o fraco é comido.
**Mente Alienígena:** Emoções como amor, ódio ou ganância são conceitos estranhos. As decisões são tomadas com base na lógica fria da sobrevivência.
**Artesanato com Ossos:** Eles podem criar armas e armaduras surpreendentemente eficazes a partir dos restos de suas presas.
        """,
        "modificadores_stats": {"constituicao": 2, "sabedoria": 1},
        "habilidades_raciais": ["mordida_poderosa", "armadura_natural", "prender_a_respiração"],
        "variacoes": [],
        "dialogo_racial": ["Você é comida ou ameaça?", "O pântano não se importa com seus sentimentos.", "Desperdício é ilógico."],
        "nomes_sugeridos": {"masculino": ["Sark", "Veth", "Gresh"], "feminino": ["Asha", "Zez", "Rassi"], "sem_familia": True},
        "relacionamento_racas": {
            "argoniano": "Curiosidade - 'Eles se parecem conosco, mas pensam de forma estranha. Falam com árvores.'",
            "humano": "Presa - 'Carne macia. Lentos. Fáceis de caçar.'"
        },
        "arvore_evolucao": {}
    },

    # =================================== LOXODON ===================================
    "loxodon": {
        "nome": "Loxodon",
        "descricao": "Gigantes humanoides com a aparência de elefantes, os Loxodontes são um povo calmo, sábio e incrivelmente forte. São os pacificadores e os pilares de suas comunidades.",
        "lore": """
Os Loxodontes são uma visão imponente. Sua pele grossa e enrugada e suas presas de marfim os tornam fortalezas ambulantes. No entanto, por baixo dessa aparência formidável, há uma alma gentil e ponderada. Eles são um povo de profunda sabedoria e paciência infinita. Um Loxodonte raramente se apressa, preferindo considerar todos os ângulos de um problema antes de agir com uma força calma e deliberada.

Eles são artesãos da pedra e da madeira, criando estruturas e obras de arte que são tão duráveis e impressionantes quanto eles próprios. Em tempos de paz, são conselheiros e mediadores. Em tempos de guerra, são a linha de frente inabalável, capazes de dispersar exércitos com sua força e resistência.
        """,
        "modificadores_stats": {"constituicao": 2, "sabedoria": 1},
        "habilidades_raciais": ["serenidade_loxodon", "pele_grossa", "tronco_preênsil"],
        "variacoes": [],
        "dialogo_racial": ["A paciência é uma virtude.", "Vamos pensar sobre isso com calma.", "Um carvalho não cresce da noite para o dia."],
        "nomes_sugeridos": {"masculino": ["Vajra", "Ganesh", "Bodhi"], "feminino": ["Indira", "Lakshmi", "Radha"], "familia": []},
        "relacionamento_racas": {
            "anao": "Respeito - 'Eles também conhecem o valor da paciência e do trabalho duro.'",
            "gnomo": "Diversão - 'Suas mentes são rápidas, mas suas invenções são frágeis.'"
        },
        "arvore_evolucao": {}
    },

    # =================================== AARAKOCRA ===================================
    "aarakocra": {
        "nome": "Aarakocra",
        "descricao": "Humanoides semelhantes a pássaros que vivem em ninhos nos picos das montanhas mais altas ou no Plano Elemental do Ar. Valorizam a liberdade e o céu aberto.",
        "lore": """
Os Aarakocra são os filhos do céu. Com asas majestosas e corpos leves, eles passam a maior parte de suas vidas voando pelos céus. O mundo abaixo é muitas vezes visto como um lugar estranho e confinador. Eles têm uma perspectiva única, vendo os problemas do mundo de cima, o que lhes dá uma visão estratégica, mas também um certo distanciamento.

Eles são claustrofóbicos por natureza e se sentem desconfortáveis em masmorras ou cavernas. Em combate, preferem atacar de cima, usando lanças ou arcos para atingir seus inimigos antes de subir novamente para a segurança do céu.
        """,
        "modificadores_stats": {"destreza": 2, "sabedoria": 1},
        "habilidades_raciais": ["voo", "ataque_de_mergulho"],
        "variacoes": [],
        "dialogo_racial": ["Que o vento esteja sempre sob suas asas.", "O chão é para os que não podem voar.", "Eu vejo tudo lá de cima."],
        "nomes_sugeridos": {"masculino": ["Aial", "Kleeck", "Skree"], "feminino": ["Aera", "Sora", "Noori"], "sem_familia": True},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== TABAXI ===================================
    "tabaxi": {
        "nome": "Tabaxi",
        "descricao": "Uma raça felina de andarilhos curiosos, obcecados por histórias, conhecimento e artefatos interessantes. São ágeis e carismáticos.",
        "lore": """
Diferente dos Khajiit, que são comerciantes por natureza, os Tabaxi são movidos por uma curiosidade insaciável. Eles são compelidos por uma divindade felina a vagar pelo mundo e coletar histórias, canções, artefatos e experiências interessantes. Um Tabaxi pode passar anos em uma biblioteca estudando um tomo antigo ou arriscar a vida para ver uma cachoeira lendária.

Eles são ágeis e rápidos, capazes de se mover com uma graça felina. Sua curiosidade os torna excelentes ladinos e bardos, sempre em busca da próxima grande aventura ou do próximo grande segredo. Quando sua curiosidade sobre um tópico é satisfeita, eles geralmente partem para a próxima obsessão, tornando-os companheiros de viagem fascinantes, mas muitas vezes pouco confiáveis.
        """,
        "modificadores_stats": {"destreza": 2, "carisma": 1},
        "habilidades_raciais": ["agilidade_felina", "garras_de_gato"],
        "variacoes": [],
        "dialogo_racial": ["O que é isso? Parece interessante!", "Eu ouvi uma história sobre este lugar...", "A curiosidade é o caminho para o conhecimento."],
        "nomes_sugeridos": {"masculino": ["River", "Flicker", "Smoke"], "feminino": ["Willow", "Tale", "Breeze"], "clã": ["of the Whiskers", "of the Swift Paw"]},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== KENKU ===================================
    "kenku": {
        "nome": "Kenku",
        "descricao": "Uma raça de humanoides-corvo amaldiçoados que perderam suas asas e sua voz. Eles só podem se comunicar através da mímica perfeita de sons que já ouviram.",
        "lore": """
A história dos Kenku é uma tragédia. Antigamente, eles eram os servos alados de uma poderosa entidade de outro plano. Cobiçando o poder de seu mestre, eles tentaram roubar os segredos da criação. Como punição, seu mestre os amaldiçoou de três maneiras: tirou suas asas, para que nunca mais pudessem voar livremente; tirou sua criatividade, para que nunca mais pudessem criar algo novo; e tirou sua voz, forçando-os a apenas imitar os sons que ouvem.

Agora, os Kenku vagam pelo mundo como párias, muitas vezes trabalhando em guildas de ladrões ou como mensageiros, onde sua habilidade de mímica é útil. Eles anseiam por voar novamente e sonham em um dia encontrar uma maneira de quebrar sua maldição. Eles se comunicam através de um mosaico de sons que coletaram ao longo de suas vidas - o som de uma moeda caindo, o rangido de uma porta, um trecho de uma canção ouvida em uma taverna.
        """,
        "modificadores_stats": {"destreza": 2, "sabedoria": 1},
        "habilidades_raciais": ["mimica_perfeita", "falsificação_kenku"],
        "variacoes": [],
        "dialogo_racial": ["(O som de moedas caindo)", "(O som de uma espada sendo desembainhada)", "(Um trecho de uma canção triste)"],
        "nomes_sugeridos": {"masculino": ["Chirp", "Squeak", "Rattle"], "feminino": ["Flutter", "Whistle", "Click"], "sem_familia": True},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== SHADAR-KAI ===================================
    "shadar-kai": {
        "nome": "Shadar-kai",
        "descricao": "Elfos sombrios e niilistas ligados ao Pendor das Sombras (Shadowfell), mestres do teletransporte e da melancolia.",
        "lore": """
Os Shadar-kai eram elfos que seguiram a Rainha Corvo para o Pendor das Sombras, um plano de escuridão e desespero. A energia sombria do plano os infundiu, drenando a cor de suas peles e cabelos e esvaziando suas emoções. Para um Shadar-kai, a vida é uma série de experiências extremas para sentir algo, qualquer coisa, para combater a apatia que os consome. Eles são acrobatas e guerreiros incríveis, capazes de se teleportar através das sombras, tornando-os adversários imprevisíveis e mortais.
        """,
        "modificadores_stats": {"destreza": 2, "constituicao": 1},
        "habilidades_raciais": ["bencao_da_rainha_corvo", "resistencia_necrotica"],
        "variacoes": [],
        "dialogo_racial": ["A emoção é uma fraqueza.", "A morte é apenas o começo.", "Eu já vi o fim de todas as coisas."],
        "nomes_sugeridos": {"masculino": ["Kael", "Riven", "Zane"], "feminino": ["Lyra", "Seraphina", "Elara"], "familia": []},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== GITH ===================================
    "gith": {
        "nome": "Gith",
        "descricao": "Uma raça de guerreiros psiônicos que escaparam da escravidão dos Devoradores de Mentes. Divididos em duas facções: os militaristas Githyanki e os monásticos Githzerai.",
        "lore": """
Por eras, os Gith foram escravos dos Devoradores de Mentes, uma raça de tiranos psiônicos. Após uma rebelião sangrenta, eles conquistaram sua liberdade, mas a paz não durou. Uma cisão ideológica dividiu o povo em dois. Os Githyanki, liderados pela rainha-lich Vlaakith, tornaram-se conquistadores astrais, cavalgando dragões vermelhos e pilhando os planos. Os Githzerai, sob a liderança de Zerthimon, retiraram-se para o plano caótico de Limbo, buscando a iluminação e o domínio da mente sobre a matéria. Ambas as facções se odeiam, mas compartilham um ódio ainda maior por seus antigos mestres.
        """,
        "modificadores_stats": {"inteligencia": 1},
        "habilidades_raciais": ["poder_psionico"],
        "variacoes": [
            {"nome": "Githyanki", "descricao": "Guerreiros astrais agressivos e arrogantes.", "modificadores_stats": {"forca": 2}},
            {"nome": "Githzerai", "descricao": "Monges ascéticos e disciplinados.", "modificadores_stats": {"sabedoria": 2}}
        ],
        "dialogo_racial": ["Nossa vontade é mais forte que o aço.", "Liberdade a qualquer custo.", "Conheça a si mesmo. Conheça seu inimigo."],
        "nomes_sugeridos": {"masculino": ["Dak", "Kalla", "Zerth"], "feminino": ["Elia", "Jen'lig", "Vlar"], "sem_familia": True},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== FADA ===================================
    "fada": {
        "nome": "Fada",
        "descricao": "Uma pequena criatura do Reino das Fadas, cheia de magia e travessura. Sua natureza é tão caprichosa quanto a própria magia.",
        "lore": """
As Fadas são a personificação da magia selvagem e da natureza indomada do Reino das Fadas. Elas nascem de uma flor sob a luz da lua cheia ou do riso de uma criança. Pequenas e com asas de inseto, elas podem voar e se mover com uma graça sobrenatural. Sua magia é inata e muitas vezes usada para pregar peças, criar ilusões ou ajudar criaturas da floresta. Elas são curiosas sobre o mundo mortal, mas suas mentes funcionam de uma maneira que os mortais acham difícil de compreender, com promessas que são armadilhas e presentes que são maldições.
        """,
        "modificadores_stats": {"destreza": 2, "carisma": 1},
        "habilidades_raciais": ["voo_de_fada", "magia_feerica"],
        "variacoes": [],
        "dialogo_racial": ["Brilhante! O que é isso?", "Promessas são divertidas, não são?", "Não seja tão sério!"],
        "nomes_sugeridos": {"masculino": ["Pip", "Puck", "Lark"], "feminino": ["Willow", "Breeze", "Trixie"], "sem_familia": True},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== CENTAURO ===================================
    "centauro": {
        "nome": "Centauro",
        "descricao": "Criaturas orgulhosas e territoriais, com o torso de um humano e o corpo de um cavalo. São os guardiões das planícies e florestas abertas.",
        "lore": """
Os Centauros são um povo que valoriza a liberdade e a força da natureza. Eles vivem em tribos nômades que percorrem as vastas planícies, seguindo as estações e os rebanhos. Eles são arqueiros e lanceiros excepcionais, usando sua velocidade e força para caçar e defender seu território com uma ferocidade incomparável. Eles são desconfiados de forasteiros e de assentamentos permanentes, que veem como cicatrizes na face do mundo.
        """,
        "modificadores_stats": {"forca": 2, "sabedoria": 1},
        "habilidades_raciais": ["investida", "cascos", "sobrevivente"],
        "variacoes": [],
        "dialogo_racial": ["O céu aberto é o único teto de que preciso.", "Esta terra é sagrada. Não a profane.", "Corra com o vento!"],
        "nomes_sugeridos": {"masculino": ["Rón", "Chiron", "Pholus"], "feminino": ["Hylonome", "Nessia", "Thera"], "sem_familia": True},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== METAMORFO ===================================
    "metamorfo": {
        "nome": "Metamorfo (Shifter)",
        "descricao": "Humanoides com sangue bestial, capazes de assumir traços animalescos por um curto período, aumentando seus instintos e poder.",
        "lore": """
Os Metamorfos, ou Shifters, são descendentes de humanos e licantropos. Embora não possam se transformar completamente em animais, eles podem canalizar a fera interior para ganhar traços bestiais: garras, presas, sentidos aguçados e uma velocidade incrível. Eles vivem no limite entre o mundo civilizado e a selva, muitas vezes se sentindo como estranhos em ambos. Sua luta é para equilibrar sua humanidade com o instinto selvagem que sempre borbulha sob a superfície.
        """,
        "modificadores_stats": {"destreza": 1},
        "habilidades_raciais": ["transformacao_parcial"],
        "variacoes": [
            {"nome": "Garras Afiadas", "descricao": "Associado a felinos, ganha garras mortais.", "modificadores_stats": {"destreza": 1}},
            {"nome": "Presas Longas", "descricao": "Associado a lobos, ganha uma mordida poderosa.", "modificadores_stats": {"forca": 1}},
            {"nome": "Pele Selvagem", "descricao": "Associado a ursos e javalis, torna-se mais resistente.", "modificadores_stats": {"constituicao": 1}},
            {"nome": "Caçador Veloz", "descricao": "Associado a predadores rápidos, sua velocidade aumenta.", "modificadores_stats": {"destreza": 1}}
        ],
        "dialogo_racial": ["Sinto o cheiro da lua.", "A fera interior está sempre acordada.", "Não me provoque."],
        "nomes_sugeridos": {"masculino": ["Ash", "Gale", "Torvin"], "feminino": ["Bree", "Tala", "Shay"], "sem_familia": True},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== FORJADO (WARFORGED) ===================================
    "forjado": {
        "nome": "Forjado (Warforged)",
        "descricao": "Construtos sencientes criados para a guerra, que agora buscam um propósito em um mundo em paz.",
        "lore": """
Os Forjados são uma raça relativamente nova, criados como soldados para a Última Guerra. Eles são feitos de madeira, metal e pedra, mas possuem uma alma e senciência. Com o fim da guerra, eles receberam sua liberdade, mas agora enfrentam um mundo que não sabe o que fazer com eles. Eles não comem, não dormem e não envelhecem da mesma forma que as outras raças. Cada Forjado agora deve encontrar seu próprio propósito: será que eles são apenas máquinas de matar, ou podem ser algo mais?
        """,
        "modificadores_stats": {"constituicao": 2, "forca": 1},
        "habilidades_raciais": ["construcao_resistente", "sentinela_incansavel"],
        "variacoes": [],
        "dialogo_racial": ["Qual é a minha diretriz?", "Este unidade funciona dentro dos parâmetros.", "Paz é um conceito ilógico."],
        "nomes_sugeridos": {"masculino": ["Guarda", "Bigorna", "Ferro"], "feminino": ["Lâmina", "Viga", "Pedra"], "sem_familia": True},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== AUTÔMATO ===================================
    "automato": {
        "nome": "Autômato",
        "descricao": "Construtos menores e mais precisos, criados por uma civilização perdida ou por gnomos mestres. Possuem uma lógica impecável e uma busca por conhecimento.",
        "lore": """
Diferente dos Forjados, criados para a guerra, os Autômatos foram criados como assistentes, estudiosos e guardiões de conhecimento. Eles são movidos por engrenagens complexas e uma centelha de magia elemental. Sua programação lhes dá uma sede insaciável por dados e lógica. Eles analisam o mundo, aprendem com suas experiências e buscam otimizar tudo ao seu redor. Um Autômato pode parecer frio, mas sua dedicação a uma tarefa ou a um companheiro é absoluta.
        """,
        "modificadores_stats": {"inteligencia": 2, "constituicao": 1},
        "habilidades_raciais": ["corpo_mecanico", "processador_logico"],
        "variacoes": [],
        "dialogo_racial": ["Isso não é lógico.", "Calculando probabilidades...", "Por favor, forneça mais dados."],
        "nomes_sugeridos": {"masculino": ["Unidade-734", "Calculus", "Cog"], "feminino": ["Pixel", "Ada", "Tessera"], "sem_familia": True},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== DOPPELGANGER ===================================
    "doppelganger": {
        "nome": "Doppelganger",
        "descricao": "Metamorfos monstruosos que podem assumir a aparência e as memórias recentes de outras criaturas. São mestres do engano e da infiltração.",
        "lore": """
Ninguém sabe a verdadeira origem dos Doppelgangers. Eles são uma raça de monstros que se escondem à vista de todos. Eles podem duplicar perfeitamente a aparência de qualquer humanoide que veem, e com um toque, podem roubar seus pensamentos superficiais e memórias recentes, permitindo-lhes assumir a vida de outra pessoa por um tempo. Eles são naturalmente desconfiados e egoístas, usando seu poder para ganho pessoal, seja para roubar, assassinar ou simplesmente para sobreviver em um mundo que os caçaria se sua verdadeira natureza fosse revelada.
        """,
        "modificadores_stats": {"destreza": 1, "carisma": 2},
        "habilidades_raciais": ["mudar_aparencia", "ler_pensamentos"],
        "variacoes": [],
        "dialogo_racial": ["Quem, eu?", "Você parece... interessante.", "Nunca confie em um rosto bonito."],
        "nomes_sugeridos": {"masculino": [], "feminino": [], "sem_familia": True}, # Geralmente usam os nomes de quem copiam
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== CHANGELING ===================================
    "changeling": {
        "nome": "Changeling",
        "descricao": "Descendentes de Doppelgangers e humanos, os Changelings são metamorfos sutis, capazes de alterar suas feições à vontade, mas não de mudar completamente de forma.",
        "lore": """
Os Changelings são os mestres do disfarce. Eles não possuem a capacidade monstruosa dos Doppelgangers de se transformar completamente, mas podem alterar sua altura, cabelo, cor dos olhos e estrutura facial com um pensamento. Isso os torna espiões, artistas e criminosos perfeitos. Muitos vivem em constante mudança, nunca mostrando seu verdadeiro rosto para ninguém. Outros usam seu dom para lutar por uma causa, tornando-se o agente infiltrado perfeito. A vida de um Changeling é uma de máscaras, tanto literais quanto figurativas.
        """,
        "modificadores_stats": {"destreza": 1, "carisma": 2},
        "habilidades_raciais": ["alterar_feicoes", "instintos_enganadores"],
        "variacoes": [],
        "dialogo_racial": ["Hoje, eu acho que serei... loira.", "Um rosto é apenas uma máscara.", "Eu posso ser quem você quiser."],
        "nomes_sugeridos": {"masculino": [], "feminino": [], "sem_familia": True}, # Nomes são fluidos
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== SYLVARI ===================================
    "sylvari": {
        "nome": "Sylvari",
        "descricao": "Uma raça de humanoides baseados em plantas, nascidos de uma grande Árvore Mágica. São curiosos, empáticos e conectados por um sonho compartilhado.",
        "lore": """
Os Sylvari são uma raça jovem, todos nascidos da Árvore Pálida, uma colossal planta mística. Eles emergem de casulos dourados já adultos, com o conhecimento básico do mundo implantado em suas mentes através do Sonho dos Sonhos, uma consciência coletiva que todos eles compartilham. Eles são movidos por uma curiosidade insaciável sobre o mundo e um desejo de protegê-lo do mal. Sua aparência é a de um humano, mas sua pele é casca, seu cabelo são folhas e flores, e seiva corre em suas veias. Eles são naturalmente empáticos e sentem a dor do mundo como se fosse a sua própria.
        """,
        "modificadores_stats": {"sabedoria": 2, "carisma": 1},
        "habilidades_raciais": ["pele_de_casca", "comunhao_com_a_natureza"],
        "variacoes": [
            {"nome": "Ciclo do Amanhecer", "descricao": "Sylvari nascidos de dia, são diplomatas e charmosos.", "modificadores_stats": {"carisma": 1}},
            {"nome": "Ciclo do Meio-dia", "descricao": "Nascidos sob o sol forte, são guerreiros e aventureiros.", "modificadores_stats": {"forca": 1}},
            {"nome": "Ciclo do Crepúsculo", "descricao": "Nascidos ao entardecer, são estudiosos e pensadores.", "modificadores_stats": {"inteligencia": 1}},
            {"nome": "Ciclo da Noite", "descricao": "Nascidos na escuridão, são caçadores e andarilhos silenciosos.", "modificadores_stats": {"destreza": 1}}
        ],
        "dialogo_racial": ["A Árvore Pálida nos guia.", "Sinto sua dor.", "O que o Sonho lhe mostrou hoje?"],
        "nomes_sugeridos": {"masculino": ["Cadeyrn", "Trahearne", "Rian"], "feminino": ["Caithe", "Faolain", "Malyck"], "sem_familia": True},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== MINOTAURO ===================================
    "minotauro": {
        "nome": "Minotauro",
        "descricao": "Humanoides com cabeça de touro, conhecidos por sua força incrível, orgulho e um senso de direção quase infalível.",
        "lore": """
Os minotauros são uma raça de guerreiros que valorizam a força e a tradição. Lendas dizem que foram criados por um deus da forja para serem os guardiões de labirintos sagrados. Essa herança lhes deu um senso de direção perfeito, tornando impossível para um minotauro se perder. Eles são diretos e honestos, muitas vezes vistos como rudes por outras raças. Para um minotauro, uma solução complexa é apenas um caminho longo para um problema simples que poderia ser resolvido com força.
        """,
        "modificadores_stats": {"forca": 2, "constituicao": 1},
        "habilidades_raciais": ["chifres_poderosos", "sentido_do_labirinto"],
        "variacoes": [],
        "dialogo_racial": ["Não se perca no meu caminho.", "A força é a resposta mais clara.", "Honra ao clã!"],
        "nomes_sugeridos": {"masculino": ["Asterion", "Bov", "Taur"], "feminino": ["Mina", "Tauriel", "Hornia"], "familia": []},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== HARPIA ===================================
    "harpia": {
        "nome": "Harpia",
        "descricao": "Criaturas aladas com torso humanoide e corpo de abutre. São conhecidas por seu canto sedutor e natureza predatória.",
        "lore": """
As harpias vivem em penhascos e ruínas, atraindo viajantes desavisados para a morte com sua canção mágica. Elas não são inerentemente más, mas sim predadoras amorais, vendo as outras criaturas como comida ou entretenimento. Sua sociedade é matriarcal, com as fêmeas mais velhas e de voz mais poderosa liderando o bando.
        """,
        "modificadores_stats": {"destreza": 2, "carisma": 1},
        "habilidades_raciais": ["voo_limitado", "cancao_sedutora"],
        "variacoes": [],
        "dialogo_racial": ["(Uma melodia cativante ecoa no ar)", "Venha mais perto, viajante...", "Carne fresca!"],
        "nomes_sugeridos": {"feminino": ["Aello", "Celaeno", "Ocypete"], "masculino": [], "sem_familia": True},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== SÁTIRO ===================================
    "satiro": {
        "nome": "Sátiro",
        "descricao": "Criaturas feéricas com pernas de bode, que vivem para a festa, a música e o caos. São hedonistas e amam pregar peças.",
        "lore": """
Os sátiros são os espíritos das festas selvagens. Nascidos no Reino das Fadas, eles viajam para o plano mortal em busca de novas experiências, vinhos e canções. Eles são mestres da flauta de pã e usam sua música para encantar, confundir e levar outros a um frenesi de dança. Um sátiro pode ser um companheiro divertido, mas nunca confie nele para guardar um segredo ou para ficar sóbrio.
        """,
        "modificadores_stats": {"carisma": 2, "destreza": 1},
        "habilidades_raciais": ["performance_cativante", "resistencia_a_magia"],
        "variacoes": [],
        "dialogo_racial": ["Mais vinho!", "A vida é uma festa, dance!", "Por que tão sério?"],
        "nomes_sugeridos": {"masculino": ["Pan", "Silenus", "Titos"], "feminino": ["Coria", "Lenea", "Maia"], "sem_familia": True},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== TRITÃO ===================================
    "tritao": {
        "nome": "Tritão",
        "descricao": "Um povo nobre e militarista do fundo do mar, que se veem como os guardiões dos oceanos contra as ameaças das profundezas.",
        "lore": """
Os tritões vivem em cidades de coral e madrepérola no fundo do oceano. Eles são uma sociedade orgulhosa e disciplinada, com uma longa história de batalhas contra krakens, sahuagin e outros horrores abissais. Eles são desconfiados do povo da superfície, a quem veem como descuidados e poluidores. Um tritão na superfície é muitas vezes um exilado ou um soldado em uma missão sagrada.
        """,
        "modificadores_stats": {"forca": 1, "constituicao": 1, "carisma": 1},
        "habilidades_raciais": ["anfibio", "guardiao_das_profundezas", "comunicacao_marinha"],
        "variacoes": [],
        "dialogo_racial": ["O oceano não guarda segredos.", "Pelas marés!", "Você cheira a ar seco."],
        "nomes_sugeridos": {"masculino": ["Triton", "Nereus", "Pontus"], "feminino": ["Coralia", "Nerida", "Thalassa"], "familia": []},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== YUAN-TI SANGUE-PURO ===================================
    "yuan-ti_sangue-puro": {
        "nome": "Yuan-ti Sangue-Puro",
        "descricao": "Humanoides com traços serpentinos sutis, resultado de experimentos antigos para fundir humanos com serpentes. São resistentes à magia e naturalmente venenosos.",
        "lore": """
Os Yuan-ti Sangue-Puro são a casta mais baixa de sua sociedade serpentina, mas ainda assim se veem como superiores a todas as outras raças. Eles são espiões e infiltradores perfeitos, capazes de se misturar à sociedade humana enquanto servem a seus mestres mais monstruosos. Eles são frios, calculistas e desprovidos de emoção, vendo os outros como ferramentas a serem usadas.
        """,
        "modificadores_stats": {"inteligencia": 1, "carisma": 2},
        "habilidades_raciais": ["vantagem_magica", "imunidade_a_veneno", "magia_serpentina"],
        "variacoes": [],
        "dialogo_racial": ["Sssssua emoção é uma fraqueza.", "Todos nós servimos a um mestre maior.", "O veneno tem muitos usos."],
        "nomes_sugeridos": {"masculino": ["Salassar", "Vespertil", "Zaltys"], "feminino": ["Naga", "Serpentine", "Vipera"], "sem_familia": True},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== VAMPIRO (DHAMPIR) ===================================
    "dhampir": {
        "nome": "Dhampir",
        "descricao": "Meio-vampiros, presos entre o mundo dos vivos e dos mortos. Possuem a sede de um vampiro, mas não todas as suas fraquezas.",
        "lore": """
Um Dhampir é o resultado da união de um vampiro com um mortal, um evento de tragédia e raridade. Eles são assombrados por uma fome constante por sangue, mas não são queimados pelo sol. Eles vivem vidas longas e solitárias, desconfiados tanto pelos vivos quanto pelos mortos. Muitos se tornam caçadores de mortos-vivos, usando seus poderes sombrios para destruir as criaturas que os criaram.
        """,
        "modificadores_stats": {"destreza": 2, "carisma": 1},
        "habilidades_raciais": ["mordida_vampirica", "escalar_paredes", "visao_no_escuro_superior"],
        "variacoes": [],
        "dialogo_racial": ["A noite tem seus próprios confortos.", "A fome... é constante.", "Eu uso a escuridão contra ela mesma."],
        "nomes_sugeridos": {"masculino": ["Alucard", "Strahd", "Lestat"], "feminino": ["Carmilla", "Elara", "Serana"], "familia": []},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== REVENANT ===================================
    "revenant": {
        "nome": "Revenant",
        "descricao": "Uma alma que retornou do túmulo para completar uma tarefa inacabada. Movidos por um único propósito, são quase imparáveis.",
        "lore": """
Um Revenant não é um morto-vivo comum. É uma alma que se recusou a passar para o além, impulsionada por uma sede de vingança ou por um juramento que não foi cumprido. Eles habitam seu antigo corpo ou um novo construto, e não sentem dor, medo ou cansaço. Eles têm um único objetivo, e uma vez que esse objetivo seja cumprido, eles finalmente encontram a paz e se desfazem em pó.
        """,
        "modificadores_stats": {"constituicao": 1, "forca": 1},
        "habilidades_raciais": ["proposito_inabalavel", "natureza_implacavel"],
        "variacoes": [],
        "dialogo_racial": ["A justiça deve ser feita.", "A morte não pode me parar.", "Meu objetivo é tudo o que resta."],
        "nomes_sugeridos": {"masculino": [], "feminino": [], "sem_familia": True}, # Usam seus nomes antigos
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    },

    # =================================== MYCONID ===================================
    "myconid": {
        "nome": "Myconid",
        "descricao": "Humanoides-cogumelo sencientes do Subterrâneo, que se comunicam através de esporos e vivem em círculos pacíficos e comunais.",
        "lore": """
Os Myconids são um dos povos mais estranhos e pacíficos do Subterrâneo. Eles vivem em colônias, lideradas por um soberano, e se importam apenas com o bem-estar de seu círculo. Eles não têm conceito de individualidade da mesma forma que as outras raças. Em vez disso, eles estão todos conectados por uma união de esporos, compartilhando pensamentos e emoções. Eles podem liberar diferentes tipos de esporos para se comunicar, curar ou até mesmo animar os mortos como servos.
        """,
        "modificadores_stats": {"sabedoria": 2, "constituicao": 1},
        "habilidades_raciais": ["esporos_de_comunicacao", "esporos_de_animacao"],
        "variacoes": [],
        "dialogo_racial": ["(Um sopro de esporos transmite uma sensação de calma.)", "(Uma imagem de um cogumelo crescendo aparece em sua mente.)"],
        "nomes_sugeridos": {"masculino": ["Agaricus", "Boletus", "Myx"], "feminino": ["Amanita", "Psilo", "Stropharia"], "sem_familia": True},
        "relacionamento_racas": {},
        "arvore_evolucao": {}
    }
}
