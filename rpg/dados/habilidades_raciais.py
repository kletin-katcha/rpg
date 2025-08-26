# ==============================================================================
# ARQUIVO DE DADOS: HABILIDADES RACIAIS
# ==============================================================================
#
# Este arquivo contém as definições para todas as habilidades raciais,
# tanto ativas quanto passivas.
#
# ==============================================================================

HABILIDADES_RACIAIS = {
    # Humano
    "esforco_heroico": {
        "nome": "Esforço Heroico", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 50,
        "descricao": "Em um momento de desespero ou determinação, você pode realizar um grande feito. Aumenta todos os atributos em 2 por 3 turnos.",
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_esforco_heroico", "duracao": 3}]
    },

    # Elfo
    "visao_no_escuro": {
        "nome": "Visão no Escuro", "tipo": "passiva",
        "descricao": "Sua herança élfica lhe concede uma visão superior na penumbra e na escuridão."
    },
    "afinidade_arcana": {
        "nome": "Afinidade Arcana", "tipo": "passiva",
        "descricao": "Sua conexão natural com a magia lhe concede maior poder e resistência mágica."
    },

    # Anão
    "resistencia_a_veneno": {
        "nome": "Resistência a Veneno", "tipo": "passiva",
        "descricao": "Sua robustez anã lhe concede grande resistência contra venenos."
    },
    "artesao_de_pedra": {
        "nome": "Artesão de Pedra", "tipo": "passiva",
        "descricao": "Seu conhecimento sobre rochas e metais lhe concede um bônus em sua defesa."
    },

    # Orc
    "furor_de_batalha": {
        "nome": "Furor de Batalha", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 40,
        "descricao": "Você entra em um frenesi de batalha, aumentando seu dano físico em 30% por 3 turnos.",
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_furor_de_batalha", "duracao": 3}]
    },

    # Khajiit
    "garras_afiadas": {
        "nome": "Garras Afiadas", "tipo": "passiva",
        "descricao": "Seus ataques desarmados causam dano extra."
    },
    "visao_noturna_superior": {
        "nome": "Visão Noturna Superior", "tipo": "passiva",
        "descricao": "Você enxerga perfeitamente na escuridão total."
    },

    # Argoniano
    "respirar_agua": {
        "nome": "Respirar Debaixo D'água", "tipo": "passiva",
        "descricao": "Você pode respirar debaixo d'água indefinidamente."
    },
    "imunidade_a_doenca_veneno": {
        "nome": "Imunidade a Doença e Veneno", "tipo": "passiva",
        "descricao": "Sua fisiologia reptiliana o torna imune a todas as doenças e venenos comuns."
    },
    "pele_hist": {
        "nome": "Pele de Hist", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 30,
        "descricao": "Você invoca o poder do Hist para regenerar sua vida rapidamente por um curto período.",
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "regen_pele_hist", "duracao": 5}]
    },

    # Gnomo
    "mente_mecanica": {
        "nome": "Mente Mecânica", "tipo": "passiva",
        "descricao": "Sua mente analítica lhe dá vantagem ao lidar com armadilhas e mecanismos."
    },
    "afinidade_com_ilusao": {
        "nome": "Afinidade com Ilusão", "tipo": "passiva",
        "descricao": "Suas magias de ilusão são mais potentes e difíceis de resistir."
    },

    # Aasimar
    "resistencia_celestial": {
        "nome": "Resistência Celestial", "tipo": "passiva",
        "descricao": "Sua herança divina lhe concede resistência a dano necrótico e radiante."
    },
    "toque_curativo": {
        "nome": "Toque Curativo", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 20,
        "descricao": "Você canaliza energia celestial para curar as feridas de uma criatura.",
        "tipo_alvo": "aliado_unico",
        "efeitos": [{"tipo": "cura", "escala_com": "sabedoria", "multiplicador_cura": 2.5}]
    },

    # Tiefling
    "resistencia_infernal": {
        "nome": "Resistência Infernal", "tipo": "passiva",
        "descricao": "Seu sangue infernal lhe concede resistência a dano de fogo."
    },
    "magia_das_sombras": {
        "nome": "Magia das Sombras", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 25,
        "descricao": "Você conjura uma escuridão mágica que cega seus inimigos.",
        "tipo_alvo": "inimigos_area",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "cegueira", "duracao": 2, "chance": 0.7}]
    },

    # Goliath
    "resistencia_da_montanha": {
        "nome": "Resistência da Montanha", "tipo": "passiva",
        "descricao": "Você é aclimatado a grandes altitudes e ao frio."
    },
    "forca_do_gigante": {
        "nome": "Força do Gigante", "tipo": "passiva",
        "descricao": "Você conta como sendo uma categoria de tamanho maior para determinar sua capacidade de carga."
    },

    # Halfling
    "sorte_dos_pequenos": {
        "nome": "Sorte dos Pequenos", "tipo": "passiva",
        "descricao": "Quando você rola um 1 em uma jogada de ataque, habilidade ou teste, você pode rolar novamente e usar o segundo resultado."
    },
    "furtividade_natural": {
        "nome": "Furtividade Natural", "tipo": "passiva",
        "descricao": "Você pode tentar se esconder mesmo quando está apenas obscurecido por uma criatura que seja pelo menos um tamanho maior que você."
    },

    # Meio-Elfo
    "heranca_feerica": {
        "nome": "Herança Feérica", "tipo": "passiva",
        "descricao": "Você tem vantagem em testes de resistência contra encantamentos e não pode ser colocado para dormir por magia."
    },
    "habilidade_versatil": {
        "nome": "Habilidade Versátil", "tipo": "passiva",
        "descricao": "Você ganha proficiência em duas perícias de sua escolha."
    },

    # Meio-Orc
    "ataques_selvagens": {
        "nome": "Ataques Selvagens", "tipo": "passiva",
        "descricao": "Quando você consegue um acerto crítico com um ataque corpo a corpo, você pode rolar um dos dados de dano da arma uma vez adicional e adicioná-lo ao dano extra do acerto crítico."
    },
    "resistencia_implacavel": {
        "nome": "Resistência Implacável", "tipo": "passiva",
        "descricao": "Quando você é reduzido a 0 pontos de vida mas não é morto instantaneamente, você pode cair para 1 ponto de vida em vez disso. Você não pode usar esta habilidade novamente até ter um descanso longo."
    },

    # Draconato
    "arma_de_sopro": {
        "nome": "Arma de Sopro", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 35,
        "descricao": "Você expele energia destrutiva. O tipo de dano depende de sua ascendência dracônica.",
        "tipo_alvo": "inimigos_area",
        "efeitos": [{"tipo": "dano_magico", "escala_com": "constituicao", "multiplicador_dano": 2.0, "elemento": "depende_da_variacao"}]
    },
    "resistencia_draconica": {
        "nome": "Resistência Dracônica", "tipo": "passiva",
        "descricao": "Você tem resistência ao tipo de dano associado à sua ascendência dracônica."
    },

    # Genasi
    "poder_elemental": {
        "nome": "Poder Elemental", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 15,
        "descricao": "Você manifesta o poder de seu elemento ancestral. O efeito depende de sua ascendência.",
        "tipo_alvo": "varia",
        "efeitos": []
    },

    # Povo-Lagarto
    "mordida_poderosa": {
        "nome": "Mordida Poderosa", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 10,
        "descricao": "Sua mandíbula é uma arma natural, que você pode usar para fazer um ataque desarmado.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.2}]
    },
    "armadura_natural": {
        "nome": "Armadura Natural", "tipo": "passiva",
        "descricao": "Sua pele escamosa oferece uma proteção natural."
    },
    "prender_a_respiração": {
        "nome": "Prender a Respiração", "tipo": "passiva",
        "descricao": "Você pode prender a respiração por até 15 minutos."
    },

    # Loxodon
    "serenidade_loxodon": {
        "nome": "Serenidade Loxodon", "tipo": "passiva",
        "descricao": "Você tem vantagem em testes de resistência contra ser encantado ou amedrontado."
    },
    "pele_grossa": {
        "nome": "Pele Grossa", "tipo": "passiva",
        "descricao": "Sua pele grossa lhe concede um bônus em sua defesa."
    },
    "tronco_preênsil": {
        "nome": "Tronco Preênsil", "tipo": "passiva",
        "descricao": "Você pode usar sua tromba para realizar tarefas simples."
    },

    # Aarakocra
    "voo": {
        "nome": "Voo", "tipo": "passiva",
        "descricao": "Você tem uma velocidade de voo de 50 pés. Para usar esta velocidade, você não pode estar vestindo armadura média ou pesada."
    },
    "ataque_de_mergulho": {
        "nome": "Ataque de Mergulho", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 20,
        "descricao": "Se você estiver voando e mergulhar pelo menos 30 pés em direção a um alvo e então o atingir com um ataque corpo a corpo no mesmo turno, o alvo sofre dano extra.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": []
    },

    # Tabaxi
    "agilidade_felina": {
        "nome": "Agilidade Felina", "tipo": "ativa", "custo_tipo": "nenhum", "custo_valor": 0,
        "descricao": "Sua agilidade felina permite que você dobre sua velocidade de movimento por um turno. Uma vez que você usa esta habilidade, você não pode usá-la novamente até que se mova 0 pés em um de seus turnos.",
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_agilidade_felina", "duracao": 1}]
    },
    "garras_de_gato": {
        "nome": "Garras de Gato", "tipo": "passiva",
        "descricao": "Você tem uma velocidade de escalada de 20 pés e suas garras são armas naturais."
    },

    # Kenku
    "mimica_perfeita": {
        "nome": "Mímica Perfeita", "tipo": "passiva",
        "descricao": "Você pode imitar sons que já ouviu, incluindo vozes."
    },
    "falsificação_kenku": {
        "nome": "Falsificação Kenku", "tipo": "passiva",
        "descricao": "Você pode duplicar a caligrafia e o artesanato de outras pessoas."
    },

    # Shadar-kai
    "bencao_da_rainha_corvo": {
        "nome": "Bênção da Rainha Corvo", "tipo": "ativa", "custo_tipo": "nenhum", "custo_valor": 0,
        "descricao": "Como uma ação bônus, você pode se teleportar magicamente até 30 pés para um espaço desocupado que você possa ver.",
        "tipo_alvo": "self",
        "efeitos": []
    },
    "resistencia_necrotica": {
        "nome": "Resistência Necrótica", "tipo": "passiva",
        "descricao": "Você tem resistência a dano necrótico."
    },

    # Gith
    "poder_psionico": {
        "nome": "Poder Psiônico", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 10,
        "descricao": "Você pode usar sua mente para empurrar ou puxar objetos e criaturas.",
        "tipo_alvo": "varia",
        "efeitos": []
    },

    # Fada
    "voo_de_fada": {
        "nome": "Voo de Fada", "tipo": "passiva",
        "descricao": "Você tem uma velocidade de voo igual à sua velocidade de caminhada."
    },
    "magia_feerica": {
        "nome": "Magia Feérica", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 15,
        "descricao": "Você pode conjurar pequenas magias de fada, como luzes dançantes ou fogo de fada.",
        "tipo_alvo": "varia",
        "efeitos": []
    },

    # Centauro
    "investida": {
        "nome": "Investida", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 15,
        "descricao": "Se você se mover pelo menos 30 pés em linha reta em direção a um alvo e então o atingir com um ataque corpo a corpo no mesmo turno, o alvo sofre dano extra.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": []
    },
    "cascos": {
        "nome": "Cascos", "tipo": "passiva",
        "descricao": "Seus cascos são armas naturais que podem ser usadas para fazer ataques desarmados."
    },
    "sobrevivente": {
        "nome": "Sobrevivente", "tipo": "passiva",
        "descricao": "Você tem proficiência em uma das seguintes perícias: Sobrevivência, Medicina ou Natureza."
    },

    # Metamorfo (Shifter)
    "transformacao_parcial": {
        "nome": "Transformação Parcial", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 25,
        "descricao": "Você pode assumir uma aparência mais bestial. Isso lhe concede pontos de vida temporários e outros bônus dependendo de sua linhagem.",
        "tipo_alvo": "self",
        "efeitos": []
    },

    # Forjado (Warforged)
    "construcao_resistente": {
        "nome": "Construção Resistente", "tipo": "passiva",
        "descricao": "Você é imune a doenças, não precisa comer, beber ou respirar, e tem vantagem em testes de resistência contra veneno."
    },
    "sentinela_incansavel": {
        "nome": "Sentinela Incansável", "tipo": "passiva",
        "descricao": "Você não precisa dormir e a magia não pode colocá-lo para dormir."
    },

    # Autômato
    "corpo_mecanico": {
        "nome": "Corpo Mecânico", "tipo": "passiva",
        "descricao": "Você é imune a doenças e venenos."
    },
    "processador_logico": {
        "nome": "Processador Lógico", "tipo": "passiva",
        "descricao": "Você tem dificuldade em entender emoções, mas é um mestre da lógica."
    },

    # Doppelganger
    "mudar_aparencia": {
        "nome": "Mudar Aparência", "tipo": "ativa", "custo_tipo": "nenhum", "custo_valor": 0,
        "descricao": "Você pode se transformar em qualquer humanoide que já tenha visto.",
        "tipo_alvo": "self",
        "efeitos": []
    },
    "ler_pensamentos": {
        "nome": "Ler Pensamentos", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 10,
        "descricao": "Você pode ler os pensamentos superficiais de uma criatura próxima.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": []
    },

    # Changeling
    "alterar_feicoes": {
        "nome": "Alterar Feições", "tipo": "ativa", "custo_tipo": "nenhum", "custo_valor": 0,
        "descricao": "Você pode alterar suas características faciais, cabelo e pele à vontade.",
        "tipo_alvo": "self",
        "efeitos": []
    },
    "instintos_enganadores": {
        "nome": "Instintos Enganadores", "tipo": "passiva",
        "descricao": "Você tem proficiência em duas das seguintes perícias: Enganação, Intimidação, Intuição ou Persuasão."
    },

    # Sylvari
    "pele_de_casca": {
        "nome": "Pele de Casca", "tipo": "passiva",
        "descricao": "Sua pele parecida com casca de árvore lhe concede um bônus natural de armadura."
    },
    "comunhao_com_a_natureza": {
        "nome": "Comunhão com a Natureza", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 10,
        "descricao": "Você pode falar com plantas e animais.",
        "tipo_alvo": "self",
        "efeitos": []
    },

    # Minotauro
    "chifres_poderosos": {
        "nome": "Chifres Poderosos", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 15,
        "descricao": "Você pode usar seus chifres como uma arma natural para atacar.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.4}]
    },
    "sentido_do_labirinto": {
        "nome": "Sentido do Labirinto", "tipo": "passiva",
        "descricao": "Você sempre sabe para que lado fica o norte e nunca pode se perder por meios não mágicos."
    },

    # Harpia
    "voo_limitado": {
        "nome": "Voo Limitado", "tipo": "passiva",
        "descricao": "Você pode voar, mas não pode pairar e deve terminar seu turno no chão."
    },
    "cancao_sedutora": {
        "nome": "Canção Sedutora", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 30,
        "descricao": "Você canta uma melodia mágica que atrai as criaturas para perto de você.",
        "tipo_alvo": "inimigos_area",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "atracao", "duracao": 2}]
    },

    # Sátiro
    "performance_cativante": {
        "nome": "Performance Cativante", "tipo": "passiva",
        "descricao": "Você tem proficiência em Performance e pode encantar multidões com sua música ou dança."
    },
    "resistencia_a_magia": {
        "nome": "Resistência à Magia", "tipo": "passiva",
        "descricao": "Você tem vantagem em testes de resistência contra magias e outros efeitos mágicos."
    },

    # Tritão
    "anfibio": {
        "nome": "Anfíbio", "tipo": "passiva",
        "descricao": "Você pode respirar ar e água."
    },
    "guardiao_das_profundezas": {
        "nome": "Guardião das Profundezas", "tipo": "passiva",
        "descricao": "Você tem resistência a dano de frio e ignora os efeitos da pressão do oceano profundo."
    },
    "comunicacao_marinha": {
        "nome": "Comunicação Marinha", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 5,
        "descricao": "Você pode se comunicar de forma simples com bestas que têm uma velocidade de natação inata."
    },

    # Yuan-ti Sangue-Puro
    "vantagem_magica": {
        "nome": "Vantagem Mágica", "tipo": "passiva",
        "descricao": "Você tem vantagem em testes de resistência contra magias."
    },
    "imunidade_a_veneno": {
        "nome": "Imunidade a Veneno", "tipo": "passiva",
        "descricao": "Você é imune a dano de veneno e à condição envenenado."
    },
    "magia_serpentina": {
        "nome": "Magia Serpentina", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 10,
        "descricao": "Você pode conjurar a magia 'Amizade Animal' à vontade, mas apenas em serpentes."
    },

    # Dhampir
    "mordida_vampirica": {
        "nome": "Mordida Vampírica", "tipo": "ativa", "custo_tipo": "stamina", "custo_valor": 10,
        "descricao": "Sua mordida causa dano e cura você por uma parte do dano causado.",
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 1.0}, {"tipo": "roubo_de_vida", "porcentagem": 0.5}]
    },
    "escalar_paredes": {
        "nome": "Escalar Paredes", "tipo": "passiva",
        "descricao": "Você tem uma velocidade de escalada igual à sua velocidade de caminhada."
    },

    # Revenant
    "proposito_inabalavel": {
        "nome": "Propósito Inabalável", "tipo": "passiva",
        "descricao": "Você é imune a ser amedrontado."
    },
    "natureza_implacavel": {
        "nome": "Natureza Implacável", "tipo": "passiva",
        "descricao": "Se você morrer, você retorna à vida após 24 horas, a menos que seu corpo seja completamente destruído ou seu objetivo seja cumprido."
    },

    # Myconid
    "esporos_de_comunicacao": {
        "nome": "Esporos de Comunicação", "tipo": "ativa", "custo_tipo": "nenhum", "custo_valor": 0,
        "descricao": "Você pode liberar esporos que permitem a comunicação telepática com criaturas próximas.",
        "tipo_alvo": "aliados_area",
        "efeitos": []
    },
    "esporos_de_animacao": {
        "nome": "Esporos de Animação", "tipo": "ativa", "custo_tipo": "mp", "custo_valor": 50,
        "descricao": "Você pode animar o corpo de um humanoide ou besta de tamanho médio ou pequeno morto recentemente. Ele se torna um servo zumbi sob seu controle.",
        "tipo_alvo": "cadaver",
        "efeitos": []
    }
}
