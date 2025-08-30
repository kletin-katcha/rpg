# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: ITENS - ARMAS
================================================================================================
"""
from typing import List, Dict

ARMAS: List[Dict] = [
    # --- TIER 1: Armas Iniciais / de Ferro ---
    {
        "id": "arma_adaga_ferro", "nome": "Adaga de Ferro", "tipo": "arma", "slot": "mao_principal",
        "dano": "1d4", "tipo_dano": "perfurante", "propriedades": ["acuidade", "leve"],
        "preco_base": 15, "descricao": "Uma adaga simples e confiável."
    },
    {
        "id": "arma_maca_ferro", "nome": "Maça de Ferro", "tipo": "arma", "slot": "mao_principal",
        "dano": "1d6", "tipo_dano": "concussao", "propriedades": [],
        "preco_base": 20, "descricao": "Uma cabeça de ferro pesada em um cabo de madeira, boa para amassar."
    },
    {
        "id": "arma_espada_curta_ferro", "nome": "Espada Curta de Ferro", "tipo": "arma", "slot": "mao_principal",
        "dano": "1d6", "tipo_dano": "perfurante", "propriedades": ["acuidade", "leve"],
        "preco_base": 25, "descricao": "Uma lâmina balanceada, favorita de batedores."
    },
    {
        "id": "arma_cajado_simples", "nome": "Cajado Simples", "tipo": "arma", "slot": "duas_maos",
        "dano": "1d6", "tipo_dano": "concussao", "propriedades": ["versatil(1d8)"],
        "preco_base": 5, "descricao": "Um cajado de carvalho, útil para caminhar e para um golpe inesperado."
    },
    {
        "id": "arma_arco_curto_simples", "nome": "Arco Curto Simples", "tipo": "arma", "slot": "duas_maos",
        "dano": "1d6", "tipo_dano": "perfurante", "propriedades": ["distancia(80/320)"],
        "preco_base": 40, "descricao": "Um arco simples de madeira de teixo."
    },

    # --- TIER 2: Armas de Aço ---
    {
        "id": "arma_espada_longa_aco", "nome": "Espada Longa de Aço", "tipo": "arma", "slot": "mao_principal",
        "dano": "1d8", "tipo_dano": "cortante", "propriedades": ["versatil(1d10)"],
        "preco_base": 75, "descricao": "Uma espada de aço bem forjada, a arma de um verdadeiro soldado."
    },
    {
        "id": "arma_machado_batalha_aco", "nome": "Machado de Batalha de Aço", "tipo": "arma", "slot": "mao_principal",
        "dano": "1d8", "tipo_dano": "cortante", "propriedades": ["versatil(1d10)"],
        "preco_base": 80, "descricao": "Uma lâmina pesada e afiada, projetada para cortar membros."
    },
    {
        "id": "arma_martelo_guerra_aco", "nome": "Martelo de Guerra de Aço", "tipo": "arma", "slot": "mao_principal",
        "dano": "1d8", "tipo_dano": "concussao", "propriedades": ["versatil(1d10)"],
        "preco_base": 85, "descricao": "Um martelo pesado de aço, perfeito para esmagar as defesas dos inimigos."
    },
    {
        "id": "arma_rapiera_aco", "nome": "Rapieira de Aço", "tipo": "arma", "slot": "mao_principal",
        "dano": "1d8", "tipo_dano": "perfurante", "propriedades": ["acuidade"],
        "preco_base": 100, "descricao": "Uma lâmina fina e elegante, valorizada por duelistas por sua precisão mortal."
    },
    {
        "id": "arma_besta_leve", "nome": "Besta Leve", "tipo": "arma", "slot": "duas_maos",
        "dano": "1d8", "tipo_dano": "perfurante", "propriedades": ["distancia(80/320)", "recarga"],
        "preco_base": 120, "descricao": "Mais fácil de manejar que sua irmã maior, mas ainda com um coice poderoso."
    },

    # --- TIER 3: Armas de Qualidade Superior (Élficas, Anãs) ---
    {
        "id": "arma_lamina_elfica", "nome": "Lâmina Élfica", "tipo": "arma", "slot": "mao_principal",
        "dano": "1d8", "tipo_dano": "cortante", "propriedades": ["acuidade", "magica(+1)"],
        "preco_base": 500, "descricao": "Uma espada graciosa e mortal, forjada com a maestria élfica. É magicamente afiada."
    },
    {
        "id": "arma_machado_anao", "nome": "Machado de Guerra Anão", "tipo": "arma", "slot": "mao_principal",
        "dano": "1d10", "tipo_dano": "cortante", "propriedades": ["versatil(1d12)", "magica(+1)"],
        "preco_base": 550, "descricao": "Um machado de batalha com o peso e o equilíbrio perfeitos, uma obra-prima da forja anã."
    },
    {
        "id": "arma_arco_longo_teixo", "nome": "Arco Longo de Teixo", "tipo": "arma", "slot": "duas_maos",
        "dano": "1d8", "tipo_dano": "perfurante", "propriedades": ["distancia(150/600)", "pesado"],
        "preco_base": 250, "descricao": "Um arco poderoso que exige grande força para ser puxado, mas recompensa com alcance e poder."
    },
    {
        "id": "arma_cajado_runico", "nome": "Cajado Rúnico", "tipo": "arma", "slot": "duas_maos",
        "dano": "1d6", "tipo_dano": "concussao", "propriedades": ["foco_arcano", "magica(+1)"],
        "preco_base": 400, "descricao": "Um cajado de carvalho branco com runas de poder entalhadas, que amplificam a magia do conjurador."
    },
]

INDICE_ARMAS = {"by_id": {a["id"]: a for a in ARMAS}}
