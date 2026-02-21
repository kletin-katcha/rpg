from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Personagem:
    nome: str
    raca: Optional[str] = None
    sub_raca: Optional[str] = None
    classe: Optional[str] = None
    nivel: int = 1

    base_forca: int = 5
    base_destreza: int = 5
    base_constituicao: int = 5
    base_inteligencia: int = 5
    base_sabedoria: int = 5
    base_carisma: int = 5

    habilidades: list[str] = field(default_factory=list)


@dataclass
class EstadoJogo:
    etapa: str = "nome"
    jogador: Optional[Personagem] = None
