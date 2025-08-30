# -*- coding: utf-8 -*-
"""
================================================================================================
GUI: VIEW - EXPLORAÇÃO
================================================================================================
Este arquivo define a classe ExploracaoView, a tela para explorar áreas selvagens.
"""

import tkinter as tk
from tkinter import ttk

class ExploracaoView(ttk.Frame):
    """
    A tela (view) que representa a exploração de uma área.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # --- Layout ---
        self.grid_rowconfigure(0, weight=3)  # Área de narração
        self.grid_rowconfigure(1, weight=1)  # Área de botões
        self.grid_columnconfigure(0, weight=1)

        # --- Widgets ---
        # Narração
        self.lbl_narration = ttk.Label(
            self,
            text="Você está nos arredores da cidade. O que você faz?",
            style="Narration.TLabel",
            wraplength=800
        )
        self.lbl_narration.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        # Frame de botões
        button_frame = ttk.Frame(self)
        button_frame.grid(row=1, column=0, pady=20)

        # Botões de Ação
        self.btn_find_trouble = ttk.Button(
            button_frame,
            text="Procurar Encrenca",
            command=lambda: self.controller.start_combat(), # A ser implementado no controller
            width=25
        )
        self.btn_find_trouble.pack(side="left", padx=10)

        self.btn_return_city = ttk.Button(
            button_frame,
            text="Voltar para a Cidade",
            command=lambda: self.controller.switch_view("cidade"),
            width=25
        )
        self.btn_return_city.pack(side="left", padx=10)
