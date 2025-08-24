# ==============================================================================
# ARQUIVO DE DADOS: QUESTS - ATO 1
# ==============================================================================
#
# Este arquivo contém as definições para as missões principais do Ato 1:
# O Despertar do Herói.
#
# ==============================================================================

from ..entidades.quest import TipoQuest

QUESTS_ATO1 = {
    "mq01_despertar": {
        "titulo": "Um Despertar Nebuloso",
        "descricao_inicio": "Você acorda em uma cama rústica, com o cheiro de ervas no ar. Sua cabeça dói e suas memórias estão em branco. Uma curandeira local, Elara, olha para você com preocupação. Ela diz que o encontrou desmaiado na floresta.",
        "ato_narrativo": 1,
        "tipo": TipoQuest.PRINCIPAL,
        "npc_inicio": "elara_curandeira",
        "objetivos": [
            {"tipo": "falar_com", "id_alvo": "elara_curandeira", "progresso": 0, "total": 1, "descricao": "Fale com Elara para entender o que aconteceu."}
        ],
        "recompensas": {"xp": 50}
    },
    "mq02_ameaca_local": {
        "titulo": "A Ameaça na Floresta",
        "descricao_inicio": "Elara lhe pede um favor. A vila tem sido atormentada por goblins agressivos da Floresta dos Sussurros. Ela pede que você investigue e, se possível, reduza o número deles para que os lenhadores possam voltar a trabalhar em segurança.",
        "ato_narrativo": 1,
        "tipo": TipoQuest.PRINCIPAL,
        "npc_inicio": "elara_curandeira",
        "pre_requisitos": ["mq01_despertar"],
        "objetivos": [
            {"tipo": "matar", "id_alvo": "goblin_batedor", "progresso": 0, "total": 5, "descricao": "Derrote 5 Batedores Goblins."},
            {"tipo": "retornar_para", "id_alvo": "elara_curandeira", "progresso": 0, "total": 1, "descricao": "Volte para Elara com notícias."}
        ],
        "recompensas": {
            "xp": 200,
            "ouro": 50,
            "itens": [{"id_item": "pocao_cura_fraca", "quantidade": 3}]
        }
    },
    "mq03_primeira_sombra": {
        "titulo": "A Primeira Sombra",
        "descricao_inicio": "Ao derrotar os goblins, você encontra um amuleto estranho e sombrio em seu líder, algo que não parece ser de fabricação goblin. Elara fica pálida ao vê-lo. Ela diz que o amuleto pertence a um culto sombrio que se pensava ter sido erradicado há muito tempo. Ela o incita a levar o amuleto para o capitão da guarda na cidade vizinha de Ponte Branca.",
        "ato_narrativo": 1,
        "tipo": TipoQuest.PRINCIPAL,
        "npc_inicio": "elara_curandeira",
        "pre_requisitos": ["mq02_ameaca_local"],
        "objetivos": [
            {"tipo": "viajar_para", "id_alvo": "cidade_ponte_branca", "progresso": 0, "total": 1, "descricao": "Vá para a cidade de Ponte Branca."},
            {"tipo": "falar_com", "id_alvo": "capitao_da_guarda_valerius", "progresso": 0, "total": 1, "descricao": "Mostre o amuleto para o Capitão Valerius."}
        ],
        "recompensas": {
            "xp": 350,
            "ouro": 100,
            "itens": [{"id_item": "carta_de_recomendacao_ponte_branca", "quantidade": 1}]
        }
    }
}
