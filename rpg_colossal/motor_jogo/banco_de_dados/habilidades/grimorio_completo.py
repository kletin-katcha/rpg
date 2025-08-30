# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: GRIMÓRIO COMPLETO
================================================================================================
Este arquivo centraliza e combina todos os dicionários de habilidades de outros
arquivos em um único GRIMÓRIO_COMPLETO para fácil acesso pelo motor de jogo.
"""

from . import fisicas, magicas_arcano, magicas_fogo, magicas_gelo, raciais, suporte

# --- Construção do Índice para Todas as Habilidades ---
# Começamos com uma base vazia
GRIMORIO_COMPLETO = {}

# Lista de todos os módulos de habilidades e os nomes de suas listas de dados
modulos_de_habilidades = [
    (fisicas, "HABILIDADES_FISICAS"),
    # Adicionar outros módulos aqui no futuro
    # (magicas_arcano, "HABILIDADES_ARCANAS"),
    # (suporte, "HABILIDADES_SUPORTE"),
]

# Itera sobre cada módulo para extrair e indexar as habilidades
for modulo, nome_lista in modulos_de_habilidades:
    if hasattr(modulo, nome_lista):
        lista_habilidades = getattr(modulo, nome_lista)
        for habilidade in lista_habilidades:
            if "id" in habilidade:
                GRIMORIO_COMPLETO[habilidade["id"]] = habilidade

print(f"GRIMÓRIO COMPLETO carregado com {len(GRIMORIO_COMPLETO)} habilidades.")
