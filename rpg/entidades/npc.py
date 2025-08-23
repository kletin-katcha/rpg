from typing import List, Dict, Any, Optional, TYPE_CHECKING

from .personagem import Personagem

if TYPE_CHECKING:
    from .item import Item
    from .quest import Quest

class NPC(Personagem):
    """
    Representa um Personagem Não-Jogável (Non-Player Character).
    Herda de Personagem, mas adiciona lógica para interações como diálogos,
    quests e comércio.
    """
    def __init__(self,
                 nome: str,
                 nivel: int,
                 id_npc: str,
                 funcao: str, # "vendedor", "curandeiro", "guarda", "cidadao", "quest_giver"
                 dialogo: Dict[str, Any], # Estrutura de árvore para diálogos
                 stats_base: Dict[str, int],
                 quests_oferecidas: Optional[List[str]] = None, # Lista de IDs de quests
                 inventario_loja: Optional[List[Dict[str, Any]]] = None):

        super().__init__(nome, nivel)

        # --- Identificação e Função ---
        self.id_npc = id_npc
        self.funcao = funcao

        # --- Interação ---
        self.dialogo = dialogo
        self.quests_oferecidas = quests_oferecidas if quests_oferecidas is not None else []
        self.inventario_loja = inventario_loja if inventario_loja is not None else [] # Ex: [{"id_item": "pocao_cura", "preco": 50, "estoque": 10}]

        # --- Atributos ---
        self.aplicar_stats_base(stats_base)
        self.recalcular_stats_completos()
        self.hp_atual = self.hp_max

    def aplicar_stats_base(self, stats: Dict[str, int]):
        """Aplica os atributos base definidos para este NPC."""
        self.forca = stats.get("forca", 5)
        self.destreza = stats.get("destreza", 5)
        self.constituicao = stats.get("constituicao", 10)
        self.inteligencia = stats.get("inteligencia", 10)
        self.sabedoria = stats.get("sabedoria", 10)
        self.carisma = stats.get("carisma", 15)

    def iniciar_dialogo(self, jogador: 'Personagem') -> Optional[str]:
        """
        Inicia uma interação de diálogo com o jogador.
        Retorna uma resposta ou inicia uma ação (quest, loja).
        A implementação real será mais complexa, navegando pela árvore de diálogo.
        """
        print(f"[{self.nome}]: Saudações, {jogador.nome}.")

        # Lógica de diálogo placeholder
        if self.funcao == "vendedor":
            print(f"[{self.nome}]: Gostaria de ver minhas mercadorias?")
            # Em uma implementação real, o jogador poderia escolher opções
            return "abrir_loja"

        if self.funcao == "quest_giver" and self.quests_oferecidas:
            # Verifica se o jogador já não tem a quest
            id_quest_exemplo = self.quests_oferecidas[0]
            if id_quest_exemplo not in [q.id_quest for q in jogador.quests_ativas]:
                print(f"[{self.nome}]: Tenho uma tarefa para você, se estiver interessado.")
                return f"oferecer_quest:{id_quest_exemplo}"

        print(f"[{self.nome}]: O tempo está bom hoje, não acha?")
        return None

    def __str__(self) -> str:
        return f"NPC: {self.nome} (Nível {self.nivel}) - {self.funcao.capitalize()}"
