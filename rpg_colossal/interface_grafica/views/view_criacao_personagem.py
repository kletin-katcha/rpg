# -*- coding: utf-8 -*-
"""
================================================================================================
GUI: VIEW - CRIAÇÃO DE PERSONAGEM (v2)
================================================================================================
Este arquivo define a classe CriacaoPersonagemView, a tela para criar um novo personagem,
seguindo a nova lógica de atributos (5 + bônus racial + 20 pontos).
"""

import tkinter as tk
from tkinter import ttk
from rpg_colossal.motor_jogo.banco_de_dados.racas.racas_base import RACAS_DATA
from rpg_colossal.motor_jogo.banco_de_dados.classes.classes_iniciais import CLASSES_INICIAIS
from rpg_colossal.motor_jogo.entidades.personagem import Personagem

class CriacaoPersonagemView(ttk.Frame):
    """
    A tela (view) para a criação de um novo personagem (v2).
    """
    BASE_ATTRIBUTE_VALUE = 5
    BONUS_POINTS_POOL = 20
    ATTRIBUTE_NAMES = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma", "sorte"]

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.races_data = RACAS_DATA
        self.classes_data = {c["nome"]: c for c in CLASSES_INICIAIS}

        # --- Variáveis de Controle ---
        self.char_name = tk.StringVar()
        self.selected_race = tk.StringVar()
        self.selected_class = tk.StringVar()

        self.player_points = {attr: tk.IntVar(value=0) for attr in self.ATTRIBUTE_NAMES}
        self.racial_bonus = {attr: tk.IntVar(value=0) for attr in self.ATTRIBUTE_NAMES}
        self.total_attributes = {attr: tk.IntVar(value=self.BASE_ATTRIBUTE_VALUE) for attr in self.ATTRIBUTE_NAMES}

        self.bonus_points_remaining = tk.IntVar(value=self.BONUS_POINTS_POOL)

        self._setup_widgets()
        self._bind_events()

    def _setup_widgets(self):
        """Cria e posiciona todos os widgets da tela."""
        self.grid_columnconfigure(0, weight=2, uniform="group1")
        self.grid_columnconfigure(1, weight=3, uniform="group1")
        self.grid_rowconfigure(0, weight=1)

        # --- Coluna da Esquerda: Seleção e Atributos ---
        left_frame = ttk.Frame(self)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        ttk.Label(left_frame, text="Criação de Personagem", font=("Trajan Pro", 20, "bold")).pack(fill="x", pady=(0, 20))

        # Nome, Raça, Classe
        entry_frame = ttk.Frame(left_frame)
        entry_frame.pack(fill="x", pady=(0, 10))
        ttk.Label(entry_frame, text="Nome:").grid(row=0, column=0, sticky="w")
        ttk.Entry(entry_frame, textvariable=self.char_name).grid(row=0, column=1, sticky="ew", padx=5)
        ttk.Label(entry_frame, text="Raça:").grid(row=1, column=0, sticky="w", pady=5)
        self.combo_race = ttk.Combobox(entry_frame, textvariable=self.selected_race, state="readonly", values=list(self.races_data.keys()))
        self.combo_race.grid(row=1, column=1, sticky="ew", padx=5)
        ttk.Label(entry_frame, text="Classe:").grid(row=2, column=0, sticky="w")
        self.combo_class = ttk.Combobox(entry_frame, textvariable=self.selected_class, state="readonly", values=list(self.classes_data.keys()))
        self.combo_class.grid(row=2, column=1, sticky="ew", padx=5)
        entry_frame.grid_columnconfigure(1, weight=1)

        # --- Distribuição de Pontos ---
        attr_frame = ttk.LabelFrame(left_frame, text="Atributos (Base + Raça + Bônus)")
        attr_frame.pack(fill="x", expand=True, pady=10)

        ttk.Label(attr_frame, text="Pontos Restantes:").grid(row=0, column=0, columnspan=2, pady=5)
        ttk.Label(attr_frame, textvariable=self.bonus_points_remaining, font=("Arial", 12, "bold")).grid(row=0, column=2, pady=5)

        for i, attr in enumerate(self.ATTRIBUTE_NAMES):
            ttk.Label(attr_frame, text=f"{attr.capitalize()}:").grid(row=i+1, column=0, sticky="w", padx=5)
            ttk.Label(attr_frame, textvariable=self.total_attributes[attr]).grid(row=i+1, column=1, sticky="w", padx=5)
            btn_minus = ttk.Button(attr_frame, text="-", width=3, command=lambda a=attr: self._subtract_point(a))
            btn_minus.grid(row=i+1, column=2)
            btn_plus = ttk.Button(attr_frame, text="+", width=3, command=lambda a=attr: self._add_point(a))
            btn_plus.grid(row=i+1, column=3)

        # --- Coluna da Direita: Descrição ---
        self.lbl_description = ttk.Label(self, text="Selecione uma raça e classe.", style="Narration.TLabel", anchor="nw", padding=(10,10))
        self.lbl_description.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # --- Botões de Ação ---
        button_frame = ttk.Frame(self)
        button_frame.grid(row=1, column=0, columnspan=2, sticky="sew", padx=20, pady=10)
        button_frame.grid_columnconfigure(0, weight=1)
        self.btn_start = ttk.Button(button_frame, text="Iniciar Jogo", state="disabled", command=self._start_game)
        self.btn_start.pack(side="right", padx=10)
        btn_back = ttk.Button(button_frame, text="Voltar", command=lambda: self.controller.switch_view("menu_principal"))
        btn_back.pack(side="right")

    def _start_game(self):
        """Coleta os dados finais e passa para o controller iniciar o jogo."""
        character_data = {
            "nome": self.char_name.get().strip(),
            "raca_key": self.selected_race.get(),
            "classe_nome": self.selected_class.get(),
            "player_points": {attr: var.get() for attr, var in self.player_points.items()}
        }
        self.controller.start_new_game(character_data)

    def _bind_events(self):
        """Associa os eventos aos seus respectivos handlers."""
        self.char_name.trace_add("write", self._update_ui)
        self.combo_race.bind("<<ComboboxSelected>>", self._on_race_select)
        self.combo_class.bind("<<ComboboxSelected>>", self._update_ui)

    def _recalculate_total(self, attr):
        """Recalcula o valor total de um atributo."""
        total = self.BASE_ATTRIBUTE_VALUE + self.racial_bonus[attr].get() + self.player_points[attr].get()
        self.total_attributes[attr].set(total)

    def _add_point(self, attr):
        if self.bonus_points_remaining.get() > 0:
            self.player_points[attr].set(self.player_points[attr].get() + 1)
            self.bonus_points_remaining.set(self.bonus_points_remaining.get() - 1)
            self._recalculate_total(attr)
            self._update_ui()

    def _subtract_point(self, attr):
        if self.player_points[attr].get() > 0:
            self.player_points[attr].set(self.player_points[attr].get() - 1)
            self.bonus_points_remaining.set(self.bonus_points_remaining.get() + 1)
            self._recalculate_total(attr)
            self._update_ui()

    def _on_race_select(self, event=None):
        """Handler para quando uma raça é selecionada."""
        race_key = self.selected_race.get()
        race_info = self.races_data.get(race_key, {})
        bonuses = race_info.get("bonus", {})

        # Reseta os pontos do jogador e o pool de bônus
        self.bonus_points_remaining.set(self.BONUS_POINTS_POOL)
        for attr in self.ATTRIBUTE_NAMES:
            self.player_points[attr].set(0)
            self.racial_bonus[attr].set(bonuses.get(attr, 0))
            self._recalculate_total(attr)

        self._update_ui()

    def _update_ui(self, *args):
        """Atualiza toda a UI com base no estado atual."""
        # Atualiza a descrição
        race_key = self.selected_race.get()
        class_name = self.selected_class.get()

        desc_text = ""
        if race_key:
            desc_text += f"{self.races_data[race_key].get('nome', '')}\n--------------------\n{self.races_data[race_key].get('descricao', '')}\n\n"
        if class_name:
            desc_text += f"{self.classes_data[class_name].get('nome', '')}\n--------------------\n{self.classes_data[class_name].get('descricao_curta', '')}"
        self.lbl_description.config(text=desc_text or "Selecione uma raça e classe.")

        # Atualiza o estado do botão Iniciar
        all_selected = self.char_name.get().strip() and race_key and class_name
        points_spent = self.bonus_points_remaining.get() == 0

        if all_selected and points_spent:
            self.btn_start.config(state="normal")
        else:
            self.btn_start.config(state="disabled")
