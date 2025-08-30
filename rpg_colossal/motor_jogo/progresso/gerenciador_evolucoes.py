# -*- coding: utf-8 -*-
"""
================================================================================================
MOTOR DE PROGRESSÃO: GERENCIADOR DE EVOLUÇÕES
================================================================================================
Este arquivo define o `GerenciadorDeEvolucoes`, o sistema responsável por uma das
mecânicas mais excitantes de Aetheria: a evolução de classes. Este gerenciador
controla como e quando um personagem pode transcender sua classe atual para se tornar
algo novo e mais poderoso.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
A evolução de classes é um sistema baseado em dados, projetado para ser robusto,
flexível e facilmente expansível.

- **Dados de Evolução Centralizados:** As possíveis evoluções e seus pré-requisitos
  não estão codificados na lógica. Eles são definidos nos arquivos de dados das
  classes (`classes_intermediarias.py`, `classes_avancadas.py`, etc.).

- **Múltiplos Pré-requisitos:** O sistema suporta uma variedade de pré-requisitos,
  tornando as evoluções verdadeiras conquistas. Os tipos de requisitos implementados
  incluem:
    - Nível mínimo do personagem.
    - Domínio de classes anteriores (histórico de classes).
    - Reputação com facções específicas.
    - Posse de itens-chave (como um tomo sagrado ou um artefato profano).
    - Alinhamento moral do personagem.

- **Verificação Modular:** A lógica de verificação é dividida em pequenos métodos
  privados, cada um responsável por validar um único tipo de requisito. Isso torna o
  código limpo e fácil de adicionar novos tipos de pré-requisitos no futuro (ex:
  localização no mundo, eventos concluídos, etc.).

- **Processo de Transformação:** Uma vez que os requisitos são atendidos, o método
  `processar_evolucao` aplica as mudanças ao personagem, atualizando sua classe,
  adicionando bônus permanentes aos atributos e concedendo novas habilidades.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
from typing import Dict, Any, List
import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

try:
    from motor_jogo.entidades.personagem import Personagem
    # Importa os bancos de dados de classes que contêm as evoluções
    from motor_jogo.banco_de_dados.classes import classes_intermediarias, classes_avancadas
except ImportError:
    # Mocks para execução independente
    Personagem = object
    class MockClassesDB:
        CLASSES_INTERMEDIARIAS = []
        CLASSES_AVANCADAS = []
    classes_intermediarias = MockClassesDB()
    classes_avancadas = MockClassesDB()

# ==============================================================================================
# == SEÇÃO 2: CLASSE GERENCIADOR DE EVOLUÇÕES ==================================================
# ==============================================================================================
class GerenciadorDeEvolucoes:
    """
    Verifica e processa as evoluções de classe para um personagem.
    """
    def __init__(self, personagem: Personagem):
        """
        Inicializa o gerenciador com o personagem a ser verificado.

        Args:
            personagem (Personagem): A instância do personagem.
        """
        self.personagem = personagem
        # Combina todas as classes que representam evoluções em uma única lista
        self.evolucoes_possiveis = (
            classes_intermediarias.CLASSES_INTERMEDIARIAS +
            classes_avancadas.CLASSES_AVANCADAS
        )

    def verificar_evolucoes_disponiveis(self) -> List[Dict]:
        """
        Verifica todas as evoluções possíveis e retorna uma lista daquelas que o
        personagem cumpre os requisitos para desbloquear.

        Returns:
            List[Dict]: Uma lista de dicionários, onde cada dicionário são os dados
                        completos da classe de evolução disponível.
        """
        disponiveis = []
        for classe_futura in self.evolucoes_possiveis:
            # Um personagem não pode evoluir para uma classe que já teve.
            if classe_futura.get("id_classe") in self.personagem.historico_classes:
                continue

            requisitos = classe_futura.get("requisitos", {})
            if self._requisitos_satisfeitos(requisitos):
                disponiveis.append(classe_futura)
        return disponiveis

    def _requisitos_satisfeitos(self, requisitos: Dict) -> bool:
        """
        Verifica se o personagem atende a um conjunto de requisitos.

        Args:
            requisitos (Dict): O dicionário de requisitos de uma classe.

        Returns:
            bool: True se TODOS os requisitos forem atendidos, False caso contrário.
        """
        # Um dicionário mapeando a chave do requisito para a função de verificação
        verificadores = {
            "nivel_minimo": self._verificar_nivel,
            "classe_base": self._verificar_classe_base,
            "classes_necessarias": self._verificar_classes_necessarias,
            "reputacao": self._verificar_reputacao,
            "item_possui": self._verificar_item_possui,
            "alinhamento": self._verificar_alinhamento,
        }

        for chave, valor_esperado in requisitos.items():
            verificador = verificadores.get(chave)
            # Se não houver um verificador para a chave, ou se a verificação falhar, retorna False
            if not verificador or not verificador(valor_esperado):
                return False

        return True

    # --- MÉTODOS DE VERIFICAÇÃO INDIVIDUAL ---

    def _verificar_nivel(self, nivel_minimo: int) -> bool:
        return self.personagem.nivel >= nivel_minimo

    def _verificar_classe_base(self, classe_base_id: str) -> bool:
        return self.personagem.classe.get("id_classe") == classe_base_id

    def _verificar_classes_necessarias(self, classes_ids: List[str]) -> bool:
        # Garante que o personagem tenha passado por todas as classes necessárias em seu histórico
        return all(cid in self.personagem.historico_classes for cid in classes_ids)

    def _verificar_reputacao(self, requisitos_rep: List[Dict]) -> bool:
        for req in requisitos_rep:
            faccao_id = req["faccao"]
            valor_minimo = req["valor"]
            if self.personagem.reputacao.get(faccao_id, 0) < valor_minimo:
                return False
        return True

    def _verificar_item_possui(self, requisitos_item: List[Dict]) -> bool:
        for req in requisitos_item:
            item_id = req["id_item"]
            quantidade_necessaria = req["quantidade"]
            # Simplificado: verifica se o item existe no inventário.
            # Um sistema real verificaria a quantidade.
            if not any(item.get("id_item") == item_id for item in self.personagem.inventario):
                return False
        return True

    def _verificar_alinhamento(self, alinhamentos_permitidos: List[str]) -> bool:
        return self.personagem.alinhamento in alinhamentos_permitidos

    # --- MÉTODO DE PROCESSAMENTO ---

    def processar_evolucao(self, dados_nova_classe: Dict) -> bool:
        """
        Aplica a evolução a um personagem, transformando sua classe.

        Args:
            dados_nova_classe (Dict): O dicionário de dados completo da nova classe.

        Returns:
            bool: True se a evolução foi bem-sucedida.
        """
        print(f"\nEVOLUÇÃO! {self.personagem.nome} está evoluindo para {dados_nova_classe['nome']}!")

        # Atualiza a classe atual do personagem
        self.personagem.classe = dados_nova_classe

        # Adiciona a nova classe ao histórico
        if dados_nova_classe['id_classe'] not in self.personagem.historico_classes:
            self.personagem.historico_classes.append(dados_nova_classe['id_classe'])

        # Aplica modificadores de atributos permanentes, se houver
        modificadores = dados_nova_classe.get("modificadores_atributos", {})
        if modificadores:
            print("Ganhos de atributos permanentes:")
            for atributo, valor in modificadores.items():
                self.personagem.atributos[atributo] += valor
                print(f"  - {atributo.capitalize()}: +{valor}")

        # Adiciona as novas habilidades da classe
        novas_habilidades = dados_nova_classe.get("arvore_de_habilidades", {}).get(str(self.personagem.nivel), [])
        if novas_habilidades:
            print("Novas habilidades adquiridas:")
            for habilidade in novas_habilidades:
                if habilidade not in self.personagem.habilidades_conhecidas:
                    self.personagem.habilidades_conhecidas.append(habilidade)
                    print(f"  - {habilidade}")

        print(f"Evolução para {dados_nova_classe['nome']} completa!")
        return True


# ==============================================================================================
# == SEÇÃO 3: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("== DEMONSTRAÇÃO DO GERENCIADOR DE EVOLUÇÕES ==")
    print("="*80)

    # Mock de dados para o teste funcionar de forma independente
    DADOS_CLASSE_GUARDAO = {
        "id_classe": "guardiao", "nome": "Guardião",
        "requisitos": {"nivel_minimo": 10, "classe_base": "guerreiro"}
    }
    DADOS_CLASSE_SACERDOTE = {
        "id_classe": "sacerdote", "nome": "Sacerdote",
        "requisitos": {"nivel_minimo": 10, "classe_base": "clerigo"}
    }
    DADOS_CLASSE_PALADINO = {
        "id_classe": "paladino", "nome": "Paladino",
        "requisitos": {
            "nivel_minimo": 30,
            "classes_necessarias": ["guardiao", "sacerdote"],
            "alinhamento": ["Leal e Bom"],
            "reputacao": [{"faccao": "ordem_da_chama_prateada", "valor": 750}],
            "item_possui": [{"id_item": "tomo_do_juramento_sagrado", "quantidade": 1}]
        },
        "modificadores_atributos": {"forca": 5, "sabedoria": 5},
        "arvore_de_habilidades": {"30": ["Ataque Smite"]}
    }

    # Adiciona os mocks ao ambiente de teste
    classes_intermediarias.CLASSES_INTERMEDIARIAS = [DADOS_CLASSE_GUARDAO, DADOS_CLASSE_SACERDOTE]
    classes_avancadas.CLASSES_AVANCADAS = [DADOS_CLASSE_PALADINO]

    # Mock da classe Personagem com todos os atributos necessários para as verificações
    class MockPersonagemEvolucao:
        def __init__(self, nome):
            self.nome = nome
            self.nivel = 1
            self.classe = {"id_classe": "guerreiro", "nome": "Guerreiro"}
            self.historico_classes = ["guerreiro"]
            self.reputacao = {}
            self.inventario = []
            self.alinhamento = "Leal e Bom"
            self.atributos = {"forca": 20, "sabedoria": 10}
            self.habilidades_conhecidas = []
            print(f"Mock de Personagem '{self.nome}' criado.")

    # 1. Criação do personagem de teste
    print("\n--- 1. Criando Personagem de Teste ---")
    jogador = MockPersonagemEvolucao("Sir Gideon")

    # 2. Instanciação do gerenciador
    gerenciador = GerenciadorDeEvolucoes(jogador)

    # 3. Verificação inicial (não deve haver evoluções)
    print("\n--- 2. Verificação Inicial ---")
    evolucoes = gerenciador.verificar_evolucoes_disponiveis()
    print(f"Evoluções disponíveis: {[e['nome'] for e in evolucoes]}")
    assert not evolucoes, "Erro: Nenhuma evolução deveria estar disponível inicialmente."

    # 4. Simulação do cumprimento dos requisitos para Paladino
    print("\n--- 3. Simulando Requisitos para Paladino ---")
    jogador.nivel = 30
    jogador.historico_classes.extend(["guardiao", "sacerdote"])
    jogador.reputacao["ordem_da_chama_prateada"] = 800
    jogador.inventario.append({"id_item": "tomo_do_juramento_sagrado"})
    print("Nível, histórico, reputação e item atualizados.")

    # 5. Nova verificação (agora Paladino deve estar disponível)
    print("\n--- 4. Verificando Novamente ---")
    evolucoes = gerenciador.verificar_evolucoes_disponiveis()
    print(f"Evoluções disponíveis: {[e['nome'] for e in evolucoes]}")
    assert len(evolucoes) == 1 and evolucoes[0]["id_classe"] == "paladino", "Erro: A evolução para Paladino deveria estar disponível."

    # 6. Processamento da evolução
    print("\n--- 5. Processando a Evolução ---")
    paladino_data = evolucoes[0]
    gerenciador.processar_evolucao(paladino_data)

    # 7. Verificação final
    print("\n--- 6. Estado Final do Personagem ---")
    print(f"Classe atual: {jogador.classe['nome']}")
    print(f"Histórico: {jogador.historico_classes}")
    print(f"Atributos: {jogador.atributos}")
    print(f"Habilidades: {jogador.habilidades_conhecidas}")
    assert jogador.classe["id_classe"] == "paladino"
    assert jogador.atributos["forca"] == 25
    assert "Ataque Smite" in jogador.habilidades_conhecidas

    print("\n\nTeste concluído com sucesso! O sistema de evoluções está funcionando como esperado.")
