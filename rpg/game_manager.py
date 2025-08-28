from typing import Optional, TYPE_CHECKING
import random
from typing import List, Dict

from .entidades.personagem import Personagem
from .sistemas import combate, quests, tempo, dungeons, evolucao
from .io import salvar_carregar, menu_loja, menu_crafting, menu_evolucao
from .fabricas.fabrica_monstros import criar_monstro_por_id
from .utilitarios import funcoes_gerais
from .sistemas.dungeons import gerar_dungeon_aleatoria
from .dados.habilidades import TODAS_HABILIDADES
from .dados.monstros_area1 import MONSTROS_AREA1
from .dados.monstros_area2 import MONSTROS_AREA2
from .dados.dungeons_data import DUNGEONS_FIXAS

if TYPE_CHECKING:
    from .entidades.personagem import Personagem
    from .sistemas.dungeons import Dungeon

class GameManager:
    def __init__(self):
        self.jogador: Optional['Personagem'] = None
        self.is_running: bool = True
        self.game_state: str = "main_menu"
        self.localizacao_atual: str = "vila"
        self.time_manager = tempo.TimeManager()
        self.dungeon_atual: Optional['Dungeon'] = None
        self.combat_state: Optional[dict] = None
        self.game_log: list[str] = []

    def _add_log(self, message: str):
        self.game_log.append(message)

    def clear_log(self):
        self.game_log.clear()

    def novo_jogo(self):
        self.jogador = None
        self.game_state = "character_creation"

    def carregar_jogo(self, save_slot: str):
        estado_carregado = salvar_carregar.carregar_jogo(save_slot)
        if estado_carregado:
            self.jogador = estado_carregado["jogador"]
            self.localizacao_atual = estado_carregado["localizacao_atual"]
            self.time_manager = tempo.TimeManager.from_dict(estado_carregado["time_manager"])
            self.game_state = "in_game"
            self._add_log(f"Jogo '{save_slot}' carregado com sucesso!")
        else:
            self._add_log(f"Falha ao carregar o jogo do slot '{save_slot}'.")

    def salvar_jogo(self, save_slot: str):
        if not self.jogador:
            self._add_log("Não há jogo para salvar.")
            return

        estado_jogo = {
            "jogador": self.jogador,
            "localizacao_atual": self.localizacao_atual,
            "time_manager": self.time_manager.to_dict(),
            "dungeon_atual": self.dungeon_atual.id_dungeon if self.dungeon_atual else None
        }
        salvar_carregar.salvar_jogo(estado_jogo, save_slot)
        self._add_log(f"Jogo salvo com sucesso em '{save_slot}.json'!")

    def encerrar_jogo(self):
        self.is_running = False

    def get_opcoes_menu_principal(self) -> list[str]:
        return ["Novo Jogo", "Carregar Jogo", "Sair"]

    def executar_opcao_menu_principal(self, opcao: str):
        if opcao == "Novo Jogo":
            self.novo_jogo()
        elif opcao == "Carregar Jogo":
            self.carregar_jogo("save_teste")
        elif opcao == "Sair":
            self.encerrar_jogo()

    def get_opcoes_localizacao(self) -> list[str]:
        opcoes_comuns = [
            "Ver Diário de Missões", "Abrir Inventário", "Ver Equipamento",
            "Ver status do personagem"
        ]
        if self.jogador and self.jogador.pontos_de_atributo_para_distribuir > 0:
            opcoes_comuns.insert(0, f"Distribuir Pontos de Atributo ({self.jogador.pontos_de_atributo_para_distribuir})")

        opcoes_comuns.extend(["Salvar Jogo", "Sair para o Menu Principal"])

        if self.localizacao_atual == "vila":
            opcoes_vila = [
                "Falar com Elara (Curandeira da Vila)",
                "Visitar a forja 'O Aço Resoluto' (Forja)",
                "Usar Bancada de Alquimia (Cabana da Elara)",
                "Usar Fogueira da Vila (Culinária)",
                "Ir para a Floresta dos Sussurros",
                "Ir para o Pântano Sombrio"
            ]
            if self.jogador and any(q.id_quest == "mq04_chamado_antigo" for q in self.jogador.quests_ativas):
                opcoes_vila.append("Viajar para Aethelgard")
            return opcoes_vila + opcoes_comuns
        elif self.localizacao_atual == "floresta":
            return ["Explorar mais fundo", "Montar Acampamento (Descansar)", "Voltar para a Vila"] + opcoes_comuns
        elif self.localizacao_atual == "pantano_sombrio":
            return ["Explorar o pântano", "Montar Acampamento (Descansar)", "Voltar para a Vila"] + opcoes_comuns
        elif self.localizacao_atual == "aethelgard":
            opcoes_aethelgard = [
                "Falar com Mestre Valerius (Grande Biblioteca)",
                "Procurar o Mestre de Classe",
                "Ir para os Ermos Rochosos",
                "Voltar para a Vila"
            ]
            return opcoes_aethelgard + opcoes_comuns
        return opcoes_comuns

    def executar_opcao_localizacao(self, opcao: str):
        self.clear_log()
        if opcao == "Salvar Jogo":
            self.salvar_jogo("save_teste")
        elif opcao == "Sair para o Menu Principal":
            self.game_state = "main_menu"
        elif self.localizacao_atual == "vila":
            if opcao == "Falar com Elara (Curandeira da Vila)":
                self.game_log.extend(quests.atualizar_progresso_quests(self.jogador, "falar_com", "elara_curandeira"))
                q_despertar_ativa = next((q for q in self.jogador.quests_ativas if q.id_quest == "mq01_despertar"), None)
                if not q_despertar_ativa and "mq01_despertar" not in self.jogador.quests_concluidas:
                    self.game_log.extend(quests.iniciar_quest(self.jogador, "mq01_despertar"))
                    self.game_log.append(quests.TODAS_AS_QUESTS["mq01_despertar"]["descricao_inicio"])

                q_despertar = next((q for q in self.jogador.quests_ativas if q.id_quest == "mq01_despertar"), None)
                q_ameaca = next((q for q in self.jogador.quests_ativas if q.id_quest == "mq02_ameaca_local"), None)
                q_pantano = next((q for q in self.jogador.quests_ativas if q.id_quest == "sq01_coracao_pantano"), None)

                if q_despertar and q_despertar.esta_completa():
                    self.game_log.extend(quests.concluir_quest(self.jogador, q_despertar))
                    self.game_log.append(quests.TODAS_AS_QUESTS["mq02_ameaca_local"]["descricao_inicio"])
                    self.game_log.extend(quests.iniciar_quest(self.jogador, "mq02_ameaca_local"))
                elif q_ameaca and q_ameaca.esta_completa():
                    self.game_log.extend(quests.concluir_quest(self.jogador, q_ameaca))
                    self.game_log.append(quests.TODAS_AS_QUESTS["sq01_coracao_pantano"]["descricao_inicio"])
                    self.game_log.extend(quests.iniciar_quest(self.jogador, "sq01_coracao_pantano"))
                elif q_pantano and q_pantano.esta_completa():
                    self.game_log.extend(quests.concluir_quest(self.jogador, q_pantano))
                    self.game_log.append(quests.TODAS_AS_QUESTS["mq04_chamado_antigo"]["descricao_inicio"])
                    self.game_log.extend(quests.iniciar_quest(self.jogador, "mq04_chamado_antigo"))
                else:
                    if not self.game_log:
                        self._add_log("'É bom ver você bem. Cuidado lá fora.'")
                funcoes_gerais.pausar()

            elif opcao == "Visitar a forja 'O Aço Resoluto' (Forja)":
                menu_loja.loja_ui(self.jogador, 'ferreiro_vila')
            elif opcao == "Usar Bancada de Alquimia (Cabana da Elara)":
                menu_crafting.crafting_ui(self.jogador, "bancada_alquimia")
            elif opcao == "Usar Fogueira da Vila (Culinária)":
                menu_crafting.crafting_ui(self.jogador, "fogueira")
            elif opcao == "Ir para a Floresta dos Sussurros":
                self.localizacao_atual = "floresta"
                self._add_log("Você deixa a segurança da vila e adentra a Floresta dos Sussurros.")
            elif opcao == "Ir para o Pântano Sombrio":
                self.localizacao_atual = "pantano_sombrio"
                self._add_log("Você segue um caminho úmido e malcheiroso em direção ao Pântano Sombrio.")
            elif opcao == "Viajar para Aethelgard":
                self.localizacao_atual = "aethelgard"
                self._add_log("Após uma longa jornada, você chega aos portões da grande cidade de Aethelgard.")
                self.game_log.extend(quests.atualizar_progresso_quests(self.jogador, "viajar_para", "cidade_aethelgard"))

        elif self.localizacao_atual == "aethelgard":
            if opcao == "Falar com Mestre Valerius (Grande Biblioteca)":
                self.game_log.extend(quests.atualizar_progresso_quests(self.jogador, "falar_com", "mestre_valerius"))
                chamado_antigo_quest = next((q for q in self.jogador.quests_ativas if q.id_quest == "mq04_chamado_antigo"), None)
                if chamado_antigo_quest and chamado_antigo_quest.esta_completa():
                    self.game_log.extend(quests.concluir_quest(self.jogador, chamado_antigo_quest))
                    self.game_log.append(quests.TODAS_AS_QUESTS["mq05_a_primeira_dungeon"]["descricao_inicio"])
                    self.game_log.extend(quests.iniciar_quest(self.jogador, "mq05_a_primeira_dungeon"))
                else:
                    self._add_log("Você encontra um homem idoso e sábio, cercado por pilhas de livros. 'Sim? Posso ajudá-lo?'")
            elif opcao == "Procurar o Mestre de Classe":
                menu_evolucao.evolucao_ui(self.jogador)
            elif opcao == "Ir para os Ermos Rochosos":
                self.localizacao_atual = "ermos_rochosos"
                self._add_log("Você viaja para os ermos rochosos nos arredores de Aethelgard.")
            elif opcao == "Voltar para a Vila":
                self.localizacao_atual = "vila"
                self._add_log("Você decide voltar para a tranquilidade de Valesereno.")
