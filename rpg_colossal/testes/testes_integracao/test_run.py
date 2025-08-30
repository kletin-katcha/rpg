# -*- coding: utf-8 -*-
"""
================================================================================================
TESTE DE INTEGRAÇÃO COMPLETO (END-TO-END)
================================================================================================
Este arquivo, `test_run.py`, é o teste de validação final para todo o motor do jogo
"Ecos da Aetheria". Diferente dos testes unitários que verificam componentes isolados,
este script simula uma campanha de jogo do início ao fim, garantindo que todos os
sistemas (`entidades`, `sistemas`, `interacoes`, `progressao`, `io`) funcionam
corretamente como um organismo coeso.

-------------------------
-- OBJETIVOS DO TESTE --
-------------------------
1.  **Validação do Fluxo de Jogo:** Simular a jornada de um jogador, desde a criação
    do personagem até o confronto com desafios de alto nível.
2.  **Integridade da Persistência:** Garantir que o estado do jogo pode ser salvo e
    carregado em pontos críticos sem perda ou corrupção de dados.
3.  **Coesão dos Sistemas:** Provar que os diferentes motores (progressão, combate,
    meta, etc.) interagem entre si conforme o esperado.
4.  **Resiliência:** Testar cenários complexos e de múltiplos passos para descobrir
    bugs de integração que não são aparentes em testes unitários.

-------------------------
-- ESTRUTURA DO TESTE --
-------------------------
O teste é estruturado como uma classe `unittest.TestCase`, com cada cenário de
teste sendo um método separado (`test_*`).

- `setUp()`: É executado antes de cada teste. Cria um ambiente limpo e isolado,
  instanciando todos os gerenciadores de sistema e criando um diretório temporário
  para os arquivos de save.
- `tearDown()`: É executado após cada teste. Destrói o ambiente de teste, removendo
  o diretório de saves e quaisquer outros artefatos.
- **Cenários de Teste:** Cada método de teste foca em uma parte específica da
  experiência de jogo, construindo sobre os resultados do anterior de forma lógica
  (embora os testes sejam tecnicamente independentes graças ao `setUp` e `tearDown`).
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import unittest
from unittest.mock import patch
import os
import shutil
import sys

# Adiciona o diretório raiz do projeto ao sys.path para permitir importações absolutas
# Isso é crucial para que os testes possam encontrar os módulos do motor.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Importa todos os sistemas e entidades necessários para a simulação
from motor_jogo.entidades.personagem import Personagem
from motor_jogo.entidades.monstro import Monstro
from motor_jogo.sistemas.criador_personagem import CriadorPersonagem
from rpg_colossal import main as orquestrador_main
from motor_jogo.sistemas.gerenciador_save import GerenciadorSave, EstadoJogo
from motor_jogo.progresso.gerenciador_niveis import GerenciadorDeNiveis
from motor_jogo.progresso.gerenciador_evolucoes import GerenciadorDeEvolucoes
from motor_jogo.progresso.meta_progressao import GerenciadorDeMetaProgressao

# ==============================================================================================
# == SEÇÃO 2: CLASSE DE TESTE DE CAMPANHA COMPLETA =============================================
# ==============================================================================================
class TestAetheriaFullCampaign(unittest.TestCase):
    """
    Suite de testes que simula uma campanha completa em Aetheria.
    """

    def setUp(self):
        """
        Configura o ambiente de teste antes de cada método de teste.
        """
        print(f"\n--- CONFIGURANDO AMBIENTE PARA: {self._testMethodName} ---")

        # Define um diretório de saves temporário para este teste
        self.test_save_dir = "temp_test_saves"
        if os.path.exists(self.test_save_dir):
            shutil.rmtree(self.test_save_dir)
        os.makedirs(self.test_save_dir)

        # Instancia todos os gerenciadores de sistema que serão usados nos testes
        self.criador_personagem = CriadorPersonagem()
        self.gerenciador_save = GerenciadorSave(diretorio_saves=self.test_save_dir)
        self.gerenciador_meta = GerenciadorDeMetaProgressao(caminho_save=os.path.join(self.test_save_dir, "meta_save.json"))

        # Mocks de dados para o criador de personagem, para tornar os testes determinísticos
        self.criador_personagem.racas_disponiveis = [{"id_raca": "humano_teste", "nome": "Humano", "descricao_curta": "Desc", "atributos_base": {"constituicao": 10}}]
        self.criador_personagem.classes_disponiveis = [{"id_classe": "guerreiro_teste", "nome": "Guerreiro", "descricao_curta": "Desc", "habilidades_iniciais": []}]

    def tearDown(self):
        """
        Limpa o ambiente de teste após a execução de cada método de teste.
        """
        print(f"--- LIMPANDO AMBIENTE DE: {self._testMethodName} ---")
        if os.path.exists(self.test_save_dir):
            shutil.rmtree(self.test_save_dir)

    # ==========================================================================================
    # == CENÁRIOS DE TESTE =====================================================================
    # ==========================================================================================

    @patch('builtins.input', side_effect=['1', '1', 'Valerius'])
    def test_cenario_jornada_do_heroi(self, mock_input):
        """
        Cenário 1: Simula a criação, progressão inicial e persistência de um herói.
        """
        print("EXECUTANDO: Teste de Jornada do Herói (Criação, Progressão, Save/Load)")

        # 1. Criação do Personagem
        personagem_original = self.criador_personagem.iniciar_criacao()
        self.assertIsNotNone(personagem_original)
        self.assertEqual(personagem_original.nome, "Valerius")
        self.assertEqual(personagem_original.raca['id_raca'], "humano_teste")
        self.assertEqual(personagem_original.classe['id_classe'], "guerreiro_teste")

        # 2. Progressão
        gerenciador_niveis = GerenciadorDeNiveis(personagem_original)
        gerenciador_niveis.ganhar_xp(150) # XP suficiente para nível 2
        self.assertEqual(personagem_original.nivel, 2)

        # Adiciona um item para testar a persistência do inventário
        personagem_original.adicionar_item({"id_item": "espada_curta", "nome": "Espada Curta"})
        self.assertEqual(len(personagem_original.inventario), 1)

        # 3. Persistência (Save)
        estado_original = EstadoJogo(
            personagem=personagem_original,
            estado_mundo={"eventos_vistos": ["inicio"]},
            metadata={"versao": "0.0.1-test"}
        )
        sucesso_save = self.gerenciador_save.salvar_jogo(estado_original, slot=1)
        self.assertTrue(sucesso_save)

        # 4. Persistência (Load)
        estado_carregado = self.gerenciador_save.carregar_jogo(slot=1)
        self.assertIsNotNone(estado_carregado)
        self.assertIsInstance(estado_carregado.personagem, Personagem)

        # 5. Verificação de Integridade
        p_carregado = estado_carregado.personagem
        self.assertEqual(p_carregado.nome, "Valerius")
        self.assertEqual(p_carregado.nivel, 2)
        self.assertEqual(p_carregado.raca['id_raca'], "humano_teste")
        self.assertEqual(len(p_carregado.inventario), 1)
        self.assertEqual(p_carregado.inventario[0]['nome'], "Espada Curta")

        print("SUCESSO: O personagem foi criado, progrediu, salvo e carregado com integridade.")

    def test_cenario_batalha_final(self):
        """
        Cenário 2: Simula uma batalha de chefe com salvamento no meio do combate.
        """
        print("EXECUTANDO: Teste da Batalha Final (Combate, Persistência Crítica)")

        # 1. Arrange: Cria um personagem de alto nível e um chefe
        jogador = Personagem(id_entidade="heroi_final", nome="Herói Lendário", dados_raca=self.criador_personagem.racas_disponiveis[0], dados_classe=self.criador_personagem.classes_disponiveis[0])
        jogador.nivel = 50
        jogador.hp_max = 500
        jogador.hp_atual = 500

        dados_chefe = {"id": "boss_final", "nome": "Lorde Demônio", "nivel": 50, "hp": 1000, "atributos": {}}
        chefe = Monstro(dados_monstro=dados_chefe)

        # 2. Act (Part 1): Simula alguns turnos de combate e salva
        print("Iniciando combate... Dano é trocado.")
        jogador.hp_atual -= 250 # Jogador sofre dano
        chefe.hp_atual -= 400   # Chefe sofre dano

        hp_jogador_antes_save = jogador.hp_atual
        hp_chefe_antes_save = chefe.hp_atual
        self.assertEqual(hp_jogador_antes_save, 250)
        self.assertEqual(hp_chefe_antes_save, 600)

        estado_meio_combate = EstadoJogo(
            personagem=jogador,
            estado_mundo={"batalha_em_andamento": True},
            metadata={"versao": "0.0.1-test"},
            monstros_na_area=[chefe]
        )

        sucesso_save = self.gerenciador_save.salvar_jogo(estado_meio_combate, slot=2)
        self.assertTrue(sucesso_save)

        # 3. Act (Part 2): Carrega o jogo
        estado_carregado = self.gerenciador_save.carregar_jogo(slot=2)
        self.assertIsNotNone(estado_carregado)

        # 4. Assert: Verifica a integridade do estado carregado
        p_carregado = estado_carregado.personagem
        monstros_carregados = estado_carregado.monstros_na_area
        self.assertEqual(len(monstros_carregados), 1)
        chefe_carregado = monstros_carregados[0]

        print(f"HP do jogador antes: {hp_jogador_antes_save}, HP carregado: {p_carregado.hp_atual}")
        print(f"HP do chefe antes: {hp_chefe_antes_save}, HP carregado: {chefe_carregado.hp_atual}")

        self.assertEqual(p_carregado.hp_atual, hp_jogador_antes_save)
        self.assertEqual(chefe_carregado.hp_atual, hp_chefe_antes_save)

        # 5. Continua o combate e vence
        print("Continuando combate... O herói desfere o golpe final!")
        chefe_carregado.receber_dano(9999)
        self.assertFalse(chefe_carregado.esta_vivo())

        print("SUCESSO: O estado do combate foi salvo e carregado perfeitamente.")

    @patch('builtins.input', side_effect=['1', '1', 'Lia'])
    def test_cenario_legado(self, mock_input):
        """
        Cenário 3: Valida o ciclo completo do sistema de meta-progressão.
        """
        print("EXECUTANDO: Teste de Legado (Meta-Progressão)")

        # 1. Arrange: Simula um evento que desbloqueia uma conquista de legado
        id_chefe_final = "boss_rei_dos_demonios"
        self.gerenciador_meta.registrar_evento("chefe_derrotado", {"id_chefe": id_chefe_final})

        # Verifica se o arquivo de meta-save foi salvo corretamente
        meta_save_path = os.path.join(self.test_save_dir, "meta_save.json")
        self.assertTrue(os.path.exists(meta_save_path))
        with open(meta_save_path, 'r') as f:
            dados_meta = f.read()
            self.assertIn("matador_do_rei_demonio", dados_meta)

        # 2. Act: Cria um novo personagem em uma "nova sessão"
        # Instancia um novo gerenciador para simular o carregamento do arquivo salvo
        novo_gerenciador_meta = GerenciadorDeMetaProgressao(caminho_save=meta_save_path)

        # Cria o novo personagem (o "herdeiro")
        herdeiro = self.criador_personagem.iniciar_criacao()
        self.assertIsNotNone(herdeiro)
        self.assertEqual(herdeiro.nome, "Lia")

        # Aplica os bônus de legado
        novo_gerenciador_meta.aplicar_bonus_de_legado(herdeiro)

        # 3. Assert: Verifica se o bônus foi aplicado
        inventario_herdeiro = herdeiro.inventario
        self.assertEqual(len(inventario_herdeiro), 1)
        self.assertEqual(inventario_herdeiro[0]['nome'], "Fragmento de Coragem")

        print("SUCESSO: A conquista de legado foi desbloqueada e o bônus foi aplicado ao herdeiro.")

    @patch('rpg_colossal.main.tela_personagem')
    @patch('rpg_colossal.main.tela_inventario')
    @patch('rpg_colossal.main.tela_exploracao')
    def test_fluxo_de_navegacao_exploracao(self, mock_tela_exploracao, mock_tela_inventario, mock_tela_personagem):
        """
        Cenário 4: Valida o novo loop de jogo baseado em ações estruturadas.
        """
        print("EXECUTANDO: Teste do Loop de Jogo com Ações Estruturadas")

        # 1. Arrange
        # Cria um personagem e um estado de jogo para o teste
        personagem = Personagem(id_entidade="p1", nome="Navegador", dados_raca=self.criador_personagem.racas_disponiveis[0], dados_classe=self.criador_personagem.classes_disponiveis[0])
        estado_de_jogo = EstadoJogo(personagem=personagem, estado_mundo={}, metadata={})

        # Configura a tela de exploração mockada para retornar uma sequência de ações
        mock_tela_exploracao.exibir_exploracao.side_effect = [
            {"tipo": "abrir_tela", "tela": "inventario"}, # Primeira ação: abrir inventário
            {"tipo": "mover", "destino": "cidade_capital"}, # Segunda ação: mover
            {"tipo": "sair"}  # Terceira ação: sair do loop
        ]

        # 2. Act
        # Executa o loop de jogo principal, que irá consumir as ações do side_effect
        orquestrador_main.loop_de_jogo(estado_de_jogo)

        # 3. Assert
        # Verifica se as telas corretas foram chamadas
        mock_tela_inventario.exibir_inventario.assert_called_once_with(personagem)

        # Verifica se a localização do personagem foi atualizada corretamente
        self.assertEqual(personagem.localizacao_atual, "cidade_capital")

        # Verifica se a tela de exploração foi chamada o número correto de vezes (3)
        self.assertEqual(mock_tela_exploracao.exibir_exploracao.call_count, 3)

        print("SUCESSO: O loop de jogo despachou as ações estruturadas corretamente.")


# ==============================================================================================
# == SEÇÃO 3: PONTO DE ENTRADA DO TESTE ========================================================
# ==============================================================================================
if __name__ == '__main__':
    # Isso permite que o arquivo de teste seja executado diretamente do terminal.
    unittest.main(verbosity=2)
