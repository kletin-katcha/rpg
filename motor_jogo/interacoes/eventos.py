# -*- coding: utf-8 -*-
"""
================================================================================================
SISTEMA DE INTERAÇÃO: EVENTOS MUNDIAIS E LOCAIS
================================================================================================
Este arquivo define o `GerenciadorDeEventos`, uma classe crucial para criar um mundo
dinâmico e vivo. Ele gerencia a ocorrência de eventos aleatórios e programados, que
podem variar de um pequeno acontecimento local a uma catástrofe que afeta todo o reino.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
- **Tipos de Eventos:**
  - **Locais:** Ocorrem em uma área ou cidade específica (ex: "Ataque de Goblins a uma Fazenda").
  - **Globais:** Afetam todo o mundo do jogo (ex: "Festival da Colheita", "Chuva de Meteoros").
- **Gatilhos (Triggers):** Eventos podem ser disparados por:
  - **Tempo:** Ocorrem em uma data específica do calendário do jogo.
  - **Ação do Jogador:** Completar uma missão ou matar um chefe pode ser o gatilho.
  - **Aleatoriedade:** Uma chance de ocorrer a cada "dia" que passa no jogo.
- **Impacto:** Os efeitos de um evento são variados e devem interagir com os outros
  sistemas:
  - Mudar a economia (`EconomiaManager`).
  - Mudar a reputação com facções (`ReputacaoManager`).
  - Desbloquear novas missões, NPCs ou dungeons.
  - Mudar os tipos de monstros que aparecem em uma área.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import random
from typing import Dict, Any, List

# Importa os sistemas com os quais os eventos irão interagir.
try:
    from ..sistemas.economia import EconomiaManager
    from ..sistemas.reputacao import ReputacaoManager
except ImportError:
    EconomiaManager = object
    ReputacaoManager = object

# ==============================================================================================
# == SEÇÃO 2: BANCO DE DADOS DE EVENTOS (EXEMPLO) ==============================================
# ==============================================================================================
# Em um jogo completo, isto estaria em `banco_de_dados/eventos.py`.
EVENTOS_EXEMPLO = {
    "festival_da_colheita": {
        "nome": "Festival da Colheita",
        "tipo": "global",
        "gatilho": {"tipo": "data", "data": "15 do Outono"},
        "duracao_dias": 7,
        "descricao": "Um festival anual para celebrar a colheita. As cidades estão decoradas, há comida abundante e jogos festivos.",
        "efeitos": [
            {"sistema": "economia", "funcao": "modificar_inflacao", "args": {"modificador": -0.05}},
            {"sistema": "social", "funcao": "aumentar_moral_geral"},
        ]
    },
    "praga_dos_goblins": {
        "nome": "Praga dos Goblins",
        "tipo": "local",
        "area_afetada": "plains_de_havenwood",
        "gatilho": {"tipo": "aleatorio", "chance_por_dia": 0.02},
        "duracao_dias": 10,
        "descricao": "Uma horda de goblins, maior que o normal, está atacando fazendas e caravanas nas planícies.",
        "efeitos": [
            {"sistema": "encontros", "funcao": "aumentar_frequencia_monstro", "args": {"id_monstro": "goblin_batedor", "fator": 2.0}},
            {"sistema": "missoes", "funcao": "desbloquear_missao", "args": {"id_missao": "cacar_chefe_goblin"}},
        ]
    }
}

# ==============================================================================================
# == SEÇÃO 3: CLASSE GERENCIADORDEEVENTOS ======================================================
# ==============================================================================================
class GerenciadorDeEventos:
    """
    Verifica e gerencia a ativação e os efeitos de eventos mundiais e locais.
    """
    def __init__(self, economia_manager: EconomiaManager, reputacao_manager: ReputacaoManager):
        self.eventos_ativos: List[Dict] = []
        self.economia_manager = economia_manager
        self.reputacao_manager = reputacao_manager
        print("Sistema de Eventos Mundiais inicializado.")

    def verificar_e_disparar_eventos(self, data_atual: str, acoes_jogador: List[str]):
        """
        Verifica todos os eventos potenciais e ativa aqueles cujos gatilhos foram cumpridos.
        """
        print(f"\nVerificando eventos para a data: {data_atual}...")
        for id_evento, dados_evento in EVENTOS_EXEMPLO.items():
            gatilho = dados_evento["gatilho"]
            if gatilho["tipo"] == "data" and gatilho["data"] == data_atual:
                self.ativar_evento(dados_evento)
            elif gatilho["tipo"] == "aleatorio":
                if random.random() < gatilho["chance_por_dia"]:
                    self.ativar_evento(dados_evento)

    def ativar_evento(self, dados_evento: Dict):
        """
        Ativa um evento e aplica seus efeitos iniciais.
        """
        print(f"EVENTO INICIADO: {dados_evento['nome']}! ({dados_evento['descricao']})")
        self.eventos_ativos.append(dados_evento)

        # Aplica os efeitos
        for efeito in dados_evento.get("efeitos", []):
            if efeito["sistema"] == "economia":
                # Lógica para chamar o sistema de economia
                # self.economia_manager.atualizar_economia_global(...)
                print(f"Efeito econômico aplicado: {efeito['funcao']} com args {efeito['args']}")
            # Adicionar outras lógicas de sistema aqui

# ==============================================================================================
# == SEÇÃO 4: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("== DEMONSTRAÇÃO DO SISTEMA DE EVENTOS ==")
    print("="*80)

    # Mocks para os managers
    class MockEcoManager:
        def atualizar_economia_global(self, *args, **kwargs): pass
    class MockRepManager: pass

    eco_mock = MockEcoManager()
    rep_mock = MockRepManager()

    gerenciador_eventos = GerenciadorDeEventos(eco_mock, rep_mock)

    print("\n--- Simulando a passagem de dias ---")
    gerenciador_eventos.verificar_e_disparar_eventos("14 do Outono", [])
    gerenciador_eventos.verificar_e_disparar_eventos("15 do Outono", []) # Deve disparar o festival

    print("\nEventos ativos no momento:")
    for evento in gerenciador_eventos.eventos_ativos:
        print(f"- {evento['nome']}")
