# ==============================================================================
# ARQUIVO DE DADOS: EVOLUÇÕES DE RAÇAS
# ==============================================================================
#
# Este arquivo contém as definições para as formas evoluídas das raças base.
# Estas são transformações poderosas que um personagem pode alcançar ao
# cumprir requisitos específicos no jogo.
#
# ==============================================================================

RACAS_EVOLUCOES = {
    # --- Evolução Humana ---
    "semideus": {
        "nome": "Semideus",
        "descricao": "Um mortal que transcendeu suas limitações, infundido com uma centelha de poder divino.",
        "lore": """
Um Semideus é um ser que caminha na linha tênue entre o mortal e o divino. Através de um feito de heroísmo incomparável, do favor direto de um deus, ou do cumprimento de uma antiga profecia, o humano ascendeu. Seu sangue agora canta com poder celestial ou infernal, seus olhos brilham com uma luz interior e sua presença pode inspirar admiração ou terror. Eles não são imortais, mas sua vida é grandemente estendida, e seu potencial, antes vasto, agora se torna quase ilimitado. Esta evolução é o ápice da ambição humana: tocar o divino e não ser consumido por ele.
        """,
        "modificadores_stats_base": {
            "forca": 10, "destreza": 10, "constituicao": 10,
            "inteligencia": 10, "sabedoria": 10, "carisma": 10
        },
        "habilidades_raciais": ["aura_divina", "poder_do_dominio"] # Domínio pode ser Luz, Sombra, Guerra, etc.
    },

    # --- Evolução Élfica ---
    "elfo_eterno": {
        "nome": "Elfo Eterno",
        "descricao": "Um elfo que se tornou um com a magia do mundo, transcendendo o ciclo da vida e da morte.",
        "lore": """
Um Elfo Eterno é um ser de pura magia e memória. Ao beber da lendária Fonte das Eras ou ao dominar um ritual arcano perdido, o elfo para de envelhecer completamente. Sua conexão com a mana se torna tão profunda que eles não mais a conjuram; eles a comandam como uma extensão de seu próprio corpo. Sua pele brilha com uma luz prateada e seus olhos contêm a sabedoria de milênios. Eles são os guardiões vivos da história e da magia, protetores contra cataclismos que poderiam desfazer a própria realidade.
        """,
        "modificadores_stats_base": {
            "destreza": 15, "inteligencia": 15, "sabedoria": 10
        },
        "habilidades_raciais": ["corpo_arcano", "tecero_realidade"]
    },

    # --- Evolução Anã ---
    "senhor_da_runa": {
        "nome": "Senhor da Runa",
        "descricao": "Um mestre artesão que aprendeu os segredos para ligar a magia primordial diretamente ao metal e à pedra.",
        "lore": """
O Senhor da Runa é o ápice da arte anã. Ele não apenas forja uma arma; ele forja uma lenda. Ao redescobrir os segredos da Forja Primordial, este anão aprende a inscrever runas que não apenas encantam um objeto, mas lhe dão uma alma. Sua armadura se torna uma segunda pele de metal vivo, e seu martelo pode quebrar montanhas. Eles são os guardiões da tradição anã, e seu poder reside não em magias chamativas, mas na durabilidade eterna da terra e do aço.
        """,
        "modificadores_stats_base": {
            "constituicao": 15, "forca": 15, "sabedoria": 10
        },
        "habilidades_raciais": ["forja_de_alma", "pele_de_runas"]
    },

    # --- Evolução Orc ---
    "senhor_da_guerra_orc": {
        "nome": "Senhor da Guerra Orc",
        "descricao": "Um orc que se provou o mais forte de seu tempo, um líder nato e um avatar da vontade de Malacath.",
        "lore": """
Um Senhor da Guerra não é apenas o chefe de uma fortaleza; ele é o chefe de todos os orcs. Através de inúmeras batalhas e da conclusão da brutal Prova de Malacath, ele se tornou a personificação da força e da honra orc. Sua voz comanda exércitos, e seu machado decide o destino de nações. Ele não sente mais a necessidade de provar sua força, pois ela é evidente para todos. Ele é o pilar de seu povo, o punho de seu deus, um líder que pode unir os clãs dispersos sob um único estandarte.
        """,
        "modificadores_stats_base": {
            "forca": 20, "constituicao": 15, "carisma": 5
        },
        "habilidades_raciais": ["grito_do_comandante", "furia_imortal"]
    },

    # --- Evolução Gnômica ---
    "mestre_artifice": {
        "nome": "Mestre Artífice",
        "descricao": "Um gnomo cuja mente se tornou uma com a própria arte da criação, capaz de construir maravilhas mecânicas e dobrar as leis da física.",
        "lore": """
O Mestre Artífice transcendeu a simples invenção. Ele não mais constrói máquinas; ele as sonha em existência. Ao construir seu 'Autômato Supremo', uma obra-prima de engenharia e magia, o gnomo alcança uma nova compreensão da realidade. Ele pode ver o mundo como um conjunto de engrenagens e alavancas, e pode 'consertar' ou 'melhorar' a realidade ao seu redor. Ele pode criar autômatos complexos em segundos, dobrar o espaço com dispositivos de teletransporte e criar armas que disparam pura lógica.
        """,
        "modificadores_stats_base": {
            "inteligencia": 20, "destreza": 15, "constituicao": 5
        },
        "habilidades_raciais": ["invocacao_de_automato", "manipular_mecanismo"]
    }
}
