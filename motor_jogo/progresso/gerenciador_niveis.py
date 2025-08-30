# -*- coding: utf-8 -*-
"""
================================================================================================
MOTOR DE PROGRESSÃO: GERENCIADOR DE NÍVEIS
================================================================================================
Este arquivo define o `GerenciadorDeNiveis`, o coração do sistema de progressão
individual de personagens em Aetheria. Ele é responsável por controlar o ganho de
experiência (XP), o processo de subida de nível (level-up), o escalonamento de
atributos e o desbloqueio de novas habilidades.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
A filosofia por trás deste sistema é a de uma progressão universal e altamente
customizável, baseada em dados.

- **Curva de XP Universal:** O XP necessário para cada nível é definido em uma estrutura
  de dados central (`XP_CURVA_EXEMPLO`). Isso permite um ajuste fino da velocidade de
  progressão do jogo. A curva é exponencial para garantir que os níveis iniciais
  sejam rápidos e os níveis finais representem um desafio maior.

- **Crescimento Baseado em Classe/Raça:** O ganho de atributos a cada nível não é
  fixo. Ele é determinado pelos dados de crescimento associados à classe e raça do
  personagem (`CRESCIMENTO_ATRIBUTOS_EXEMPLO`). Um 'Guerreiro' pode ganhar mais 'forca'
  e 'vitalidade', enquanto um 'Mago' ganha mais 'inteligencia' e 'mana'.

- **Desbloqueio de Habilidades por Marcos:** Novas habilidades não são simplesmente
  concedidas. Elas são desbloqueadas em níveis específicos, definidos em
  `HABILIDADES_POR_NIVEL_EXEMPLO`. Isso cria marcos de poder claros para o jogador,
  dando-lhe algo pelo que ansiar.

- **Modularidade:** O `GerenciadorDeNiveis` opera sobre uma instância de uma entidade
  (como `Personagem`), modificando seus atributos diretamente. Ele não possui estado
  próprio, tornando-o flexível e fácil de usar em qualquer ponto do jogo (após
  combates, ao completar missões, etc.).
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
from typing import Dict, Any, List
import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path para permitir importações absolutas
# Isso é útil para garantir que os módulos possam ser encontrados, especialmente em testes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

try:
    from motor_jogo.entidades.personagem import Personagem
except ImportError:
    # Classe Mock para permitir que o arquivo seja executado de forma independente para testes
    # Esta classe simula a assinatura e os atributos essenciais da classe Personagem real.
    class Personagem:
        def __init__(self, id_entidade: str, nome: str, dados_raca: Dict, dados_classe: Dict):
            self.id_entidade = id_entidade
            self.nome = nome
            self.raca = dados_raca
            self.classe = dados_classe
            self.nivel = 1
            self.xp_atual = 0
            self.xp_para_proximo_nivel = 100
            self.atributos = dados_raca.get("atributos_base", {}).copy()
            self.habilidades_conhecidas = dados_classe.get("habilidades_iniciais", [])
            print(f"Mock de Personagem '{self.nome}' criado.")

# ==============================================================================================
# == SEÇÃO 2: ESTRUTURAS DE DADOS DE PROGRESSÃO (EXEMPLOS) =====================================
# ==============================================================================================

# A curva de XP pode ser tão longa quanto necessário.
# A chave é o nível atual, o valor é o XP necessário para alcançar o próximo.
XP_CURVA_EXEMPLO: Dict[int, int] = {
    1: 100,
    2: 150,
    3: 225,
    4: 340,
    5: 510,
    # ... e assim por diante, com uma progressão exponencial
}

# Define o ganho de atributos por nível para diferentes classes.
# Isso permite uma customização profunda do desenvolvimento do personagem.
CRESCIMENTO_ATRIBUTOS_EXEMPLO: Dict[str, Dict[str, int]] = {
    "guerreiro": {"forca": 3, "destreza": 1, "inteligencia": 0, "vitalidade": 2},
    "mago": {"forca": 0, "destreza": 1, "inteligencia": 3, "vitalidade": 1},
    "ladino": {"forca": 1, "destreza": 3, "inteligencia": 1, "vitalidade": 1},
    # Adicionar mais classes aqui
}

# Define as habilidades desbloqueadas em cada nível para diferentes classes.
HABILIDADES_POR_NIVEL_EXEMPLO: Dict[str, Dict[int, List[str]]] = {
    "guerreiro": {
        3: ["ataque_poderoso"],
        5: ["grito_de_guerra"],
    },
    "mago": {
        3: ["bola_de_fogo"],
        5: ["barreira_de_gelo"],
    },
    # Adicionar mais classes aqui
}


# ==============================================================================================
# == SEÇÃO 3: CLASSE GERENCIADOR DE NÍVEIS =====================================================
# ==============================================================================================
class GerenciadorDeNiveis:
    """
    Gerencia a progressão de nível de uma entidade.
    """
    def __init__(self, personagem: Personagem):
        """
        Inicializa o gerenciador com a entidade a ser progredida.

        Args:
            personagem (Personagem): A instância do personagem cujos níveis serão gerenciados.
        """
        if not hasattr(personagem, 'nivel') or not hasattr(personagem, 'xp_atual'):
            raise TypeError("A entidade fornecida não possui atributos 'nivel' e 'xp_atual'.")
        self.personagem = personagem

    def ganhar_xp(self, quantidade: int):
        """
        Adiciona uma quantidade de XP ao personagem e verifica se ele subiu de nível.

        Args:
            quantidade (int): A quantidade de experiência a ser adicionada.
        """
        if quantidade <= 0:
            return

        print(f"\n{self.personagem.nome} ganhou {quantidade} de XP!")
        self.personagem.xp_atual += quantidade
        self._verificar_level_up()

    def _verificar_level_up(self):
        """
        Verifica continuamente se o personagem tem XP suficiente para subir de nível.
        Permite múltiplos level-ups de uma só vez.
        """
        subiu_de_nivel = False
        while self.personagem.xp_atual >= self.personagem.xp_para_proximo_nivel:
            xp_excedente = self.personagem.xp_atual - self.personagem.xp_para_proximo_nivel
            self.personagem.nivel += 1
            self.personagem.xp_atual = xp_excedente

            # Busca o próximo valor de XP na curva, ou usa uma fórmula padrão se não encontrar
            self.personagem.xp_para_proximo_nivel = XP_CURVA_EXEMPLO.get(
                self.personagem.nivel,
                self.personagem.xp_para_proximo_nivel * 1.5 # Fórmula de fallback
            )

            subiu_de_nivel = True
            print("-" * 40)
            print(f"** LEVEL UP! {self.personagem.nome} alcançou o nível {self.personagem.nivel}! **")
            print("-" * 40)

            self._aplicar_ganhos_de_status()
            self._desbloquear_habilidades()

        if subiu_de_nivel:
            print(f"Progresso atual: Nível {self.personagem.nivel}, XP {self.personagem.xp_atual}/{self.personagem.xp_para_proximo_nivel}")

    def _aplicar_ganhos_de_status(self):
        """
        Aplica os ganhos de atributos baseados na classe do personagem.
        """
        id_classe = self.personagem.classe.get("id", "")
        ganhos = CRESCIMENTO_ATRIBUTOS_EXEMPLO.get(id_classe, {})
        if not ganhos:
            print(f"Aviso: Nenhum dado de crescimento de atributos encontrado para a classe '{id_classe}'.")
            return

        print("Atributos aumentados:")
        for atributo, valor in ganhos.items():
            if atributo in self.personagem.atributos:
                self.personagem.atributos[atributo] += valor
                print(f"  - {atributo.capitalize()}: +{valor} -> {self.personagem.atributos[atributo]}")

    def _desbloquear_habilidades(self):
        """
        Verifica e desbloqueia novas habilidades para o nível atual do personagem.
        """
        id_classe = self.personagem.classe.get("id", "")
        habilidades_da_classe = HABILIDADES_POR_NIVEL_EXEMPLO.get(id_classe, {})
        novas_habilidades = habilidades_da_classe.get(self.personagem.nivel, [])

        if not novas_habilidades:
            return

        print("Novas habilidades desbloqueadas:")
        for habilidade in novas_habilidades:
            # O atributo correto na classe Personagem é 'habilidades_conhecidas'
            if habilidade not in self.personagem.habilidades_conhecidas:
                self.personagem.habilidades_conhecidas.append(habilidade)
                print(f"  - {habilidade}")


# ==============================================================================================
# == SEÇÃO 4: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("== DEMONSTRAÇÃO DO GERENCIADOR DE NÍVEIS ==")
    print("="*80)

    # Mock de dados para simular o banco de dados, necessário para instanciar Personagem
    DADOS_RACA_MOCK = {
        "id": "humano", "nome": "Humano",
        "atributos_base": {"forca": 10, "destreza": 10, "inteligencia": 10, "vitalidade": 10, "constituicao": 10},
        "habilidades_raciais": []
    }
    DADOS_CLASSE_MOCK = {
        "id": "guerreiro", "nome": "Guerreiro",
        "habilidades_iniciais": ["ataque_basico"]
    }

    # 1. Criação de um personagem para o teste
    print("\n--- 1. Criando Personagem de Teste ---")
    # A classe Personagem real será usada aqui, pois a importação deve funcionar.
    jogador_teste = Personagem(
        id_entidade="arion_test_01",
        nome="Arion",
        dados_raca=DADOS_RACA_MOCK,
        dados_classe=DADOS_CLASSE_MOCK
    )

    # O __init__ de Personagem já define xp_para_proximo_nivel, mas podemos garantir que ele
    # usa o valor da nossa curva de teste para consistência.
    jogador_teste.xp_para_proximo_nivel = XP_CURVA_EXEMPLO[1]

    # 2. Instanciação do gerenciador
    print("\n--- 2. Inicializando Gerenciador ---")
    gerenciador = GerenciadorDeNiveis(jogador_teste)

    # 3. Exibição do estado inicial
    print("\n--- 3. Estado Inicial do Personagem ---")
    print(f"Nome: {jogador_teste.nome}, Nível: {jogador_teste.nivel}")
    print(f"XP: {jogador_teste.xp_atual}/{jogador_teste.xp_para_proximo_nivel}")
    print(f"Atributos: {jogador_teste.atributos}")
    print(f"Habilidades: {jogador_teste.habilidades_conhecidas}")

    # 4. Simulação de ganho de XP massivo (suficiente para múltiplos níveis)
    print("\n" + "="*80)
    print("== SIMULANDO GANHO DE XP PARA MÚLTIPLOS NÍVEIS (350 XP) ==")
    print("="*80)
    gerenciador.ganhar_xp(350) # XP para ir do nível 1 para o 3 (100 + 150 = 250) + 100 de sobra

    # 5. Exibição do estado final
    print("\n" + "="*80)
    print("== ESTADO FINAL DO PERSONAGEM ==")
    print("="*80)
    print(f"Nome: {jogador_teste.nome}, Nível: {jogador_teste.nivel}")
    print(f"XP: {jogador_teste.xp_atual}/{jogador_teste.xp_para_proximo_nivel}")
    print(f"Atributos: {jogador_teste.atributos}")
    print(f"Habilidades: {jogador_teste.habilidades_conhecidas}")

    print("\n--- Verificação do Teste ---")
    # O personagem deve estar no nível 3
    assert jogador_teste.nivel == 3, f"Erro: Nível esperado 3, mas foi {jogador_teste.nivel}"
    # XP deve ser 100 (350 - 100 - 150)
    assert jogador_teste.xp_atual == 100, f"Erro: XP esperado 100, mas foi {jogador_teste.xp_atual}"
    # A habilidade 'ataque_poderoso' (nível 3) deve ter sido adicionada
    assert "ataque_poderoso" in jogador_teste.habilidades_conhecidas, "Erro: Habilidade 'ataque_poderoso' não foi desbloqueada."
    # A força deve ter aumentado em 6 (3 por nível 2, 3 por nível 3)
    assert jogador_teste.atributos['forca'] == 16, f"Erro: Força esperada 16, mas foi {jogador_teste.atributos['forca']}"

    print("\nTeste concluído com sucesso! O sistema de níveis está funcionando como esperado.")
