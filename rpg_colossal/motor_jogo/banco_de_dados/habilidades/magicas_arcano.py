# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: HABILIDADES MÁGICAS - ARCANO
================================================================================================
Este arquivo contém a definição das habilidades da escola Arcana, focadas na manipulação
de energia mágica pura. São as ferramentas principais do Mago.
"""
from typing import List, Dict

HABILIDADES_ARCANO: List[Dict] = [
    # --- ÁRVORE DE HABILIDADES: MAGO (Níveis 1-20) ---
    {
        "id": "mago_seta_de_fogo",
        "nome": "Seta de Fogo",
        "tipo": "ativa", "categoria": "magico", "requisitos": {"nivel": 1},
        "custo": {"mana": 10},
        "multiplicador": 1.4, "atributo_chave": "inteligencia", "precisao": 0.95, "tipo_dano": "fogo",
        "descricao": "Um projétil de fogo que causa dano em um único alvo."
    },
    {
        "id": "mago_escudo_arcano",
        "nome": "Escudo Arcano",
        "tipo": "ativa", "categoria": "suporte", "requisitos": {"nivel": 2},
        "custo": {"mana": 15},
        "efeitos": [{"tipo": "buff", "atributo": "defesa_magica", "valor": 10, "duracao": 3}],
        "descricao": "Cria uma barreira mágica que aumenta a defesa contra magias."
    },
    {
        "id": "mago_raio_de_gelo",
        "nome": "Raio de Gelo",
        "tipo": "ativa", "categoria": "magico", "requisitos": {"nivel": 3},
        "custo": {"mana": 12},
        "multiplicador": 1.2, "atributo_chave": "inteligencia", "precisao": 0.90, "tipo_dano": "gelo",
        "efeitos": [{"tipo": "debuff", "atributo": "velocidade", "valor": -10, "duracao": 2, "chance": 0.7}],
        "descricao": "Dispara um raio de gelo que causa dano e pode deixar o inimigo mais lento."
    },
    {
        "id": "mago_intelecto_brilhante",
        "nome": "Intelecto Brilhante",
        "tipo": "ativa", "categoria": "suporte", "requisitos": {"nivel": 5},
        "custo": {"mana": 20}, "cooldown": 5,
        "efeitos": [{"tipo": "buff", "atributo": "inteligencia", "valor": 10, "duracao": 4}],
        "descricao": "O mago foca sua mente, aumentando sua inteligência temporariamente."
    },
    {
        "id": "mago_bola_de_fogo",
        "nome": "Bola de Fogo",
        "tipo": "ativa", "categoria": "magico", "requisitos": {"nivel": 8},
        "custo": {"mana": 30}, "area_de_efeito": "todos_inimigos",
        "multiplicador": 1.5, "atributo_chave": "inteligencia", "precisao": 0.9, "tipo_dano": "fogo",
        "descricao": "Lança uma esfera de fogo que explode ao atingir o alvo, causando dano em área."
    },
    {
        "id": "mago_contrafeitiço",
        "nome": "Contrafeitiço",
        "tipo": "ativa", "categoria": "suporte", "requisitos": {"nivel": 12},
        "custo": {"mana": 25}, "cooldown": 4,
        "efeitos": [{"tipo": "silencio", "duracao": 1, "chance": 0.85}],
        "descricao": "Interrompe a conjuração de um inimigo, silenciando-o por um turno."
    },
    {
        "id": "mago_clarividencia",
        "nome": "Clarividência",
        "tipo": "passiva", "categoria": "suporte", "requisitos": {"nivel": 15},
        "efeitos": [{"tipo": "buff_passivo", "habilidade": "analisar_inimigo", "sucesso": True}],
        "descricao": "Sua mente afiada permite que você veja os pontos fracos e fortes dos inimigos no início do combate."
    },
    {
        "id": "mago_tempestade_de_meteoros",
        "nome": "Tempestade de Meteoros",
        "tipo": "ativa", "categoria": "magico", "requisitos": {"nivel": 20},
        "custo": {"mana": 80}, "cooldown": 8, "area_de_efeito": "todos_inimigos",
        "multiplicador": 3.0, "atributo_chave": "inteligencia", "precisao": 0.8, "tipo_dano": "fogo_e_concussao",
        "descricao": "Invoca uma chuva de meteoros do céu, causando dano massivo a todos os inimigos."
    }
]

# Construção do índice para acesso rápido
GRIMORIO_ARCANO = {"by_id": {h["id"]: h for h in HABILIDADES_ARCANO}}
