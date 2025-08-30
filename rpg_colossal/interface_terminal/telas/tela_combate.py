# -*- coding: utf-8 -*-
"""
================================================================================================
TELA: COMBATE
================================================================================================
Este módulo é responsável por renderizar e gerenciar a tela de combate, a interface
para os encontros por turno de Aetheria.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
- **Controlador de Loop de Combate:** A função `exibir_combate` atua como o
  controlador principal para a interface de combate. Ela instancia o `CombatManager`
  e entra em um loop que persiste enquanto o combate estiver em andamento.

- **Renderização de Estado:** A cada passo do loop, a tela é limpa e o estado
  atual do combate (HP dos combatentes, log de ações) é renderizado. A função
  `_renderizar_estado_combate` é responsável por essa apresentação visual.

- **Entrada de Ação do Jogador:** Quando é o turno de um personagem do jogador, o
  loop pausa e a função `_obter_acao_jogador_ui` é chamada. Esta função apresenta
  um menu de ações (Atacar, Habilidades, etc.) e retorna a ação escolhida pelo
  jogador em um formato que o `CombatManager` entende.

- **Desacoplamento UI-Lógica:** A tela de combate não sabe *como* calcular dano
  ou processar uma habilidade. Sua única responsabilidade é exibir o estado que o
  `CombatManager` fornece e enviar as intenções do jogador de volta para o
.  `CombatManager` processar.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import sys
import os
from typing import List, Dict, Any

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

try:
    from rpg_colossal.motor_jogo.entidades.personagem import Personagem
    from rpg_colossal.motor_jogo.entidades.monstro import Monstro
    from rpg_colossal.motor_jogo.sistemas.combate import CombatManager
    from rpg_colossal.motor_jogo.utilitarios import funcoes_gerais as geral
except ImportError:
    # Mocks para execução independente
    class Personagem: pass
    class Monstro: pass
    class CombatManager:
        def __init__(self, p, m): self.estado_combate = "vitoria_jogador"
        def obter_estado_atual(self): return {"log_combate": []}
    class geral:
        def limpar_tela(): pass
        def pausar_tela(): pass

# ==============================================================================================
# == SEÇÃO 2: FUNÇÕES DA TELA DE COMBATE =======================================================
# ==============================================================================================

def _renderizar_estado_combate(estado: Dict):
    """Renderiza o estado atual do campo de batalha."""
    geral.limpar_tela()
    print("=" * 80)

    # Exibe inimigos
    print("Inimigos:")
    for inimigo in estado.get("grupo_inimigos", []):
        hp_bar = f"HP: {inimigo.hp_atual}/{inimigo.hp_max}"
        print(f"  - {inimigo.nome:<20} | {hp_bar}")

    print("-" * 80)

    # Exibe grupo do jogador
    print("Sua Equipe:")
    for jogador in estado.get("grupo_jogador", []):
        hp_bar = f"HP: {jogador.hp_atual}/{jogador.hp_max}"
        mana_bar = f"MP: {jogador.mana_atual}/{jogador.mana_max}"
        print(f"  - {jogador.nome:<20} | {hp_bar:<20} | {mana_bar}")

    print("=" * 80)

    # Exibe o log de combate
    print("\n--- LOG DE COMBATE ---")
    log_recente = estado.get("log_combate", [])[-5:] # Mostra as últimas 5 entradas
    for linha in log_recente:
        print(linha)
    print("-" * 22)


def _obter_acao_jogador_ui(jogador: Personagem, estado_combate: Dict) -> Dict | None:
    """Exibe o menu de ações e obtém a escolha do jogador."""
    print(f"\nÉ a sua vez, {jogador.nome}!")
    print("[1] Atacar")
    print("[2] Habilidades (Não implementado)")
    print("[3] Itens (Não implementado)")

    escolha_acao = input("> ")

    if escolha_acao == '1':
        # Lógica para escolher um alvo
        inimigos_vivos = [e for e in estado_combate["grupo_inimigos"] if e.esta_vivo()]
        if not inimigos_vivos: return None

        print("Escolha um alvo:")
        for i, inimigo in enumerate(inimigos_vivos):
            print(f"  [{i+1}] {inimigo.nome}")

        try:
            escolha_alvo = int(input("> ")) - 1
            if 0 <= escolha_alvo < len(inimigos_vivos):
                alvo = inimigos_vivos[escolha_alvo]
                return {"habilidade_id": "ataque_basico", "alvo_id": alvo.id_entidade}
        except (ValueError, TypeError):
            print("Seleção de alvo inválida.")
            return None
    return None


def exibir_combate(personagem: Personagem, inimigos: List[Monstro]):
    """
    Inicia e gerencia o loop interativo da tela de combate.
    """
    combat_manager = CombatManager([personagem], inimigos)

    while combat_manager.estado_combate == "em_andamento":
        estado = combat_manager.obter_estado_atual()
        _renderizar_estado_combate(estado)

        entidade_da_vez = estado.get("entidade_da_vez")

        if entidade_da_vez == personagem:
            acao = _obter_acao_jogador_ui(personagem, estado)
            if acao:
                combat_manager.executar_acao_jogador(personagem, acao)
            else:
                print("Ação inválida ou cancelada. Passando o turno.")
                combat_manager.turno_atual += 1 # Simplesmente avança o turno
        else:
            # Turno do inimigo é processado automaticamente pelo manager
            print(f"\nTurno de {entidade_da_vez.nome if entidade_da_vez else 'Ninguém'}. Pressione ENTER.")
            geral.pausar_tela()
            combat_manager.processar_proximo_turno()

    # Exibe o estado final do combate
    _renderizar_estado_combate(combat_manager.obter_estado_atual())
    print("\nCombate finalizado!")
    geral.pausar_tela()

# ==============================================================================================
# == SEÇÃO 3: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
import unittest
from unittest.mock import patch, MagicMock

class TestTelaCombate(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '1']) # 1 (Atacar), 1 (Alvo 1)
    @patch(__name__ + '.geral')
    @patch(__name__ + '.CombatManager')
    def test_fluxo_de_turno_do_jogador(self, MockCombatManager, mock_geral, mock_input):
        """Verifica se a UI chama o CombatManager com a ação correta do jogador."""
        # --- Arrange ---
        # Configura a instância mock do CombatManager que será criada dentro da função
        mock_manager_instance = MockCombatManager.return_value

        # Define o estado inicial que o manager retornará
        mock_personagem = MagicMock(spec=Personagem, nome="Herói")
        mock_personagem.hp_atual = 100
        mock_personagem.hp_max = 100
        mock_personagem.mana_atual = 50
        mock_personagem.mana_max = 50
        mock_personagem.classe = {"nome": "Guerreiro"}
        mock_monstro = MagicMock(spec=Monstro, nome="Goblin", id_entidade="goblin_1")
        mock_monstro.esta_vivo.return_value = True
        mock_monstro.hp_atual = 80
        mock_monstro.hp_max = 80

        # O manager começa com o combate em andamento
        mock_manager_instance.estado_combate = "em_andamento"

        # A primeira chamada a obter_estado_atual retorna o turno do jogador
        estado_inicial = {
            "grupo_inimigos": [mock_monstro],
            "entidade_da_vez": mock_personagem
        }
        mock_manager_instance.obter_estado_atual.return_value = estado_inicial

        # Para parar o loop, configuramos o mock de executar_acao_jogador
        # para mudar o estado do combate para "vitoria_jogador"
        def terminar_combate(*args, **kwargs):
            mock_manager_instance.estado_combate = "vitoria_jogador"

        mock_manager_instance.executar_acao_jogador.side_effect = terminar_combate

        # --- Act ---
        # Executa a função da tela de combate
        exibir_combate(mock_personagem, [mock_monstro])

        # --- Assert ---
        # Verifica se o método para executar a ação do jogador foi chamado uma vez
        mock_manager_instance.executar_acao_jogador.assert_called_once()

        # Verifica se a ação passada para o manager foi a correta
        acao_esperada = {"habilidade_id": "ataque_basico", "alvo_id": "goblin_1"}
        mock_manager_instance.executar_acao_jogador.assert_called_with(mock_personagem, acao_esperada)

if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
    unittest.main(verbosity=2)
