# -*- coding: utf-8 -*-
"""
================================================================================================
GUI: VIEW - CRÉDITOS
================================================================================================
Este arquivo define a classe CreditosView, que é a tela de créditos do jogo.
"""

import tkinter as tk
from tkinter import ttk

class CreditosView(ttk.Frame):
    """
    A tela (view) que exibe os créditos do jogo.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # --- Layout e Estilo ---
        # Configura o grid para centralizar os elementos
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1) # Ajustado para 3 para dar espaço ao botão
        self.grid_columnconfigure(0, weight=1)

        # --- Widgets ---
        # Título da Tela
        lbl_title = ttk.Label(
            self,
            text="Créditos",
            font=("Trajan Pro", 24, "bold")
        )
        lbl_title.grid(row=0, column=0, pady=(20, 20), sticky="s")

        # Texto de Créditos
        credits_text = """
        Ecos da Aetheria

        Um projeto de RPG Colossal em Python.

        Desenvolvido com a assistência de IA.
        Interface Gráfica: Tkinter

        Agradecimentos Especiais:
        A todos os aventureiros que ousam explorar este mundo.
        """
        lbl_credits = ttk.Label(
            self,
            text=credits_text,
            style="Narration.TLabel", # Usa o novo estilo customizável
            justify="center"
        )
        lbl_credits.grid(row=1, column=0, pady=20)

        # Botão Voltar
        btn_voltar = ttk.Button(
            self,
            text="Voltar",
            command=lambda: controller.switch_view("menu_principal"),
            width=20
        )
        btn_voltar.grid(row=2, column=0, pady=(20, 20), sticky="n")
