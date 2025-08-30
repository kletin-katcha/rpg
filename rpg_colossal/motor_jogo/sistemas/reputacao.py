# -*- coding: utf-8 -*-
"""
================================================================================================
SISTEMA DE REPUTAÇÃO E ALINHAMENTO
================================================================================================
Este arquivo define o `ReputacaoManager`, responsável por rastrear e gerenciar a
reputação do jogador com as diversas facções do mundo, bem como seu alinhamento moral.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
O sistema é projetado para dar peso às escolhas do jogador, fazendo com que suas
ações tenham consequências sociais e narrativas.

- **Reputação de Facção:** A reputação é medida em uma escala numérica (ex: -1000 a
  1000). Valores altos desbloqueiam missões, mercadores especiais e diálogos
  amigáveis. Valores baixos podem levar à hostilidade.
- **Alinhamento Moral:** Um sistema mais simples (ex: um único valor numérico) que
  rastreia as escolhas "boas", "neutras" e "más" do jogador, podendo afetar
  habilidades de certas classes (como Paladino) e o final do jogo.
- **Modificadores:** Ações como completar missões, tomar certas decisões em diálogos
  ou até mesmo ser pego roubando podem modificar tanto a reputação quanto o alinhamento.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
from typing import Dict, Any

# Importa a classe de entidade para interagir com o estado do jogador.
try:
    from ..entidades.personagem import Personagem
except ImportError:
    Personagem = object

# ==============================================================================================
# == SEÇÃO 2: DADOS DE FACÇÕES (EXEMPLO) =======================================================
# ==============================================================================================
# Em um jogo completo, isto estaria em `banco_de_dados/faccoes.py`.
FACOES_EXEMPLO = {
    "guilda_dos_aventureiros": {"nome": "Guilda dos Aventureiros", "rivais": []},
    "alianca_mercante": {"nome": "Aliança Mercante", "rivais": ["guilda_dos_ladroes"]},
    "guilda_dos_ladroes": {"nome": "Guilda dos Ladrões", "rivais": ["alianca_mercante"]},
    "circulo_dos_druidas": {"nome": "Círculo dos Druidas", "rivais": []},
}

NIVEIS_REPUTACAO = {
    (-1000, -751): "Odiado",
    (-750, -251): "Hostil",
    (-250, 250): "Neutro",
    (251, 750): "Amigável",
    (751, 1000): "Venerado",
}

# ==============================================================================================
# == SEÇÃO 3: CLASSE REPUTACAOMANAGER ==========================================================
# ==============================================================================================
class ReputacaoManager:
    """
    Gerencia a reputação e o alinhamento do jogador.
    """
    def __init__(self, personagem: Personagem, faccoes: Dict):
        """
        Inicializa o sistema de reputação para um personagem específico.

        Args:
            personagem (Personagem): O personagem do jogador.
            faccoes (Dict): O dicionário de todas as facções do jogo.
        """
        self.personagem = personagem
        # Inicializa a reputação do personagem com todas as facções como neutra (0).
        if not hasattr(self.personagem, 'reputacao'):
            self.personagem.reputacao = {f_id: 0 for f_id in faccoes.keys()}
        # Inicializa o alinhamento como neutro.
        if not hasattr(self.personagem, 'alinhamento'):
            self.personagem.alinhamento = 0 # -100 (Mau) a 100 (Bom)

    def alterar_reputacao(self, id_faccao: str, pontos: int):
        """
        Altera a reputação do jogador com uma facção.

        Args:
            id_faccao (str): O ID da facção a ser modificada.
            pontos (int): A quantidade de pontos a serem adicionados (pode ser negativa).
        """
        if id_faccao in self.personagem.reputacao:
            self.personagem.reputacao[id_faccao] += pontos
            print(f"Sua reputação com '{FACOES_EXEMPLO[id_faccao]['nome']}' mudou em {pontos}.")
            self.verificar_mudanca_de_nivel(id_faccao)
        else:
            print(f"DEBUG: Facção desconhecida: {id_faccao}")

    def alterar_alinhamento(self, pontos: int):
        """Altera o alinhamento moral do jogador."""
        self.personagem.alinhamento += pontos
        self.personagem.alinhamento = max(-100, min(100, self.personagem.alinhamento)) # Limita entre -100 e 100
        print(f"Seu alinhamento moral mudou em {pontos}.")

    def verificar_mudanca_de_nivel(self, id_faccao: str):
        """Verifica e anuncia se o nível de reputação mudou."""
        rep_atual = self.personagem.reputacao[id_faccao]
        for (min_val, max_val), nome_nivel in NIVEIS_REPUTACAO.items():
            if min_val <= rep_atual <= max_val:
                print(f"Seu status com '{FACOES_EXEMPLO[id_faccao]['nome']}' agora é: {nome_nivel}")
                break

# ==============================================================================================
# == SEÇÃO 4: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("== DEMONSTRAÇÃO DO SISTEMA DE REPUTAÇÃO ==")
    print("="*80)

    class MockPersonagemReputacao:
        def __init__(self, nome):
            self.nome = nome

    jogador_teste = MockPersonagemReputacao("Aventureiro Influente")

    # Inicia o manager para o jogador
    gerenciador_rep = ReputacaoManager(jogador_teste, FACOES_EXEMPLO)

    print(f"\nReputação inicial: {jogador_teste.reputacao}")
    print(f"Alinhamento inicial: {jogador_teste.alinhamento}")

    # Simula a conclusão de uma missão para a guilda dos aventureiros
    print("\n-- Completando missão para a Guilda dos Aventureiros --")
    gerenciador_rep.alterar_reputacao("guilda_dos_aventureiros", 50)
    gerenciador_rep.alterar_alinhamento(10) # Ação considerada "boa"

    # Simula ser pego roubando da aliança mercante
    print("\n-- Sendo pego roubando da Aliança Mercante --")
    gerenciador_rep.alterar_reputacao("alianca_mercante", -70)
    gerenciador_rep.alterar_alinhamento(-15) # Ação considerada "má"

    print(f"\nReputação final: {jogador_teste.reputacao}")
    print(f"Alinhamento final: {jogador_teste.alinhamento}")
