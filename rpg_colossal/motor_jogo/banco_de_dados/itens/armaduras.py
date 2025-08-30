# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: ITENS - ARMADURAS
================================================================================================
"""
from typing import List, Dict

ARMADURAS: List[Dict] = [
    # --- TIER 1: Armaduras Leves ---
    {
        "id": "armadura_acolchoada", "nome": "Armadura Acolchoada", "tipo": "armadura", "slot": "peito",
        "categoria": "leve", "defesa_base": 11, "penalidade_furtividade": True, "preco_base": 10,
        "descricao": "Várias camadas de pano e enchimento. Barata, mas barulhenta."
    },
    {
        "id": "armadura_de_couro", "nome": "Armadura de Couro", "tipo": "armadura", "slot": "peito",
        "categoria": "leve", "defesa_base": 12, "penalidade_furtividade": False, "preco_base": 25,
        "descricao": "Couro fervido e endurecido. A escolha de batedores e ladinos."
    },
    {
        "id": "botas_de_couro_macio", "nome": "Botas de Couro Macio", "tipo": "armadura", "slot": "pes",
        "categoria": "leve", "defesa_base": 0, "preco_base": 8,
        "descricao": "Botas simples e confortáveis, ideais para longas viagens."
    },
    {
        "id": "elmo_de_couro", "nome": "Elmo de Couro", "tipo": "armadura", "slot": "cabeca",
        "categoria": "leve", "defesa_base": 1, "preco_base": 10,
        "descricao": "Um capacete de couro simples."
    },

    # --- TIER 2: Armaduras Médias ---
    {
        "id": "brunea", "nome": "Brunea", "tipo": "armadura", "slot": "peito",
        "categoria": "media", "defesa_base": 14, "penalidade_furtividade": True, "preco_base": 75,
        "descricao": "Uma armadura de couro reforçada com anéis de metal."
    },
    {
        "id": "peitoral_de_escamas", "nome": "Peitoral de Escamas", "tipo": "armadura", "slot": "peito",
        "categoria": "media", "defesa_base": 15, "penalidade_furtividade": True, "preco_base": 120,
        "descricao": "Um peitoral de couro com pequenas escamas de metal sobrepostas, oferecendo boa proteção."
    },
    {
        "id": "botas_reforcadas", "nome": "Botas Reforçadas", "tipo": "armadura", "slot": "pes",
        "categoria": "media", "defesa_base": 1, "preco_base": 30,
        "descricao": "Botas de couro com placas de metal para proteger os pés."
    },

    # --- TIER 3: Armaduras Pesadas ---
    {
        "id": "cota_de_malha", "nome": "Cota de Malha", "tipo": "armadura", "slot": "peito",
        "categoria": "pesada", "defesa_base": 16, "penalidade_furtividade": True,
        "preco_base": 150, "descricao": "Uma armadura flexível e resistente de anéis de metal interligados."
    },
    {
        "id": "peitoral_de_aco", "nome": "Peitoral de Aço", "tipo": "armadura", "slot": "peito",
        "categoria": "pesada", "defesa_base": 17, "penalidade_furtividade": True,
        "preco_base": 400, "descricao": "Uma placa sólida de aço que cobre o torso."
    },
    {
        "id": "armadura_de_placas_completa", "nome": "Armadura de Placas Completa", "tipo": "armadura", "slot": "peito",
        "categoria": "pesada", "defesa_base": 18, "penalidade_furtividade": True,
        "preco_base": 1500, "descricao": "O auge da proteção pessoal, uma armadura completa de placas de aço moldadas."
    },
    {
        "id": "elmo_de_aco", "nome": "Elmo de Aço", "tipo": "armadura", "slot": "cabeca",
        "categoria": "pesada", "defesa_base": 2, "preco_base": 60,
        "descricao": "Um capacete de aço fechado que oferece excelente proteção."
    },
    {
        "id": "grevas_de_aco", "nome": "Grevas de Aço", "tipo": "armadura", "slot": "pernas",
        "categoria": "pesada", "defesa_base": 1, "preco_base": 100,
        "descricao": "Placas de metal que protegem as canelas."
    },

    # --- Escudos ---
    {
        "id": "escudo_de_madeira", "nome": "Escudo de Madeira", "tipo": "armadura", "slot": "mao_secundaria",
        "categoria": "escudo", "defesa_base": 2, "preco_base": 20,
        "descricao": "Um escudo simples feito de madeira reforçada."
    },
    {
        "id": "escudo_de_aco", "nome": "Escudo de Aço", "tipo": "armadura", "slot": "mao_secundaria",
        "categoria": "escudo", "defesa_base": 3, "preco_base": 80,
        "descricao": "Um escudo de aço pesado que oferece proteção substancial."
    },
]

INDICE_ARMADURAS = {"by_id": {a["id"]: a for a in ARMADURAS}}
