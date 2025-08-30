# -*- coding: utf-8 -*-
"""
================================================================================================
SISTEMA DE CRAFTING (CRIAÇÃO DE ITENS)
================================================================================================
Este arquivo define o sistema de criação de itens de Aetheria. Ele gerencia as
receitas, os materiais necessários e a lógica para forjar, costurar ou encantar
novos equipamentos e consumíveis.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
O sistema de crafting é baseado em funções, pois o ato de criar um item é em grande
parte um processo sem estado (stateless), que recebe entradas (materiais, receita)
e produz uma saída (o item, ou uma falha).

- **Receitas:** A base do sistema. Cada item criável tem uma receita correspondente
  que define os materiais e as condições necessárias.
- **Probabilidade de Sucesso:** O sucesso não é garantido. A chance de criar um item
  pode depender da habilidade do personagem (ex: "Ferraria"), do nível da receita
  e da qualidade dos materiais.
- **Resultados Múltiplos:** Uma tentativa de criação pode ter vários resultados:
  - **Falha Crítica:** Os materiais são perdidos.
  - **Falha:** Alguns materiais são perdidos.
  - **Sucesso:** O item é criado com stats base.
  - **Sucesso Crítico:** O item é criado com bônus (ex: "Obra-Prima").
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import random
from typing import Dict, Any, List, Optional

# Importa as classes de entidade para interagir com o inventário do jogador.
try:
    from ..entidades.personagem import Personagem
except ImportError:
    Personagem = object

# ==============================================================================================
# == SEÇÃO 2: BANCO DE DADOS DE RECEITAS (EXEMPLO) =============================================
# ==============================================================================================
# Em um jogo completo, isto estaria em `banco_de_dados/receitas.py`.
# Para demonstração, está incluído aqui.
RECEITAS_EXEMPLO = {
    "espada_de_ferro": {
        "nome": "Espada de Ferro",
        "materiais": {"lingote_de_ferro": 5, "tiras_de_couro": 2},
        "nivel_habilidade": {"ferraria": 10},
        "item_criado_id": "item_espada_de_ferro"
    },
    "pocao_cura_menor": {
        "nome": "Poção de Cura Menor",
        "materiais": {"frasco_vazio": 1, "erva_simples": 3},
        "nivel_habilidade": {"alquimia": 5},
        "item_criado_id": "item_pocao_cura_menor"
    }
}

# ==============================================================================================
# == SEÇÃO 3: LÓGICA DE CRAFTING ===============================================================
# ==============================================================================================
def verificar_materiais(personagem: Personagem, receita: Dict) -> bool:
    """Verifica se o personagem possui os materiais necessários."""
    # Lógica placeholder
    print(f"Verificando se {personagem.nome} tem os materiais para '{receita['nome']}'...")
    return True

def consumir_materiais(personagem: Personagem, receita: Dict) -> None:
    """Remove os materiais do inventário do personagem."""
    # Lógica placeholder
    print("Consumindo materiais do inventário...")
    pass

def tentar_criar_item(personagem: Personagem, id_receita: str) -> Optional[Dict]:
    """
    Tenta criar um item com base em uma receita.

    Args:
        personagem (Personagem): O personagem que está tentando a criação.
        id_receita (str): O ID da receita a ser usada.

    Returns:
        Optional[Dict]: Um dicionário representando o item criado, ou None em caso de falha.
    """
    receita = RECEITAS_EXEMPLO.get(id_receita)
    if not receita:
        print(f"Receita '{id_receita}' não encontrada.")
        return None

    if not verificar_materiais(personagem, receita):
        print("Materiais insuficientes.")
        return None

    consumir_materiais(personagem, receita)

    # Lógica de Sucesso (simplificada)
    # No futuro, usaria `personagem.habilidades['ferraria']` vs `receita['nivel_habilidade']`
    chance_sucesso = 0.8
    rolagem = random.random()

    if rolagem > chance_sucesso:
        print(f"A criação de '{receita['nome']}' falhou! Alguns materiais foram perdidos.")
        return None

    # Lógica de Sucesso Crítico
    chance_critico = 0.1
    if random.random() < chance_critico:
        print(f"✨ SUCESSO CRÍTICO! Você criou uma '{receita['nome']}' de qualidade superior!")
        # item_criado = carregar_item(receita['item_criado_id'])
        # item_criado['stats'] *= 1.2 # Bônus de 20% nos stats
        # return item_criado
    else:
        print(f"Sucesso! Você criou '{receita['nome']}'.")
        # item_criado = carregar_item(receita['item_criado_id'])
        # return item_criado

    # Retorna um item mock por enquanto
    return {"id": receita["item_criado_id"], "nome": receita["nome"]}


# ==============================================================================================
# == SEÇÃO 4: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("== DEMONSTRAÇÃO DO SISTEMA DE CRAFTING ==")
    print("="*80)

    class MockPersonagemCrafting:
        def __init__(self, nome):
            self.nome = nome
            self.inventario = {"lingote_de_ferro": 10, "tiras_de_couro": 5}

    jogador_teste = MockPersonagemCrafting("Ferreiro Habilidoso")

    print(f"\n{jogador_teste.nome} tenta criar uma Espada de Ferro...")

    item_criado = tentar_criar_item(jogador_teste, "espada_de_ferro")

    if item_criado:
        print(f"Item recebido: {item_criado['nome']}")
    else:
        print("Melhor sorte na próxima vez.")
