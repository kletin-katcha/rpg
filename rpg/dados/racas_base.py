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
    }
}
