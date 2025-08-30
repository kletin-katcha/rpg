# -*- coding: utf-8 -*-
"""
================================================================================================
GUI: VIEW - COMBATE
================================================================================================
Este arquivo define a classe CombateView, a tela para o combate em turnos.
"""

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class CombateView(ttk.Frame):
    """
    A tela (view) que representa o combate entre o jogador e um monstro.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.player = None
        self.monster = None

        # --- Layout Principal ---
        self.grid_rowconfigure(0, weight=2)  # Área de status das entidades
        self.grid_rowconfigure(1, weight=3)  # Log de combate
        self.grid_rowconfigure(2, weight=1)  # Área de ações do jogador
        self.grid_columnconfigure(0, weight=1)

        self._setup_status_display()
        self._setup_combat_log()
        self._setup_action_buttons()

    def _setup_status_display(self):
        """Cria os frames para exibir o status do jogador e do monstro."""
        status_frame = ttk.Frame(self)
        status_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        status_frame.grid_columnconfigure(0, weight=1)
        status_frame.grid_columnconfigure(1, weight=1)
        status_frame.grid_rowconfigure(0, weight=1)

        # --- Painel do Jogador (Esquerda) ---
        player_panel = ttk.LabelFrame(status_frame, text="Jogador")
        player_panel.grid(row=0, column=0, sticky="nsew", padx=5)
        self.lbl_player_name = ttk.Label(player_panel, text="Player Name", font=("Arial", 16, "bold"))
        self.lbl_player_name.pack(pady=5)
        self.lbl_player_hp = ttk.Label(player_panel, text="HP: 100/100", font=("Arial", 12))
        self.lbl_player_hp.pack(pady=5)
        self.prog_player_hp = ttk.Progressbar(player_panel, orient="horizontal", length=200, mode="determinate")
        self.prog_player_hp.pack(pady=5, padx=10)

        # --- Painel do Monstro (Direita) ---
        monster_panel = ttk.LabelFrame(status_frame, text="Monstro")
        monster_panel.grid(row=0, column=1, sticky="nsew", padx=5)
        self.lbl_monster_name = ttk.Label(monster_panel, text="Monster Name", font=("Arial", 16, "bold"))
        self.lbl_monster_name.pack(pady=5)
        self.lbl_monster_hp = ttk.Label(monster_panel, text="HP: 50/50", font=("Arial", 12))
        self.lbl_monster_hp.pack(pady=5)
        self.prog_monster_hp = ttk.Progressbar(monster_panel, orient="horizontal", length=200, mode="determinate")
        self.prog_monster_hp.pack(pady=5, padx=10)

    def _setup_combat_log(self):
        """Cria a área de log de combate."""
        log_frame = ttk.LabelFrame(self, text="Log de Combate")
        log_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        log_frame.grid_rowconfigure(0, weight=1)
        log_frame.grid_columnconfigure(0, weight=1)

        self.log_text = ScrolledText(log_frame, state="disabled", wrap=tk.WORD, font=("Arial", 10), bg="#1e1e1e", fg="white")
        self.log_text.grid(row=0, column=0, sticky="nsew")

    def _setup_action_buttons(self):
        """Cria os botões de ação do jogador."""
        actions_frame = ttk.Frame(self)
        actions_frame.grid(row=2, column=0, pady=10)

        self.btn_atacar = ttk.Button(actions_frame, text="Atacar", width=15, command=self.controller.player_attack)
        self.btn_atacar.pack(side="left", padx=5)

        self.btn_habilidades = ttk.Button(actions_frame, text="Habilidades", width=15, command=self.controller.open_skill_selection)
        self.btn_habilidades.pack(side="left", padx=5)

        self.btn_itens = ttk.Button(actions_frame, text="Itens", width=15, command=self.controller.open_item_selection)
        self.btn_itens.pack(side="left", padx=5)

        self.btn_fugir = ttk.Button(actions_frame, text="Fugir", width=15, command=self.controller.player_flee)
        self.btn_fugir.pack(side="left", padx=5)

    def set_combatants(self, player, monster):
        """Define o jogador e o monstro para o combate e limpa o log."""
        self.player = player
        self.monster = monster
        self.log_text.config(state="normal")
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state="disabled")
        self.add_log_message(f"--- {self.player.nome} encontra um {self.monster.nome}! ---")
        self.update_ui()

    def add_log_message(self, message):
        """Adiciona uma mensagem ao log de combate."""
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.config(state="disabled")
        self.log_text.see(tk.END) # Auto-scroll

    def update_ui(self, log_messages=None):
        """Atualiza todos os elementos da UI com os dados atuais."""
        if log_messages:
            for msg in log_messages:
                self.add_log_message(msg)

        if self.player:
            self.lbl_player_name.config(text=self.player.nome)
            hp_text = f"HP: {self.player.hp_atual}/{self.player.hp_max}"
            self.lbl_player_hp.config(text=hp_text)
            self.prog_player_hp['value'] = self.player.hp_atual
            self.prog_player_hp['maximum'] = self.player.hp_max

        if self.monster:
            self.lbl_monster_name.config(text=self.monster.nome)
            hp_text = f"HP: {self.monster.hp_atual}/{self.monster.hp_max}"
            self.lbl_monster_hp.config(text=hp_text)
            self.prog_monster_hp['value'] = self.monster.hp_atual
            self.prog_monster_hp['maximum'] = self.monster.hp_max

        # Força a atualização dos widgets da UI
        self.update_idletasks()
