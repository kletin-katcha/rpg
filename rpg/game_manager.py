from typing import Optional, TYPE_CHECKING
import random
from typing import List, Dict

from .entidades.personagem import Personagem
from .sistemas import combate, quests, tempo, dungeons
from .io import salvar_carregar
from .fabricas.fabrica_monstros import criar_monstro_por_id
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
        # A UI agora é responsável pela criação do personagem.
        # Esta função prepara o estado para o jogo começar.
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
            # A UI deve fornecer o nome do slot
            self.carregar_jogo("save_teste")
        elif opcao == "Sair":
            self.encerrar_jogo()

    def get_opcoes_localizacao(self) -> list[str]:
        opcoes_comuns = [
            "Ver Diário de Missões", "Abrir Inventário", "Ver Equipamento",
            "Ver status do personagem"
        ]
        # Adiciona a opção de distribuir pontos se o jogador tiver algum
        if self.jogador and self.jogador.pontos_de_atributo_para_distribuir > 0:
            opcoes_comuns.insert(0, f"Distribuir Pontos de Atributo ({self.jogador.pontos_de_atributo_para_distribuir})")

        opcoes_comuns.extend(["Salvar Jogo", "Sair para o Menu Principal"])

        if self.localizacao_atual == "vila":
            opcoes_vila = ["Falar com Elara (Curandeira da Vila)", "Ir para a Floresta dos Sussurros", "Ir para o Pântano Sombrio"]
            # Adiciona a opção de viajar se o jogador tiver a quest
            if self.jogador and any(q.id_quest == "mq04_chamado_antigo" for q in self.jogador.quests_ativas):
                opcoes_vila.append("Viajar para Aethelgard")
            return opcoes_vila + opcoes_comuns
        elif self.localizacao_atual == "floresta":
            return ["Explorar mais fundo", "Montar Acampamento (Descansar)", "Voltar para a Vila"] + opcoes_comuns
        elif self.localizacao_atual == "pantano_sombrio":
            return ["Explorar o pântano", "Montar Acampamento (Descansar)", "Voltar para a Vila"] + opcoes_comuns
        return opcoes_comuns

    def executar_opcao_localizacao(self, opcao: str):
        self.clear_log()
        if opcao == "Salvar Jogo":
            self.salvar_jogo("save_teste")
        elif opcao == "Sair para o Menu Principal":
            self.game_state = "main_menu"
        elif self.localizacao_atual == "vila":
            if opcao == "Falar com Elara (Curandeira da Vila)":
                # Lógica de quests com Elara...
                pantano_quest = next((q for q in self.jogador.quests_ativas if q.id_quest == "sq01_coracao_pantano"), None)

                if pantano_quest and pantano_quest.esta_completa():
                    quests.concluir_quest(self.jogador, pantano_quest)
                    quests.iniciar_quest(self.jogador, "mq04_chamado_antigo")
                elif "mq02_ameaca_local" in self.jogador.quests_concluidas and not pantano_quest and "sq01_coracao_pantano" not in self.jogador.quests_concluidas:
                    quests.iniciar_quest(self.jogador, "sq01_coracao_pantano")
                else:
                    self._add_log("'É bom ver você bem. Cuidado lá fora.'")

            elif opcao == "Ir para a Floresta dos Sussurros":
                self.time_manager.avancar_tempo(60)
                self.localizacao_atual = "floresta"
                self._add_log("Você deixa a segurança da vila e adentra a Floresta dos Sussurros.")
            elif opcao == "Ir para o Pântano Sombrio":
                self.time_manager.avancar_tempo(90)
                self.localizacao_atual = "pantano_sombrio"
                self._add_log("Você segue um caminho úmido e malcheiroso em direção ao Pântano Sombrio.")
            elif opcao == "Viajar para Aethelgard":
                self.time_manager.avancar_tempo(240)
                self.localizacao_atual = "aethelgard"
                self._add_log("Após uma longa jornada, você chega aos portões da grande cidade de Aethelgard.")
                quests.atualizar_progresso_quests(self.jogador, "viajar_para", "cidade_aethelgard")

        elif self.localizacao_atual == "floresta":
            if opcao == "Explorar mais fundo":
                self.time_manager.avancar_tempo(30)
                if random.random() < 0.15: # 15% de chance de achar uma dungeon
                    self.dungeon_atual = gerar_dungeon_aleatoria(self.jogador.nivel)
                    self.game_state = "in_dungeon"
                    self._add_log(f"Você encontra a entrada para uma {self.dungeon_atual.nome}!")
                elif random.random() < 0.75:
                    id_monstro = random.choice(list(MONSTROS_AREA1.keys()))
                    self.iniciar_combate([id_monstro])
                else:
                    self._add_log("Você explora a floresta, mas não encontra nada de interessante.")
            elif opcao == "Voltar para a Vila":
                self.time_manager.avancar_tempo(60)
                self.localizacao_atual = "vila"
                self._add_log("Você retorna para a segurança de Valesereno.")
            elif opcao == "Montar Acampamento (Descansar)":
                self.time_manager.avancar_tempo(480)
                self.jogador.hp_atual = self.jogador.hp_max
                self.jogador.mp_atual = self.jogador.mp_max
                self._add_log("Você dorme por 8 horas e recupera suas forças.")
        elif self.localizacao_atual == "pantano_sombrio":
            if opcao == "Explorar o pântano":
                self.time_manager.avancar_tempo(45)
                if random.random() < 0.20: # Chance maior no pântano
                    self.dungeon_atual = gerar_dungeon_aleatoria(self.jogador.nivel)
                    self.game_state = "in_dungeon"
                    self._add_log(f"Você encontra a entrada para uma {self.dungeon_atual.nome}!")
                elif random.random() < 0.8: # Pântano é mais perigoso
                    id_monstro = random.choice(list(MONSTROS_AREA2.keys()))
                    self.iniciar_combate([id_monstro])
                else:
                    self._add_log("O ar pesado e os sons estranhos o deixam em alerta, mas nada acontece.")
            elif opcao == "Voltar para a Vila":
                self.time_manager.avancar_tempo(90)
                self.localizacao_atual = "vila"
                self._add_log("Você retorna para a segurança de Valesereno.")
            elif opcao == "Montar Acampamento (Descansar)":
                self._add_log("Você não consegue encontrar um local seco e seguro para descansar no pântano.")
        elif self.localizacao_atual == "aethelgard":
            if opcao == "Falar com Mestre Valerius":
                quests.atualizar_progresso_quests(self.jogador, "falar_com", "mestre_valerius")
                chamado_antigo_quest = next((q for q in self.jogador.quests_ativas if q.id_quest == "mq04_chamado_antigo"), None)

                if chamado_antigo_quest and chamado_antigo_quest.esta_completa():
                    quests.concluir_quest(self.jogador, chamado_antigo_quest)
                    quests.iniciar_quest(self.jogador, "mq05_a_primeira_dungeon")
                else:
                    self._add_log("Você encontra um homem idoso e sábio, cercado por pilhas de livros. 'Sim? Posso ajudá-lo?'")

            elif opcao == "Ir para os Ermos Rochosos":
                self.localizacao_atual = "ermos_rochosos"
                self._add_log("Você viaja para os ermos rochosos nos arredores de Aethelgard.")

            elif opcao == "Voltar para a Vila":
                self.localizacao_atual = "vila"
                self._add_log("Você decide voltar para a tranquilidade de Valesereno.")

    def executar_opcao_dungeon(self, opcao: str):
        """Executa uma ação dentro de uma dungeon."""
        self.clear_log()
        if not self.dungeon_atual: return

        sala_atual = self.dungeon_atual.sala_atual
        if opcao == "Avançar para a próxima sala":
            if sala_atual.concluida:
                if not self.dungeon_atual.avancar_sala():
                    self._add_log("Você chegou ao fim da dungeon!")
                    # Lógica para sair da dungeon
                    self.game_state = "in_game"
                    self.localizacao_atual = "ermos_rochosos"
                    self.dungeon_atual = None
            else:
                self._add_log("Você precisa derrotar todos os monstros antes de avançar.")

        elif opcao == "Pegar tesouro":
            if sala_atual.tesouros:
                tesouro = sala_atual.tesouros.pop(0) # Pega o primeiro tesouro
                if random.random() < tesouro.get("chance", 1.0):
                    self.jogador.adicionar_item(tesouro["id_item"], 1)
                    quests.atualizar_progresso_quests(self.jogador, "encontrar_item", tesouro["id_item"])
                else:
                    self._add_log("Você não encontrou nada de valor.")
            else:
                self._add_log("Não há tesouros nesta sala.")

        elif opcao == "Sair da dungeon":
            self.game_state = "in_game"
            self.localizacao_atual = "ermos_rochosos" # Retorna para a entrada
            self.dungeon_atual = None
            self._add_log("Você saiu da dungeon.")

        elif self.localizacao_atual == "ermos_rochosos":
            if opcao == "Entrar nas Ruínas de Al'Khem":
                self.entrar_dungeon("ruinas_alkhem")
            elif opcao == "Voltar para Aethelgard":
                self.localizacao_atual = "aethelgard"
                self._add_log("Você retorna para a cidade.")

    def entrar_dungeon(self, id_dungeon: str):
        """Coloca o jogador dentro de uma dungeon."""
        dungeon_data = DUNGEONS_FIXAS.get(id_dungeon)
        if not dungeon_data:
            self._add_log("Dungeon não encontrada.")
            return

        salas = [dungeons.Room(**sala_data) for sala_data in dungeon_data["salas"]]
        self.dungeon_atual = dungeons.Dungeon(
            id_dungeon=id_dungeon,
            nome=dungeon_data["nome"],
            descricao=dungeon_data["descricao"],
            nivel_minimo=dungeon_data["nivel_minimo"],
            salas=salas
        )
        self.game_state = "in_dungeon"
        quests.atualizar_progresso_quests(self.jogador, "entrar_em", id_dungeon)
        self._add_log(f"Você entrou em {self.dungeon_atual.nome}.")

    def iniciar_combate(self, ids_monstros: list[str]):
        monstros = [criar_monstro_por_id(id_monstro) for id_monstro in ids_monstros]
        todos_combatentes = [self.jogador] + monstros
        todos_combatentes.sort(key=lambda c: c.destreza, reverse=True)

        self.game_state = "combat"
        self.combat_state = {
            "todos_combatentes": todos_combatentes,
            "turn_index": 0,
            "jogador": self.jogador,
            "inimigos": monstros,
        }
        self._add_log(f"Combate iniciado contra {[m.nome for m in monstros]}!")
        ordem_str = " -> ".join([c.nome for c in todos_combatentes])
        self._add_log(f"Ordem de iniciativa: {ordem_str}")

    def get_combatente_atual(self) -> Optional[Personagem]:
        if not self.combat_state: return None
        idx = self.combat_state["turn_index"]
        return self.combat_state["todos_combatentes"][idx]

    def _avancar_turno(self):
        if not self.combat_state: return
        # Loop para garantir que o próximo combatente esteja vivo
        for _ in range(len(self.combat_state["todos_combatentes"])):
            current_idx = self.combat_state["turn_index"]
            next_idx = (current_idx + 1) % len(self.combat_state["todos_combatentes"])
            self.combat_state["turn_index"] = next_idx
            if self.get_combatente_atual().esta_vivo():
                return

    def executar_turno_combate(self, acao: dict) -> dict:
        self.clear_log()
        if not self.combat_state or self.game_state != "combat":
            self._add_log("ERRO: Não está em modo de combate.")
            return {"resultado": "erro", "log": self.game_log}

        combatente_atual = self.get_combatente_atual()
        if not combatente_atual.esta_vivo():
            self._add_log(f"{combatente_atual.nome} está fora de combate e não pode agir.")
            self._avancar_turno()
            return {"resultado": "continuar", "log": self.game_log}

        log_turno = combate._regenerar_recursos(combatente_atual)
        if not combatente_atual.esta_vivo():
            log_turno.append(f"{combatente_atual.nome} sucumbiu aos seus ferimentos no início do turno.")
            self._add_log("\n".join(log_turno))
            self._avancar_turno()
            return {"resultado": "continuar", "log": self.game_log}

        acao_final = acao
        if combatente_atual != self.jogador: # É um monstro
            acao_final = combatente_atual.decidir_acao(
                aliados=self.combat_state["inimigos"],
                inimigos=[self.jogador]
            )

        log_turno.extend(combate.executar_acao(combatente_atual, acao_final, [self.jogador], self.combat_state["inimigos"]))
        self._add_log("\n".join(log_turno))

        inimigos_vivos = [m for m in self.combat_state["inimigos"] if m.esta_vivo()]
        if not inimigos_vivos:
            self.game_state = "in_game"
            self._add_log("Você venceu a batalha!")

            # Processar recompensas e progresso de quests
            xp_total = 0
            for inimigo_morto in self.combat_state["inimigos"]:
                xp_total += inimigo_morto.xp_recompensa
                quests.atualizar_progresso_quests(self.jogador, "matar", inimigo_morto.id_monstro)

            self.jogador.ganhar_xp(xp_total)
            self.combat_state = None
            return {"resultado": "vitoria", "log": self.game_log}

        if not self.jogador.esta_vivo():
            self.game_state = "main_menu"
            self._add_log("Você foi derrotado.")
            self.combat_state = None
            return {"resultado": "derrota", "log": self.game_log}

        self._avancar_turno()
        return {"resultado": "continuar", "log": self.game_log}

    def get_opcoes_combate(self) -> list[str]:
        return ["Atacar", "Habilidade", "Item", "Defender", "Fugir"]

    def get_habilidades_ativas_jogador(self) -> List[Dict]:
        if not self.jogador: return []
        habilidades_ativas = []
        for hab_id in self.jogador.habilidades:
            hab_data = TODAS_HABILIDADES.get(hab_id)
            if hab_data and hab_data.get("tipo") == "ativa":
                custo = hab_data.get("custo_valor", 0)
                recurso_atual = self.jogador.mp_atual if hab_data.get("custo_tipo") == "mp" else self.jogador.stamina_atual
                if recurso_atual >= custo:
                    habilidades_ativas.append(hab_data)
        return habilidades_ativas
