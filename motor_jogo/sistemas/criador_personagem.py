# -*- coding: utf-8 -*-
"""
================================================================================================
SISTEMA: CRIADOR DE PERSONAGEM
================================================================================================
Este arquivo define o `CriadorPersonagem`, uma classe-sistema responsável por
orquestrar o processo de criação de um novo personagem pelo jogador.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
- **Orquestrador de Fluxo:** Esta classe atua como um maestro, guiando o jogador
  através das várias etapas da criação de personagem de forma sequencial e lógica.
  Ele não lida com a renderização da UI, apenas com o fluxo de dados e decisões.

- **Baseado em Dados:** O criador é totalmente dependente dos dados definidos no
  `banco_de_dados` do motor. Ele carrega as raças de `racas_base.py` e as classes
  de `classes_iniciais.py`, garantindo que qualquer adição ou modificação nesses
  arquivos seja refletida automaticamente no processo de criação.

- **Produção de Entidade:** O resultado final do processo de criação é uma instância
  válida e totalmente formada da classe `motor_jogo.entidades.personagem.Personagem`,
  pronta para ser usada pelo loop principal do jogo.

- **Testabilidade:** O design separa a lógica do fluxo da captura de entrada,
  permitindo que a função `input` seja facilmente mockada para testes automatizados,
  validando todo o processo de criação sem a necessidade de interação manual.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import sys
import os
import uuid

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

try:
    from motor_jogo.entidades.personagem import Personagem
    from motor_jogo.banco_de_dados.racas import racas_base
    from motor_jogo.banco_de_dados.classes import classes_iniciais
except ImportError:
    # Mocks para permitir a execução independente e testes
    class Personagem:
        def __init__(self, id_entidade, nome, dados_raca, dados_classe):
            self.id_entidade = id_entidade
            self.nome = nome
            self.raca = dados_raca
            self.classe = dados_classe
    class MockDB:
        RACAS_BASE = []
        CLASSES_INICIAIS = []
    racas_base = MockDB()
    classes_iniciais = MockDB()

# ==============================================================================================
# == SEÇÃO 2: CLASSE CRIADOR DE PERSONAGEM =====================================================
# ==============================================================================================
class CriadorPersonagem:
    """
    Orquestra o processo de criação de um novo personagem.
    """
    def __init__(self):
        # Carrega os dados necessários dos bancos de dados na inicialização
        self.racas_disponiveis = racas_base.RACAS_BASE
        self.classes_disponiveis = classes_iniciais.CLASSES_INICIAIS

    def iniciar_criacao(self) -> Personagem | None:
        """
        Inicia e gerencia o fluxo completo de criação de personagem.

        Returns:
            Personagem | None: Uma nova instância de Personagem se a criação for
                                bem-sucedida, ou None se for cancelada.
        """
        print("\n" + "="*40)
        print("== FORJA DE HERÓIS DE AETHERIA ==")
        print("="*40)
        print("Vamos criar seu novo herói. Siga os passos abaixo.")

        # Etapa 1: Escolher a Raça
        dados_raca = self._escolher_raca()
        if not dados_raca:
            print("Criação cancelada.")
            return None

        # Etapa 2: Escolher a Classe
        dados_classe = self._escolher_classe()
        if not dados_classe:
            print("Criação cancelada.")
            return None

        # Etapa 3: Inserir o Nome
        nome_personagem = self._inserir_nome()
        if not nome_personagem:
            print("Criação cancelada.")
            return None

        # Etapa 4: Criar a instância do Personagem
        print("\nForjando seu herói...")
        novo_personagem = Personagem(
            id_entidade=f"player_{uuid.uuid4()}", # Gera um ID único
            nome=nome_personagem,
            dados_raca=dados_raca,
            dados_classe=dados_classe
        )

        print("-" * 40)
        print("HERÓI CRIADO COM SUCESSO!")
        print(f"Bem-vindo a Aetheria, {novo_personagem.nome}, o {novo_personagem.raca['nome']} {novo_personagem.classe['nome']}!")
        print("-" * 40)

        return novo_personagem

    def _escolher_raca(self) -> dict | None:
        """Exibe as raças e gerencia a seleção do jogador."""
        print("\n--- PASSO 1: ESCOLHA SUA RAÇA ---")
        for i, raca in enumerate(self.racas_disponiveis):
            print(f"[{i+1}] {raca['nome']} - {raca['descricao_curta']}")

        while True:
            try:
                escolha = input(f"Digite o número da raça (1-{len(self.racas_disponiveis)}): ")
                idx = int(escolha) - 1
                if 0 <= idx < len(self.racas_disponiveis):
                    return self.racas_disponiveis[idx]
                else:
                    print("Escolha inválida.")
            except (ValueError, TypeError):
                print("Entrada inválida. Por favor, digite um número.")

    def _escolher_classe(self) -> dict | None:
        """Exibe as classes e gerencia a seleção do jogador."""
        print("\n--- PASSO 2: ESCOLHA SUA CLASSE ---")
        for i, classe in enumerate(self.classes_disponiveis):
            print(f"[{i+1}] {classe['nome']} - {classe['descricao_curta']}")

        while True:
            try:
                escolha = input(f"Digite o número da classe (1-{len(self.classes_disponiveis)}): ")
                idx = int(escolha) - 1
                if 0 <= idx < len(self.classes_disponiveis):
                    return self.classes_disponiveis[idx]
                else:
                    print("Escolha inválida.")
            except (ValueError, TypeError):
                print("Entrada inválida. Por favor, digite um número.")

    def _inserir_nome(self) -> str | None:
        """Solicita e valida o nome do personagem."""
        print("\n--- PASSO 3: ESCOLHA SEU NOME ---")
        while True:
            nome = input("Digite o nome do seu personagem: ").strip()
            if 3 <= len(nome) <= 20: # Exemplo de validação
                return nome
            else:
                print("Nome inválido. Deve ter entre 3 e 20 caracteres.")

# ==============================================================================================
# == SEÇÃO 3: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
if __name__ == "__main__":
    import unittest
    from unittest.mock import patch

    print("\n" + "="*80)
    print("== TESTES DO CRIADOR DE PERSONAGEM ==")
    print("="*80)

    # Mock dos dados do banco de dados para o teste
    MOCK_RACAS = [
        {"id_raca": "humano_t", "nome": "Humano Teste", "descricao_curta": "Adaptável."},
        {"id_raca": "elfo_t", "nome": "Elfo Teste", "descricao_curta": "Ágil."}
    ]
    MOCK_CLASSES = [
        {"id_classe": "guerreiro_t", "nome": "Guerreiro Teste", "descricao_curta": "Forte."},
        {"id_classe": "mago_t", "nome": "Mago Teste", "descricao_curta": "Inteligente."}
    ]

    class TestCriadorPersonagem(unittest.TestCase):

        @patch('builtins.input', side_effect=['2', '1', 'Elara']) # Simula: 2 (Elfo), 1 (Guerreiro), "Elara"
        @patch(__name__ + '.racas_base')
        @patch(__name__ + '.classes_iniciais')
        def test_fluxo_criacao_completo(self, mock_classes_db, mock_racas_db, mock_input):
            print("\n--- Testando o fluxo de criação completo ---")

            # Configura os mocks dos bancos de dados
            mock_racas_db.RACAS_BASE = MOCK_RACAS
            mock_classes_db.CLASSES_INICIAIS = MOCK_CLASSES

            criador = CriadorPersonagem()
            personagem_criado = criador.iniciar_criacao()

            # Verificações
            self.assertIsNotNone(personagem_criado)
            self.assertIsInstance(personagem_criado, Personagem)
            self.assertEqual(personagem_criado.nome, "Elara")
            self.assertEqual(personagem_criado.raca['nome'], "Elfo Teste")
            self.assertEqual(personagem_criado.classe['nome'], "Guerreiro Teste")
            print("Teste de fluxo completo bem-sucedido.")

    # Executa os testes
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCriadorPersonagem))
    runner = unittest.TextTestRunner()
    runner.run(suite)
