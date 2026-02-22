from dataclasses import dataclass, field

from rpg.content.loader import load_catalog
from rpg.core.errors import RegraNegocioError
from rpg.core.types import CharacterState
from rpg.systems.character.service import criar_personagem
from rpg.systems.inventory.service import adicionar_item_catalogado
from rpg.systems.combat.service import combater_ate_fim


@dataclass
class GameState:
    etapa: str = "criacao"
    cidade_atual: str = "Vila Aurora"
    jogador: CharacterState | None = None
    inventario: dict[str, int] = field(default_factory=dict)
    log: list[str] = field(default_factory=list)


class Game:
    """Fase 2: núcleo jogável + combate por turnos com XP e loot."""

    def __init__(self) -> None:
        self.running = True
        self.state = GameState()

    def start_message(self) -> str:
        return "RPG Surreal iniciado: fase 2 pronta (combate + progressão + loot)."

    def opcoes_criacao(self) -> dict[str, list[str]]:
        racas = load_catalog("racas")
        classes = load_catalog("classes")
        return {
            "racas": sorted(racas.keys()),
            "classes": sorted(classes.keys()),
        }

    def criar_jogador(self, nome: str, raca_id: str, classe_id: str) -> CharacterState:
        jogador = criar_personagem(nome, raca_id, classe_id)
        self.state.jogador = jogador
        self.state.etapa = "cidade"
        self.state.log.append(
            f"Personagem criado: {jogador.nome} ({raca_id}/{classe_id}) em {self.state.cidade_atual}."
        )
        return jogador

    def opcoes_cidade(self) -> list[str]:
        return [
            "descansar",
            "coletar_item_inicial",
            "cacar_lobo",
            "cacar_goblin",
            "ver_status",
            "sair",
        ]

    def executar_acao_cidade(self, acao: str) -> str:
        if self.state.jogador is None:
            raise RegraNegocioError("Jogador não criado")

        if acao == "descansar":
            self.state.jogador.hp_atual = self.state.jogador.hp_max
            msg = "Você descansou na estalagem e recuperou todo HP."
        elif acao == "coletar_item_inicial":
            adicionar_item_catalogado(self.state.inventario, "pocao_cura", 1)
            msg = "Você recebeu 1 Poção de Cura."
        elif acao == "cacar_lobo":
            resultado = combater_ate_fim(self.state.jogador, "lobo_cinzento", self.state.inventario)
            msg = (
                f"Combate concluído. Vitória={resultado['vitoria']} | XP +{resultado['xp_recebido']} | "
                f"Loot={resultado['loot']}"
            )
        elif acao == "cacar_goblin":
            resultado = combater_ate_fim(self.state.jogador, "goblin_batedor", self.state.inventario)
            msg = (
                f"Combate concluído. Vitória={resultado['vitoria']} | XP +{resultado['xp_recebido']} | "
                f"Loot={resultado['loot']}"
            )
        elif acao == "ver_status":
            msg = (
                f"Status: nível {self.state.jogador.nivel}, HP {self.state.jogador.hp_atual}/{self.state.jogador.hp_max}, "
                f"inventário={self.state.inventario}"
            )
        elif acao == "sair":
            self.running = False
            msg = "Saindo do jogo."
        else:
            raise RegraNegocioError(f"Ação de cidade inválida: {acao}")

        self.state.log.append(msg)
        return msg
