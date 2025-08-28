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
    },

    # --- ITENS INICIAIS DE CLASSE FALTANTES ---
    "machado_grande_de_duas_maos": {
        "nome": "Machado Grande de Duas Mãos", "descricao": "Um machado enorme e pesado, preferido por bárbaros e guerreiros fortes.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 45,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 15}
    },
    "tanga_de_peles": {
        "nome": "Tanga de Peles", "descricao": "Proteção mínima, mas oferece máxima liberdade de movimento.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 5,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 2}
    },
    "rapiera": {
        "nome": "Rapieira", "descricao": "Uma espada fina e leve, ideal para estocadas precisas.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 30,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 7, "precisao": 5}
    },
    "alaude": {
        "nome": "Alaúde", "descricao": "Um instrumento musical. Pode ser usado para inspirar aliados ou... como uma arma improvisada.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 15,
        "slot_equipamento": "arma_secundaria", "modificadores": {"carisma": 1}
    },
    "roupas_de_viajante": {
        "nome": "Roupas de Viajante", "descricao": "Roupas confortáveis e resistentes para longas jornadas.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 10,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 3}
    },
    "cajado_de_galho_retorcido": {
        "nome": "Cajado de Galho Retorcido", "descricao": "Um cajado feito de um galho de carvalho antigo, ainda pulsando com energia natural.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 20,
        "slot_equipamento": "arma_principal", "modificadores": {"poder_magico": 5, "sabedoria": 1}
    },
    "armadura_de_peles_e_folhas": {
        "nome": "Armadura de Peles e Folhas", "descricao": "Uma armadura leve feita de materiais da floresta.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 15,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 4}
    },
    "arco_longo": {
        "nome": "Arco Longo", "descricao": "Um arco alto e poderoso que exige força para ser usado, mas oferece grande alcance e poder.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 40,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 10}
    },
    "armadura_de_couro": {
        "nome": "Armadura de Couro", "descricao": "Uma armadura padrão para batedores e caçadores.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 20,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 6}
    },
    "espada_longa": {
        "nome": "Espada Longa", "descricao": "Uma espada versátil, balanceada para cortes e estocadas.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 50,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 11}
    },
    "escudo_de_aco": {
        "nome": "Escudo de Aço", "descricao": "Um escudo de metal resistente que oferece excelente proteção.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 35,
        "slot_equipamento": "arma_secundaria", "modificadores": {"defesa_fisica": 8}
    },
    "armadura_de_placas": {
        "nome": "Armadura de Placas", "descricao": "Armadura pesada que oferece a melhor proteção física, ao custo de mobilidade.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 75,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 15}
    },
    "adaga_ornamentada": {
        "nome": "Adaga Ornamentada", "descricao": "Uma adaga com uma pequena gema no pomo. Mais um símbolo de status do que uma arma.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 25,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 4, "carisma": 1}
    },
    "roupas_finas": {
        "nome": "Roupas Finas", "descricao": "Roupas de alta qualidade que não oferecem proteção, mas impressionam.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 30,
        "slot_equipamento": "peitoral", "modificadores": {"carisma": 2}
    },
    "grimorio_sombrio": {
        "nome": "Grimório Sombrio", "descricao": "Um livro com uma capa de couro escuro, contendo os pactos iniciais de um bruxo.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 30,
        "slot_equipamento": "arma_secundaria", "modificadores": {"poder_magico": 6}
    },
    "robe_escuro": {
        "nome": "Robe Escuro", "descricao": "Um robe simples de cor escura, preferido por aqueles que lidam com segredos.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 15,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_magica": 5}
    },
    "besta_leve": {
        "nome": "Besta Leve", "descricao": "Uma arma de projéteis fácil de usar, mas lenta para recarregar.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 35,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 9}
    },
    "avental_de_couro_reforcado": {
        "nome": "Avental de Couro Reforçado", "descricao": "Um avental de artesão, com placas de metal costuradas para proteção.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 20,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 7}
    },
    "escudo_torre": {
        "nome": "Escudo Torre", "descricao": "Um escudo massivo que pode cobrir o corpo inteiro.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 60,
        "slot_equipamento": "arma_secundaria", "modificadores": {"defesa_fisica": 10}
    },
    "armadura_de_placas_completa": {
        "nome": "Armadura de Placas Completa", "descricao": "Uma armadura de placas que cobre o usuário da cabeça aos pés.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 100,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 18}
    },
    "gibao_de_couro": {
        "nome": "Gibão de Couro", "descricao": "Uma jaqueta de couro acolchoada, comum entre batedores e mercenários.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 22,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 6}
    },
    "adaga_ritualistica": {
        "nome": "Adaga Ritualística", "descricao": "Uma adaga com runas gravadas, usada em rituais sombrios.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 28,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 4, "poder_magico": 3}
    },
    "robe_negro": {
        "nome": "Robe Negro", "descricao": "Um robe de lã preta, simples e sinistro.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 18,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_magica": 6}
    },
    "camisa_de_seda": {
        "nome": "Camisa de Seda", "descricao": "Uma camisa de seda elegante, usada por duelistas e nobres.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 40,
        "slot_equipamento": "peitoral", "modificadores": {"carisma": 1, "esquiva": 2}
    },
    "pistola_de_pederneira": {
        "nome": "Pistola de Pederneira", "descricao": "Uma arma de fogo primitiva, barulhenta e poderosa.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 75,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 18}
    },
    "casaco_de_couro": {
        "nome": "Casaco de Couro", "descricao": "Um casaco longo e resistente, popular entre caçadores e atiradores.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 30,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 8}
    },
    "clava_ritualistica": {
        "nome": "Clava Ritualística", "descricao": "Uma clava de madeira com entalhes de espíritos animais.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 20,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 7, "sabedoria": 1}
    },
    "vestes_tribais": {
        "nome": "Vestes Tribais", "descricao": "Roupas feitas de peles e tecidos naturais, adornadas com ossos e penas.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 12,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 3, "defesa_magica": 3}
    },
    "roupas_simples_de_monasterio": {
        "nome": "Roupas Simples de Monastério", "descricao": "Roupas leves e sem restrições, ideais para artistas marciais.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 5,
        "slot_equipamento": "peitoral", "modificadores": {"esquiva": 4}
    },
    "adaga_de_osso": {
        "nome": "Adaga de Osso", "descricao": "Uma adaga feita do fêmur de alguma criatura infeliz.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 18,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 4, "poder_magico": 2}
    },
    "robe_com_capuz": {
        "nome": "Robe com Capuz", "descricao": "Um robe que esconde o rosto, preferido por necromantes e outros tipos discretos.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 15,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_magica": 5}
    },
    "gladio": {
        "nome": "Gládio", "descricao": "A espada curta e larga dos gladiadores de arena.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 40,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 9}
    },
    "parma": {
        "nome": "Parma", "descricao": "Um pequeno escudo redondo, usado para desviar golpes rápidos.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 20,
        "slot_equipamento": "arma_secundaria", "modificadores": {"defesa_fisica": 4}
    },
    "armadura_de_gladiador": {
        "nome": "Armadura de Gladiador", "descricao": "Uma armadura assimétrica que protege o essencial enquanto permite o máximo de espetáculo.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 55,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 10, "carisma": 1}
    },
    "besta_pesada": {
        "nome": "Besta Pesada", "descricao": "Uma arma poderosa que dispara virotes com força para perfurar armaduras.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 60,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 16}
    },
    "machete": {
        "nome": "Machete", "descricao": "Uma lâmina larga e pesada, boa para cortar vegetação e... outras coisas.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 25,
        "slot_equipamento": "arma_secundaria", "modificadores": {"dano_arma": 6}
    },
    "sobretudo_de_couro": {
        "nome": "Sobretudo de Couro", "descricao": "Um casaco longo e resistente, popular entre caçadores e atiradores.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 35,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 9}
    },
    "martelo_de_guerra": {
        "nome": "Martelo de Guerra", "descricao": "Um martelo pesado projetado para esmagar através de armaduras de placas.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 55,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 14}
    },
    "armadura_de_placas_com_insignia": {
        "nome": "Armadura de Placas com Insígnia", "descricao": "Uma armadura de placas com o símbolo de uma ordem sagrada.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 80,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 16, "defesa_magica": 2}
    },
    "peitoral_de_aco": {
        "nome": "Peitoral de Aço", "descricao": "Uma placa de aço sólida que cobre o torso.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 65,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 14}
    },
    "manoplas_de_batalha": {
        "nome": "Manoplas de Batalha", "descricao": "Manoplas de aço que protegem as mãos e reforçam os socos.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 25,
        "slot_equipamento": "luvas", "modificadores": {"ataque_fisico": 2}
    },
    "cajado_elegante": {
        "nome": "Cajado Elegante", "descricao": "Um cajado fino e polido, com entalhes que parecem se mover quando você não está olhando.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 30,
        "slot_equipamento": "arma_principal", "modificadores": {"poder_magico": 5, "carisma": 1}
    },
    "robe_com_padroes_hipnoticos": {
        "nome": "Robe com Padrões Hipnóticos", "descricao": "Um robe cujos padrões parecem ondular, confundindo o olhar.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 25,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_magica": 7}
    },
    "machadinha": {
        "nome": "Machadinha", "descricao": "Uma pequena machadinha, versátil para cortar madeira ou inimigos.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 20,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 7}
    },
    "chicote": {
        "nome": "Chicote", "descricao": "Uma arma de alcance que pode ser usada para desarmar ou controlar.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 15,
        "slot_equipamento": "arma_secundaria", "modificadores": {"destreza": 1}
    },
    "armadura_de_couro_reforcado": {
        "nome": "Armadura de Couro Reforçado", "descricao": "Armadura de couro com placas de metal costuradas nos pontos vitais.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 40,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 10}
    },
    "cajado_carbonizado": {
        "nome": "Cajado Carbonizado", "descricao": "Um cajado de madeira que está perpetuamente quente ao toque.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 22,
        "slot_equipamento": "arma_principal", "modificadores": {"poder_magico": 6}
    },
    "robe_vermelho": {
        "nome": "Robe Vermelho", "descricao": "Um robe de cor carmesim, popular entre os piromantes.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 18,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_magica": 5, "resistencia_fogo": 0.05}
    },
    "varinha_de_cristal": {
        "nome": "Varinha de Cristal", "descricao": "Uma varinha curta que foca a energia do gelo.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 22,
        "slot_equipamento": "arma_principal", "modificadores": {"poder_magico": 6}
    },
    "robe_branco_e_azul": {
        "nome": "Robe Branco e Azul", "descricao": "Um robe que parece estar sempre frio, não importa o clima.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 18,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_magica": 5, "resistencia_gelo": 0.05}
    },
    "martelo_de_pedra": {
        "nome": "Martelo de Pedra", "descricao": "Um martelo pesado feito de uma única peça de granito.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 30,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 13}
    },
    "robe_marrom": {
        "nome": "Robe Marrom", "descricao": "Um robe de tecido grosso e resistente, da cor da terra.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 15,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 2, "defesa_magica": 4}
    },
    "cajado_leve": {
        "nome": "Cajado Leve", "descricao": "Um cajado feito de uma madeira muito leve, quase flutuante.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 25,
        "slot_equipamento": "arma_principal", "modificadores": {"poder_magico": 5, "destreza": 1}
    },
    "roupas_esvoacantes": {
        "nome": "Roupas Esvoaçantes", "descricao": "Roupas leves que se movem com o vento.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 15,
        "slot_equipamento": "peitoral", "modificadores": {"esquiva": 5}
    },
    "haste_de_metal": {
        "nome": "Haste de Metal", "descricao": "Uma haste de ferro que atrai eletricidade estática.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 28,
        "slot_equipamento": "arma_principal", "modificadores": {"poder_magico": 7}
    },
    "robe_com_fios_de_cobre": {
        "nome": "Robe com Fios de Cobre", "descricao": "Um robe com fios de cobre tecidos no padrão, que zumbem com energia.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 20,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_magica": 6, "resistencia_raio": 0.05}
    },
    "adaga_reforcada": {
        "nome": "Adaga Reforçada", "descricao": "Uma adaga grossa e resistente, mais ferramenta que arma.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 18,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 6}
    },
    "avental_de_alquimista": {
        "nome": "Avental de Alquimista", "descricao": "Um avental de couro grosso, manchado por inúmeros produtos químicos.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 15,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 4, "resistencia_veneno": 0.05}
    },
    "bolsa_de_reagentes": {
        "nome": "Bolsa de Reagentes", "descricao": "Uma bolsa com vários compartimentos para guardar ingredientes alquímicos.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 10,
        "slot_equipamento": "acessorio", "modificadores": {"inteligencia": 1}
    },
    "barril_pequeno_nas_costas": {
        "nome": "Barril Pequeno nas Costas", "descricao": "Um pequeno barril contendo uma bebida especial. Pode ser usado como arma de impacto.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 20,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 8, "constituicao": 1}
    },
    "roupas_rusticas": {
        "nome": "Roupas Rústicas", "descricao": "Roupas simples e resistentes, comuns entre camponeses e mestres cervejeiros.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 8,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 3}
    },
    "orbe_de_cristal": {
        "nome": "Orbe de Cristal", "descricao": "Um orbe de cristal polido, usado para focar a visão interior.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 25,
        "slot_equipamento": "arma_secundaria", "modificadores": {"sabedoria": 2}
    },
    "mantos_de_oraculo": {
        "nome": "Mantos de Oráculo", "descricao": "Mantos pesados e ornamentados, usados por videntes e oráculos.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 20,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_magica": 8}
    },
    "katana": {
        "nome": "Katana", "descricao": "Uma lâmina curva de uma única gume, conhecida por sua capacidade de corte.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 60,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 13}
    },
    "wakizashi": {
        "nome": "Wakizashi", "descricao": "Uma espada curta que serve de par para a katana.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 40,
        "slot_equipamento": "arma_secundaria", "modificadores": {"dano_arma": 7}
    },
    "armadura_o-yoroi": {
        "nome": "Armadura O-Yoroi", "descricao": "A armadura tradicional dos samurais, feita de placas de metal e couro laqueado.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 85,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 17}
    },
    "ninjato": {
        "nome": "Ninjato", "descricao": "Uma espada reta e curta, prática para o combate furtivo.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 45,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 9, "esquiva": 3}
    },
    "shurikens": {
        "nome": "Shurikens", "descricao": "Estrelas de arremesso, úteis para distrair ou ferir à distância.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 5,
        "slot_equipamento": "acessorio", "modificadores": {"destreza": 1}
    },
    "traje_shinobi": {
        "nome": "Traje Shinobi", "descricao": "Um traje escuro que ajuda a se misturar com as sombras.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 30,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 5, "esquiva": 5}
    },
    "cimitarra": {
        "nome": "Cimitarra", "descricao": "Uma espada curva, ideal para cortes rápidos a partir do convés de um navio.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 40,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 10}
    },
    "casaco_de_capitao": {
        "nome": "Casaco de Capitão", "descricao": "Um casaco longo e imponente, usado por capitães de navios.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 35,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 7, "carisma": 1}
    },
    "roupas_reforcadas": {
        "nome": "Roupas Reforçadas", "descricao": "Roupas de tecido grosso com inserções de couro para proteção.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 25,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 6}
    },
    "adaga_sacrificial": {
        "nome": "Adaga Sacrificial", "descricao": "Uma adaga com uma lâmina estranhamente sedenta.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 30,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 5, "poder_magico": 4}
    },
    "robe_manchado_de_sangue": {
        "nome": "Robe Manchado de Sangue", "descricao": "Um robe que já foi branco, agora permanentemente manchado.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 20,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_magica": 6, "constituicao": 1}
    },
    "florete": {
        "nome": "Florete", "descricao": "Uma espada leve de estocada, usada por duelistas que valorizam a técnica.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 45,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 8, "precisao": 8}
    },
    "jaqueta_de_couro": {
        "nome": "Jaqueta de Couro", "descricao": "Uma jaqueta de couro estilosa que oferece alguma proteção.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 25,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 7}
    },
    "machado_duplo": {
        "nome": "Machado Duplo", "descricao": "Um machado com duas lâminas, para o dobro da carnificina.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 65,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 18}
    },
    "peito_nu_com_pinturas_de_guerra": {
        "nome": "Peito Nu com Pinturas de Guerra", "descricao": "A única armadura de que um verdadeiro berserker precisa é sua fúria.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 2,
        "slot_equipamento": "peitoral", "modificadores": {"forca": 1}
    },
    "maça_leve": {
        "nome": "Maça Leve", "descricao": "Uma maça pequena, fácil de manusear.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 20,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 8}
    },
    "tunica_de_acolito": {
        "nome": "Túnica de Acólito", "descricao": "A túnica simples usada por aprendizes em uma ordem religiosa.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 10,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_magica": 4}
    },
    "besta_de_repeticao": {
        "nome": "Besta de Repetição", "descricao": "Uma besta com um mecanismo que permite múltiplos disparos antes de recarregar.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 80,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 11}
    },
    "espada_curta_prateada": {
        "nome": "Espada Curta Prateada", "descricao": "Uma espada curta revestida em prata, eficaz contra certas criaturas sobrenaturais.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 100,
        "slot_equipamento": "arma_secundaria", "modificadores": {"dano_arma": 6}
    },
    "sobretudo_de_couro_escuro": {
        "nome": "Sobretudo de Couro Escuro", "descricao": "Um sobretudo prático que ajuda a se misturar nas sombras.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 40,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 9}
    },
    "escudo_com_simbolo_sagrado": {
        "nome": "Escudo com Símbolo Sagrado", "descricao": "Um escudo de aço com o emblema de uma divindade gravado.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 45,
        "slot_equipamento": "arma_secundaria", "modificadores": {"defesa_fisica": 7, "defesa_magica": 3}
    },
    "armadura_de_placas_ornamentada": {
        "nome": "Armadura de Placas Ornamentada", "descricao": "Uma armadura de placas completa com gravuras e decorações.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 120,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 18, "carisma": 1}
    },
    "tomo_arcano": {
        "nome": "Tomo Arcano", "descricao": "Um livro pesado contendo teorias e fórmulas arcanas. Pode ser usado para focar magias.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 35,
        "slot_equipamento": "arma_secundaria", "modificadores": {"inteligencia": 2}
    },
    "robe_de_erudito": {
        "nome": "Robe de Erudito", "descricao": "Um robe usado por acadêmicos e estudiosos.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 20,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_magica": 6}
    },
    "tambor_de_guerra": {
        "nome": "Tambor de Guerra", "descricao": "Um tambor que pode ser usado para ditar o ritmo da batalha.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 25,
        "slot_equipamento": "arma_secundaria", "modificadores": {"constituicao": 1}
    },
    "besta_de_mao": {
        "nome": "Besta de Mão", "descricao": "Uma besta pequena que pode ser disparada com uma mão.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 50,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 8}
    },
    "capuz_e_manto_escuro": {
        "nome": "Capuz e Manto Escuro", "descricao": "Vestimentas que escondem a identidade e ajudam na furtividade.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 25,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 4, "esquiva": 3}
    },
    "soqueiras_de_bronze": {
        "nome": "Soqueiras de Bronze", "descricao": "Reforços de metal para os punhos.",
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.COMUM, "valor": 15,
        "slot_equipamento": "arma_principal", "modificadores": {"dano_arma": 4}
    },
    "camisa_rasgada": {
        "nome": "Camisa Rasgada", "descricao": "Os restos de uma camisa. Oferece pouca proteção, mas mostra que você é durão.",
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.COMUM, "valor": 1,
        "slot_equipamento": "peitoral", "modificadores": {"defesa_fisica": 1}
    },

    # --- MATERIAIS DE DUNGEON (RUÍNAS DE AL'KHEM) ---
    "nucleo_de_construto_danificado": {
        "nome": "Núcleo de Construto Danificado", "descricao": "O núcleo de energia de um construto, rachado e vazando energia arcana.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.COMUM, "valor": 40,
        "empilhavel": True, "max_pilha": 10
    },
    "placa_de_bronze_antiga": {
        "nome": "Placa de Bronze Antiga", "descricao": "Uma placa de bronze com gravuras de uma era esquecida.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.COMUM, "valor": 25,
        "empilhavel": True, "max_pilha": 10
    },
    "nucleo_de_construto_intacto": {
        "nome": "Núcleo de Construto Intacto", "descricao": "Um núcleo de energia estável, recuperado de um construto arcano.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.INCOMUM, "valor": 120,
        "empilhavel": True, "max_pilha": 5
    },
    "lente_de_cristal_focadora": {
        "nome": "Lente de Cristal Focadora", "descricao": "Uma lente mágica usada por construtos para focar seus raios de energia.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.INCOMUM, "valor": 150,
        "empilhavel": True, "max_pilha": 3
    },
    "nucleo_de_construto_grande": {
        "nome": "Núcleo de Construto Grande", "descricao": "O coração pulsante de um construto massivo.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.RARO, "valor": 400,
        "empilhavel": False
    },
    "fragmento_de_armadura_ancestral": {
        "nome": "Fragmento de Armadura Ancestral", "descricao": "Um pedaço de armadura de uma era esquecida, imbuído com poder.",
        "tipo": TipoItem.MATERIAL_CRAFTING, "raridade": RaridadeItem.RARO, "valor": 250,
        "empilhavel": True, "max_pilha": 5
    },
    "grimorio_antigo_rasgado": {
        "nome": "Grimório Antigo Rasgado", "descricao": "Páginas de um grimório que detalham rituais de proteção.",
        "tipo": TipoItem.LIVRO, "raridade": RaridadeItem.COMUM, "valor": 10
    },
    "mapa_das_sombras": {
        "nome": "Mapa das Sombras", "descricao": "Um mapa antigo que parece mostrar movimentações em um território desconhecido.",
        "tipo": TipoItem.ITEM_QUEST, "raridade": RaridadeItem.UNICO, "valor": 0
    }
}
