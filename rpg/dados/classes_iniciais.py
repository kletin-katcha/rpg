# ==============================================================================
# ARQUIVO DE DADOS: CLASSES INICIAIS
# ==============================================================================
#
# Este arquivo contém as definições para todas as classes jogáveis iniciais.
# A estrutura é um dicionário onde a chave é o ID da classe e o valor é
# outro dicionário com os detalhes da classe.
#
# ==============================================================================

CLASSES_INICIAIS = {
    # =================================== GUERREIRO ===================================
    "guerreiro": {
        "nome": "Guerreiro",
        "descricao": "Mestre do combate corpo a corpo, treinado no uso de todas as armas e armaduras.",
        "lore": "O caminho do guerreiro é um caminho de disciplina, aço e sangue.",
        "stats_primarios": ["forca", "constituicao"],
        "ataques_base_disponiveis": ["ataque_leve", "ataque_normal", "ataque_pesado"],
        "habilidades_iniciais": ["ataque_poderoso", "grito_de_guerra"],
        "equipamento_inicial": {"arma_principal": "espada_curta_ferro", "peitoral": "peitoral_de_couro_batido", "escudo": "escudo_de_madeira"}
    },

    # =================================== MAGO ===================================
    "mago": {
        "nome": "Mago",
        "descricao": "Um estudioso das artes arcanas, capaz de manipular as energias mágicas.",
        "lore": "O mago é um cientista da realidade.",
        "stats_primarios": ["inteligencia", "sabedoria"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["bola_de_fogo", "barreira_de_gelo"],
        "equipamento_inicial": {"arma_principal": "cajado_de_aprendiz", "peitoral": "tunica_simples"}
    },

    # =================================== LADINO ===================================
    "ladino": {
        "nome": "Ladino",
        "descricao": "Um especialista em furtividade e subterfúgio.",
        "lore": "Onde o guerreiro usa a força e o mago o poder, o ladino usa a astúcia.",
        "stats_primarios": ["destreza", "carisma"],
        "ataques_base_disponiveis": ["ataque_leve", "ataque_normal"],
        "habilidades_iniciais": ["ataque_furtivo", "disparada"],
        "equipamento_inicial": {"arma_principal": "adaga_de_ferro", "arma_secundaria": "adaga_de_ferro", "peitoral": "armadura_de_couro_leve"}
    },

    # =================================== CLÉRIGO ===================================
    "clerigo": {
        "nome": "Clérigo",
        "descricao": "Um servo devoto de uma divindade, que canaliza poder sagrado.",
        "lore": "A fé de um clérigo é sua arma e seu escudo.",
        "stats_primarios": ["sabedoria", "constituicao"],
        "ataques_base_disponiveis": ["ataque_normal"],
        "habilidades_iniciais": ["cura_leve", "punicao_divina"],
        "equipamento_inicial": {"arma_principal": "maca_simples", "escudo": "escudo_de_madeira", "peitoral": "cota_de_malha"}
    },

    # =================================== BÁRBARO ===================================
    "barbaro": {
        "nome": "Bárbaro",
        "descricao": "Um guerreiro tribal que canaliza uma fúria primordial.",
        "lore": "Longe das muralhas das cidades, vive o bárbaro.",
        "stats_primarios": ["forca", "constituicao"],
        "ataques_base_disponiveis": ["ataque_pesado"],
        "habilidades_iniciais": ["furia_selvagem", "golpe_brutal"],
        "equipamento_inicial": {"arma_principal": "machado_grande_de_duas_maos", "peitoral": "tanga_de_peles"}
    },

    # =================================== BARDO ===================================
    "bardo": {
        "nome": "Bardo",
        "descricao": "Um mestre da música, da palavra e do encanto.",
        "lore": "O bardo sabe que as palavras podem ser mais afiadas que as espadas.",
        "stats_primarios": ["carisma", "destreza"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["cancao_da_coragem", "nota_ dissonante"],
        "equipamento_inicial": {"arma_principal": "rapiera", "arma_secundaria": "alaude", "peitoral": "roupas_de_viajante"}
    },

    # =================================== DRUIDA ===================================
    "druida": {
        "nome": "Druida",
        "descricao": "Um guardião do equilíbrio natural, que extrai poder da própria essência da vida.",
        "lore": "O druida é um sacerdote da natureza.",
        "stats_primarios": ["sabedoria", "constituicao"],
        "ataques_base_disponiveis": ["ataque_normal"],
        "habilidades_iniciais": ["forma_de_urso", "enraizar"],
        "equipamento_inicial": {"arma_principal": "cajado_de_galho_retorcido", "peitoral": "armadura_de_peles_e_folhas"}
    },

    # =================================== RANGER ===================================
    "ranger": {
        "nome": "Ranger",
        "descricao": "Um caçador e rastreador mestre das terras selvagens.",
        "lore": "O ranger é a ponte entre a civilização e a selva.",
        "stats_primarios": ["destreza", "sabedoria"],
        "ataques_base_disponiveis": ["ataque_normal"],
        "habilidades_iniciais": ["tiro_certeiro", "companheiro_animal_lobo"],
        "equipamento_inicial": {"arma_principal": "arco_longo", "arma_secundaria": "espada_curta_ferro", "peitoral": "armadura_de_couro"}
    },

    # =================================== PALADINO ===================================
    "paladino": {
        "nome": "Paladino",
        "descricao": "Um guerreiro sagrado vinculado por um juramento a uma causa maior.",
        "lore": "Um paladino é mais do que um guerreiro e mais do que um clérigo.",
        "stats_primarios": ["forca", "carisma"],
        "ataques_base_disponiveis": ["ataque_normal", "ataque_pesado"],
        "habilidades_iniciais": ["golpe_divino", "aura_de_protecao"],
        "equipamento_inicial": {"arma_principal": "espada_longa", "escudo": "escudo_de_aço", "peitoral": "armadura_de_placas"}
    },

    # =================================== FEITICEIRO ===================================
    "feiticeiro": {
        "nome": "Feiticeiro",
        "descricao": "Um conjurador que nasceu com magia em seu sangue.",
        "lore": "Enquanto o mago estuda a magia, o feiticeiro *é* a magia.",
        "stats_primarios": ["carisma", "constituicao"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["raio_do_caos", "onda_de_forca"],
        "equipamento_inicial": {"arma_principal": "adaga_ornamentada", "peitoral": "roupas_finas"}
    },

    # =================================== BRUXO ===================================
    "bruxo": {
        "nome": "Bruxo",
        "descricao": "Um conjurador que obtém seu poder através de um pacto com uma entidade de outro mundo.",
        "lore": "O poder pode ser conquistado, pode ser herdado, ou pode ser... negociado.",
        "stats_primarios": ["carisma", "inteligencia"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["explosao_mistica", "maldição_do_patrono"],
        "equipamento_inicial": {"arma_principal": "grimorio_sombrio", "peitoral": "robe_escuro"}
    },

    # =================================== ARTÍFICE ===================================
    "artifice": {
        "nome": "Artífice",
        "descricao": "Um mestre da invenção, que funde magia e tecnologia.",
        "lore": "O artífice vê a magia como um sistema complexo.",
        "stats_primarios": ["inteligencia", "destreza"],
        "ataques_base_disponiveis": ["ataque_normal"],
        "habilidades_iniciais": ["infusao_magica", "construir_torreta"],
        "equipamento_inicial": {"arma_principal": "besta_leve", "peitoral": "avental_de_couro_reforcado"}
    },

    # =================================== CAVALEIRO ===================================
    "cavaleiro": {
        "nome": "Cavaleiro",
        "descricao": "Um guerreiro de armadura pesada focado na defesa.",
        "lore": "O cavaleiro é a muralha inabalável.",
        "stats_primarios": ["constituicao", "forca"],
        "ataques_base_disponiveis": ["ataque_normal"],
        "habilidades_iniciais": ["postura_defensiva", "provocacao_em_massa"],
        "equipamento_inicial": {"arma_principal": "espada_longa", "escudo": "escudo_torre", "peitoral": "armadura_de_placas_completa"}
    },

    # =================================== BATEDOR ===================================
    "batedor": {
        "nome": "Batedor",
        "descricao": "Especialista em reconhecimento e sobrevivência.",
        "lore": "Os olhos e ouvidos do exército.",
        "stats_primarios": ["destreza", "sabedoria"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["tiro_marcado", "montar_armadilha"],
        "equipamento_inicial": {"arma_principal": "arco_longo", "peitoral": "gibao_de_couro"}
    },

    # =================================== SACERDOTE DAS SOMBRAS ===================================
    "sacerdote_das_sombras": {
        "nome": "Sacerdote das Sombras",
        "descricao": "Um clérigo que usa magias de sombras para debilitar.",
        "lore": "Nem toda divindade é de luz.",
        "stats_primarios": ["sabedoria", "inteligencia"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["toque_vampirico", "palavra_de_dor"],
        "equipamento_inicial": {"arma_principal": "adaga_ritualistica", "peitoral": "robe_negro"}
    },

    # =================================== ESPADACHIM ===================================
    "espadachim": {
        "nome": "Espadachim (Swashbuckler)",
        "descricao": "Um duelista carismático e audacioso.",
        "lore": "O espadachim vive por sua reputação e seu charme.",
        "stats_primarios": ["destreza", "carisma"],
        "ataques_base_disponiveis": ["ataque_leve", "ataque_normal"],
        "habilidades_iniciais": ["finta_audaciosa", "duelo_elegante"],
        "equipamento_inicial": {"arma_principal": "rapiera", "peitoral": "camisa_de_seda"}
    },

    # =================================== ATIRADOR ===================================
    "atirador": {
        "nome": "Atirador (Gunslinger)",
        "descricao": "Um pioneiro de uma nova forma de combate, usando armas de fogo.",
        "lore": "Em um mundo de espadas e magia, o som de um tiro é o som do futuro.",
        "stats_primarios": ["destreza", "inteligencia"],
        "ataques_base_disponiveis": ["ataque_normal"],
        "habilidades_iniciais": ["tiro_mirado", "consertar_arma"],
        "equipamento_inicial": {"arma_principal": "pistola_de_pederneira", "peitoral": "casaco_de_couro"}
    },

    # =================================== XAMÃ ===================================
    "xama": {
        "nome": "Xamã",
        "descricao": "Um guia espiritual que se comunica com os espíritos.",
        "lore": "O xamã é a ponte entre o mundo físico e o mundo espiritual.",
        "stats_primarios": ["sabedoria", "constituicao"],
        "ataques_base_disponiveis": ["ataque_normal"],
        "habilidades_iniciais": ["choque_flamejante", "totem_de_cura"],
        "equipamento_inicial": {"arma_principal": "clava_ritualistica", "peitoral": "vestes_tribais"}
    },

    # =================================== MONGE ===================================
    "monge": {
        "nome": "Monge",
        "descricao": "Um artista marcial disciplinado que transforma seu próprio corpo em uma arma.",
        "lore": "Através de uma disciplina rigorosa e meditação, o monge alcança a perfeição.",
        "stats_primarios": ["destreza", "sabedoria"],
        "ataques_base_disponiveis": ["ataque_leve", "ataque_normal"],
        "habilidades_iniciais": ["rajada_de_golpes", "defesa_paciente"],
        "equipamento_inicial": {"arma_principal": "desarmado", "peitoral": "roupas_simples_de_monasterio"}
    },

    # =================================== NECROMANTE ===================================
    "necromante": {
        "nome": "Necromante",
        "descricao": "Um mago que estuda a tênue linha entre a vida e a morte.",
        "lore": "A necromancia é talvez a mais temida e incompreendida de todas as artes mágicas.",
        "stats_primarios": ["inteligencia", "constituicao"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["erguer_morto", "raio_doentio"],
        "equipamento_inicial": {"arma_principal": "adaga_de_osso", "peitoral": "robe_com_capuz"}
    },

    # =================================== GLADIADOR ===================================
    "gladiador": {
        "nome": "Gladiador",
        "descricao": "Um guerreiro focado em espetáculo e combate de arena.",
        "lore": "O gladiador não luta por um reino ou por uma causa, mas pela glória.",
        "stats_primarios": ["forca", "carisma"],
        "ataques_base_disponiveis": ["ataque_normal", "ataque_pesado"],
        "habilidades_iniciais": ["golpe_de_exibicao", "rede_e_tridente"],
        "equipamento_inicial": {"arma_principal": "gladio", "escudo":"parma", "peitoral": "armadura_de_gladiador"}
    },

    # =================================== CAÇADOR DE RECOMPENSAS ===================================
    "cacador_de_recompensas": {
        "nome": "Caçador de Recompensas",
        "descricao": "Um rastreador implacável que caça alvos por dinheiro.",
        "lore": "O caçador de recompensas é a personificação da tenacidade.",
        "stats_primarios": ["destreza", "inteligencia"],
        "ataques_base_disponiveis": ["ataque_leve", "ataque_normal"],
        "habilidades_iniciais": ["rastrear_alvo", "disparo_debilitante"],
        "equipamento_inicial": {"arma_principal": "besta_pesada", "arma_secundaria": "machete", "peitoral": "sobretudo_de_couro"}
    },

    # =================================== INQUISIDOR ===================================
    "inquisidor": {
        "nome": "Inquisidor",
        "descricao": "Um caçador de hereges e feiticeiros, que combina fervor divino com táticas.",
        "lore": "Onde há suspeita de corrupção sombria, o Inquisidor é enviado.",
        "stats_primarios": ["sabedoria", "forca"],
        "ataques_base_disponiveis": ["ataque_normal"],
        "habilidades_iniciais": ["julgamento", "fogo_purificador"],
        "equipamento_inicial": {"arma_principal": "martelo_de_guerra", "peitoral": "armadura_de_placas_com_insignia"}
    },

    # =================================== MAGO DE BATALHA ===================================
    "mago_de_batalha": {
        "nome": "Mago de Batalha",
        "descricao": "Um mago que treina para o combate na linha de frente.",
        "lore": "O mago de batalha ri da ideia de se esconder atrás de seus companheiros.",
        "stats_primarios": ["inteligencia", "forca"],
        "ataques_base_disponiveis": ["ataque_normal"],
        "habilidades_iniciais": ["golpe_arcano", "armadura_de_mago"],
        "equipamento_inicial": {"arma_principal": "espada_longa", "peitoral": "peitoral_de_aço", "luvas": "manoplas_de_batalha"}
    },

    # =================================== ILUSIONISTA ===================================
    "ilusionista": {
        "nome": "Ilusionista",
        "descricao": "Um mestre do engano e da manipulação mental.",
        "lore": "Para o ilusionista, a percepção é a realidade.",
        "stats_primarios": ["inteligencia", "carisma"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["imagem_espelhada", "medo_fantasmagorico"],
        "equipamento_inicial": {"arma_principal": "cajado_elegante", "peitoral": "robe_com_padroes_hipnoticos"}
    },

    # =================================== MESTRE DAS FERAS ===================================
    "mestre_das_feras": {
        "nome": "Mestre das Feras",
        "descricao": "Um guerreiro que luta em perfeita harmonia com um ou mais companheiros animais.",
        "lore": "O Mestre das Feras e seu companheiro animal são duas metades de um todo.",
        "stats_primarios": ["forca", "destreza"],
        "ataques_base_disponiveis": ["ataque_normal"],
        "habilidades_iniciais": ["ataque_coordenado", "vinculo_bestial"],
        "equipamento_inicial": {"arma_principal": "machadinha", "arma_secundaria": "chicote", "peitoral": "armadura_de_couro_reforcado"}
    },

    # =================================== PIROMANTE ===================================
    "piromante": {
        "nome": "Piromante",
        "descricao": "Um mago especializado na mais destrutiva das escolas elementais: o fogo.",
        "lore": "Alguns magos buscam conhecimento, outros buscam controle. O piromante busca a purificação.",
        "stats_primarios": ["inteligencia", "constituicao"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["seta_de_fogo", "aura_flamejante"],
        "equipamento_inicial": {"arma_principal": "cajado_carbonizado", "peitoral": "robe_vermelho"}
    },

    # =================================== CRIOMANTE ===================================
    "criomante": {
        "nome": "Criomante",
        "descricao": "Um mago focado no controle do frio e do gelo.",
        "lore": "O oposto do piromante, o criomante encontra poder no zero absoluto.",
        "stats_primarios": ["inteligencia", "sabedoria"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["lanca_de_gelo", "armadura_de_geada"],
        "equipamento_inicial": {"arma_principal": "varinha_de_cristal", "peitoral": "robe_branco_e_azul"}
    },

    # =================================== GEOMANTE ===================================
    "geomante": {
        "nome": "Geomante",
        "descricao": "Um mago que extrai poder da terra, da pedra e das montanhas.",
        "lore": "O geomante é paciente, teimoso e inabalável como a montanha.",
        "stats_primarios": ["inteligencia", "constituicao"],
        "ataques_base_disponiveis": ["ataque_normal"],
        "habilidades_iniciais": ["pele_de_pedra", "arremessar_rocha"],
        "equipamento_inicial": {"arma_principal": "martelo_de_pedra", "peitoral": "robe_marrom"}
    },

    # =================================== AEROMANTE ===================================
    "aeromante": {
        "nome": "Aeromante",
        "descricao": "Um mago que comanda os ventos e os céus.",
        "lore": "Livre e imprevisível como o vento, o aeromante é um mestre do ar.",
        "stats_primarios": ["inteligencia", "destreza"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["rajada_de_vento", "salto_do_vento"],
        "equipamento_inicial": {"arma_principal": "cajado_leve", "peitoral": "roupas_esvoacantes"}
    },

    # =================================== ELETROMANTE ===================================
    "eletromante": {
        "nome": "Eletromante",
        "descricao": "Um mago que canaliza a energia bruta dos relâmpagos.",
        "lore": "O eletromante lida com a energia pura e crepitante da tempestade.",
        "stats_primarios": ["inteligencia", "destreza"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["choque", "raio_em_cadeia"],
        "equipamento_inicial": {"arma_principal": "haste_de_metal", "peitoral": "robe_com_fios_de_cobre"}
    },

    # =================================== ALQUIMISTA ===================================
    "alquimista": {
        "nome": "Alquimista",
        "descricao": "Um cientista que usa conhecimento de química e reagentes exóticos.",
        "lore": "Onde o artífice constrói, o alquimista mistura.",
        "stats_primarios": ["inteligencia", "destreza"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["arremessar_bomba_de_fogo", "criar_pocao_de_cura_rapida"],
        "equipamento_inicial": {"arma_principal": "adaga_reforcada", "peitoral": "avental_de_alquimista", "acessorio": "bolsa_de_reagentes"}
    },

    # =================================== MESTRE CERVEJEIRO ===================================
    "mestre_cervejeiro": {
        "nome": "Mestre Cervejeiro",
        "descricao": "Um monge ou guerreiro que encontra poder em bebidas alcoólicas.",
        "lore": "O Mestre Cervejeiro é uma figura subestimada.",
        "stats_primarios": ["constituicao", "forca"],
        "ataques_base_disponiveis": ["ataque_normal"],
        "habilidades_iniciais": ["estilo_do_bebado", "baforada_de_fogo_alcoolico"],
        "equipamento_inicial": {"arma_principal": "barril_pequeno_nas_costas", "peitoral": "roupas_rusticas"}
    },

    # =================================== VIDENTE ===================================
    "vidente": {
        "nome": "Vidente",
        "descricao": "Um conjurador que perscruta o passado, o presente e o futuro.",
        "lore": "O vidente carrega o fardo de ver o que foi, o que é e o que poderia ser.",
        "stats_primarios": ["sabedoria", "inteligencia"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["premonicao", "maldição_do_azar"],
        "equipamento_inicial": {"arma_principal": "orbe_de_cristal", "peitoral": "mantos_de_oraculo"}
    },

    # =================================== SAMURAI ===================================
    "samurai": {
        "nome": "Samurai",
        "descricao": "Um guerreiro de uma terra distante, ligado por um código de honra estrito.",
        "lore": "O samurai é um guerreiro de elite, cuja vida é dedicada ao bushido.",
        "stats_primarios": ["forca", "destreza"],
        "ataques_base_disponiveis": ["ataque_normal", "ataque_pesado"],
        "habilidades_iniciais": ["golpe_iaijutsu", "postura_inabalavel"],
        "equipamento_inicial": {"arma_principal": "katana", "arma_secundaria": "wakizashi", "peitoral": "armadura_o-yoroi"}
    },

    # =================================== NINJA ===================================
    "ninja": {
        "nome": "Ninja",
        "descricao": "Um agente de furtividade e espionagem de uma terra distante.",
        "lore": "O ninja opera nas sombras, um fantasma no meio da noite.",
        "stats_primarios": ["destreza", "inteligencia"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["bomba_de_fumaca", "substituicao"],
        "equipamento_inicial": {"arma_principal": "ninjato", "acessorio": "shurikens", "peitoral": "traje_shinobi"}
    },

    # =================================== CORSÁRIO ===================================
    "corsario": {
        "nome": "Corsário",
        "descricao": "Um marinheiro e guerreiro dos mares.",
        "lore": "A vida do corsário é o mar.",
        "stats_primarios": ["destreza", "forca"],
        "ataques_base_disponiveis": ["ataque_normal"],
        "habilidades_iniciais": ["chute_baixo", "tiro_de_pistola"],
        "equipamento_inicial": {"arma_principal": "cimitarra", "arma_secundaria": "pistola_de_pederneira", "peitoral": "casaco_de_capitao"}
    },

    # =================================== DOMADOR ===================================
    "domador": {
        "nome": "Domador",
        "descricao": "Um especialista em capturar, treinar e lutar ao lado de monstros e bestas.",
        "lore": "O Domador vê o mundo como um zoológico de potencial.",
        "stats_primarios": ["carisma", "sabedoria"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["capturar_besta", "ordem_de_ataque"],
        "equipamento_inicial": {"arma_principal": "chicote", "peitoral": "roupas_reforcadas"}
    },

    # =================================== MAGO DO SANGUE ===================================
    "mago_do_sangue": {
        "nome": "Mago do Sangue",
        "descricao": "Um conjurador que usa a própria força vital como combustível para sua magia.",
        "lore": "A magia do sangue é uma das artes mais antigas e temidas.",
        "stats_primarios": ["constituicao", "inteligencia"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["sacrificio_de_sangue", "lanca_de_sangue"],
        "equipamento_inicial": {"arma_principal": "adaga_sacrificial", "peitoral": "robe_manchado_de_sangue"}
    },

    # =================================== DEFENSOR ===================================
    "defensor": {
        "nome": "Defensor",
        "descricao": "Um especialista em proteção.",
        "lore": "O Defensor é a âncora de qualquer grupo.",
        "stats_primarios": ["constituicao", "forca"],
        "ataques_base_disponiveis": ["ataque_normal"],
        "habilidades_iniciais": ["bloqueio_com_escudo", "intervir"],
        "equipamento_inicial": {"arma_principal": "espada_curta_ferro", "escudo": "escudo_de_torre", "peitoral": "armadura_de_placas_completa"}
    },

    # =================================== DUELISTA ===================================
    "duelista": {
        "nome": "Duelista",
        "descricao": "Um guerreiro focado no combate um-a-um.",
        "lore": "Para o duelista, o campo de batalha é uma série de confrontos individuais.",
        "stats_primarios": ["destreza", "forca"],
        "ataques_base_disponiveis": ["ataque_leve", "ataque_normal"],
        "habilidades_iniciais": ["aparar_e_ripostar", "estocada_precisa"],
        "equipamento_inicial": {"arma_principal": "florete", "peitoral": "jaqueta_de_couro"}
    },

    # =================================== BERSERKER ===================================
    "berserker": {
        "nome": "Berserker",
        "descricao": "Um guerreiro que entra em um estado de fúria cega em batalha.",
        "lore": "Se o Bárbaro canaliza a fúria, o Berserker é consumido por ela.",
        "stats_primarios": ["forca", "constituicao"],
        "ataques_base_disponiveis": ["ataque_pesado"],
        "habilidades_iniciais": ["furia_cega", "ignorar_dor"],
        "equipamento_inicial": {"arma_principal": "machado_duplo", "peitoral": "peito_nu_com_pinturas_de_guerra"}
    },

    # =================================== ACÓLITO ===================================
    "acolito": {
        "nome": "Acólito",
        "descricao": "Um aprendiz de uma ordem religiosa ou culto.",
        "lore": "O acólito está no primeiro degrau de uma longa escada para o poder.",
        "stats_primarios": ["sabedoria", "carisma"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["bencao_menor", "assistencia_ritualistica"],
        "equipamento_inicial": {"arma_principal": "maça_leve", "peitoral": "tunica_de_acolito"}
    },

    # =================================== ANDARILHO ESPIRITUAL ===================================
    "andarilho_espiritual": {
        "nome": "Andarilho Espiritual",
        "descricao": "Um indivíduo que pode projetar sua consciência para fora de seu corpo.",
        "lore": "O andarilho espiritual vive com um pé em dois mundos.",
        "stats_primarios": ["sabedoria", "constituicao"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["projecao_astral", "toque_etereo"],
        "equipamento_inicial": {"arma_principal": "desarmado", "peitoral": "roupas_simples"}
    },

    # =================================== CAÇADOR DE BRUXAS ===================================
    "cacador_de_bruxas": {
        "nome": "Caçador de Bruxas",
        "descricao": "Um guerreiro especializado em caçar e matar usuários de magia corrompida.",
        "lore": "Onde a magia floresce, também floresce a corrupção.",
        "stats_primarios": ["sabedoria", "destreza"],
        "ataques_base_disponiveis": ["ataque_normal"],
        "habilidades_iniciais": ["resistencia_a_magia", "disparo_de_ferro_frio"],
        "equipamento_inicial": {"arma_principal": "besta_de_repeticao", "arma_secundaria": "espada_curta_prateada", "peitoral": "sobretudo_de_couro_escuro"}
    },

    # =================================== TEMPLÁRIO ===================================
    "templario": {
        "nome": "Templário",
        "descricao": "Um guerreiro de uma ordem sagrada, que combina a disciplina de um soldado com o zelo de um clérigo.",
        "lore": "O Templário é o braço armado de uma igreja.",
        "stats_primarios": ["forca", "sabedoria"],
        "ataques_base_disponiveis": ["ataque_normal"],
        "habilidades_iniciais": ["arma_abençoada", "escudo_da_fe"],
        "equipamento_inicial": {"arma_principal": "espada_longa", "escudo": "escudo_com_simbolo_sagrado", "peitoral": "armadura_de_placas_ornamentada"}
    },

    # =================================== ARCANISTA ===================================
    "arcanista": {
        "nome": "Arcanista",
        "descricao": "Um estudioso que busca o conhecimento arcano por si só.",
        "lore": "Se o mago é o cientista, o arcanista é o filósofo.",
        "stats_primarios": ["inteligencia", "sabedoria"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["analise_magica", "runa_de_poder"],
        "equipamento_inicial": {"arma_principal": "tomo_arcano", "peitoral": "robe_de_erudito"}
    },

    # =================================== BARDO DA BRAVURA ===================================
    "bardo_da_bravura": {
        "nome": "Bardo da Bravura",
        "descricao": "Um bardo que inspira coragem e heroísmo no campo de batalha.",
        "lore": "O Bardo da Bravura conta as histórias de heróis, e aspira a se tornar um.",
        "stats_primarios": ["carisma", "forca"],
        "ataques_base_disponiveis": ["ataque_normal"],
        "habilidades_iniciais": ["cancao_de_batalha", "golpe_inspirador"],
        "equipamento_inicial": {"arma_principal": "machadinha", "arma_secundaria": "tambor_de_guerra", "peitoral": "cota_de_malha"}
    },

    # =================================== PATRULHEIRO URBANO ===================================
    "patrulheiro_urbano": {
        "nome": "Patrulheiro Urbano",
        "descricao": "Um ranger que adaptou suas habilidades para a selva de pedra.",
        "lore": "Para o Patrulheiro Urbano, as vielas são desfiladeiros e os telhados são as copas das árvores.",
        "stats_primarios": ["destreza", "sabedoria"],
        "ataques_base_disponiveis": ["ataque_leve"],
        "habilidades_iniciais": ["movimento_de_telhado", "tiro_rapido_de_besta"],
        "equipamento_inicial": {"arma_principal": "besta_de_mao", "arma_secundaria": "espada_curta_ferro", "peitoral": "capuz_e_manto_escuro"}
    },

    # =================================== PUGILISTA ===================================
    "pugilista": {
        "nome": "Pugilista",
        "descricao": "Um lutador de rua que confia em seus punhos e em sua resistência.",
        "lore": "O pugilista aprendeu a lutar nas tavernas e nas docas.",
        "stats_primarios": ["forca", "constituicao"],
        "ataques_base_disponiveis": ["ataque_leve", "ataque_normal"],
        "habilidades_iniciais": ["soco_direto", "queixo_de_granito"],
        "equipamento_inicial": {"arma_principal": "soqueiras_de_bronze", "peitoral": "camisa_rasgada"}
    }
}
