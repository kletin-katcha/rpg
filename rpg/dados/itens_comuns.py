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
        "modificadores": {"ataque_fisico": 5}
    },
    "adaga_de_ferro": {
        "nome": "Adaga de Ferro", "descricao": "Uma adaga leve, ideal para ataques rápidos ou para ser usada na mão inábil.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 15,
        "slot_equipamento": "arma_principal", # Pode ser equipada em qualquer mão
        "modificadores": {"ataque_fisico": 3, "chance_critico": 0.02}
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
        "modificadores": {"ataque_fisico": 6}
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
        "tipo": TipoItem.ARMADUA, "raridade": RaridadeItem.COMUM, "valor": 50,
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

    # --- EXPANSÃO DE EQUIPAMENTOS COMUNS ---
    # Armas
    "arco_curto_simples": {
        "nome": "Arco Curto Simples", "descricao": "Um arco de madeira simples, bom para caça ou para um arqueiro iniciante.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 28,
        "slot_equipamento": "arma_principal",
        "modificadores": {"ataque_fisico": 4, "precisao": 5}
    },
    "machado_de_batalha_ferro": {
        "nome": "Machado de Batalha de Ferro", "descricao": "Um machado de uma mão com uma lâmina pesada, capaz de causar ferimentos graves.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 35,
        "slot_equipamento": "arma_principal",
        "modificadores": {"ataque_fisico": 7, "dano_critico": 0.1}
    },
    "lanca_curta": {
        "nome": "Lança Curta", "descricao": "Uma lança simples, boa para manter os inimigos a uma pequena distância.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 20,
        "slot_equipamento": "arma_principal",
        "modificadores": {"ataque_fisico": 6}
    },
    # Armaduras
    "elmo_de_ferro": {
        "nome": "Elmo de Ferro", "descricao": "Um capacete de ferro básico que oferece boa proteção para a cabeça.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 25,
        "slot_equipamento": "elmo",
        "modificadores": {"defesa_fisica": 4}
    },
    "botas_de_couro": {
        "nome": "Botas de Couro", "descricao": "Botas resistentes que protegem os pés sem fazer muito barulho.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 15,
        "slot_equipamento": "botas",
        "modificadores": {"defesa_fisica": 2, "esquiva": 1}
    },
    "luvas_de_ferro": {
        "nome": "Luvas de Ferro", "descricao": "Manoplas de ferro que protegem as mãos e os antebraços.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 18,
        "slot_equipamento": "luvas",
        "modificadores": {"defesa_fisica": 3}
    },
    "calcas_de_pano": {
        "nome": "Calças de Pano", "descricao": "Calças simples feitas de tecido grosso.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 5,
        "slot_equipamento": "calcas",
        "modificadores": {"defesa_fisica": 1}
    },

    # --- EXPANSÃO DE CONSUMÍVEIS ---
    "pocao_mana_fraca": {
        "nome": "Poção de Mana Fraca", "descricao": "Um líquido azulado cintilante que restaura uma pequena quantidade de mana.",
        "tipo": TipoItem.POCAO, "raridade": RaridadeItem.COMUM, "valor": 30,
        "empilhavel": True, "max_pilha": 10,
        "efeito_consumo": {"tipo": "cura_mp", "quantidade": 40}
    },
    "antidoto_simples": {
        "nome": "Antídoto Simples", "descricao": "Uma mistura de ervas que neutraliza venenos fracos.",
        "tipo": TipoItem.POCAO, "raridade": RaridadeItem.COMUM, "valor": 40,
        "empilhavel": True, "max_pilha": 5,
        "efeito_consumo": {"tipo": "remover_efeito", "id_efeito": "veneno_fraco"}
    },

    # --- EXPANSÃO DE MATERIAIS ---
    "minerio_de_ferro": {
        "nome": "Minério de Ferro", "descricao": "Uma rocha contendo ferro. Pode ser fundida em uma barra de ferro.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.COMUM, "valor": 10,
        "empilhavel": True, "max_pilha": 20
    },
    "tora_de_pinho": {
        "nome": "Tora de Pinho", "descricao": "Madeira de uma árvore de pinho. Usada para fazer arcos, cabos de armas e escudos.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.COMUM, "valor": 8,
        "empilhavel": True, "max_pilha": 20
    },
    "erva_do_sol": {
        "nome": "Erva do Sol", "descricao": "Uma erva com pétalas amarelas que floresce sob luz solar intensa. Ingrediente comum em poções de cura.",
        "tipo": TipoItem.INGREDIENTE, "raridade": RaridadeItem.COMUM, "valor": 5,
        "empilhavel": True, "max_pilha": 30
    },
    "raiz_da_terra": {
        "nome": "Raiz da Terra", "descricao": "Uma raiz grossa e nodosa, conhecida por suas propriedades restauradoras de vigor.",
        "tipo": TipoItem.INGREDIENTE, "raridade": RaridadeItem.COMUM, "valor": 7,
        "empilhavel": True, "max_pilha": 30
    }
}
