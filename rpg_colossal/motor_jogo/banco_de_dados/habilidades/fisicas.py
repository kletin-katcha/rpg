# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: HABILIDADES FÍSICAS
================================================================================================
Este arquivo contém a definição de todas as habilidades da categoria "Física".
Essas habilidades são tipicamente usadas por classes marciais como Guerreiros, Bárbaros,
Ladinos e outras que dependem de força ou destreza.
"""
from typing import List, Dict

HABILIDADES_FISICAS: List[Dict] = [
    # Habilidade Geral
    {
        "id": "ataque_basico",
        "nome": "Ataque Básico",
        "tipo": "ativa", "categoria": "fisico",
        "custo": {"stamina": 5},
        "multiplicador": 1.0, "atributo_chave": "forca",
        "precisao": 0.95,
        "descricao": "Um golpe simples com a arma equipada."
    },
    # --- ÁRVORE DE HABILIDADES: GUERREIRO (Níveis 1-20) ---
    {
        "id": "guerreiro_golpe_poderoso",
        "nome": "Golpe Poderoso",
        "tipo": "ativa", "categoria": "fisico", "requisitos": {"nivel": 2},
        "custo": {"stamina": 15},
        "multiplicador": 1.8, "atributo_chave": "forca", "precisao": 0.80,
        "descricao": "Um ataque devastador que sacrifica precisão por poder bruto."
    },
    {
        "id": "guerreiro_grito_de_guerra",
        "nome": "Grito de Guerra",
        "tipo": "ativa", "categoria": "suporte", "requisitos": {"nivel": 3},
        "custo": {"stamina": 20},
        "efeitos": [{"tipo": "buff", "atributo": "forca", "valor": 5, "duracao": 3}],
        "descricao": "Um grito intimidador que aumenta o ataque do guerreiro."
    },
    {
        "id": "guerreiro_corte_profundo",
        "nome": "Corte Profundo",
        "tipo": "ativa", "categoria": "fisico", "requisitos": {"nivel": 5},
        "custo": {"stamina": 20},
        "multiplicador": 1.2, "atributo_chave": "forca", "precisao": 0.9,
        "efeitos": [{"tipo": "dano_por_turno", "dano": "1d4", "duracao": 3, "chance": 1.0, "nome_efeito": "Sangramento"}],
        "descricao": "Um golpe que causa sangramento no alvo por vários turnos."
    },
    {
        "id": "guerreiro_segundo_folego",
        "nome": "Segundo Fôlego",
        "tipo": "ativa", "categoria": "suporte", "requisitos": {"nivel": 8},
        "custo": {"stamina": 0}, "cooldown": 5,
        "efeitos": [{"tipo": "cura", "valor": "1d10"}],
        "descricao": "Recupera uma pequena quantidade de vida em um momento de necessidade. Só pode ser usado uma vez por combate."
    },
    {
        "id": "guerreiro_golpe_giratorio",
        "nome": "Golpe Giratório",
        "tipo": "ativa", "categoria": "fisico", "requisitos": {"nivel": 12},
        "custo": {"stamina": 30}, "area_de_efeito": "todos_inimigos",
        "multiplicador": 0.8, "atributo_chave": "forca", "precisao": 0.85,
        "descricao": "Um ataque em área que atinge todos os inimigos próximos."
    },
    {
        "id": "guerreiro_inquebravel",
        "nome": "Inquebrável",
        "tipo": "passiva", "categoria": "suporte", "requisitos": {"nivel": 15},
        "efeitos": [{"tipo": "buff_passivo", "atributo": "defesa", "valor": 10}],
        "descricao": "Sua determinação e resiliência concedem um bônus permanente à sua defesa."
    },
    {
        "id": "guerreiro_executar",
        "nome": "Executar",
        "tipo": "ativa", "categoria": "fisico", "requisitos": {"nivel": 20},
        "custo": {"stamina": 25}, "cooldown": 3,
        "multiplicador": 2.5, "atributo_chave": "forca", "precisao": 0.9,
        "condicao": {"alvo_hp_percentual_menor_que": 0.25},
        "descricao": "Um golpe final devastador que causa dano massivo a inimigos com pouca vida."
    },
    # --- ÁRVORE DE HABILIDADES: LADINO (Níveis 1-20) ---
    {
        "id": "ladino_ataque_furtivo",
        "nome": "Ataque Furtivo",
        "tipo": "ativa", "categoria": "fisico", "requisitos": {"nivel": 1},
        "custo": {"stamina": 10},
        "multiplicador": 1.4, "atributo_chave": "destreza", "precisao": 1.0,
        "descricao": "Um ataque preciso que causa dano extra se o inimigo ainda não agiu no combate."
    },
    {
        "id": "ladino_lancar_areia",
        "nome": "Lançar Areia",
        "tipo": "ativa", "categoria": "suporte", "requisitos": {"nivel": 2},
        "custo": {"stamina": 5},
        "efeitos": [{"tipo": "debuff", "atributo": "precisao", "valor": -0.25, "duracao": 2, "chance": 0.9}],
        "descricao": "Joga areia nos olhos do inimigo, reduzindo sua precisão."
    },
    {
        "id": "ladino_passo_sombrio",
        "nome": "Passo Sombrio",
        "tipo": "ativa", "categoria": "suporte", "requisitos": {"nivel": 4},
        "custo": {"stamina": 25},
        "efeitos": [{"tipo": "buff", "atributo": "esquiva", "valor": 0.50, "duracao": 1}],
        "descricao": "Move-se rapidamente pelas sombras, tornando-se muito difícil de acertar por um turno."
    },
    {
        "id": "ladino_golpe_venenoso",
        "nome": "Golpe Venenoso",
        "tipo": "ativa", "categoria": "fisico", "requisitos": {"nivel": 6},
        "custo": {"stamina": 15},
        "multiplicador": 1.1, "atributo_chave": "destreza", "precisao": 0.95,
        "efeitos": [{"tipo": "dano_por_turno", "dano": "1d6", "duracao": 3, "chance": 1.0, "nome_efeito": "Veneno"}],
        "descricao": "Aplica um veneno de ação rápida na lâmina, causando dano contínuo ao alvo."
    },
    {
        "id": "ladino_expor_fraqueza",
        "nome": "Expor Fraqueza",
        "tipo": "ativa", "categoria": "suporte", "requisitos": {"nivel": 10},
        "custo": {"stamina": 20}, "cooldown": 4,
        "efeitos": [{"tipo": "debuff", "atributo": "defesa", "valor": -15, "duracao": 3, "chance": 1.0}],
        "descricao": "Analisa a defesa do inimigo e aponta uma falha, tornando-o mais vulnerável a ataques."
    },
    {
        "id": "ladino_eviscerar",
        "nome": "Eviscerar",
        "tipo": "ativa", "categoria": "fisico", "requisitos": {"nivel": 15},
        "custo": {"stamina": 35},
        "multiplicador": 2.2, "atributo_chave": "destreza", "precisao": 0.9,
        "descricao": "Um golpe final brutal que causa dano massivo. O dano é aumentado se o alvo estiver sangrando ou envenenado."
    },
    {
        "id": "ladino_mestre_da_fuga",
        "nome": "Mestre da Fuga",
        "tipo": "passiva", "categoria": "suporte", "requisitos": {"nivel": 20},
        "efeitos": [{"tipo": "buff_passivo", "habilidade": "fugir", "chance_sucesso": 1.0}],
        "descricao": "Você se torna um mestre em escapar de situações perigosas. A ação de fugir do combate sempre funciona."
    }
]

# Construção do índice para acesso rápido
GRIMORIO_FISICO = {"by_id": {h["id"]: h for h in HABILIDADES_FISICAS}}
