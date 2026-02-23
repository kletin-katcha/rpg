from dataclasses import dataclass, field


@dataclass
class CharacterState:
    id: str
    nome: str
    nivel: int = 1
    xp: int = 0
    atributos: dict[str, int] = field(default_factory=dict)
    hp_atual: int = 100
    hp_max: int = 100
    habilidades_desbloqueadas: list[str] = field(default_factory=list)


@dataclass
class EnemyState:
    id: str
    nome: str
    nivel: int = 1
    hp_atual: int = 50
    hp_max: int = 50
    ataque_base: int = 5
    velocidade: int = 5
    arquetipo: str = "agressivo"
    fase: int = 1


@dataclass
class CombatContext:
    personagem: CharacterState
    inimigo: EnemyState
    acao: str = "ataque_basico"
    bonus_dano_personagem: int = 0
    reducao_dano_personagem: int = 0
    bonus_dano_inimigo: int = 0


@dataclass
class CombatResult:
    dano_causado: int
    dano_recebido: int
    inimigo_derrotado: bool
    personagem_derrotado: bool
