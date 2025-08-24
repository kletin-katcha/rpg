# ==============================================================================
# ARQUIVO DE DADOS: HABILIDADES RACIAIS
# ==============================================================================
#
# Este arquivo contém as definições para todas as habilidades raciais únicas
# mencionadas nas definições de raças em racas_base.py.
#
# ==============================================================================

HABILIDADES_RACIAIS = {
    # Humano
    "esforco_heroico": {"nome": "Esforço Heróico", "descricao": "Passiva: Uma vez por dia, pode escolher ter vantagem em um teste de atributo."},

    # Elfo
    "visao_no_escuro": {"nome": "Visão no Escuro", "descricao": "Passiva: Você enxerga na penumbra como se fosse luz plena, e na escuridão como se fosse penumbra."},
    "afinidade_arcana": {"nome": "Afinidade Arcana", "descricao": "Passiva: O custo de mana para todas as magias é reduzido em 5%."},

    # Anão
    "resistencia_a_veneno": {"nome": "Resistência a Veneno", "descricao": "Passiva: Reduz todo o dano de veneno recebido em 25%."},
    "artesao_de_pedra": {"nome": "Artesão de Pedra", "descricao": "Passiva: Bônus de 10% de chance de sucesso ao criar itens de metal ou pedra."},

    # Orc
    "furor_de_batalha": {"nome": "Furor de Batalha", "descricao": "Ativa: Por 3 turnos, aumenta o dano físico em 25%, mas reduz a defesa em 10%."},

    # Khajiit
    "garras_afiadas": {"nome": "Garras Afiadas", "descricao": "Passiva: Seus ataques desarmados causam dano cortante."},
    "visao_noturna_superior": {"nome": "Visão Noturna Superior", "descricao": "Passiva: Enxerga perfeitamente na escuridão, mesmo a mágica."},

    # Argoniano
    "respirar_agua": {"nome": "Respirar Água", "descricao": "Passiva: Você pode respirar debaixo d'água indefinidamente."},
    "imunidade_a_doenca_veneno": {"nome": "Imunidade a Doença e Veneno", "descricao": "Passiva: Você é imune a todas as doenças e venenos não-mágicos."},
    "pele_hist": {"nome": "Pele de Hist", "descricao": "Ativa: Uma vez por dia, pode regenerar uma grande quantidade de vida rapidamente."},

    # Gnomo
    "mente_mecanica": {"nome": "Mente Mecânica", "descricao": "Passiva: Vantagem em testes para entender ou desarmar mecanismos."},
    "afinidade_com_ilusao": {"nome": "Afinidade com Ilusão", "descricao": "Passiva: O custo de mana para magias de ilusão é reduzido em 15%."},

    # Aasimar
    "resistencia_celestial": {"nome": "Resistência Celestial", "descricao": "Passiva: Reduz o dano de fontes sagradas e necróticas em 10%."},
    "toque_curativo": {"nome": "Toque Curativo", "descricao": "Ativa: Uma vez por dia, pode curar um alvo com um toque."},

    # Tiefling
    "resistencia_infernal": {"nome": "Resistência Infernal", "descricao": "Passiva: Reduz o dano de fogo recebido em 25%."},
    "magia_das_sombras": {"nome": "Magia das Sombras", "descricao": "Ativa: Pode conjurar a magia 'Escuridão' uma vez por dia sem custo de mana."},

    # Goliath
    "resistencia_da_montanha": {"nome": "Resistência da Montanha", "descricao": "Passiva: Reduz o dano de frio recebido em 25% e se aclimatou a grandes altitudes."},
    "forca_do_gigante": {"nome": "Força do Gigante", "descricao": "Passiva: Sua capacidade de carga é dobrada."},

    # Halfling
    "sorte_dos_pequenos": {"nome": "Sorte dos Pequenos", "descricao": "Passiva: Uma vez por dia, pode rolar novamente um teste em que falhou."},
    "furtividade_natural": {"nome": "Furtividade Natural", "descricao": "Passiva: Pode tentar se esconder mesmo quando apenas obscurecido por uma criatura maior."},

    # Meio-Elfo
    "heranca_feerica": {"nome": "Herança Feérica", "descricao": "Passiva: Vantagem em testes contra ser enfeitiçado, e a magia não pode colocá-lo para dormir."},
    "habilidade_versatil": {"nome": "Habilidade Versátil", "descricao": "Passiva: No nível 1, ganha proficiência em duas perícias à sua escolha."},

    # Meio-Orc
    "ataques_selvagens": {"nome": "Ataques Selvagens", "descricao": "Passiva: Quando você obtém um acerto crítico com um ataque corpo a corpo, pode rolar um dos dados de dano da arma uma vez adicional e adicioná-lo ao dano extra do acerto crítico."},
    "resistencia_implacavel": {"nome": "Resistência Implacável", "descricao": "Passiva: Quando você é reduzido a 0 pontos de vida, mas não é morto, você pode cair para 1 ponto de vida em vez disso. Não pode usar esta habilidade novamente até ter um descanso longo."},

    # Draconato
    "arma_de_sopro": {"nome": "Arma de Sopro", "descricao": "Ativa: Expele energia elemental destrutiva. O tipo de dano é determinado pela sua ascendência dracônica."},
    "resistencia_draconica": {"nome": "Resistência Dracônica", "descricao": "Passiva: Você tem resistência ao tipo de dano associado à sua ascendência dracônica."},

    # Genasi
    "poder_elemental": {"nome": "Poder Elemental", "descricao": "Ativa: Dependendo da sua variação elemental, pode conjurar um pequeno feitiço elemental sem custo."},

    # Povo-Lagarto
    "mordida_poderosa": {"nome": "Mordida Poderosa", "descricao": "Ativa: Faz um ataque desarmado com sua mordida."},
    "armadura_natural": {"nome": "Armadura Natural", "descricao": "Passiva: Sua pele escamosa fornece uma base de defesa física."},
    "prender_a_respiração": {"nome": "Prender a Respiração", "descricao": "Passiva: Pode prender a respiração por até 15 minutos."},

    # Loxodon
    "serenidade_loxodon": {"nome": "Serenidade Loxodon", "descricao": "Passiva: Vantagem em testes contra ser enfeitiçado ou amedrontado."},
    "pele_grossa": {"nome": "Pele Grossa", "descricao": "Passiva: Bônus na defesa física."},
    "tronco_preênsil": {"nome": "Tronco Preênsil", "descricao": "Passiva: Pode usar seu tronco para interagir com objetos."},

    # Aarakocra
    "voo": {"nome": "Voo", "descricao": "Passiva: Você tem uma velocidade de voo."},
    "ataque_de_mergulho": {"nome": "Ataque de Mergulho", "descricao": "Ativa: Se estiver voando e mergulhar pelo menos 9 metros em direção a um alvo, causa dano extra."},

    # Tabaxi
    "agilidade_felina": {"nome": "Agilidade Felina", "descricao": "Ativa: Pode dobrar sua velocidade de movimento por um turno. Precisa descansar um turno para usar novamente."},
    "garras_de_gato": {"nome": "Garras de Gato", "descricao": "Passiva: Seus ataques desarmados causam dano e você tem uma velocidade de escalada."},

    # Kenku
    "mimica_perfeita": {"nome": "Mímica Perfeita", "descricao": "Passiva: Pode imitar perfeitamente qualquer som que já ouviu."},
    "falsificação_kenku": {"nome": "Falsificação Kenku", "descricao": "Passiva: Vantagem em testes para criar cópias de documentos ou caligrafia."},

    # Shadar-kai
    "bencao_da_rainha_corvo": {"nome": "Bênção da Rainha Corvo", "descricao": "Ativa: Teletransporta-se para um local desocupado que possa ver. Ganha resistência a todo dano até o final do seu turno."},
    "resistencia_necrotica": {"nome": "Resistência Necrótica", "descricao": "Passiva: Reduz o dano necrótico recebido."},

    # Gith
    "poder_psionico": {"nome": "Poder Psiônico", "descricao": "Passiva: Conhece o truque 'Mão Mágica' e pode conjurar outros feitiços psiônicos em níveis mais altos."},

    # Fada
    "voo_de_fada": {"nome": "Voo de Fada", "descricao": "Passiva: Você pode voar."},
    "magia_feerica": {"nome": "Magia Feérica", "descricao": "Ativa: Pode conjurar magias de fada, como 'Fogo das Fadas'."},

    # Centauro
    "investida": {"nome": "Investida", "descricao": "Ativa: Se mover pelo menos 9 metros em linha reta antes de atacar, causa dano extra."},
    "cascos": {"nome": "Cascos", "descricao": "Passiva: Seus cascos são armas naturais."},
    "sobrevivente": {"nome": "Sobrevivente", "descricao": "Passiva: Proficiência em perícias de sobrevivência."},

    # Metamorfo
    "transformacao_parcial": {"nome": "Transformação Parcial", "descricao": "Ativa: Assume traços bestiais por 1 minuto, ganhando benefícios baseados na sua variação."},

    # Forjado
    "construcao_resistente": {"nome": "Construção Resistente", "descricao": "Passiva: Vantagem contra veneno, não precisa comer, beber ou respirar, e imune a doenças."},
    "sentinela_incansavel": {"nome": "Sentinela Incansável", "descricao": "Passiva: Não precisa dormir e a magia não pode colocá-lo para dormir."},

    # Autômato
    "corpo_mecanico": {"nome": "Corpo Mecânico", "descricao": "Passiva: Imune a doenças, não precisa comer ou beber."},
    "processador_logico": {"nome": "Processador Lógico", "descricao": "Passiva: Adiciona bônus a testes de perícia específicos."},

    # Doppelganger
    "mudar_aparencia": {"nome": "Mudar Aparência", "descricao": "Ativa: Transforma-se em qualquer humanoide que já viu."},
    "ler_pensamentos": {"nome": "Ler Pensamentos", "descricao": "Ativa: Sonda a mente de uma criatura para ler seus pensamentos superficiais."},

    # Changeling
    "alterar_feicoes": {"nome": "Alterar Feições", "descricao": "Ativa: Muda suas características faciais, cabelo e pele à vontade."},
    "instintos_enganadores": {"nome": "Instintos Enganadores", "descricao": "Passiva: Proficiência em perícias de engano."},

    # Sylvari
    "pele_de_casca": {"nome": "Pele de Casca", "descricao": "Passiva: Sua pele semelhante a casca de árvore lhe concede um bônus na defesa."},
    "comunhao_com_a_natureza": {"nome": "Comunhão com a Natureza", "descricao": "Ativa: Pode falar com plantas e animais."},

    # Minotauro
    "chifres_poderosos": {"nome": "Chifres Poderosos", "descricao": "Passiva: Seus chifres são uma arma natural."},
    "sentido_do_labirinto": {"nome": "Sentido do Labirinto", "descricao": "Passiva: Você não pode se perder por meios não-mágicos."},

    # Harpia
    "voo_limitado": {"nome": "Voo Limitado", "descricao": "Passiva: Você tem uma velocidade de voo, mas não pode voar com armadura pesada."},
    "cancao_sedutora": {"nome": "Canção Sedutora", "descricao": "Ativa: Canta uma melodia que pode enfeitiçar aqueles que a ouvem."},

    # Sátiro
    "performance_cativante": {"nome": "Performance Cativante", "descricao": "Passiva: Proficiência em performance e instrumentos musicais."},
    "resistencia_a_magia": {"nome": "Resistência à Magia", "descricao": "Passiva: Vantagem em testes de resistência contra magias."},

    # Tritão
    "anfibio": {"nome": "Anfíbio", "descricao": "Passiva: Pode respirar ar e água."},
    "guardiao_das_profundezas": {"nome": "Guardião das Profundezas", "descricao": "Passiva: Resistência a dano de frio."},
    "comunicacao_marinha": {"nome": "Comunicação Marinha", "descricao": "Ativa: Pode se comunicar de forma simples com bestas que vivem na água."},

    # Yuan-ti
    "vantagem_magica": {"nome": "Vantagem Mágica", "descricao": "Passiva: Vantagem em testes de resistência contra magias e outros efeitos mágicos."},
    "imunidade_a_veneno": {"nome": "Imunidade a Veneno", "descricao": "Passiva: Você é imune a dano de veneno e à condição envenenado."},
    "magia_serpentina": {"nome": "Magia Serpentina", "descricao": "Ativa: Conhece o truque 'Rajada de Veneno' e pode conjurar 'Amizade Animal' (apenas em cobras)."},

    # Dhampir
    "mordida_vampirica": {"nome": "Mordida Vampírica", "descricao": "Ativa: Faz um ataque com sua mordida. Se acertar, pode recuperar vida igual ao dano causado."},
    "escalar_paredes": {"nome": "Escalar Paredes", "descricao": "Passiva: Você tem uma velocidade de escalada igual à sua velocidade de caminhada."},

    # Revenant
    "proposito_inabalavel": {"nome": "Propósito Inabalável", "descricao": "Passiva: Vantagem contra ser enfeitiçado ou amedrontado."},
    "natureza_implacavel": {"nome": "Natureza Implacável", "descricao": "Passiva: Você não precisa dormir e é imune à exaustão."},

    # Myconid
    "esporos_de_comunicacao": {"nome": "Esporos de Comunicação", "descricao": "Ativa: Libera esporos que permitem a comunicação telepática com criaturas próximas."},
    "esporos_de_animacao": {"nome": "Esporos de Animação", "descricao": "Ativa: Anima o cadáver de uma criatura pequena ou média para lutar por você por 1 hora."},

    # --- HABILIDADES DE RAÇAS EVOLUÍDAS ---

    # Semideus
    "aura_divina": {"nome": "Aura Divina", "descricao": "Passiva: Você emana uma aura que inspira aliados e desmoraliza inimigos em um raio próximo, concedendo pequenos bônus e penalidades."},
    "poder_do_dominio": {"nome": "Poder do Domínio", "descricao": "Ativa: Libera uma onda de energia do seu domínio divino (Luz, Sombra, etc.), causando um efeito massivo."},

    # Elfo Eterno
    "corpo_arcano": {"nome": "Corpo Arcano", "descricao": "Passiva: Você não é mais considerado um humanoide, mas sim um elemental. Você é imune a venenos, doenças e não precisa dormir."},
    "tecero_realidade": {"nome": "Tecer a Realidade", "descricao": "Ativa: Uma vez por semana, pode alterar um evento recente de pequena escala (ex: refazer um teste de perícia falho)."},

    # Senhor da Runa
    "forja_de_alma": {"nome": "Forja de Alma", "descricao": "Passiva: Pode vincular sua alma a uma arma ou armadura, fazendo com que ela suba de nível com você."},
    "pele_de_runas": {"nome": "Pele de Runas", "descricao": "Ativa: Runas de proteção brilham em sua pele, absorvendo uma grande quantidade de dano mágico."},

    # Senhor da Guerra Orc
    "grito_do_comandante": {"nome": "Grito do Comandante", "descricao": "Ativa: Um grito de guerra que concede a todos os aliados um turno de ação extra."},
    "furia_imortal": {"nome": "Fúria Imortal", "descricao": "Passiva: Se você fosse morrer, em vez disso, fica com 1 ponto de vida e se torna imune a dano por 1 turno. Usos limitados."},

    # Mestre Artífice
    "invocacao_de_automato": {"nome": "Invocação de Autômato", "descricao": "Ativa: Constrói e invoca um poderoso autômato de combate para lutar ao seu lado."},
    "manipular_mecanismo": {"nome": "Manipular Mecanismo", "descricao": "Ativa: Pode instantaneamente desarmar uma armadilha mecânica ou travar uma arma de um inimigo por um turno."}
}
