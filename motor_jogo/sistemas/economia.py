# -*- coding: utf-8 -*-
"""
================================================================================================
SISTEMA DE ECONOMIA
================================================================================================
Este arquivo define o `EconomiaManager`, responsável por todas as transações financeiras,
preços de itens e o estado geral da economia do mundo de Aetheria.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
A economia é projetada para ser dinâmica, embora de forma simulada inicialmente.
Os principais componentes são:
- **Múltiplas Moedas:** O jogo pode suportar diferentes tipos de moeda (ouro, gemas,
  essências de alma), cada uma com seu próprio valor e uso.
- **Preços Base:** Cada item no banco de dados terá um `preco_base`.
- **Modificadores de Preço:** O preço final de um item pode ser afetado por:
  - `inflacao_global`: Uma taxa que afeta toda a economia.
  - `modificador_regional`: Preços podem variar de cidade para cidade.
  - `habilidade_personagem`: Habilidades como "Barganha" podem reduzir preços.
- **Transações Seguras:** Funções para comprar e vender garantem que o jogador
  tenha fundos suficientes e que os itens e moedas sejam trocados corretamente.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
from typing import Dict, Any, Optional

# Importa as classes de entidade para interagir com o inventário e carteira do jogador.
try:
    from ..entidades.personagem import Personagem
except ImportError:
    Personagem = object

# ==============================================================================================
# == SEÇÃO 2: CLASSE ECONOMIAMANAGER ===========================================================
# ==============================================================================================
class EconomiaManager:
    """
    Gerencia a economia global e as transações do jogo.
    """
    def __init__(self, precos_base: Dict[str, int], inflacao_inicial: float = 0.0):
        """
        Inicializa o sistema de economia.

        Args:
            precos_base (Dict[str, int]): Um dicionário mapeando `item_id` a seu preço base.
            inflacao_inicial (float): A taxa de inflação inicial do mundo.
        """
        self.precos_base: Dict[str, int] = precos_base
        self.inflacao_global: float = inflacao_inicial
        print("Sistema de Economia inicializado.")

    def obter_preco_final(self, item_id: str, personagem: Optional[Personagem] = None) -> int:
        """
        Calcula o preço final de um item, aplicando inflação e outros modificadores.

        Args:
            item_id (str): O ID do item a ser precificado.
            personagem (Optional[Personagem]): O personagem envolvido na transação,
                                               para aplicar bônus de habilidades.

        Returns:
            int: O preço final calculado.
        """
        preco_base = self.precos_base.get(item_id, 99999) # Preço alto se o item não for encontrado
        preco_ajustado = preco_base * (1 + self.inflacao_global)

        # Lógica futura para bônus de personagem (habilidade de barganha, etc.)
        # if personagem e personagem.tem_habilidade("Barganha"):
        #     preco_ajustado *= 0.9

        return int(preco_ajustado)

    def comprar_item(self, personagem: Personagem, item_id: str, quantidade: int = 1) -> bool:
        """
        Processa a compra de um item por um personagem.

        Verifica se o personagem tem fundos, subtrai o custo e adiciona o item.

        Returns:
            bool: True se a compra foi bem-sucedida, False caso contrário.
        """
        preco_total = self.obter_preco_final(item_id) * quantidade

        # Simplificado para usar uma única moeda "ouro".
        if personagem.carteira.get("ouro", 0) >= preco_total:
            personagem.carteira["ouro"] -= preco_total
            # item_data = carregar_item_do_banco_de_dados(item_id)
            # for _ in range(quantidade):
            #     personagem.adicionar_item(item_data)

            print(f"{personagem.nome} comprou {quantidade}x '{item_id}' por {preco_total} de ouro.")
            return True
        else:
            print(f"{personagem.nome} não tem ouro suficiente para comprar '{item_id}'.")
            return False

    def vender_item(self, personagem: Personagem, item_id: str, quantidade: int = 1) -> bool:
        """
        Processa a venda de um item por um personagem.

        O preço de venda é geralmente uma fração do preço de compra.
        """
        # Verifica se o personagem possui o item.
        # if personagem.inventario.count(item_id) >= quantidade:
        preco_venda_unitario = int(self.obter_preco_final(item_id) * 0.5) # Vende pela metade do preço
        preco_total = preco_venda_unitario * quantidade

        personagem.carteira["ouro"] = personagem.carteira.get("ouro", 0) + preco_total
        # for _ in range(quantidade):
        #     personagem.remover_item(item_id)

        print(f"{personagem.nome} vendeu {quantidade}x '{item_id}' por {preco_total} de ouro.")
        return True
        # else:
        #     print(f"{personagem.nome} não tem '{item_id}' para vender.")
        #     return False

    def atualizar_economia_global(self, evento_mundial: Dict) -> None:
        """
        Ajusta a inflação global com base em eventos do mundo.
        (Placeholder para uma mecânica complexa)
        """
        modificador = evento_mundial.get("modificador_inflacao", 0.0)
        self.inflacao_global += modificador
        print(f"Evento mundial '{evento_mundial['nome']}' afetou a economia! Inflação agora é de {self.inflacao_global:.2%}.")


# ==============================================================================================
# == SEÇÃO 3: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("== DEMONSTRAÇÃO DO SISTEMA DE ECONOMIA ==")
    print("="*80)

    # --- Mocks e Stubs para Teste ---
    class MockPersonagem:
        def __init__(self, nome, ouro_inicial):
            self.nome = nome
            self.carteira = {"ouro": ouro_inicial}
            self.inventario = []

    # --- Cenário de Teste ---
    precos_teste = {"pocao_cura": 50, "espada_de_ferro": 200}
    economia = EconomiaManager(precos_base=precos_teste, inflacao_inicial=0.1)

    jogador_teste = MockPersonagem("Aventureiro Rico", 1000)

    print(f"\nPreço de uma poção: {economia.obter_preco_final('pocao_cura')} de ouro.")

    print(f"\n{jogador_teste.nome} tem {jogador_teste.carteira['ouro']} de ouro.")

    # Tentativa de compra
    economia.comprar_item(jogador_teste, "pocao_cura", 5)
    print(f"Ouro restante: {jogador_teste.carteira['ouro']}")

    # Tentativa de venda
    economia.vender_item(jogador_teste, "pocao_cura", 2)
    print(f"Ouro final: {jogador_teste.carteira['ouro']}")

    # Simulação de evento mundial
    evento = {"nome": "Guerra no Norte", "modificador_inflacao": 0.15}
    economia.atualizar_economia_global(evento)
    print(f"Novo preço de uma poção após o evento: {economia.obter_preco_final('pocao_cura')} de ouro.")
