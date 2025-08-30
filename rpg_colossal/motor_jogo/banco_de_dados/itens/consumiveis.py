# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: ITENS - CONSUMÍVEIS
================================================================================================
"""
from typing import List, Dict

CONSUMIVEIS: List[Dict] = [
    # --- Poções de Cura ---
    {
        "id": "pocao_cura_fraca", "nome": "Poção de Cura Fraca", "tipo": "consumivel",
        "efeito": {"tipo": "cura", "valor": "2d4+2"}, "preco_base": 50,
        "descricao": "Um frasco com um líquido vermelho que restaura um pouco de vida."
    },
    {
        "id": "pocao_cura_normal", "nome": "Poção de Cura", "tipo": "consumivel",
        "efeito": {"tipo": "cura", "valor": "4d4+4"}, "preco_base": 200,
        "descricao": "Restaura uma quantidade moderada de vida."
    },
    {
        "id": "pocao_cura_forte", "nome": "Poção de Cura Forte", "tipo": "consumivel",
        "efeito": {"tipo": "cura", "valor": "8d4+8"}, "preco_base": 750,
        "descricao": "Um líquido radiante que fecha ferimentos graves em segundos."
    },

    # --- Poções de Mana ---
    {
        "id": "pocao_mana_fraca", "nome": "Poção de Mana Fraca", "tipo": "consumivel",
        "efeito": {"tipo": "restaurar_mana", "valor": 20}, "preco_base": 60,
        "descricao": "Um líquido azul cintilante que restaura um pouco de mana."
    },
    {
        "id": "pocao_mana_normal", "nome": "Poção de Mana", "tipo": "consumivel",
        "efeito": {"tipo": "restaurar_mana", "valor": 50}, "preco_base": 250,
        "descricao": "Restaura uma quantidade moderada de mana."
    },

    # --- Elixires e Antídotos ---
    {
        "id": "antidoto_comum", "nome": "Antídoto Comum", "tipo": "consumivel",
        "efeito": {"tipo": "remover_debuff", "nome_efeito": "Veneno"}, "preco_base": 75,
        "descricao": "Neutraliza venenos comuns."
    },
    {
        "id": "elixir_da_forca_do_urso", "nome": "Elixir da Força do Urso", "tipo": "consumivel",
        "efeito": {"tipo": "buff_temporario", "atributo": "forca", "valor": 5, "duracao": 60},
        "preco_base": 300, "descricao": "Concede a força de um urso por um minuto."
    },
    {
        "id": "oleo_da_lamina_afiada", "nome": "Óleo da Lâmina Afiada", "tipo": "consumivel",
        "efeito": {"tipo": "buff_temporario_arma", "atributo": "dano", "valor": 3, "duracao": 60},
        "preco_base": 200, "descricao": "Um óleo que, quando aplicado a uma arma, a torna magicamente mais afiada."
    },

    # --- Utilidades ---
    {
        "id": "tocha", "nome": "Tocha", "tipo": "consumivel",
        "efeito": {"tipo": "iluminacao", "duracao_segundos": 600}, "preco_base": 1,
        "descricao": "Ilumina áreas escuras. Queima por 10 minutos."
    },
    {
        "id": "kit_de_arrombamento", "nome": "Kit de Arrombamento", "tipo": "consumivel",
        "efeito": {"tipo": "ferramenta", "uso": "abrir_fechadura"}, "preco_base": 25,
        "descricao": "Um conjunto de gazuas e outras ferramentas para ladrões habilidosos."
    },
    {
        "id": "armadilha_de_urso", "nome": "Armadilha de Urso", "tipo": "consumivel",
        "efeito": {"tipo": "armadilha_de_chao", "dano": "1d10", "efeito_secundario": "imobilizar"},
        "preco_base": 40, "descricao": "Uma armadilha de metal serrilhada que prende e fere quem pisa nela."
    }
]

INDICE_CONSUMIVEIS = {"by_id": {c["id"]: c for c in CONSUMIVEIS}}
