# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: ITENS - RECEITAS DE CRAFTING
================================================================================================
"""
from typing import List, Dict

RECEITAS: List[Dict] = [
    # --- Alquimia ---
    {
        "id": "rec_pocao_cura_fraca", "nome": "Receita: Poção de Cura Fraca",
        "item_criado_id": "pocao_cura_fraca", "quantidade_criada": 1,
        "ingredientes": {"erva_simples": 2, "frasco_de_vidro": 1},
        "profissao": "alquimia", "nivel_necessario": 1,
        "descricao": "Ensina a criar uma poção de cura fraca."
    },
    {
        "id": "rec_pocao_mana_fraca", "nome": "Receita: Poção de Mana Fraca",
        "item_criado_id": "pocao_mana_fraca", "quantidade_criada": 1,
        "ingredientes": {"essencia_espiritual": 1, "frasco_de_vidro": 1},
        "profissao": "alquimia", "nivel_necessario": 5,
        "descricao": "Ensina a criar uma poção de mana fraca."
    },
    {
        "id": "rec_antidoto_comum", "nome": "Receita: Antídoto Comum",
        "item_criado_id": "antidoto_comum", "quantidade_criada": 1,
        "ingredientes": {"folha_de_serpentina": 1, "rabo_de_rato": 1, "frasco_de_vidro": 1},
        "profissao": "alquimia", "nivel_necessario": 8,
        "descricao": "Ensina a neutralizar venenos comuns."
    },
    {
        "id": "rec_oleo_da_lamina_afiada", "nome": "Receita: Óleo da Lâmina Afiada",
        "item_criado_id": "oleo_da_lamina_afiada", "quantidade_criada": 1,
        "ingredientes": {"glandula_de_veneno_potente": 1, "oleo_base": 1},
        "profissao": "alquimia", "nivel_necessario": 15,
        "descricao": "Ensina a criar um óleo que aumenta o dano da arma."
    },

    # --- Couraria (Leatherworking) ---
    {
        "id": "rec_armadura_de_couro", "nome": "Receita: Armadura de Couro",
        "item_criado_id": "armadura_de_couro", "quantidade_criada": 1,
        "ingredientes": {"pele_de_lobo": 5, "linha_de_linho": 2},
        "profissao": "couraria", "nivel_necessario": 1,
        "descricao": "Ensina a transformar peles de lobo em uma armadura de couro."
    },
    {
        "id": "rec_botas_de_couro_macio", "nome": "Receita: Botas de Couro Macio",
        "item_criado_id": "botas_de_couro_macio", "quantidade_criada": 1,
        "ingredientes": {"pele_de_lobo": 2, "linha_de_linho": 1},
        "profissao": "couraria", "nivel_necessario": 2,
        "descricao": "Ensina a criar botas de couro simples."
    },

    # --- Ferraria ---
    {
        "id": "rec_adaga_de_ferro", "nome": "Receita: Adaga de Ferro",
        "item_criado_id": "arma_adaga_ferro", "quantidade_criada": 1,
        "ingredientes": {"lingote_de_ferro": 2, "tiras_de_couro": 1},
        "profissao": "ferraria", "nivel_necessario": 5,
        "descricao": "Ensina a forjar uma adaga de ferro básica."
    },
    {
        "id": "rec_espada_longa_aco", "nome": "Receita: Espada Longa de Aço",
        "item_criado_id": "arma_espada_longa_aco", "quantidade_criada": 1,
        "ingredientes": {"lingote_de_aco": 5, "tiras_de_couro": 2},
        "profissao": "ferraria", "nivel_necessario": 15,
        "descricao": "Ensina a forjar uma espada longa de aço de alta qualidade."
    },
    {
        "id": "rec_cota_de_malha", "nome": "Receita: Cota de Malha",
        "item_criado_id": "cota_de_malha", "quantidade_criada": 1,
        "ingredientes": {"aneis_de_aco": 20, "tiras_de_couro": 5},
        "profissao": "ferraria", "nivel_necessario": 20,
        "descricao": "Ensina a montar uma cota de malha a partir de anéis de aço."
    },

    # --- Culinária ---
    {
        "id": "rec_carne_cozida", "nome": "Receita: Carne Cozida",
        "item_criado_id": "carne_cozida", "quantidade_criada": 1,
        "ingredientes": {"carne_de_lobo": 1, "sal_comum": 1},
        "profissao": "culinaria", "nivel_necessario": 1,
        "descricao": "Cozinhar a carne de lobo a torna mais palatável e nutritiva."
    }
]

INDICE_RECEITAS = {"by_id": {r["id"]: r for r in RECEITAS}}
