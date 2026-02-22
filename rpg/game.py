from dataclasses import dataclass, field

from rpg.content.loader import load_catalog
from rpg.core.errors import RegraNegocioError
from rpg.core.types import CharacterState
from rpg.systems.character.service import criar_personagem
from rpg.systems.inventory.service import adicionar_item_catalogado
from rpg.systems.combat.service import combater_ate_fim
from rpg.systems.city import CityState, construir_estrutura, melhorar_estrutura, ativar_plano_automacao, processar_automacao
from rpg.systems.crafting import forjar_receita


@dataclass
class GameState:
    etapa: str = "criacao"
    cidade_atual: str = "Vila Aurora"
    jogador: CharacterState | None = None
    inventario: dict[str, int] = field(default_factory=dict)
    log: list[str] = field(default_factory=list)
    cidade: CityState = field(default_factory=CityState)


class Game:
    """Fase 3: cidade, forja e automação inicial sobre o núcleo jogável."""

    def __init__(self) -> None:
        self.running = True
        self.state = GameState()

    def start_message(self) -> str:
        return "RPG Surreal iniciado: fase 3 pronta (cidade + forja + automação)."

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
            "forjar_espada_longa",
            "construir_oficina",
            "melhorar_oficina",
            "construir_nucleo_automacao",
            "ativar_automacao",
            "avancar_dia",
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
        elif acao == "forjar_espada_longa":
            forjar_receita(self.state.inventario, "forja_espada_longa")
            msg = "Forja concluída: 1 Espada Longa criada."
        elif acao == "construir_oficina":
            nivel = construir_estrutura(self.state.cidade, "oficina")
            msg = f"Oficina construída no nível {nivel}."
        elif acao == "melhorar_oficina":
            nivel = melhorar_estrutura(self.state.cidade, "oficina")
            msg = f"Oficina melhorada para nível {nivel}."
        elif acao == "construir_nucleo_automacao":
            nivel = construir_estrutura(self.state.cidade, "nucleo_automacao")
            msg = f"Núcleo de automação construído no nível {nivel}."
        elif acao == "ativar_automacao":
            ativar_plano_automacao(self.state.cidade, "coleta_sucata")
            msg = "Plano de automação 'coleta_sucata' ativado."
        elif acao == "avancar_dia":
            processar_automacao(self.state.cidade, self.state.inventario)
            msg = "Um dia se passou. Automação processada."
        elif acao == "ver_status":
            msg = (
                f"Status: nível {self.state.jogador.nivel}, HP {self.state.jogador.hp_atual}/{self.state.jogador.hp_max}, "
                f"inventário={self.state.inventario}, ouro={self.state.cidade.ouro}, estruturas={self.state.cidade.estruturas}"
            )
        elif acao == "sair":
            self.running = False
            msg = "Saindo do jogo."
        else:
            raise RegraNegocioError(f"Ação de cidade inválida: {acao}")

        self.state.log.append(msg)
        return msg
