# -*- coding: utf-8 -*-
"""
================================================================================================
CLASSE: NPC (Non-Player Character)
================================================================================================
Este arquivo define a classe `NPC`, que representa todos os personagens não-jogáveis
do mundo com os quais o jogador pode interagir, como mercadores, ferreiros, guardas
e quest-givers.

-------------------------
-- HERANÇA E DESIGN --
-------------------------
A classe `NPC` herda da `entidade_base.Entidade`, pois NPCs podem, em certas
situações, participar de combates ou ser alvos. No entanto, sua principal
funcionalidade não é o combate, mas a interação.

A classe `NPC` adiciona camadas para:
- **Diálogo:** Armazena e gerencia as árvores de diálogo.
- **Missões:** Sabe quais missões pode oferecer ao jogador.
- **Serviços:** Pode estar associado a uma loja ou outro serviço na cidade.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
from typing import Dict, Any, List

# Importa a classe base para herança.
from .entidade_base import Entidade

# ==============================================================================================
# == SEÇÃO 2: DEFINIÇÃO DA CLASSE NPC ==========================================================
# ==============================================================================================
class NPC(Entidade):
    """
    Representa um personagem não-jogável (NPC) no mundo.

    Herda de `Entidade` e adiciona sistemas de diálogo, missões e serviços.

    Attributes:
        ocupacao (str): A profissão ou papel do NPC no mundo.
        dialogos (Dict): Uma estrutura de dados (ex: dict) contendo as falas do NPC.
        missoes_disponiveis (List[str]): Lista de IDs de missões que este NPC oferece.
        id_loja (str, optional): Se o NPC for um mercador, o ID de sua loja.
    """

    def __init__(self, dados_npc: Dict[str, Any]):
        """
        Inicializa um novo objeto NPC a partir de um dicionário de dados.

        Args:
            dados_npc (Dict[str, Any]): O dicionário de dados completo do NPC,
                                       vindo de um futuro banco de dados de NPCs.
        """
        # NPCs geralmente não têm stats de combate complexos, então podemos usar valores padrão.
        atributos_base = dados_npc.get("atributos", {"forca": 5, "destreza": 5, "constituicao": 10, "inteligencia": 10, "sabedoria": 10, "carisma": 10})

        super().__init__(
            id_entidade=dados_npc.get("id", "npc_desconhecido"),
            nome=dados_npc.get("nome", "Cidadão"),
            nivel=dados_npc.get("nivel", 1),
            hp=dados_npc.get("hp", 50),
            atributos=atributos_base
        )

        # Atributos específicos do NPC
        self.ocupacao: str = dados_npc.get("ocupacao", "Viajante")
        self.dialogos: Dict = dados_npc.get("dialogos", {})
        self.missoes_disponiveis: List[str] = dados_npc.get("missoes", [])
        self.id_loja: Optional[str] = dados_npc.get("id_loja")

    def __str__(self) -> str:
        """Retorna uma representação em string do NPC."""
        return f"[NPC] {self.nome} ({self.ocupacao})"

    def iniciar_dialogo(self, jogador: 'Personagem') -> None:
        """
        Inicia uma interação de diálogo com o jogador.

        Esta é uma função placeholder. Uma implementação real seria uma máquina de
        estados complexa que apresenta opções de diálogo ao jogador e reage às
        suas escolhas, possivelmente verificando o estado de missões ou a reputação
        do jogador.

        Args:
            jogador ('Personagem'): O objeto do personagem que está interagindo com o NPC.
        """
        print(f"\nVocê se aproxima de {self.nome}.")

        # Lógica de diálogo simplificada
        fala_inicial = self.dialogos.get("saudacao", f"Olá, {jogador.nome}.")
        print(f'"{fala_inicial}"')

        # Lógica de missão simplificada
        if self.missoes_disponiveis:
            self.oferecer_missao(jogador, self.missoes_disponiveis[0])

    def oferecer_missao(self, jogador: 'Personagem', id_missao: str) -> None:
        """
        Apresenta uma missão ao jogador e pergunta se ele quer aceitá-la.

        Args:
            jogador ('Personagem'): O jogador a quem a missão é oferecida.
            id_missao (str): O ID da missão a ser oferecida.
        """
        # Lógica para buscar os detalhes da missão no banco de dados de missões
        print(f'\n{self.nome} parece ter um trabalho para você.')
        print(f"[MISSÃO OFERECIDA: {id_missao}]")

        # Simulação da aceitação
        # resposta = input("Você aceita a missão? (s/n): ")
        # if resposta.lower() == 's':
        #     jogador.iniciar_missao(id_missao)
        #     self.missoes_disponiveis.remove(id_missao)
        pass

# Fim da definição da classe NPC.
