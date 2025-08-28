# ==============================================================================
# ARQUIVO DE DADOS: ITENS RAROS
# ==============================================================================
#
# Este arquivo contém as definições para itens de raridade Rara.
# Estes itens são significativamente mais poderosos que os comuns e
# geralmente possuem encantamentos ou propriedades especiais.
#
# ==============================================================================

from ..entidades.item import TipoItem, RaridadeItem

ITENS_RAROS = {
    "espada_do_cavaleiro_solar": {
        "nome": "Espada do Cavaleiro Solar",
        "descricao": "Uma espada longa que brilha com uma luz fraca. Dizem que foi forjada sob o sol do meio-dia.",
        "lore": "Pertenceu a Sir Gideon, um cavaleiro de uma ordem solar há muito esquecida. A lâmina parece nunca perder o fio e é especialmente eficaz contra criaturas da noite.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.RARO, "valor": 350,
        "slot_equipamento": "arma_principal",
        "modificadores": {
            "ataque_fisico": 15,
            "dano_magico_extra": {"elemento": "sagrado", "quantidade": 8}
        },
        "requisitos": {"nivel": 10, "forca": 15}
    },
    "arco_de_teixo_elfico": {
        "nome": "Arco de Teixo Élfico",
        "descricao": "Um arco longo feito da madeira de um teixo antigo, com runas élficas que guiam a flecha.",
        "lore": "Cada um desses arcos leva uma década para ser esculpido e encantado por um mestre arqueiro élfico. A madeira 'lembra' o caminho da flecha, tornando os tiros incrivelmente precisos.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.RARO, "valor": 400,
        "slot_equipamento": "arma_principal",
        "modificadores": {
            "ataque_fisico": 10,
            "precisao": 25
        },
        "requisitos": {"nivel": 12, "destreza": 20}
    },
    "cota_de_malha_anã_reforcada": {
        "nome": "Cota de Malha Anã Reforçada",
        "descricao": "Uma cota de malha feita com anéis de aço anão, surpreendentemente leve para sua resistência.",
        "lore": "Forjada nas profundezas de uma fortaleza anã, cada anel desta armadura foi temperado em cerveja e abençoado com runas de proteção. É dito que pode parar a mordida de um dragão... talvez um filhote.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.RARO, "valor": 500,
        "slot_equipamento": "peitoral",
        "modificadores": {
            "defesa_fisica": 25,
            "resistencia_fisico": 0.05 # 5% de resistência a dano físico
        },
        "requisitos": {"nivel": 15, "constituicao": 18}
    },
    "robe_do_arquimago_aprendiz": {
        "nome": "Robe do Arquimago Aprendiz",
        "descricao": "Um robe de seda encantado que parece cintilar com poder arcano. Aumenta a reserva de mana do usuário.",
        "lore": "Este robe foi o trabalho de conclusão de curso de um promissor aprendiz de arquimago. As runas bordadas nos punhos e na gola ajudam a regular o fluxo de mana, permitindo que magias mais complexas sejam tecidas com menos esforço.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.RARO, "valor": 300,
        "slot_equipamento": "peitoral",
        "modificadores": {
            "defesa_magica": 15,
            "mp_max": 50
        },
        "requisitos": {"nivel": 8, "inteligencia": 15}
    },
    "pocao_de_cura_maior": {
        "nome": "Poção de Cura Maior",
        "descricao": "Um líquido vibrante que fecha feridas profundas em segundos.",
        "lore": "Criada por alquimistas mestres, esta poção usa ingredientes raros como lágrimas de grifo e pó de chifre de unicórnio.",
        "tipo": TipoItem.POCAO, "raridade": RaridadeItem.RARO, "valor": 200,
        "empilhavel": True, "max_pilha": 10,
        "efeito_consumo": {"tipo": "cura_hp", "quantidade": 250}
    }
}
