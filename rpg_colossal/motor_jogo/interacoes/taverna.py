# -*- coding: utf-8 -*-
"""
================================================================================================
SISTEMA DE INTERAÇÃO: TAVERNA
================================================================================================
Este arquivo define o `GerenciadorDeTaverna`, uma classe que gerencia as interações
dentro de uma taverna. Tavernas são centros sociais vitais em Aetheria, onde o
jogador pode descansar, obter informações, contratar ajuda e participar de atividades
de lazer.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
- **Gerador de Rumores:** O coração da taverna. Um sistema que gera aleatoriamente
  trechos de conversas e rumores que o jogador pode "ouvir". Alguns rumores são
  apenas para dar cor ao mundo, enquanto outros podem ser pistas para missões
  secretas ou tesouros escondidos.
- **Contratação de Mercenários:** A taverna é um local comum para encontrar
  aventureiros em busca de trabalho. Este sistema permitirá ao jogador contratar
  aliados temporários.
- **Mini-jogos:** Um framework para a implementação de mini-jogos, como jogos de
  cartas ou dados, para que o jogador possa relaxar e talvez ganhar algum dinheiro.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import random
from typing import Dict, Any, List

# Importa as classes de entidade para interagir com o jogador.
try:
    from ..entidades.personagem import Personagem
except ImportError:
    Personagem = object

# ==============================================================================================
# == SEÇÃO 2: BANCO DE DADOS DE RUMORES (EXEMPLO) ==============================================
# ==============================================================================================
# Em um jogo completo, isto estaria em `banco_de_dados/rumores.py`.
RUMORES_GENERICOS = [
    "Dizem que o ferreiro anda de mau humor desde que sua remessa de aço foi roubada...",
    "Ouvi dizer que a velha torre na floresta emite luzes estranhas durante a noite.",
    "Cuidado com a estrada ao sul, um grupo de bandidos tem atacado viajantes.",
    "A colheita deste ano parece promissora, graças aos deuses.",
    "O lorde local aumentou os impostos de novo... tempos difíceis.",
]
RUMORES_DE_MISSAO = [
    {
        "rumor": "Um velho mapa foi encontrado nas ruínas do Templo do Sol... dizem que leva a um tesouro antigo.",
        "id_missao_relacionada": "missao_tesouro_escondido"
    },
    {
        "rumor": "O filho do moleiro desapareceu perto da Caverna dos Goblins. Ele oferece uma boa recompensa para quem o trouxer de volta.",
        "id_missao_relacionada": "missao_resgate_goblin"
    }
]

# ==============================================================================================
# == SEÇÃO 3: CLASSE GERENCIADORDETAVERNA ======================================================
# ==============================================================================================
class GerenciadorDeTaverna:
    """
    Gerencia as interações e eventos dentro de uma taverna.
    """
    def __init__(self, nome_taverna: str):
        self.nome_taverna = nome_taverna
        print(f"Você entra na taverna '{self.nome_taverna}'. O ambiente está cheio de conversas e o cheiro de cerveja.")

    def ouvir_rumores(self) -> str:
        """
        Gera e retorna um rumor aleatório para o jogador.
        """
        # Chance de ouvir um rumor de missão em vez de um genérico
        if random.random() < 0.2: # 20% de chance
            rumor_especial = random.choice(RUMORES_DE_MISSAO)
            print(f"Você ouve um sussurro interessante em uma mesa próxima...")
            return rumor_especial["rumor"]
        else:
            print("Você presta atenção às conversas ao redor...")
            return random.choice(RUMORES_GENERICOS)

    def jogar_cartas(self, jogador: Personagem, aposta: int) -> None:
        """Placeholder para um mini-jogo de cartas."""
        print(f"\nVocê se senta para uma partida de 'Dragões e Tesouros', o jogo de cartas local.")
        print("A lógica do jogo ainda não foi implementada.")
        # Lógica do jogo...
        # if vitoria:
        #     jogador.carteira['ouro'] += aposta
        # else:
        #     jogador.carteira['ouro'] -= aposta
        pass

    def contratar_mercenario(self, jogador: Personagem) -> None:
        """Placeholder para o sistema de contratação."""
        print("\nVocê se aproxima do quadro de mercenários.")
        print("Ainda não há ninguém disponível para contratação.")
        # Lógica para listar mercenários e contratar...
        pass

    def iniciar_interacao(self, jogador: Personagem):
        """Apresenta o menu de opções da taverna."""
        while True:
            print(f"\n--- Taverna: {self.nome_taverna} ---")
            print("[1] - Ouvir rumores")
            print("[2] - Jogar cartas (Aposta: 10 ouro)")
            print("[3] - Contratar mercenário")
            print("[4] - Sair da taverna")

            escolha = input("> ")

            if escolha == "1":
                rumor = self.ouvir_rumores()
                print(f"Rumor: “{rumor}”")
            elif escolha == "2":
                self.jogar_cartas(jogador, 10)
            elif escolha == "3":
                self.contratar_mercenario(jogador)
            elif escolha == "4":
                print("Você termina sua bebida e sai da taverna.")
                break
            else:
                print("Opção inválida.")

# ==============================================================================================
# == SEÇÃO 4: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("== DEMONSTRAÇÃO DO SISTEMA DE TAVERNA ==")
    print("="*80)

    class MockPersonagemTaverna:
        def __init__(self, nome):
            self.nome = nome

    jogador_teste = MockPersonagemTaverna("Aventureiro Curioso")
    taverna = GerenciadorDeTaverna("O Pônei Saltitante")

    print("\n--- Testando o sistema de rumores ---")
    for i in range(3):
        print(f"\nTentativa {i+1}:")
        rumor_ouvido = taverna.ouvir_rumores()
        print(f"Rumor ouvido: “{rumor_ouvido}”")

    print("\n--- Testando outras opções (placeholders) ---")
    taverna.jogar_cartas(jogador_teste, 10)
    taverna.contratar_mercenario(jogador_teste)
