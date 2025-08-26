# ==============================================================================
# ARQUIVO DE DADOS: ITENS COMUNS
# ==============================================================================
#
# Este arquivo contém as definições para itens de raridade Comum.
# A estrutura é um dicionário onde a chave é o ID do item.
#
# Estrutura de cada Item:
# ------------------------
# Ver a classe Item em rpg/entidades/item.py para a estrutura completa.
#
# ==============================================================================

from ..entidades.item import TipoItem, RaridadeItem

ITENS_COMUNS = {
    # --- EQUIPAMENTOS INICIAIS ---
    "espada_curta_ferro": {
        "nome": "Espada Curta de Ferro", "descricao": "Uma espada curta, simples e confiável. Comum entre aventureiros iniciantes.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 25,
        "slot_equipamento": "arma_principal",
        "modificadores": {"dano_arma": 8}
    },
    "adaga_de_ferro": {
        "nome": "Adaga de Ferro", "descricao": "Uma adaga leve, ideal para ataques rápidos ou para ser usada na mão inábil.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 15,
        "slot_equipamento": "arma_principal",
        "modificadores": {"dano_arma": 5, "chance_critico": 0.02}
    },
    "cajado_de_aprendiz": {
        "nome": "Cajado de Aprendiz", "descricao": "Um cajado de madeira com um pequeno cristal na ponta. Ajuda a canalizar as primeiras magias.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 20,
        "slot_equipamento": "arma_principal",
        "modificadores": {"poder_magico": 4}
    },
    "maca_simples": {
        "nome": "Maça Simples", "descricao": "Uma arma de impacto direta e eficaz, boa para amassar armaduras e ossos.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 22,
        "slot_equipamento": "arma_principal",
        "modificadores": {"dano_arma": 10}
    },
    "peitoral_de_couro_batido": {
        "nome": "Peitoral de Couro Batido", "descricao": "Oferece proteção modesta sem restringir muito os movimentos.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 30,
        "slot_equipamento": "peitoral",
        "modificadores": {"defesa_fisica": 8}
    },
    "armadura_de_couro_leve": {
        "nome": "Armadura de Couro Leve", "descricao": "Feita para agilidade, oferece menos proteção mas não atrapalha a esquiva.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 25,
        "slot_equipamento": "peitoral",
        "modificadores": {"defesa_fisica": 5, "esquiva": 3}
    },
    "tunica_simples": {
        "nome": "Túnica Simples", "descricao": "Roupas simples de tecido, preferidas por magos por não interferir com gestos arcanos.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 10,
        "slot_equipamento": "peitoral",
        "modificadores": {"defesa_magica": 4}
    },
    "cota_de_malha": {
        "nome": "Cota de Malha", "descricao": "Uma armadura de anéis de metal interligados. Oferece boa proteção física, mas é pesada.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 50,
        "slot_equipamento": "peitoral",
        "modificadores": {"defesa_fisica": 12}
    },
    "escudo_de_madeira": {
        "nome": "Escudo de Madeira", "descricao": "Um escudo básico de madeira, melhor que nada.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 15,
        "slot_equipamento": "arma_secundaria",
        "modificadores": {"defesa_fisica": 5}
    },

    # --- CONSUMÍVEIS ---
    "pocao_cura_fraca": {
        "nome": "Poção de Cura Fraca", "descricao": "Um líquido avermelhado que restaura uma pequena quantidade de vida.",
        "tipo": TipoItem.POCAO, "raridade": RaridadeItem.COMUM, "valor": 25,
        "empilhavel": True, "max_pilha": 10,
        "efeito_consumo": {"tipo": "cura_hp", "quantidade": 50}
    },

    # --- MATERIAIS DE LOOT ---
    "pele_de_lobo": {
        "nome": "Pele de Lobo", "descricao": "Uma pele de lobo cinzento, útil para artesanato em couro.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.COMUM, "valor": 5,
        "empilhavel": True, "max_pilha": 20
    },
    "dente_de_lobo": {
        "nome": "Dente de Lobo", "descricao": "Um dente afiado de um lobo. Pode ser usado em alquimia ou para fazer amuletos.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.COMUM, "valor": 2,
        "empilhavel": True, "max_pilha": 50
    },
    "caco_de_arma_enferrujada": {
        "nome": "Caco de Arma Enferrujada", "descricao": "Um pedaço de metal que já foi uma arma goblin. Inútil em combate, mas pode ser derretido.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.COMUM, "valor": 1,
        "empilhavel": True, "max_pilha": 10
    },
    "carne_de_javali": {
        "nome": "Carne de Javali", "descricao": "Carne de caça. Pode ser cozida para criar um alimento que recupera vida.",
        "tipo": TipoItem.INGREDIENTE, "raridade": RaridadeItem.COMUM, "valor": 8,
        "empilhavel": True, "max_pilha": 10
    },
    "presa_de_javali": {
        "nome": "Presa de Javali", "descricao": "Uma presa grande e amarelada. Valorizada por alguns artesãos.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.COMUM, "valor": 12,
        "empilhavel": True, "max_pilha": 10
    },
    "ferrao_de_vespa": {
        "nome": "Ferrão de Vespa", "descricao": "O ferrão de uma vespa gigante. Afiado e oco.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.COMUM, "valor": 3,
        "empilhavel": True, "max_pilha": 30
    },
    "glandula_de_veneno_fraca": {
        "nome": "Glândula de Veneno Fraca", "descricao": "Uma glândula contendo um veneno de baixa potência. Ingrediente chave para poções venenosas.",
        "tipo": TipoItem.INGREDIENTE, "raridade": RaridadeItem.COMUM, "valor": 20,
        "empilhavel": True, "max_pilha": 5
    },
    "gosma_de_slime": {
        "nome": "Gosma de Slime", "descricao": "Uma substância pegajosa e levemente ácida. Usada como base em várias poções alquímicas.",
        "tipo": TipoItem.INGREDIENTE, "raridade": RaridadeItem.COMUM, "valor": 2,
        "empilhavel": True, "max_pilha": 50
    },
    "machado_de_batalha_ferro": {
        "nome": "Machado de Batalha de Ferro", "descricao": "Um machado de uma mão com uma lâmina pesada, capaz de causar ferimentos graves.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 35,
        "slot_equipamento": "arma_principal",
        "modificadores": {"dano_arma": 12, "dano_critico": 0.1}
    },

    # --- MATERIAIS DO PÂNTANO (ÁREA 2) ---
    "glandula_de_sanguessuga": {
        "nome": "Glândula de Sanguessuga", "descricao": "Uma glândula pulsante de uma sanguessuga. Usada em poções de cura mais potentes.",
        "tipo": TipoItem.INGREDIENTE, "raridade": RaridadeItem.COMUM, "valor": 30,
        "empilhavel": True, "max_pilha": 10
    },
    "escama_de_homem_lagarto": {
        "nome": "Escama de Homem-Lagarto", "descricao": "Uma escama verde e resistente, ideal para fazer armaduras leves.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.COMUM, "valor": 15,
        "empilhavel": True, "max_pilha": 20
    },
    "lanca_primitiva": {
        "nome": "Lança Primitiva", "descricao": "Uma lança rústica feita de madeira do pântano e uma ponta de osso afiado.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 40,
        "slot_equipamento": "arma_principal",
        "modificadores": {"dano_arma": 14}
    },
    "essencia_espectral": {
        "nome": "Essência Espectral", "descricao": "Os restos translúcidos e frios de um espectro. Brilha com uma luz fraca.",
        "tipo": TipoItem.INGREDIENTE, "raridade": RaridadeItem.COMUM, "valor": 50,
        "empilhavel": True, "max_pilha": 5
    },
    "po_ectoplasmico": {
        "nome": "Pó Ectoplásmico", "descricao": "Um pó fino e pegajoso deixado para trás por uma manifestação espiritual.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.COMUM, "valor": 25,
        "empilhavel": True, "max_pilha": 15
    },
    "couro_de_crocodilo_gigante": {
        "nome": "Couro de Crocodilo Gigante", "descricao": "Um pedaço de couro extremamente grosso e durável.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.COMUM, "valor": 80,
        "empilhavel": True, "max_pilha": 5
    },
    "dente_de_crocodilo_gigante": {
        "nome": "Dente de Crocodilo Gigante", "descricao": "Um dente do tamanho de uma adaga. Pode ser usado para criar armas poderosas.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.COMUM, "valor": 45,
        "empilhavel": True, "max_pilha": 10
    },
    "escama_de_hydra": {
        "nome": "Escama de Hydra", "descricao": "Uma escama com um brilho estranho, resistente a quase tudo.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.INCOMUM, "valor": 150,
        "empilhavel": True, "max_pilha": 10
    },
    "sangue_de_hydra": {
        "nome": "Sangue de Hydra", "descricao": "Um sangue verde e borbulhante com potentes propriedades regenerativas e cáusticas.",
        "tipo": TipoItem.INGREDIENTE, "raridade": RaridadeItem.RARO, "valor": 300,
        "empilhavel": True, "max_pilha": 5
    },
    "coracao_de_hydra": {
        "nome": "Coração de Hydra", "descricao": "Um coração que ainda pulsa fracamente. Um ingrediente de poder lendário.",
        "tipo": TipoItem.INGREDIENTE, "raridade": RaridadeItem.LENDARIO, "valor": 1000,
        "empilhavel": False
    }
}
