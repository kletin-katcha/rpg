# -*- coding: utf-8 -*-
"""
================================================================================================
SISTEMA DE INTERAÇÃO: CIDADE
================================================================================================
Este arquivo define o `GerenciadorDeCidade`, uma classe responsável por gerenciar o
estado e as interações de uma cidade específica no jogo. Ele atua como um "mestre de
cena" para tudo o que acontece dentro dos muros de um assentamento.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
A classe `GerenciadorDeCidade` é instanciada quando o jogador entra em uma cidade.
Ela carrega os dados da cidade correspondente e gerencia seu ciclo de vida.

- **Estado da Cidade:** Controla a população, a economia local, os NPCs presentes
  e os eventos urbanos em andamento.
- **Interação com Sistemas:** Atua como um hub, conectando o jogador aos vários
  sistemas disponíveis na cidade (economia, reputação, missões).
- **Simulação Dinâmica:** Possui métodos para simular a passagem do tempo na cidade,
  o que pode alterar a disponibilidade de NPCs, os preços nas lojas (influenciando
  a economia global) e gerar pequenos eventos locais.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
from typing import Dict, Any, List
import random

# Importa as classes e dados necessários
try:
    from ..entidades.personagem import Personagem
    from ..entidades.npc import NPC
    from ..banco_de_dados.mundo.cidades import INDICE_CIDADES
    # Futuramente, importará dados de NPCs específicos da cidade
except ImportError:
    Personagem = object
    NPC = object
    INDICE_CIDADES = {"by_id": {}}

# ==============================================================================================
# == SEÇÃO 2: CLASSE GERENCIADORDECIDADE =======================================================
# ==============================================================================================
class GerenciadorDeCidade:
    """
    Gerencia o estado e as interações de uma única cidade.
    """
    def __init__(self, id_cidade: str):
        """
        Inicializa o gerenciador para uma cidade específica.

        Args:
            id_cidade (str): O ID da cidade a ser carregada.
        """
        dados_cidade = INDICE_CIDADES["by_id"].get(id_cidade)
        if not dados_cidade:
            raise ValueError(f"Cidade com ID '{id_cidade}' não encontrada no banco de dados.")

        self.id = id_cidade
        self.nome = dados_cidade["nome"]
        self.dados = dados_cidade
        self.populacao_atual = dados_cidade["populacao"]
        self.npcs_presentes: List[NPC] = []
        self.eventos_ativos: List[Dict] = []

        print(f"Bem-vindo a {self.nome}! {self.dados['descricao']}")
        self._carregar_npcs_iniciais()

    def _carregar_npcs_iniciais(self):
        """Carrega os NPCs principais associados a esta cidade."""
        # Lógica placeholder para popular a cidade com NPCs
        # No futuro, leria um banco de dados de NPCs filtrado por localização.
        print(f"Carregando NPCs de {self.nome}...")
        # self.npcs_presentes.append(NPC(dados_npc_exemplo))
        pass

    def simular_passagem_de_um_dia(self):
        """
        Simula um ciclo de um dia na cidade, atualizando seu estado.
        """
        print(f"\nUm novo dia amanhece em {self.nome}...")

        # Simula pequenas mudanças na população
        mod_pop = random.randint(-self.populacao_atual // 100, self.populacao_atual // 100)
        self.populacao_atual += mod_pop

        # Simula um evento local que pode afetar a economia
        # if random.random() < 0.1:
        #     evento = {"nome": "Chegada de Caravana", "modificador_inflacao": -0.05}
        #     print(f"EVENTO: Uma grande caravana chegou! Os preços podem baixar.")
        #     # Esta informação seria passada para o EconomiaManager

        print(f"População atual: {self.populacao_atual}")

    def iniciar_interacao(self, personagem: Personagem):
        """
        Apresenta o menu principal de interações da cidade ao jogador.
        """
        print(f"\nO que você gostaria de fazer em {self.nome}?")

        servicos = self.dados.get("servicos", {})
        opcoes = {}
        i = 1

        # Cria um menu dinâmico com base nos serviços disponíveis
        for loja_id in servicos.get("lojas", []):
            opcoes[str(i)] = {"texto": f"Visitar a loja '{loja_id}'", "acao": "visitar_loja", "id": loja_id}
            i += 1
        if servicos.get("taverna"):
            opcoes[str(i)] = {"texto": "Ir para a taverna", "acao": "visitar_taverna"}
            i += 1
        if servicos.get("templo"):
            opcoes[str(i)] = {"texto": "Visitar o templo", "acao": "visitar_templo"}
            i += 1

        opcoes[str(i)] = {"texto": "Sair da cidade", "acao": "sair"}

        for key, value in opcoes.items():
            print(f"[{key}] - {value['texto']}")

        # Lógica de escolha do jogador (placeholder)
        # escolha = input("> ")
        # ... processar escolha ...

# ==============================================================================================
# == SEÇÃO 3: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("== DEMONSTRAÇÃO DO SISTEMA DE CIDADE ==")
    print("="*80)

    # Adiciona um mock ao índice para o teste funcionar isoladamente
    INDICE_CIDADES["by_id"]["havenwood"] = {
        "id": "havenwood", "nome": "Havenwood (Mock)",
        "populacao": 2500,
        "descricao": "Uma cidade próspera para testes.",
        "servicos": { "lojas": ["ferreiro_teste"], "taverna": True, "templo": True }
    }

    print("\n--- Carregando a cidade de Havenwood ---")
    try:
        cidade_teste = GerenciadorDeCidade("havenwood")

        print("\n--- Simulando a passagem de um dia ---")
        cidade_teste.simular_passagem_de_um_dia()

        print("\n--- Iniciando interação com um jogador mock ---")
        cidade_teste.iniciar_interacao(Personagem()) # Usando um mock implícito

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")
