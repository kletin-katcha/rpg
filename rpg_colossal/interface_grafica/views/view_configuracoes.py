# -*- coding: utf-8 -*-
"""
================================================================================================
GUI: VIEW - CONFIGURAÇÕES
================================================================================================
Este arquivo define a classe ConfiguracoesView, que é a tela de configurações do jogo.
"""

import tkinter as tk
from tkinter import ttk
from rpg_colossal.motor_jogo.utilitarios.gerenciador_config import load_settings, save_settings

class ConfiguracoesView(ttk.Frame):
    """
    A tela (view) que exibe as opções de configuração do jogo.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # --- Carregar Configurações ---
        self.settings = load_settings()

        # --- Variáveis de Controle ---
        # Estas variáveis podem ser usadas para obter/definir os valores das configurações
        self.font_size = tk.IntVar(value=self.settings.get("font_size", 12))
        self.difficulty = tk.StringVar(value=self.settings.get("difficulty", "Normal"))

        # --- Layout e Estilo ---
        # Centraliza o conteúdo principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # --- Frame Principal para Conteúdo ---
        # Usar um frame interno ajuda a organizar e agrupar os widgets
        main_frame = ttk.Frame(self)
        main_frame.grid(row=1, column=0, sticky="nsew")
        main_frame.grid_columnconfigure(1, weight=1) # Faz a segunda coluna (widgets) expandir

        # Título
        lbl_title = ttk.Label(main_frame, text="Configurações", font=("Trajan Pro", 24, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, 40))

        # Opção: Tamanho da Fonte
        lbl_font_size = ttk.Label(main_frame, text="Tamanho da Fonte:", font=("Arial", 14))
        lbl_font_size.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="w")

        scale_font_size = ttk.Scale(
            main_frame,
            from_=8,
            to=24,
            orient="horizontal",
            variable=self.font_size,
            length=300
        )
        scale_font_size.grid(row=1, column=1, padx=(0, 20), pady=10, sticky="ew")

        # Opção: Dificuldade
        lbl_difficulty = ttk.Label(main_frame, text="Dificuldade:", font=("Arial", 14))
        lbl_difficulty.grid(row=2, column=0, padx=(20, 10), pady=20, sticky="w")

        difficulty_frame = ttk.Frame(main_frame)
        difficulty_frame.grid(row=2, column=1, padx=(0, 20), pady=20, sticky="ew")
        difficulty_frame.grid_columnconfigure((0, 1, 2), weight=1) # Distribui o espaço

        rb_facil = ttk.Radiobutton(difficulty_frame, text="Fácil", variable=self.difficulty, value="Fácil")
        rb_normal = ttk.Radiobutton(difficulty_frame, text="Normal", variable=self.difficulty, value="Normal")
        rb_dificil = ttk.Radiobutton(difficulty_frame, text="Difícil", variable=self.difficulty, value="Difícil")

        rb_facil.grid(row=0, column=0, sticky="ew")
        rb_normal.grid(row=0, column=1, sticky="ew")
        rb_dificil.grid(row=0, column=2, sticky="ew")

        # Botão Salvar e Voltar
        btn_save_back = ttk.Button(
            self,
            text="Salvar e Voltar",
            command=self.save_and_go_back,
            width=20
        )
        btn_save_back.grid(row=3, column=0, pady=(20, 0))

    def save_and_go_back(self):
        """Salva as configurações atuais e volta para o menu principal."""
        current_settings = {
            "font_size": self.font_size.get(),
            "difficulty": self.difficulty.get(),
        }
        save_settings(current_settings)

        # Opcional: notificar o controller para aplicar as mudanças
        if hasattr(self.controller, "apply_settings"):
            self.controller.apply_settings()

        self.controller.switch_view("menu_principal")
