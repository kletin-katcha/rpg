# -*- coding: utf-8 -*-
"""
================================================================================================
GUI: JANELA PRINCIPAL
================================================================================================
Este arquivo define a classe `MainWindow`, que é a janela raiz da aplicação gráfica
usando o framework Tkinter.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
- **Raiz do Tkinter:** A classe herda de `tkinter.Tk`, tornando-se a janela
  principal da aplicação.
- **Controlador de Views:** Ela contém um frame principal que atua como um
  container. A responsabilidade da `MainWindow` será a de gerenciar qual "view"
  (tela do jogo, como menu, exploração, etc.) está sendo exibida neste container.
- **Ponto de Entrada:** O método `start()` inicia o loop principal do Tkinter,
  tornando a janela visível e interativa.
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Importa as views
from .views.view_menu_principal import MenuPrincipalView
from .views.view_creditos import CreditosView
from .views.view_configuracoes import ConfiguracoesView
from .views.view_criacao_personagem import CriacaoPersonagemView
from .views.view_cidade import CidadeView
from .views.view_exploracao import ExploracaoView
from .views.view_combate import CombateView
from .views.view_personagem import PersonagemView
from .views.view_loja import LojaView
from .views.view_taverna import TavernaView

import random
# Importa o gerenciador de configuração e entidades
from rpg_colossal.motor_jogo.utilitarios.gerenciador_config import load_settings
from rpg_colossal.motor_jogo.utilitarios.rolador_dados import rolar_dados
from rpg_colossal.motor_jogo.entidades.personagem import Personagem
from rpg_colossal.motor_jogo.entidades.monstro import Monstro
from rpg_colossal.motor_jogo.banco_de_dados.racas.racas_base import RACAS_DATA
from rpg_colossal.motor_jogo.banco_de_dados.classes.classes_iniciais import CLASSES_INICIAIS
from rpg_colossal.motor_jogo.banco_de_dados.monstros.monstros_regiao_inicial import MONSTROS_REGIAO_INICIAL
from rpg_colossal.motor_jogo.sistemas.combate import CombatManager
from rpg_colossal.motor_jogo.sistemas.gerenciador_save import GerenciadorSave, EstadoJogo
from rpg_colossal.motor_jogo.banco_de_dados.habilidades import (
    fisicas, magicas_arcano, magicas_fogo, magicas_gelo, raciais, suporte
)
from rpg_colossal.motor_jogo.banco_de_dados.itens import consumiveis

# --- Montagem do Grimório Completo ---
GRIMORIO_COMPLETO = {}
GRIMORIO_COMPLETO.update(fisicas.GRIMORIO_FISICO["by_id"])
# Adicionar outros grimórios aqui quando forem indexados

# --- Montagem do Índice de Itens Completo ---
INDICE_ITENS_COMPLETO = {}
INDICE_ITENS_COMPLETO.update(consumiveis.INDICE_CONSUMIVEIS["by_id"])
# Adicionar outros índices de itens aqui

class MainWindow(tk.Tk):
    """
    A janela principal da aplicação gráfica de Aetheria.
    """
    def __init__(self):
        super().__init__()

        # --- Configuração da Janela Principal ---
        self.title("Ecos da Aetheria")
        self.geometry("1280x720") # Tamanho inicial da janela
        self.configure(bg="#212121") # Cor de fundo escura

        # --- Carrega e Aplica Configurações de Estilo ---
        self.apply_settings()

        # --- Container Principal ---
        # Todas as outras views (telas) serão colocadas dentro deste frame.
        self.container = ttk.Frame(self, padding="10")
        self.container.pack(expand=True, fill="both")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Dicionário para armazenar as diferentes views do jogo
        self.views = {}
        self.jogador_atual = None # Armazena a instância do personagem do jogador
        self.combat_manager = None # Armazena a instância do gerenciador de combate
        self.save_manager = GerenciadorSave() # Armazena o gerenciador de save

        # Adiciona as views ao dicionário
        self.add_view("menu_principal", MenuPrincipalView)
        self.add_view("creditos", CreditosView)
        self.add_view("configuracoes", ConfiguracoesView)
        self.add_view("criacao_personagem", CriacaoPersonagemView)
        self.add_view("cidade", CidadeView)
        self.add_view("exploracao", ExploracaoView)
        self.add_view("combate", CombateView)
        self.add_view("personagem", PersonagemView)
        self.add_view("loja", LojaView)
        self.add_view("taverna", TavernaView)

        # Exibe a view inicial
        self.switch_view("menu_principal")


    def apply_settings(self):
        """Carrega as configurações e aplica os estilos na aplicação."""
        settings = load_settings()
        font_size = settings.get("font_size", 12)

        style = ttk.Style(self)
        style.theme_use('clam')

        # Estilos Gerais
        style.configure("TFrame", background="#212121")
        style.configure("TLabel", background="#212121", foreground="white", font=("Arial", 12))
        style.configure("TButton", background="#424242", foreground="white", font=("Arial", 12, "bold"))
        style.map("TButton", background=[('active', '#616161')])

        # Estilo para Narração/Texto Principal com fonte customizável
        style.configure("Narration.TLabel",
                        background="#212121",
                        foreground="white",
                        font=("Arial", font_size),
                        wraplength=800, # Quebra de linha automática
                        anchor="center")


    def add_view(self, name: str, view_class):
        """Cria e armazena uma instância de uma view (tela)."""
        frame = view_class(self.container, self)
        self.views[name] = frame
        # O frame não é empacotado aqui, apenas criado.
        # `switch_view` cuidará de qual frame é visível.
        frame.grid(row=0, column=0, sticky="nsew")


    def switch_view(self, name: str):
        """Traz a view especificada para o topo e atualiza se necessário."""
        view = self.views.get(name)
        if view:
            # Lógica específica de atualização para cada view
            if hasattr(view, 'set_player') and self.jogador_atual:
                view.set_player(self.jogador_atual)
            elif name == "combate" and self.combat_manager:
                if hasattr(view, 'update_ui'):
                    view.update_ui()

            view.tkraise()
            self.title(f"Ecos da Aetheria - {name.replace('_', ' ').capitalize()}")
        else:
            print(f"Erro: View '{name}' não encontrada.")

    def start_new_game(self, character_data):
        """
        Cria a instância do personagem, calcula seus atributos finais e
        transiciona para a tela da cidade.
        """
        try:
            nome_personagem = character_data["nome"]
            race_key = character_data["raca_key"]
            class_name = character_data["classe_nome"]
            player_points = character_data["player_points"]

            dados_raca = RACAS_DATA[race_key]
            dados_classe = next((c for c in CLASSES_INICIAIS if c["nome"] == class_name), None)

            if not dados_classe:
                print(f"Erro Crítico: Classe '{class_name}' não encontrada.")
                return

            self.jogador_atual = Personagem(
                id_entidade=f"player_{nome_personagem.lower()}",
                nome=nome_personagem,
                dados_raca=dados_raca,
                dados_classe=dados_classe
            )

            final_attributes = {}
            racial_bonuses = dados_raca.get("bonus", {})
            ATTRIBUTE_NAMES = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma", "sorte"]

            for attr in ATTRIBUTE_NAMES:
                final_attributes[attr] = 5 + racial_bonuses.get(attr, 0) + player_points.get(attr, 0)

            self.jogador_atual.atributos = final_attributes
            self.jogador_atual.hp_max = final_attributes["constituicao"] * 10
            self.jogador_atual.hp_atual = self.jogador_atual.hp_max

            print(f"Novo Jogo Iniciado! Personagem criado: {self.jogador_atual}")
            print(f"Atributos Finais: {self.jogador_atual.atributos}")

            # Adiciona itens iniciais para teste
            self.jogador_atual.adicionar_item(INDICE_ITENS_COMPLETO["pocao_cura_fraca"])
            self.jogador_atual.adicionar_item(INDICE_ITENS_COMPLETO["pocao_cura_fraca"])

            self.switch_view("cidade")

        except Exception as e:
            print(f"Ocorreu um erro ao criar o personagem: {e}")

    def start_combat(self):
        """Inicia um novo combate com um monstro aleatório."""
        if not self.jogador_atual:
            print("ERRO: Tentativa de iniciar combate sem um jogador criado.")
            return

        dados_monstro = random.choice(MONSTROS_REGIAO_INICIAL)
        monstro = Monstro(dados_monstro)

        self.combat_manager = CombatManager(
            grupo_jogador=[self.jogador_atual],
            grupo_inimigos=[monstro]
        )

        self.switch_view("combate")

        # Processa os turnos até ser a vez do jogador
        self.combat_manager.processar_proximo_turno()
        self._update_combat_ui()

    def player_attack(self):
        """Executa a ação de ataque do jogador."""
        if not self.combat_manager or self.combat_manager.estado_combate != "em_andamento":
            return

        monster = self.combat_manager.grupo_inimigos[0]
        action = {"habilidade_id": "ataque_basico", "alvo_id": monster.id_entidade}

        self.combat_manager.executar_acao_jogador(self.jogador_atual, action)

        self._update_combat_ui()
        self._check_combat_end()

    def _update_combat_ui(self):
        """Pede para a view de combate se atualizar com os dados mais recentes."""
        combate_view = self.views.get("combate")
        if combate_view and self.combat_manager:
            combate_view.update_ui(self.combat_manager.log_combate)
            self.combat_manager.log_combate = [] # Limpa o log para não repetir mensagens

    def _check_combat_end(self):
        """Verifica se o combate terminou e lida com o resultado."""
        estado = self.combat_manager.estado_combate
        if estado != "em_andamento":
            if estado == "vitoria_jogador":
                messagebox.showinfo("Vitória!", "Você venceu o combate!")
                # Lógica de XP e Loot viria aqui
            else: # derrota_jogador
                messagebox.showerror("Derrota!", "Você foi derrotado!")
                # Lógica de penalidade viria aqui

            self.switch_view("cidade")
            self.combat_manager = None # Limpa o combate

    def open_skill_selection(self):
        """Abre uma nova janela para o jogador selecionar uma habilidade."""
        if not self.combat_manager or not self.jogador_atual:
            return

        skill_window = tk.Toplevel(self)
        skill_window.title("Escolha uma Habilidade")
        skill_window.geometry("300x400")
        skill_window.transient(self)
        skill_window.grab_set()

        for skill_id in self.jogador_atual.habilidades_conhecidas:
            skill_data = GRIMORIO_COMPLETO.get(skill_id)
            if skill_data and skill_data.get("tipo") == "ativa":
                btn = ttk.Button(
                    skill_window,
                    text=skill_data.get("nome", "Habilidade Desconhecida"),
                    command=lambda s_id=skill_id, s_win=skill_window: self.player_use_skill(s_id, s_win)
                )
                btn.pack(pady=5, padx=10, fill="x")

    def player_use_skill(self, skill_id, skill_window):
        """Executa a ação de usar uma habilidade específica."""
        if not self.combat_manager or self.combat_manager.estado_combate != "em_andamento":
            return

        skill_window.destroy() # Fecha a janela de habilidades

        monster = self.combat_manager.grupo_inimigos[0]
        action = {"habilidade_id": skill_id, "alvo_id": monster.id_entidade}

        self.combat_manager.executar_acao_jogador(self.jogador_atual, action)

        self._update_combat_ui()
        self._check_combat_end()

    def open_item_selection(self):
        """Abre uma nova janela para o jogador selecionar um item."""
        if not self.combat_manager or not self.jogador_atual:
            return

        item_window = tk.Toplevel(self)
        item_window.title("Escolha um Item")
        item_window.geometry("300x400")
        item_window.transient(self)
        item_window.grab_set()

        # Agrupa itens para contagem
        item_counts = {}
        for item in self.jogador_atual.inventario:
            item_id = item.get("id")
            if item_id:
                item_counts[item_id] = item_counts.get(item_id, 0) + 1

        for item_id, count in item_counts.items():
            item_data = INDICE_ITENS_COMPLETO.get(item_id)
            if item_data and item_data.get("tipo") == "consumivel":
                btn_text = f"{item_data.get('nome')} (x{count})"
                btn = ttk.Button(
                    item_window,
                    text=btn_text,
                    command=lambda i_id=item_id, i_win=item_window: self.player_use_item(i_id, i_win)
                )
                btn.pack(pady=5, padx=10, fill="x")

    def player_use_item(self, item_id, item_window):
        """Executa a ação de usar um item."""
        if not self.combat_manager or self.combat_manager.estado_combate != "em_andamento":
            return

        item_window.destroy()

        item_data = INDICE_ITENS_COMPLETO.get(item_id)
        if not item_data:
            print(f"Erro: Item {item_id} não encontrado no índice.")
            return

        # Lógica de efeito do item
        effect = item_data.get("efeito", {})
        if effect.get("tipo") == "cura":
            cura_valor_str = effect.get("valor", "0")
            cura_total = rolar_dados(cura_valor_str)
            log_messages = self.jogador_atual.receber_cura(cura_total)
            self.combat_manager.log_combate.extend(log_messages)
        else:
            self.combat_manager.log_combate.append(f"{self.jogador_atual.nome} usa {item_data.get('nome')}, mas nada acontece.")

        # Remove o item do inventário
        self.jogador_atual.remover_item(item_id)

        self.combat_manager.turno_atual += 1
        self.combat_manager.processar_proximo_turno()
        self._update_combat_ui()
        self._check_combat_end()

    def player_flee(self):
        """Tenta fugir do combate."""
        if not self.combat_manager or self.combat_manager.estado_combate != "em_andamento":
            return

        player_dex = self.jogador_atual.atributos.get("destreza", 10)
        monster_dex = self.combat_manager.grupo_inimigos[0].atributos.get("destreza", 10)

        # Fórmula de chance de fuga
        chance = max(0.1, min(0.9, 0.5 + (player_dex - monster_dex) * 0.05))

        if random.random() < chance:
            self.combat_manager.log_combate.append(f"{self.jogador_atual.nome} consegue fugir do combate!")
            self._update_combat_ui()
            messagebox.showinfo("Fuga", "Você escapou com sucesso!")
            self.switch_view("cidade")
            self.combat_manager = None
        else:
            self.combat_manager.log_combate.append(f"{self.jogador_atual.nome} tenta fugir, mas falha!")
            # Perde o turno
            self.combat_manager.turno_atual += 1
            self.combat_manager.processar_proximo_turno()
            self._update_combat_ui()
            self._check_combat_end()

    def player_buy_item(self, item_id):
        """Lógica para o jogador comprar um item."""
        if not self.jogador_atual: return

        item_data = INDICE_ITENS_COMPLETO.get(item_id)
        if not item_data: return

        preco = item_data.get("preco_base", 0)
        if self.jogador_atual.dinheiro >= preco:
            self.jogador_atual.dinheiro -= preco
            self.jogador_atual.adicionar_item(item_data)
            self.views["loja"].update_ui()
            print(f"{self.jogador_atual.nome} comprou {item_data.get('nome')}.")
        else:
            messagebox.showwarning("Dinheiro Insuficiente", "Você não tem dinheiro suficiente para comprar este item.")

    def player_sell_item(self, item_id):
        """Lógica para o jogador vender um item."""
        if not self.jogador_atual: return

        item_data = INDICE_ITENS_COMPLETO.get(item_id)
        if not item_data: return

        # Vende pela metade do preço base
        preco_venda = item_data.get("preco_base", 0) // 2

        if self.jogador_atual.remover_item(item_id):
            self.jogador_atual.dinheiro += preco_venda
            self.views["loja"].update_ui()
            print(f"{self.jogador_atual.nome} vendeu {item_data.get('nome')}.")
        else:
            print(f"ERRO: Tentativa de vender o item {item_id} que o jogador não possui.")

    def rest_at_tavern(self):
        """Lógica para descansar na taverna."""
        if not self.jogador_atual: return

        cost = 10
        if self.jogador_atual.dinheiro >= cost:
            self.jogador_atual.dinheiro -= cost
            self.jogador_atual.hp_atual = self.jogador_atual.hp_max
            self.jogador_atual.mana_atual = self.jogador_atual.mana_max
            messagebox.showinfo("Descanso", f"Você paga {cost}g e descansa. Suas energias foram restauradas!")
        else:
            messagebox.showwarning("Dinheiro Insuficiente", "Você não tem dinheiro suficiente para descansar.")

    def talk_to_bartender(self):
        """Lógica para conversar com o taverneiro."""
        messagebox.showinfo("Taverneiro", "O taverneiro limpa um copo e diz: 'Tenha cuidado nas planícies. Ouvi dizer que um Lobo Alfa tem sido visto por lá.'")

    def save_game(self):
        """Pede um slot e salva o jogo."""
        if not self.jogador_atual:
            messagebox.showwarning("Aviso", "Não há jogo em andamento para salvar.")
            return

        slot = simpledialog.askinteger("Salvar Jogo", "Digite o número do slot para salvar (1-10):", minvalue=1, maxvalue=10)
        if slot:
            # Criamos o objeto de estado do jogo para salvar
            estado_jogo = EstadoJogo(
                personagem=self.jogador_atual,
                estado_mundo={}, # Placeholder
                metadata={
                    "timestamp": datetime.now(),
                    "nome_personagem": self.jogador_atual.nome,
                    "nivel": self.jogador_atual.nivel
                }
            )
            if self.save_manager.salvar_jogo(estado_jogo, slot):
                messagebox.showinfo("Sucesso", f"Jogo salvo com sucesso no slot {slot}!")
            else:
                messagebox.showerror("Erro", "Ocorreu um erro ao salvar o jogo.")

    def load_game(self, slot):
        """Carrega um jogo de um slot específico."""
        estado_carregado = self.save_manager.carregar_jogo(slot)
        if estado_carregado:
            self.jogador_atual = estado_carregado.personagem
            # Restaurar outros estados do mundo aqui
            messagebox.showinfo("Sucesso", f"Jogo do slot {slot} carregado!")
            self.switch_view("cidade")
        else:
            messagebox.showerror("Erro", f"Não foi possível carregar o jogo do slot {slot}.")

    def delete_save(self, slot):
        """Apaga um arquivo de save."""
        if messagebox.askyesno("Confirmar", f"Você tem certeza que quer apagar o save do slot {slot}?"):
            if self.save_manager.apagar_save(slot):
                messagebox.showinfo("Sucesso", f"Save do slot {slot} apagado.")
                self.views["carregar_jogo"].update_save_list()
            else:
                messagebox.showerror("Erro", f"Não foi possível apagar o save do slot {slot}.")

    def start(self):
        """Inicia o loop principal da aplicação."""
        self.mainloop()

# Bloco para testar a janela de forma isolada
if __name__ == "__main__":
    app = MainWindow()
    app.start()
