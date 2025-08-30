# -*- coding: utf-8 -*-
"""
================================================================================================
GUI: VIEW - TAVERNA
================================================================================================
Este arquivo define a classe TavernaView, a tela para interação com a taverna.
"""

import tkinter as tk
from tkinter import ttk

class TavernaView(ttk.Frame):
    """
    A tela (view) que representa a taverna local.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # --- Layout ---
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # --- Widgets ---
        lbl_title = ttk.Label(self, text="A Lareira Aconchegante", font=("Trajan Pro", 24, "bold"))
        lbl_title.grid(row=0, column=0, pady=20, sticky="s")

        button_frame = ttk.Frame(self)
        button_frame.grid(row=1, column=0)

        # Botões de Ação
        btn_rest = ttk.Button(
            button_frame,
            text="Descansar (10g)",
            command=self.controller.rest_at_tavern,
            width=30
        )
        btn_rest.pack(pady=10)

        btn_talk = ttk.Button(
            button_frame,
            text="Conversar com o Taverneiro",
            command=self.controller.talk_to_bartender,
            width=30
        )
        btn_talk.pack(pady=10)

        btn_back = ttk.Button(
            self,
            text="Sair da Taverna",
            command=lambda: controller.switch_view("cidade"),
            width=30
        )
        btn_back.grid(row=2, column=0, pady=20, sticky="n")
