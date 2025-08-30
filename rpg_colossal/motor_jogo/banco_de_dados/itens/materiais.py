# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: ITENS - MATERIAIS DE CRAFTING
================================================================================================
Este arquivo contém a definição de todos os materiais usados em receitas de criação.
"""
from typing import List, Dict

MATERIAIS: List[Dict] = [
    # --- Materiais de Monstros ---
    {
        "id": "pele_de_lobo", "nome": "Pele de Lobo", "tipo": "material",
        "preco_base": 8, "descricao": "A pele de um lobo, útil para couraria."
    },
    {
        "id": "carne_de_lobo", "nome": "Carne de Lobo", "tipo": "material",
        "preco_base": 5, "descricao": "Carne de caça, pode ser cozida."
    },
    {
        "id": "presa_de_javali", "nome": "Presa de Javali", "tipo": "material",
        "preco_base": 12, "descricao": "Uma presa afiada, pode ser usada em artesanato ou como um componente alquímico."
    },
    {
        "id": "rabo_de_rato", "nome": "Rabo de Rato", "tipo": "material",
        "preco_base": 1, "descricao": "Não muito útil, exceto talvez em alguma poção duvidosa."
    },

    # --- Materiais de Coleta (Minérios e Ervas) ---
    {
        "id": "lingote_de_ferro", "nome": "Lingote de Ferro", "tipo": "material",
        "preco_base": 10, "descricao": "Uma barra de ferro puro, pronta para ser forjada."
    },
    {
        "id": "lingote_de_aco", "nome": "Lingote de Aço", "tipo": "material",
        "preco_base": 30, "descricao": "Aço refinado, mais forte e mais durável que o ferro."
    },
    {
        "id": "erva_simples", "nome": "Erva Simples", "tipo": "material",
        "preco_base": 2, "descricao": "Uma erva comum com propriedades curativas fracas."
    },
    {
        "id": "folha_de_serpentina", "nome": "Folha de Serpentina", "tipo": "material",
        "preco_base": 15, "descricao": "Uma erva conhecida por suas propriedades desintoxicantes."
    },

    # --- Componentes Compráveis ---
    {
        "id": "frasco_de_vidro", "nome": "Frasco de Vidro", "tipo": "material",
        "preco_base": 1, "descricao": "Um frasco vazio, essencial para a alquimia."
    },
    {
        "id": "linha_de_linho", "nome": "Linha de Linho", "tipo": "material",
        "preco_base": 2, "descricao": "Linha forte usada em costura e couraria."
    },
    {
        "id": "sal_comum", "nome": "Sal Comum", "tipo": "material",
        "preco_base": 1, "descricao": "Usado para preservar e temperar alimentos."
    }
]

INDICE_MATERIAIS = {"by_id": {m["id"]: m for m in MATERIAIS}}
