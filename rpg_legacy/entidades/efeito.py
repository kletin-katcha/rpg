from typing import Dict, Any, Optional
from enum import Enum

class TipoEfeito(Enum):
    BUFF = "Buff" # Efeito benéfico
    DEBUFF = "Debuff" # Efeito prejudicial

class Efeito:
    """
    Representa um efeito de status temporário ou persistente em um personagem.
    Pode ser um buff, um debuff, dano por segundo (DoT), cura por segundo (HoT), etc.
    """
    def __init__(self,
                 id_efeito: str,
                 nome: str,
                 descricao: str,
                 tipo: TipoEfeito,
                 duracao_turnos: int, # -1 para permanente até ser removido
                 modificadores: Optional[Dict[str, Any]] = None, # Ex: {"forca": 10, "resistencia_fogo": 0.15}
                 efeito_por_turno: Optional[Dict[str, Any]] = None, # Ex: {"tipo": "dano_veneno", "quantidade": 10}
                 aplicado_por: Optional['Personagem'] = None):

        # --- Identificação ---
        self.id_efeito = id_efeito
        self.nome = nome
        self.descricao = descricao

        # --- Classificação ---
        self.tipo = tipo
        self.duracao_original = duracao_turnos
        self.turnos_restantes = duracao_turnos

        # --- Dados de Jogo ---
        # Modificadores de stats que duram enquanto o efeito está ativo
        self.modificadores = modificadores if modificadores is not None else {}

        # Efeitos que acontecem a cada turno (DoT, HoT)
        self.efeito_por_turno = efeito_por_turno if efeito_por_turno is not None else {}

        # --- Origem ---
        # Guarda quem aplicou o efeito, útil para cálculos de dano de DoT
        self.aplicado_por = aplicado_por

    def é_permanente(self) -> bool:
        """Verifica se o efeito tem duração infinita."""
        return self.duracao_original == -1

    def tick(self) -> Optional[Dict[str, Any]]:
        """
        Processa um turno do efeito.
        Diminui a duração e retorna o efeito por turno, se houver.
        """
        if not self.é_permanente():
            self.turnos_restantes -= 1

        return self.efeito_por_turno

    def expirou(self) -> bool:
        """Verifica if o efeito acabou."""
        if self.é_permanente():
            return False
        return self.turnos_restantes <= 0

    def __str__(self) -> str:
        duracao = "Permanente" if self.é_permanente() else f"{self.turnos_restantes} turnos"
        return f"{self.nome} ({self.tipo.value}) - Duração: {duracao}"
