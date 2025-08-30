# -*- coding: utf-8 -*-
"""
================================================================================================
SISTEMA DE INTERAÇÃO: GUILDA
================================================================================================
Este arquivo define o `GerenciadorDeGuilda`, uma classe para gerenciar as interações
e a progressão do jogador dentro de uma facção ou guilda específica.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
- **Progressão de Facção:** Guildas são a principal forma de o jogador interagir com o
  sistema de reputação. Completar missões para uma guilda aumenta a reputação,
  desbloqueando novos ranks, itens e missões.
- **Quadro de Missões:** Cada guilda possui um "quadro" de missões que são
  disponibilizadas aos membros. A complexidade e a recompensa das missões
  aumentam conforme o ranking do jogador na guilda.
- **Rivalidades:** Ações para uma guilda podem impactar negativamente a reputação
  com facções rivais, criando escolhas com consequências.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
from typing import Dict, Any, List

# Importa as classes e sistemas necessários
try:
    from ..entidades.personagem import Personagem
    from ..sistemas.reputacao import ReputacaoManager
except ImportError:
    Personagem = object
    ReputacaoManager = object

# ==============================================================================================
# == SEÇÃO 2: DADOS DE GUILDA (EXEMPLO) ========================================================
# ==============================================================================================
# Em um jogo completo, isto estaria em `banco_de_dados/faccoes.py` ou `guildas.py`.
DADOS_GUILDA_EXEMPLO = {
    "guilda_dos_aventureiros": {
        "nome": "Guilda dos Aventureiros",
        "ranks": ["Iniciante", "Explorador", "Veterano", "Mestre da Guilda"],
        "quadro_de_missoes": {
            "Iniciante": ["missao_coletar_peles_lobo", "missao_limpar_covil_goblin"],
            "Explorador": ["missao_escoltar_mercador", "missao_investigar_ruinas"],
        }
    }
}

# ==============================================================================================
# == SEÇÃO 3: CLASSE GERENCIADORDEGUILDA =======================================================
# ==============================================================================================
class GerenciadorDeGuilda:
    """
    Gerencia as interações e a progressão do jogador em uma guilda.
    """
    def __init__(self, id_guilda: str, reputacao_manager: ReputacaoManager):
        dados_guilda = DADOS_GUILDA_EXEMPLO.get(id_guilda)
        if not dados_guilda:
            raise ValueError(f"Guilda com ID '{id_guilda}' não encontrada.")

        self.id_guilda = id_guilda
        self.dados = dados_guilda
        self.nome = dados_guilda["nome"]
        self.reputacao_manager = reputacao_manager
        print(f"Você está no salão da '{self.nome}'.")

    def obter_rank_jogador(self, personagem: Personagem) -> str:
        """Calcula o rank do jogador com base na sua reputação."""
        rep = self.reputacao_manager.personagem.reputacao.get(self.id_guilda, 0)
        if rep < 250: return "Não-membro"
        if rep < 500: return "Iniciante"
        if rep < 750: return "Explorador"
        return "Veterano"

    def mostrar_quadro_de_missoes(self, personagem: Personagem):
        """Mostra as missões disponíveis para o rank atual do jogador."""
        rank_atual = self.obter_rank_jogador(personagem)
        print(f"\n--- QUADRO DE MISSÕES (Rank: {rank_atual}) ---")

        missoes_disponiveis = self.dados["quadro_de_missoes"].get(rank_atual, [])
        if not missoes_disponiveis:
            print("Não há missões disponíveis para o seu rank no momento.")
            return

        for i, id_missao in enumerate(missoes_disponiveis):
            print(f"[{i+1}] - {id_missao}")

    def iniciar_interacao(self, personagem: Personagem):
        """Apresenta o menu de opções da guilda."""
        while True:
            rank = self.obter_rank_jogador(personagem)
            print(f"\n--- {self.nome} (Seu Rank: {rank}) ---")
            print("[1] - Ver Quadro de Missões")
            print("[2] - Falar com o Mestre da Guilda")
            print("[3] - Sair da Guilda")

            escolha = input("> ")
            if escolha == "1":
                self.mostrar_quadro_de_missoes(personagem)
            elif escolha == "2":
                print("O Mestre da Guilda está ocupado no momento.")
            elif escolha == "3":
                break
            else:
                print("Opção inválida.")

# ==============================================================================================
# == SEÇÃO 4: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("== DEMONSTRAÇÃO DO SISTEMA DE GUILDA ==")
    print("="*80)

    class MockPersonagemGuilda:
        def __init__(self, nome):
            self.nome = nome
            self.reputacao = {"guilda_dos_aventureiros": 260} # Começa como Amigável -> Iniciante

    class MockReputacaoManager:
        def __init__(self, personagem):
            self.personagem = personagem

    jogador_teste = MockPersonagemGuilda("Aventureiro Promissor")
    rep_manager_teste = MockReputacaoManager(jogador_teste)

    guilda = GerenciadorDeGuilda("guilda_dos_aventureiros", rep_manager_teste)

    print(f"\n--- Verificando o rank de {jogador_teste.nome} ---")
    rank = guilda.obter_rank_jogador(jogador_teste)
    print(f"Rank atual: {rank}")

    print("\n--- Mostrando missões disponíveis ---")
    guilda.mostrar_quadro_de_missoes(jogador_teste)

    print("\n--- Simulando aumento de reputação ---")
    jogador_teste.reputacao["guilda_dos_aventureiros"] = 510 # Sobe para Explorador
    rank = guilda.obter_rank_jogador(jogador_teste)
    print(f"Novo rank: {rank}")
    guilda.mostrar_quadro_de_missoes(jogador_teste)
