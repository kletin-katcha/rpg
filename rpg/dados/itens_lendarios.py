# ==============================================================================
# ARQUIVO DE DADOS: ITENS LENDÁRIOS
# ==============================================================================
#
# Este arquivo contém as definições para itens de raridade Lendária.
# Estes são artefatos únicos ou extremamente raros, com nomes, poderes
# e histórias próprias.
#
# ==============================================================================

from ..entidades.item import TipoItem, RaridadeItem

ITENS_LENDARIOS = {
    "portadora_do_amanhecer": {
        "nome": "Portadora do Amanhecer",
        "descricao": "Uma espada longa que pulsa com o calor e a luz de uma estrela nascente. A lâmina é quente ao toque e canta suavemente na presença da escuridão.",
        "lore": """
Forjada no coração de uma estrela por um deus esquecido do sol, a Portadora do Amanhecer foi um presente para o primeiro rei dos homens, para que ele pudesse banir a noite eterna que assolava o mundo primordial. A espada bebe a luz do sol para se fortalecer e libera essa energia em explosões de fogo sagrado. Dizem que nenhum morto-vivo pode suportar seu brilho e que sua luz pode curar os ferimentos daqueles que são puros de coração. A espada foi perdida há eras, quando o último rei de sua linhagem caiu em uma batalha contra o Lorde das Sombras, e aguarda ser encontrada por um novo campeão digno de empunhá-la.
        """,
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.LENDARIO, "valor": 10000,
        "slot_equipamento": "arma_principal",
        "modificadores": {
            "ataque_fisico": 35,
            "dano_magico_extra": {"elemento": "sagrado", "quantidade": 25}
        },
        "habilidades_concedidas": ["explosao_solar"], # Habilidade única concedida ao equipar
        "requisitos": {"alinhamento": "bom", "sabedoria": 25}
    },
    "manto_das_sombras_serpente": {
        "nome": "Manto das Sombras da Serpente",
        "descricao": "Um manto feito de sombras solidificadas, que parece se contorcer e se mover por conta própria. Permite que o usuário se torne um com a escuridão.",
        "lore": """
Costurado com os fios da própria escuridão por uma antiga deusa aranha, este manto foi o prêmio de um lendário mestre ladrão que conseguiu roubar o silêncio da noite. O manto concede ao seu portador a habilidade de se tornar invisível nas sombras, de se mover sem som e de atacar sem ser visto. No entanto, o manto é ciumento e sussurra segredos sombrios na mente de seu dono, tentando-o a cometer atos cada vez mais audaciosos de furto e engano.
        """,
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.LENDARIO, "valor": 8500,
        "slot_equipamento": "peitoral",
        "modificadores": {
            "esquiva": 30,
            "furtividade": 50 # Um stat hipotético para furtividade
        },
        "habilidades_concedidas": ["passo_da_sombra"],
        "requisitos": {"classe": "ladino", "destreza": 30}
    },
    "coracao_da_montanha": {
        "nome": "Coração da Montanha",
        "descricao": "Um amuleto contendo um único e perfeito rubi que pulsa lentamente, como um coração batendo. Concede a resistência da própria terra.",
        "lore": """
Este não é um rubi comum. É o coração cristalizado de uma montanha anciã que sacrificou sua vida para impedir uma catástrofe mágica. O amuleto concede ao seu usuário uma fração da resiliência da montanha, tornando sua pele dura como granito e seu vigor quase inesgotável. O usuário pode sentir os tremores da terra e, em momentos de grande necessidade, pode pedir à terra que se levante para protegê-lo.
        """,
        "tipo": TipoItem.ARMADURA, "raridade": RaridadeItem.LENDARIO, "valor": 12000,
        "slot_equipamento": "amuleto",
        "modificadores": {
            "constituicao": 10,
            "defesa_fisica": 20,
            "hp_max": 100
        },
        "habilidades_concedidas": ["baluarte_de_pedra"],
        "requisitos": {"raca": "anao"}
    },
    "grimorio_do_arquimago_louco": {
        "nome": "Grimório do Arquimago Louco",
        "descricao": "Um livro pesado, encadernado em pele de criatura desconhecida, cujas páginas parecem se reescrever constantemente com feitiços caóticos e proibidos.",
        "lore": """
Pertenceu ao Arquimago Lyzander, que em sua busca pelo conhecimento absoluto, olhou para além do véu da realidade e enlouqueceu. O livro é um reflexo de sua mente fraturada, contendo feitiços de poder inimaginável, mas que são perigosamente instáveis. Cada vez que o livro é aberto, a magia contida nele pode se manifestar de formas imprevisíveis. Empunhar este grimório é brincar com o fogo da própria criação, um ato de poder e de loucura.
        """,
        "tipo": TipoItem.ARMA, "raridade": RaridadeItem.LENDARIO, "valor": 9000,
        "slot_equipamento": "arma_secundaria",
        "modificadores": {
            "inteligencia": 15,
            "poder_magico": 40
        },
        "habilidades_concedidas": ["magia_selvagem"], # Passiva: Chance de qualquer feitiço ter um efeito aleatório adicional
        "requisitos": {"inteligencia": 35}
    }
}
