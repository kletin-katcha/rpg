# -*- coding: utf-8 -*-
"""
================================================================================================
PACOTE DO BANCO DE DADOS: MONSTROS
================================================================================================
Este arquivo `__init__.py` serve como o agregador central para todos os monstros
definidos no pacote. Ele importa as listas de monstros de todos os arquivos
individuais e as combina em uma única lista mestre e em um dicionário indexado
para fácil acesso pelo resto do motor do jogo.

-------------------------
-- ESTRUTURA E PROPÓSITO --
-------------------------
- **Agregação:** Evita que outros módulos precisem saber sobre os arquivos
  específicos (`monstros_floresta.py`, `bosses.py`, etc.). Eles podem simplesmente
  importar `INDICE_MONSTROS` deste pacote.
- **Indexação:** Cria o `INDICE_MONSTROS`, um dicionário onde as chaves são os IDs
  dos monstros. Isso permite uma busca de monstros extremamente rápida e eficiente
  (O(1) em vez de O(n) se fosse preciso percorrer uma lista).
- **Manutenibilidade:** Para adicionar novos monstros, basta criar um novo arquivo
  no pacote e adicionar a importação e a concatenação da lista aqui. O resto do
  código funcionará sem alterações.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES E AGREGAÇÃO ==========================================================
# ==============================================================================================
from typing import List, Dict

# Importa as listas de monstros de cada arquivo de dados
from .monstros_regiao_inicial import MONSTROS_REGIAO_INICIAL
from .monstros_floresta import MONSTROS_FLORESTA
from .monstros_cavernas import MONSTROS_CAVERNAS
# from .bosses import BOSSES # Comentado até que o arquivo seja populado
# Adicionar outras importações conforme novos arquivos são criados...

# Combina todas as listas em uma única lista mestre de todos os monstros do jogo.
LISTA_MESTRA_MONSTROS = (
    MONSTROS_REGIAO_INICIAL +
    MONSTROS_FLORESTA +
    MONSTROS_CAVERNAS
    # + BOSSES
)

# ==============================================================================================
# == SEÇÃO 2: CONSTRUÇÃO DO ÍNDICE =============================================================
# ==============================================================================================
def construir_indice_monstros(lista_de_dados: List[Dict]) -> Dict:
    """Constrói um dicionário indexado por ID a partir de uma lista."""
    indice_por_id = {item["id"]: item for item in lista_de_dados}
    return {"by_id": indice_por_id, "lista_completa": lista_de_dados}

# O índice final que será importado por outros módulos do jogo.
INDICE_MONSTROS = construir_indice_monstros(LISTA_MESTRA_MONSTROS)
