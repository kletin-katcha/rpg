# -*- coding: utf-8 -*-
"""
================================================================================================
TELA: EXPLORAÇÃO
================================================================================================
Este módulo é responsável por renderizar a tela principal do jogo, onde o jogador
passa a maior parte do tempo: o modo de exploração.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
- **Interface de Informação:** A função principal é atuar como uma janela para o
  mundo do jogo. Ela pega o estado atual do personagem (especificamente sua
  localização) e os dados do mundo (do banco de dados de áreas) e os apresenta
  de forma clara e imersiva para o jogador.

- **Formatação e Clareza:** Utiliza funções auxiliares (como as de `funcoes_gerais`)
  para formatar a saída, usando caixas e cabeçalhos para separar visualmente as
  diferentes informações (descrição da área, status do jogador, pontos de interesse).

- **Coleta de Comando:** Após apresentar o estado, sua segunda responsabilidade é
  capturar o próximo comando do jogador e retorná-lo ao loop de jogo principal
  (`main.py`) para processamento.

- **Desacoplamento:** A tela de exploração não contém lógica de jogo. Ela não sabe
  o que acontece quando o jogador digita "norte"; ela apenas informa ao `main.py`
  que o comando foi "norte". Essa separação é crucial para a arquitetura.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

try:
    from rpg_colossal.motor_jogo.entidades.personagem import Personagem
    from rpg_colossal.motor_jogo.banco_de_dados.mundo.areas import INDICE_AREAS
    from rpg_colossal.motor_jogo.utilitarios import funcoes_gerais as geral
except ImportError:
    # Mocks para execução independente
    class Personagem:
        def __init__(self):
            self.nome = "Tester"
            self.hp_atual = 100
            self.hp_max = 100
            self.localizacao_atual = "mock_area"
    INDICE_AREAS = {"by_id": {"mock_area": {"nome": "Área Mock", "descricao": "Desc Mock", "cidades_proximas": [], "dungeons": []}}}
    class geral:
        def limpar_tela(): print("\n--- TELA LIMPA ---")
        def criar_cabecalho(t): return f"== {t} =="
        def desenhar_caixa(t, c): return f"== {t} ==\n" + "\n".join(c)

# ==============================================================================================
# == SEÇÃO 2: FUNÇÃO PRINCIPAL DA TELA =========================================================
# ==============================================================================================
def exibir_exploracao(personagem: Personagem, db_areas=INDICE_AREAS, ui_utils=geral) -> dict:
    """
    Renderiza a tela de exploração e retorna uma ação estruturada escolhida pelo jogador.
    """
    ui_utils.limpar_tela()

    dados_area = db_areas["by_id"].get(personagem.localizacao_atual)
    if not dados_area:
        return {"tipo": "erro", "mensagem": f"Localização '{personagem.localizacao_atual}' não encontrada."}

    # --- Renderização ---
    status_str = f"HP: {personagem.hp_atual}/{personagem.hp_max} | Nível: {personagem.nivel}"
    print(ui_utils.desenhar_caixa(f"{personagem.nome} | {personagem.classe['nome']}", [status_str]))
    print(ui_utils.criar_cabecalho(dados_area["nome"]))
    print(dados_area["descricao"])

    # --- Construção do Menu de Ações Dinâmico ---
    acoes_disponiveis = []
    # Adiciona pontos de interesse como ações de movimento
    for cidade in dados_area.get("cidades_proximas", []):
        acoes_disponiveis.append({"texto": f"Ir para a cidade: {cidade}", "acao": {"tipo": "mover", "destino": cidade}})
    for dungeon in dados_area.get("dungeons", []):
        acoes_disponiveis.append({"texto": f"Entrar na dungeon: {dungeon}", "acao": {"tipo": "mover", "destino": dungeon}})

    # Adiciona ações padrão
    acoes_disponiveis.append({"texto": "Ver ficha de personagem", "acao": {"tipo": "abrir_tela", "tela": "personagem"}})
    acoes_disponiveis.append({"texto": "Abrir inventário", "acao": {"tipo": "abrir_tela", "tela": "inventario"}})
    acoes_disponiveis.append({"texto": "Salvar e sair para o menu", "acao": {"tipo": "sair"}})

    print("\nO que você faz?")
    for i, item_acao in enumerate(acoes_disponiveis):
        print(f"[{i+1}] {item_acao['texto']}")

    # --- Obter e Validar Entrada ---
    while True:
        try:
            escolha = input("> ")
            idx = int(escolha) - 1
            if 0 <= idx < len(acoes_disponiveis):
                return acoes_disponiveis[idx]["acao"] # Retorna o dicionário de ação
            else:
                print("Escolha inválida.")
        except (ValueError, TypeError):
            print("Entrada inválida. Por favor, digite um número.")

# ==============================================================================================
# == SEÇÃO 3: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
import unittest
from unittest.mock import patch, MagicMock

# Os Mocks de dados e a classe de teste devem estar no escopo do módulo
mock_raca_data = {"id": "humano_t", "nome": "Humano de Teste", "atributos_base": {"constituicao": 10}}
mock_classe_data = {"id_classe": "explorador_t", "nome": "Explorador", "habilidades_iniciais": []}

MOCK_PERSONAGEM = Personagem(
    id_entidade="mock_player_01",
    nome="Aventureiro Teste",
    dados_raca=mock_raca_data,
    dados_classe=mock_classe_data
)
MOCK_PERSONAGEM.nivel = 5
MOCK_PERSONAGEM.hp_atual = 80
MOCK_PERSONAGEM.hp_max = 100
MOCK_PERSONAGEM.localizacao_atual = "floresta_teste"

MOCK_AREAS_DB = {
    "by_id": {
        "floresta_teste": {
            "nome": "Floresta do Eco",
            "descricao": "Uma floresta verdejante e cheia de vida.",
            "cidades_proximas": ["Vila Sombria"],
            "dungeons": ["Caverna do Urso"]
        }
    }
}

class TestTelaExploracao(unittest.TestCase):
    @patch('builtins.input', return_value='1') # Simula o jogador escolhendo a primeira opção
    @patch('builtins.print')
    def test_retorna_acao_estruturada(self, mock_print, mock_input):
        """
        Verifica se a tela retorna um dicionário de ação estruturado.
        """
        mock_ui_utils = MagicMock()

        acao_retornada = exibir_exploracao(
            personagem=MOCK_PERSONAGEM,
            db_areas=MOCK_AREAS_DB,
            ui_utils=mock_ui_utils
        )

        # A primeira ação na lista dinâmica é ir para "Vila Sombria"
        acao_esperada = {"tipo": "mover", "destino": "Vila Sombria"}

        self.assertEqual(acao_retornada, acao_esperada)

if __name__ == "__main__":
    print("\n" + "="*80)
    print("== TESTES DA TELA DE EXPLORAÇÃO ==")
    print("="*80)
    # A chamada a unittest.main() permanece aqui para permitir a execução direta do arquivo
    unittest.main(verbosity=2)
