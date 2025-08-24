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
    },

    # --- HABILIDADES DE RANGER ---
    "tiro_certeiro": {
        "nome": "Tiro Certeiro",
        "descricao": "Um disparo cuidadosamente mirado que causa dano extra e tem alta chance de acerto crítico.",
        "lore": "O ranger respira fundo, acalma o coração e se torna um com seu arco. O mundo desaparece, e apenas o alvo permanece. A flecha nunca erra.",
        "custo_tipo": "stamina",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {
                "tipo": "dano_fisico",
                "escala_com": "destreza",
                "multiplicador_dano": 1.3,
                "bonus_chance_critico": 0.25 # Adiciona 25% de chance de crítico
            }
        ]
    },

    # --- HABILIDADES DE PALADINO ---
    "golpe_divino": {
        "nome": "Golpe Divino",
        "descricao": "Imbui sua arma com energia sagrada, causando dano físico e mágico extra no próximo ataque.",
        "lore": "Canalizando a força de seu juramento, o paladino transforma sua arma em um instrumento da vontade divina, capaz de punir os injustos com fogo sagrado.",
        "custo_tipo": "mp",
        "custo_valor": 20,
        "tipo_alvo": "self",
        "efeitos": [
            {
                "tipo": "aplicar_efeito",
                "id_efeito": "buff_golpe_divino", # Efeito que adiciona dano sagrado ao próximo ataque
                "duracao": 1 # Dura apenas para o próximo ataque
            }
        ]
    },

    # --- HABILIDADES FÍSICAS ADICIONAIS (NÍVEL 1-10) ---

    # --- Geral / Espadas ---
    "corte_transversal": {
        "nome": "Corte Transversal",
        "descricao": "Um rápido corte horizontal que pode atingir múltiplos inimigos próximos.",
        "lore": "Uma técnica fundamental para lidar com multidões, ensinada em todas as escolas de esgrima.",
        "custo_tipo": "stamina",
        "custo_valor": 20,
        "tipo_alvo": "inimigos_area",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 0.8}]
    },
    "aparar": {
        "nome": "Aparar",
        "descricao": "Antecipa um ataque corpo a corpo, bloqueando-o e criando uma abertura para um contra-ataque.",
        "lore": "Mais do que força, a esgrima é sobre tempo. Um mestre espadachim pode transformar a agressão de um inimigo em sua própria ruína.",
        "custo_tipo": "stamina",
        "custo_valor": 10,
        "tipo_alvo": "self",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "buff_aparar", "duracao": 1}] # Efeito que contra-ataca se atingido
    },

    # --- Arcos ---
    "tiro_duplo": {
        "nome": "Tiro Duplo",
        "descricao": "Dispara duas flechas em rápida sucessão no mesmo alvo.",
        "lore": "Uma demonstração de velocidade e precisão, o tiro duplo é a marca de um arqueiro experiente.",
        "custo_tipo": "stamina",
        "custo_valor": 25,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 0.9},
            {"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 0.9}
        ]
    },
    "flecha_farpada": {
        "nome": "Flecha Farpada",
        "descricao": "Dispara uma flecha com farpas que causa dano de sangramento ao longo do tempo.",
        "lore": "Uma invenção cruel, mas eficaz. A flecha é projetada para ser mais difícil de remover do que de entrar, causando dor contínua.",
        "custo_tipo": "stamina",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {"tipo": "dano_fisico", "escala_com": "destreza", "multiplicador_dano": 0.7},
            {"tipo": "aplicar_efeito", "id_efeito": "sangramento_fraco", "duracao": 3}
        ]
    },

    # --- Armas de Haste (Lanças) ---
    "estocada_perfurante": {
        "nome": "Estocada Perfurante",
        "descricao": "Uma estocada focada que visa as brechas na armadura do inimigo.",
        "lore": "A lança não tem o poder de corte de uma espada, mas sua ponta pode encontrar o menor dos vãos em uma armadura de placas.",
        "custo_tipo": "stamina",
        "custo_valor": 15,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.1, "penetracao_armadura": 0.4}]
    },

    # --- Armas de Impacto (Maças, Martelos) ---
    "quebra_ossos": {
        "nome": "Quebra-Ossos",
        "descricao": "Um golpe poderoso que visa as articulações, com chance de reduzir a capacidade de ataque do inimigo.",
        "lore": "Um golpe brutal que ensina ao inimigo uma lição dolorosa sobre o poder do impacto.",
        "custo_tipo": "stamina",
        "custo_valor": 20,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [
            {"tipo": "dano_fisico", "escala_com": "forca", "multiplicador_dano": 1.3},
            {"tipo": "aplicar_efeito", "id_efeito": "debuff_ataque_pequeno", "chance": 0.3, "duracao": 3}
        ]
    },

    # --- Utilidade / Geral ---
    "intimidar": {
        "nome": "Intimidar",
        "descricao": "Usa sua presença física para intimidar um alvo, potencialmente o assustando.",
        "lore": "Às vezes, a melhor arma é a reputação e a aparência. Um olhar frio pode parar um inimigo antes mesmo que a luta comece.",
        "custo_tipo": "stamina",
        "custo_valor": 10,
        "tipo_alvo": "inimigo_unico",
        "efeitos": [{"tipo": "aplicar_efeito", "id_efeito": "medo", "duracao": 2, "escala_com": "forca"}]
    }
}
