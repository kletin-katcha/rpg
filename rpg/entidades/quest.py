from typing import List, Dict, Any, Optional
from enum import Enum

class TipoQuest(Enum):
    PRINCIPAL = "Principal"
    SECUNDARIA = "Secundária"
    GUILDA = "Guilda"
    CLASSE = "Classe"
    PROCEDURAL = "Procedural"

class EstadoQuest(Enum):
    INATIVA = "Inativa"
    ATIVA = "Ativa"
    CONCLUIDA = "Concluída"
    FALHOU = "Falhou"

class Quest:
    """
    Representa uma missão ou tarefa que o jogador pode realizar.
    Contém os objetivos, o estado atual e as recompensas.
    """
    def __init__(self,
                 id_quest: str,
                 titulo: str,
                 descricao_inicio: str,
                 ato_narrativo: int, # A qual dos 10 atos a quest pertence
                 tipo: TipoQuest,
                 npc_inicio: str, # ID do NPC que dá a quest
                 objetivos: List[Dict[str, Any]], # Ex: [{"tipo": "coletar", "id_item": "pele_lobo", "progresso": 0, "total": 10}]
                 recompensas: Dict[str, Any], # Ex: {"xp": 1000, "ouro": 500, "itens": [{"id_item": "espada_rara", "quantidade": 1}]}
                 descricao_fim: Optional[str] = None,
                 npc_fim: Optional[str] = None,
                 pre_requisitos: Optional[List[str]] = None): # Lista de IDs de quests que devem ser concluídas antes

        # --- Identificação ---
        self.id_quest = id_quest
        self.titulo = titulo
        self.descricao_inicio = descricao_inicio
        self.descricao_fim = descricao_fim if descricao_fim is not None else "Missão concluída!"

        # --- Classificação e Narrativa ---
        self.ato_narrativo = ato_narrativo
        self.tipo = tipo

        # --- NPCs e Requisitos ---
        self.npc_inicio = npc_inicio
        self.npc_fim = npc_fim if npc_fim is not None else npc_inicio
        self.pre_requisitos = pre_requisitos if pre_requisitos is not None else []

        # --- Estado e Progresso ---
        self.estado = EstadoQuest.INATIVA
        self.objetivos = objetivos

        # --- Recompensas ---
        self.recompensas = recompensas

    def iniciar(self):
        """Muda o estado da quest para ativa."""
        if self.estado == EstadoQuest.INATIVA:
            self.estado = EstadoQuest.ATIVA
            print(f"Nova missão iniciada: [{self.tipo.value}] {self.titulo}")

    def atualizar_progresso(self, tipo_objetivo: str, id_alvo: str, quantidade: int = 1):
        """
        Atualiza o progresso de um objetivo da quest.
        Ex: tipo="matar", id="goblin", quantidade=1
        """
        if self.estado != EstadoQuest.ATIVA:
            return

        for obj in self.objetivos:
            if obj["tipo"] == tipo_objetivo and obj["id_alvo"] == id_alvo:
                obj["progresso"] = min(obj["total"], obj["progresso"] + quantidade)
                print(f"Progresso da missão '{self.titulo}': {obj['progresso']}/{obj['total']} {obj['id_alvo']} {obj['tipo']}s.")

    def esta_completa(self) -> bool:
        """Verifica se todos os objetivos da quest foram alcançados."""
        if self.estado != EstadoQuest.ATIVA:
            return False

        return all(obj["progresso"] >= obj["total"] for obj in self.objetivos)

    def concluir(self, personagem: 'Personagem'):
        """Muda o estado para concluída e entrega as recompensas ao jogador."""
        if self.esta_completa():
            self.estado = EstadoQuest.CONCLUIDA
            print(f"Missão Concluída: {self.titulo}!")
            # TODO: Entregar recompensas ao personagem
            # personagem.ganhar_xp(self.recompensas.get("xp", 0))
            # personagem.ouro += self.recompensas.get("ouro", 0)
            # for item_rec in self.recompensas.get("itens", []):
            #     personagem.inventario.adicionar_item(item_rec['id_item'], item_rec['quantidade'])
            return True
        return False

    def __str__(self) -> str:
        return f"[{self.tipo.value}] {self.titulo} ({self.estado.value})"
