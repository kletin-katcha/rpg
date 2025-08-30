# -*- coding: utf-8 -*-
"""
================================================================================================
SISTEMA DE INTERAÇÃO: ARENA
================================================================================================
Este arquivo define o `GerenciadorDeArena`, uma classe que gerencia os combates
oficiais, torneios e o sistema de ranking da arena de uma cidade.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
- **Combates Ranqueados:** O jogador pode lutar contra uma série de oponentes controlados
  pela IA para subir no ranking da arena.
- **Torneios:** Eventos especiais onde múltiplos combatentes lutam em um sistema de
  chaves até que reste apenas um campeão.
- **Recompensas e Honra:** Vencer na arena concede recompensas monetárias, itens
  especiais e "Pontos de Honra", que podem ser uma moeda de troca para equipamentos
  exclusivos da arena.
- **Integração com Combate:** A arena é um grande consumidor do `CombatManager`.
  Ela cria os encontros (jogador vs. oponente da arena) e passa para o sistema de
  combate resolver.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
from typing import Dict, Any, List

# Importa as classes e sistemas necessários
try:
    from ..entidades.personagem import Personagem
    from ..entidades.npc import NPC # Oponentes podem ser NPCs
    from ..sistemas.combate import CombatManager
except ImportError:
    Personagem = object
    NPC = object
    CombatManager = object

# ==============================================================================================
# == SEÇÃO 2: DADOS DA ARENA (EXEMPLO) =========================================================
# ==============================================================================================
# Oponentes da arena, com stats e níveis definidos.
OPONENTES_ARENA = {
    "rank_d": [
        {"id": "oponente_goblin_lutador", "nome": "Grishnak, o Goblin Lutador", "nivel": 5},
    ],
    "rank_c": [
        {"id": "oponente_humano_gladiador", "nome": "Crixus, o Gladiador", "nivel": 15},
    ]
}

# ==============================================================================================
# == SEÇÃO 3: CLASSE GERENCIADORDEARENA ========================================================
# ==============================================================================================
class GerenciadorDeArena:
    """
    Gerencia as atividades da arena de combate.
    """
    def __init__(self):
        print("Você está na entrada da grande arena. O som da multidão e o cheiro de areia e aço estão no ar.")
        self.ranking = {} # {id_jogador: pontos_honra}

    def desafiar_oponente(self, jogador: Personagem, id_oponente: str) -> None:
        """
        Inicia uma luta contra um oponente específico da arena.
        """
        # Lógica para carregar os dados do oponente
        # oponente_dados = ...
        # oponente_entidade = NPC(oponente_dados)

        print(f"Você desafia {id_oponente} para um duelo na arena!")

        # Mock de oponentes para o teste
        oponente_mock = NPC({"id": id_oponente, "nome": "Oponente Mock", "nivel": jogador.nivel})

        # Inicia o combate
        # combate = CombatManager([jogador], [oponente_mock])
        # resultado = combate.iniciar_combate()

        # if resultado == "vitoria_jogador":
        #     pontos_ganhos = 10
        #     self.ranking[jogador.id_entidade] = self.ranking.get(jogador.id_entidade, 0) + pontos_ganhos
        #     print(f"VITÓRIA! Você ganhou {pontos_ganhos} pontos de honra.")
        print("A luta foi feroz... (simulação de combate concluída).")


    def iniciar_interacao(self, jogador: Personagem):
        """Apresenta o menu de opções da arena."""
        while True:
            honra = self.ranking.get(jogador.id_entidade, 0)
            print(f"\n--- ARENA DE COMBATE (Sua Honra: {honra}) ---")
            print("[1] - Desafiar oponente do Rank D")
            print("[2] - Participar de Torneio (Em Breve)")
            print("[3] - Ver Ranking")
            print("[4] - Sair da Arena")

            escolha = input("> ")
            if escolha == "1":
                self.desafiar_oponente(jogador, "oponente_goblin_lutador")
            elif escolha == "2":
                print("Não há torneios agendados no momento.")
            elif escolha == "3":
                print(f"Ranking atual: {self.ranking}")
            elif escolha == "4":
                break
            else:
                print("Opção inválida.")

# ==============================================================================================
# == SEÇÃO 4: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("== DEMONSTRAÇÃO DO SISTEMA DE ARENA ==")
    print("="*80)

    class MockPersonagemArena:
        def __init__(self, id, nome, nivel):
            self.id_entidade = id
            self.nome = nome
            self.nivel = nivel

    class MockNPC:
        def __init__(self, dados):
            self.id_entidade = dados.get("id")
            self.nome = dados.get("nome")
            self.nivel = dados.get("nivel")

    # Sobrescreve o NPC importado com o nosso mock local para o teste funcionar
    NPC = MockNPC

    jogador_teste = MockPersonagemArena("player_arena_1", "Gladiador Novato", 10)
    arena = GerenciadorDeArena()

    print("\n--- Testando a interação com a arena ---")
    # A linha abaixo seria para um teste interativo, vamos apenas chamar a função de desafio
    # arena.iniciar_interacao(jogador_teste)

    arena.desafiar_oponente(jogador_teste, "oponente_humano_gladiador")

    print(f"\nRanking final (mock): {arena.ranking}")
