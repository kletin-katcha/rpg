from typing import Optional, TYPE_CHECKING
import random
from typing import List, Dict
from .entidades.personagem import Personagem
from .sistemas import combate, quests
from .io import menu_inventario, menu_equipamento, salvar_carregar
from .io import criacao_personagem as cc_api
# O narrador será substituído por um sistema de log de eventos
# from .utilitarios import funcoes_gerais, narrador
from .fabricas.fabrica_monstros import criar_monstro_por_id
from .dados.habilidades import TODAS_HABILIDADES

if TYPE_CHECKING:
    from .entidades.personagem import Personagem

class GameManager:
    """
    A classe central que gerencia o estado e a lógica principal do jogo.
    Funciona como o "motor" que será consumido por qualquer interface (GUI, console, etc.).
    """
    def __init__(self):
        self.jogador: Optional['Personagem'] = None
        self.is_running: bool = True
        # O estado do jogo pode ser: 'main_menu', 'in_game', 'combat'
        self.game_state: str = "main_menu"
        self.combat_state: Optional[dict] = None
        self.game_log: list[str] = [] # Log de eventos para a UI

    def _add_log(self, message: str):
        """Adiciona uma mensagem ao log do jogo para ser exibida na UI."""
        self.game_log.append(message)

    def clear_log(self):
        """Limpa o log de eventos."""
        self.game_log.clear()

    def novo_jogo(self):
        """
        Prepara o jogo para um novo estado. A criação de personagem
        agora é gerenciada pela UI, que então define o jogador.
        """
        # A UI chamará a criação de personagem e então definirá self.jogador
        # e mudará o estado para 'in_game'.
        self.jogador = None
        self.game_state = "in_game" # A UI irá popular o jogador antes de entrar no loop in_game.
        print("DEBUG: Novo jogo iniciado. Aguardando criação de personagem pela UI.")

    def carregar_jogo(self, save_slot: str):
        """
        Carrega o estado do jogo a partir de um arquivo de save.
        """
        # TODO: Implementar a lógica de carregamento
        print(f"DEBUG: Lógica de carregar do slot '{save_slot}' a ser implementada.")
        self.game_state = "in_game"

    def encerrar_jogo(self):
        """
        Sinaliza para a aplicação que o jogo deve ser encerrado.
        """
        self.is_running = False
        print("DEBUG: Jogo encerrado.")

    # --- Funções de API para a interface ---

    def get_opcoes_menu_principal(self) -> list[str]:
        """Retorna as opções disponíveis no menu principal."""
        return ["Novo Jogo", "Carregar Jogo", "Sair"]

    def executar_opcao_menu_principal(self, opcao: str):
        """Executa uma ação do menu principal."""
        if opcao == "Novo Jogo":
            self.novo_jogo()
        elif opcao == "Carregar Jogo":
            # A interface precisará fornecer o slot de save
            self.carregar_jogo("slot_1")
        elif opcao == "Sair":
            self.encerrar_jogo()

    # --- Métodos da API de Criação de Personagem (REMOVIDOS) ---
    # A lógica de criação de personagem foi movida para o cliente de UI
    # para melhor separação de responsabilidades.

    def get_opcoes_cidade(self) -> list[str]:
        """Retorna as opções de ação disponíveis na cidade atual."""
        # No futuro, isso pode mudar dependendo da cidade ou do estado do jogo.
        return [
            "Falar com Elara (Curandeira da Vila)",
            "Explorar a Floresta dos Sussurros",
            "Viajar",
            "Ver Diário de Missões",
            "Abrir Inventário",
            "Ver Equipamento",
            "Ver status do personagem",
            "Salvar Jogo",
            "Sair para o Menu Principal"
        ]

    def executar_opcao_cidade(self, opcao: str) -> dict:
        """
        Executa uma ação na cidade e retorna um dicionário com o resultado
        para a interface. Substitui o loop de `if/elif` em `main.py`.
        """
        self.clear_log() # Limpa o log de eventos anteriores

        if opcao == "Falar com Elara (Curandeira da Vila)":
            self._add_log("Você se aproxima de Elara, a curandeira local. Ela sorri calorosamente.")

            quest_despertar = next((q for q in self.jogador.quests_ativas if q.id_quest == "mq01_despertar"), None)
            quest_ameaca = next((q for q in self.jogador.quests_ativas if q.id_quest == "mq02_ameaca_local"), None)

            if not quest_despertar and "mq01_despertar" not in self.jogador.quests_concluidas:
                self._add_log("'Que bom que você acordou! Você estava desmaiado na floresta. Como se sente?'")
                quests.iniciar_quest(self.jogador, "mq01_despertar")
            elif quest_despertar and not quest_despertar.esta_completa():
                quests.atualizar_progresso_quests(self.jogador, "falar_com", "elara_curandeira")
                if quest_despertar.esta_completa():
                    quests.concluir_quest(self.jogador, quest_despertar)
                    self._add_log("'Fico feliz que esteja se recuperando. Na verdade, preciso de um favor...'")
                    quests.iniciar_quest(self.jogador, "mq02_ameaca_local")
            elif quest_ameaca and quest_ameaca.esta_completa():
                quests.concluir_quest(self.jogador, quest_ameaca)
                self._add_log("'Não acredito que você conseguiu! A vila está em dívida com você. Mas ao derrotá-los, você encontrou algo estranho...'")
                quests.iniciar_quest(self.jogador, "mq03_primeira_sombra")
            else:
                self._add_log("'É bom ver você bem. Cuidado lá fora.'")

            if self.jogador.hp_atual < self.jogador.hp_max or self.jogador.mp_atual < self.jogador.mp_max:
                self._add_log("\n'Você parece cansado. Deixe-me restaurar suas energias.'")
                return {"tipo": "pergunta", "prompt": "Aceitar a cura? (s/n)", "acao": "curar_jogador", "log": self.game_log}

            return {"tipo": "feedback", "log": self.game_log}

        elif opcao == "Explorar a Floresta dos Sussurros":
            if random.random() < 0.75:
                id_monstro_encontrado = random.choice(list(MONSTROS_AREA1.keys()))
                self.iniciar_combate([id_monstro_encontrado])
                # A lógica de recompensa e quest progress agora deve ser chamada após o combate
                # Esta parte precisará de mais refatoração no futuro.
                return {"tipo": "transicao_estado", "novo_estado": "combat", "log": self.game_log}
            else:
                self._add_log("Você explora a floresta, mas não encontra nada de interessante.")
                return {"tipo": "feedback", "log": self.game_log}

        elif opcao == "Viajar":
            self._add_log("Você ainda não sabe para onde ir. Melhor continuar explorando a área local.")
            return {"tipo": "feedback", "log": self.game_log}

        elif opcao == "Ver Diário de Missões":
            # A UI chamaria uma função para obter os dados das quests e exibi-los.
            return {"tipo": "abrir_tela", "tela": "diario_missoes"}

        elif opcao == "Abrir Inventário":
            return {"tipo": "abrir_tela", "tela": "inventario"}

        elif opcao == "Ver Equipamento":
            return {"tipo": "abrir_tela", "tela": "equipamento"}

        elif opcao == "Ver status do personagem":
            return {"tipo": "abrir_tela", "tela": "status_personagem"}

        elif opcao == "Salvar Jogo":
            # A UI forneceria o nome do save.
            salvar_carregar.salvar_jogo(self.jogador, "save_teste")
            self._add_log("Jogo salvo com sucesso.")
            return {"tipo": "feedback", "log": self.game_log}

        elif opcao == "Sair para o Menu Principal":
            self.game_state = "main_menu"
            return {"tipo": "transicao_estado", "novo_estado": "main_menu"}

        else:
            self._add_log("Opção desconhecida.")
            return {"tipo": "feedback", "log": self.game_log}

    def executar_acao_contextual(self, acao: str):
        """Executa uma ação contextual, como aceitar uma cura."""
        self.clear_log()
        if acao == "curar_jogador":
            self.jogador.hp_atual = self.jogador.hp_max
            self.jogador.mp_atual = self.jogador.mp_max
            self._add_log("Você se sente revigorado! HP e MP totalmente restaurados.")
            return {"tipo": "feedback", "log": self.game_log}
        return {"tipo": "feedback", "log": ["Ação contextual desconhecida."]}


    # --- Métodos da API de Combate ---

    def iniciar_combate(self, ids_monstros: list[str]):
        """Prepara o estado de combate, incluindo a ordem de iniciativa."""
        monstros = [criar_monstro_por_id(id_monstro) for id_monstro in ids_monstros]

        # Cria a lista de todos os combatentes e a ordena pela Destreza (iniciativa)
        todos_combatentes = [self.jogador] + monstros
        todos_combatentes.sort(key=lambda c: c.destreza, reverse=True)

        self.game_state = "combat"
        self.combat_state = {
            "todos_combatentes": todos_combatentes,
            "turn_index": 0,
            "jogador": self.jogador, # Mantém referência fácil
            "inimigos": monstros,     # Mantém referência fácil
            "log_combate": []
        }
        self._add_log(f"Combate iniciado contra {[m.nome for m in monstros]}!")
        ordem_str = " -> ".join([c.nome for c in todos_combatentes])
        self._add_log(f"Ordem de iniciativa: {ordem_str}")

    def get_opcoes_combate(self) -> list[str]:
        """Retorna as ações de combate disponíveis para o jogador."""
        opcoes = ["Atacar", "Defender"]
        # Adiciona a opção de habilidade apenas se o jogador tiver habilidades ativas
        if self.get_habilidades_ativas_jogador():
            opcoes.append("Habilidade")
        # TODO: Adicionar checagem de itens consumíveis
        opcoes.append("Item")
        opcoes.append("Fugir")
        return opcoes

    def get_habilidades_ativas_jogador(self) -> List[Dict]:
        """
        Retorna uma lista de dicionários das habilidades ativas que o jogador possui
        e pode pagar o custo.
        """
        if not self.jogador:
            return []

        habilidades_ativas = []
        for hab_id in self.jogador.habilidades:
            hab_data = TODAS_HABILIDADES.get(hab_id)
            if hab_data and hab_data.get("tipo") == "ativa":
                custo = hab_data.get("custo_valor", 0)
                recurso_atual = 0
                if hab_data.get("custo_tipo") == "mp":
                    recurso_atual = self.jogador.mp_atual
                elif hab_data.get("custo_tipo") == "stamina":
                    recurso_atual = self.jogador.stamina_atual
                else: # Habilidades sem custo
                    recurso_atual = custo

                if recurso_atual >= custo:
                    habilidades_ativas.append(hab_data)

        return habilidades_ativas

    def get_estado_combate(self) -> dict:
        """Retorna o estado atual do combate para a UI renderizar."""
        return self.combat_state

    def get_combatente_atual(self) -> Optional['Personagem']:
        """Retorna o combatente cujo turno está ativo."""
        if not self.combat_state:
            return None
        idx = self.combat_state["turn_index"]
        return self.combat_state["todos_combatentes"][idx]

    def _avancar_turno(self):
        """Avança o índice de turno na fila de iniciativa."""
        if not self.combat_state: return

        # Loop para garantir que o próximo combatente esteja vivo
        for _ in range(len(self.combat_state["todos_combatentes"])):
            current_idx = self.combat_state["turn_index"]
            next_idx = (current_idx + 1) % len(self.combat_state["todos_combatentes"])
            self.combat_state["turn_index"] = next_idx
            if self.get_combatente_atual().esta_vivo():
                return

    def executar_turno_combate(self, acao: dict = None) -> dict:
        """
        Executa o turno para o combatente atual na fila de iniciativa.
        Se for o turno do jogador, a 'acao' fornecida é usada.
        Se for um monstro, a IA decide a ação.
        """
        if not self.combat_state or self.game_state != "combat":
            return {"erro": "Não está em modo de combate."}

        log_turno = []
        combatente_atual = self.get_combatente_atual()

        # Se o combatente atual não pode agir (ex: atordoado) ou está morto, apenas avança o turno.
        if not combatente_atual.esta_vivo():
            log_turno.append(f"{combatente_atual.nome} está fora de combate.")
            self._avancar_turno()
            return {"resultado": "continuar", "log": log_turno}

        # Processa regeneração e efeitos (DoTs, HoTs) no início do turno de cada um.
        log_turno.extend(combate._regenerar_recursos(combatente_atual))
        if not combatente_atual.esta_vivo():
            log_turno.append(f"{combatente_atual.nome} sucumbiu aos seus ferimentos no início do turno.")
            self._avancar_turno()
            return {"resultado": "continuar", "log": log_turno}

        # Determina a ação a ser executada
        acao_final = acao
        if isinstance(combatente_atual, Personagem) and combatente_atual != self.jogador: # Se for um Monstro
            acao_final = combatente_atual.decidir_acao(
                aliados=[c for c in self.combat_state["todos_combatentes"] if isinstance(c, Personagem) and c != self.jogador],
                inimigos=[self.jogador]
            )
        elif not acao:
             return {"erro": "Ação do jogador não fornecida."}

        # Executa a ação
        log_turno.extend(combate.executar_acao(combatente_atual, acao_final, [self.jogador], self.combat_state["inimigos"]))

        # Verifica condição de fim de combate
        inimigos_vivos = [m for m in self.combat_state["inimigos"] if m.esta_vivo()]
        if not inimigos_vivos:
            self.game_state = "in_game"
            log_turno.append("Você venceu a batalha!")
            xp_total = sum(i.xp_recompensa for i in self.combat_state["inimigos"])
            ouro_total = sum(i.ouro for i in self.combat_state["inimigos"])
            log_turno.append(f"Você ganhou {xp_total} de XP e {ouro_total} de ouro.")
            self.jogador.ganhar_xp(xp_total)
            self.jogador.ouro += ouro_total
            # ... (código de loot) ...
            self.combat_state = None
            return {"resultado": "vitoria", "log": log_turno}

        if not self.jogador.esta_vivo():
            self.game_state = "main_menu"
            log_turno.append("Você foi derrotado.")
            self.combat_state = None
            return {"resultado": "derrota", "log": log_turno}

        # Avança para o próximo combatente na fila
        self._avancar_turno()
        return {"resultado": "continuar", "log": log_turno}
