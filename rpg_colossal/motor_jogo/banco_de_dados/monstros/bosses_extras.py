# -*- coding: utf-8 -*-
"""
################################################################################################
##                                                                                            ##
##    ██████╗  ██████╗ ███████╗███████╗    ██╗   ██╗██╗████████╗██████╗  █████╗ ███████╗         ##
##    ██╔══██╗██╔═══██╗██╔════╝██╔════╝    ██║   ██║██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝         ##
##    ██████╔╝██║   ██║███████╗███████╗    ██║   ██║██║   ██║   ██████╔╝███████║███████╗         ##
##    ██╔══██╗██║   ██║╚════██║╚════██║    ██║   ██║██║   ██║   ██╔══██╗██╔══██║╚════██║         ##
##    ██║  ██║╚██████╔╝███████║███████║    ╚██████╔╝██║   ██║   ██║  ██║██║  ██║███████║         ##
##    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝     ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝         ##
##                                                                                            ##
################################################################################################
################################################################################################

================================================================================================
BANCO DE DADOS: BOSSES EXTRAS E OPCIONAIS
================================================================================================
Este arquivo contém as definições de chefes extras, opcionais ou secretos que o jogador
pode encontrar em Aetheria. Diferente do boss final, estas lutas são desafios únicos
que recompensam a exploração e a curiosidade do jogador com loot e lore especiais.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
from typing import List, Dict, Any

# ==============================================================================================
# == LISTA DE BOSSES EXTRAS ====================================================================
# ==============================================================================================
BOSSES_EXTRAS = [
    {
        "id": "boss_dragao_ancestral_ignis",
        "nome": "Ignis, o Dragão Ancestral",
        "nivel": 50,
        "hp": 15000,
        "atributos": {"forca": 35, "destreza": 15, "defesa": 30, "resistencia_fogo": 0.9, "vulnerabilidade_gelo": 0.5},
        "habilidades": ["sk_dragao_sopro_de_fogo_avassalador", "sk_dragao_batida_de_asa", "sk_dragao_cauda_varredora"],
        "mecanicas_especiais": ["Fúria do Dragão: Abaixo de 50% de HP, seus ataques de sopro cobrem uma área maior e aplicam uma queimadura mais forte."],
        "dialogos": {},
        "descricao": "Um dragão vermelho colossal, antigo como as próprias montanhas. Suas escamas brilham como brasas e seu rugido pode derreter rochas. Ele guarda um tesouro acumulado ao longo de milênios em sua toca vulcânica.",
        "loot_especial": ["item_escama_de_ignis", "item_tesouro_do_dragao"]
    },
    {
        "id": "boss_lich_veklor",
        "nome": "Vek'lor, o Lich",
        "nivel": 45,
        "hp": 8000,
        "atributos": {"inteligencia": 40, "sabedoria": 35, "defesa": 15, "imunidade": ["veneno", "necrotico"]},
        "habilidades": ["sk_lich_toque_da_morte", "sk_lich_invocar_esqueletos", "sk_lich_drenar_vida"],
        "mecanicas_especiais": ["Filactério: Enquanto seu filactério estiver escondido na dungeon, Vek'lor se regenerará lentamente durante o combate. Destruir o filactério antes da luta o enfraquece permanentemente."],
        "dialogos": {"inicio_luta": "Tolos... Acham que podem desafiar a própria morte?"},
        "descricao": "Um mestre necromante que alcançou a imortalidade através de um ritual profano. Vek'lor comanda legiões de mortos-vivos de sua cripta escura, buscando poder para mergulhar o mundo em uma noite eterna.",
        "loot_especial": ["item_filacterio_de_veklor_quebrado", "item_cajado_do_necromante"]
    },
    {
        "id": "boss_colosso_de_pedra",
        "nome": "O Colosso de Pedra Adormecido",
        "nivel": 40,
        "hp": 20000,
        "atributos": {"forca": 50, "destreza": 5, "defesa": 50, "imunidade": ["critico", "veneno", "sangramento"]},
        "habilidades": ["sk_colosso_terremoto", "sk_colosso_pisao_esmagador"],
        "mecanicas_especiais": ["Pontos Fracos: O Colosso é imune a dano na maior parte do corpo. O jogador deve atacar pontos fracos específicos (runas em seus joelhos e costas) que são revelados após certas ações para poder causar dano significativo."],
        "dialogos": {},
        "descricao": "Um golem gigantesco do tamanho de uma colina, criado por uma civilização perdida para proteger algo de grande poder. Ele permaneceu adormecido por eras, coberto de musgo e árvores, mas despertará para esmagar qualquer um que se aproxime de seu tesouro.",
        "loot_especial": ["item_coracao_do_colosso", "item_tablete_runico_antigo"]
    },
    {
        "id": "boss_hydra_abissal",
        "nome": "Hydra Abissal",
        "nivel": 35,
        "hp": 10000,
        "atributos": {"forca": 25, "destreza": 18, "defesa": 18},
        "habilidades": ["sk_hydra_mordida_multipla", "sk_hydra_sopro_acido", "sk_hydra_regeneracao"],
        "mecanicas_especiais": ["Regeneração de Cabeças: A cada 20% de HP perdido, uma nova cabeça cresce, permitindo que a Hydra use 'Mordida Múltipla' mais uma vez por turno. As cabeças só param de crescer se o dano final for de fogo ou ácido."],
        "dialogos": {},
        "descricao": "Uma monstruosidade de múltiplas cabeças que habita as profundezas do Pântano das Almas Perdidas. Cada cabeça age de forma independente, e cortá-las apenas parece fortalecer a criatura.",
        "loot_especial": ["item_dente_de_hydra", "item_sangue_regenerativo_de_hydra"]
    },
    {
        "id": "boss_doppelganger_mestre",
        "nome": "O Doppelganger Mestre",
        "nivel": "variavel",
        "hp": "variavel",
        "atributos": {},
        "habilidades": [],
        "mecanicas_especiais": ["Cópia Perfeita: O Doppelganger copia a aparência, os atributos e as habilidades do personagem do jogador no início do combate. A luta é um espelho de si mesmo, exigindo que o jogador explore suas próprias fraquezas."],
        "dialogos": {"inicio_luta": "Vamos ver do que você é realmente feito... ou melhor, do que EU sou feito."},
        "descricao": "Uma criatura metamorfa que alcançou o ápice de sua habilidade. Não tem forma própria, existindo apenas como um reflexo perfeito de seu oponente mais forte. Encontrá-lo é um teste de autoconhecimento.",
        "loot_especial": ["item_espelho_da_alma_rachado"]
    },
]

# ==============================================================================================
# == CONSTRUÇÃO DO ÍNDICE DE BOSSES ============================================================
# ==============================================================================================
def construir_indice(lista_de_dados: List[Dict]) -> Dict:
    """Constrói um dicionário indexado por ID a partir de uma lista."""
    indice_por_id = {item["id"]: item for item in lista_de_dados}
    return {"by_id": indice_por_id, "lista_completa": lista_de_dados}

INDICE_BOSSES_EXTRAS = construir_indice(BOSSES_EXTRAS)
