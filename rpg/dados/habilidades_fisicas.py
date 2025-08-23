# ==============================================================================
# ARQUIVO DE DADOS: HABILIDADES FÍSICAS
# ==============================================================================
#
# Este arquivo contém as definições para habilidades baseadas em atributos
# físicos como Força e Destreza.
#
# Estrutura de cada Habilidade:
# -----------------------------
# "nome": (str) O nome da habilidade.
# "descricao": (str) O que a habilidade faz, em termos de jogo.
# "lore": (str) Uma pequena história ou contexto da habilidade no mundo.
# "custo_tipo": (str) O recurso consumido ("mp", "stamina", "hp").
# "custo_valor": (int) A quantidade de recurso consumido.
# "tipo_alvo": (str) Quem a habilidade pode afetar ("self", "inimigo_unico",
#                "aliado_unico", "inimigos_area", "aliados_area").
# "condicao": (str, opcional) Condição especial para o uso ou para efeito bônus
#             (ex: "requer_furtividade", "alvo_sangrando").
# "efeitos": (list) Uma lista de dicionários, cada um descrevendo um efeito.
#   - "tipo": (str) O tipo de efeito (ex: "dano_fisico", "aplicar_efeito").
#   - ... (outras chaves dependendo do tipo de efeito)
#
# ==============================================================================

HABILIDADES_FISICAS = {
    # --- HABILIDADES DE GUERREIRO ---
    "ataque_poderoso": {
        "nome": "Ataque Poderoso",
        "descricao": "Um golpe pesado que sacrifica precisão por dano bruto.",
        "lore": "Uma técnica básica para qualquer combatente que prefere força sobre fineza. O objetivo é simples: colocar todo o peso do corpo e da arma em um único golpe esmagador.",
        "custo_tipo": "stamina",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {
                "tipo": "dano_fisico",
                "escala_com": "forca",
                "multiplicador_dano": 1.5,
                "penalidade_precisao": 0.2 # Reduz a precisão deste ataque em 20%
            }
        ]
    },
    "grito_de_guerra": {
        "nome": "Grito de Guerra",
        "descricao": "Um grito intimidador que aumenta o ataque do usuário e de seus aliados próximos por um curto período.",
        "lore": "O rugido de um guerreiro no campo de batalha pode virar o rumo do combate, inspirando coragem nos corações dos aliados e instilando medo nos inimigos.",
        "custo_tipo": "stamina",
        "custo_valor": 20,
        "tipo_alvo": "aliados_area",
        "efeitos": [
            {
                "tipo": "aplicar_efeito",
                "id_efeito": "buff_ataque_pequeno", # Buff de +10% de ataque por 3 turnos
                "duracao": 3
            }
        ]
    },

    # --- HABILIDADES DE LADINO ---
    "ataque_furtivo": {
        "nome": "Ataque Furtivo",
        "descricao": "Um ataque preciso em um ponto vital. Causa dano massivo se o usuário não for o foco do alvo.",
        "lore": "A arte do assassino. Não se trata de força, mas de timing, posicionamento e conhecimento da anatomia do alvo. Um golpe bem-sucedido pode terminar uma luta antes que ela comece.",
        "custo_tipo": "stamina",
        "custo_valor": 25,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {
                "tipo": "dano_fisico_condicional",
                "condicao": "alvo_nao_focado_em_usuario",
                "escala_com": "destreza",
                "multiplicador_dano_bonus": 3.0,
                "multiplicador_dano_normal": 1.0
            }
        ]
    },
    "disparada": {
        "nome": "Disparada",
        "descricao": "Move-se rapidamente, tornando-se muito mais difícil de acertar por um curto período.",
        "lore": "Para um ladino, não ser atingido é tão importante quanto atacar. A disparada é uma explosão de velocidade para se reposicionar ou simplesmente evitar um golpe mortal.",
        "custo_tipo": "stamina",
        "custo_valor": 10,
        "tipo_alvo": "self",
        "efeitos": [
            {
                "tipo": "aplicar_efeito",
                "id_efeito": "buff_esquiva_grande", # Buff de +50% de esquiva por 1 turno
                "duracao": 1
            }
        ]
    },
    "arremessar_adaga": {
        "nome": "Arremessar Adaga",
        "descricao": "Arremessa uma adaga com precisão. Um ataque à distância rápido e de baixo custo.",
        "lore": "Todo ladino carrega algumas facas extras, seja para o trabalho sujo de perto ou para acertar um inimigo em fuga.",
        "custo_tipo": "stamina",
        "custo_valor": 5,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {
                "tipo": "dano_fisico",
                "escala_com": "destreza",
                "multiplicador_dano": 0.8
            }
        ]
    },

    # --- HABILIDADES DE BÁRBARO ---
    "furia_selvagem": {
        "nome": "Fúria Selvagem",
        "descricao": "Entra em um estado de fúria, aumentando o dano causado e a resistência a dano, mas diminuindo a defesa.",
        "lore": "O bárbaro canaliza sua raiva primordial, ignorando a dor e se tornando uma força da natureza. A mente se vai, e apenas o instinto de lutar permanece.",
        "custo_tipo": "recurso_especial", # Fúria, um recurso que aumenta em combate
        "custo_valor": 50,
        "tipo_alvo": "self",
        "efeitos": [
            {
                "tipo": "aplicar_efeito",
                "id_efeito": "estado_furia_barbaro", # Aumenta Força, Constituição, mas reduz Defesa e impede uso de itens.
                "duracao": 5
            }
        ]
    },
    "golpe_brutal": {
        "nome": "Golpe Brutal",
        "descricao": "Um ataque devastador que ignora uma porção da armadura do inimigo.",
        "lore": "Não é um golpe de técnica, mas de pura força. O objetivo é quebrar não apenas a arma ou armadura do inimigo, mas seu espírito.",
        "custo_tipo": "stamina",
        "custo_valor": 20,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {
                "tipo": "dano_fisico",
                "escala_com": "forca",
                "multiplicador_dano": 1.2,
                "penetracao_armadura": 0.3 # Ignora 30% da defesa física do alvo
            }
        ]
    }
}
