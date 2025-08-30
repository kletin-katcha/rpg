# -*- coding: utf-8 -*-
"""
================================================================================================
GUI: VIEW - CIDADE
================================================================================================
Este arquivo define a classe CidadeView, a tela principal de uma cidade.
"""

import tkinter as tk
from tkinter import ttk

class CidadeView(ttk.Frame):
    """
    A tela (view) que representa uma cidade ou hub central.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.player = None

        # --- Layout ---
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # --- Widgets ---
        self.lbl_welcome = ttk.Label(self, text="", font=("Trajan Pro", 24, "bold"), anchor="center")
        self.lbl_welcome.grid(row=0, column=0, pady=20, sticky="s")

        button_frame = ttk.Frame(self)
        button_frame.grid(row=1, column=0)

        # Botões de Ação
        btn_taverna = ttk.Button(button_frame, text="Ir para a Taverna", command=lambda: controller.switch_view("taverna"), width=25)
        btn_taverna.pack(pady=10)

        btn_loja = ttk.Button(button_frame, text="Visitar a Loja", command=lambda: controller.switch_view("loja"), width=25)
        btn_loja.pack(pady=10)

        btn_explorar = ttk.Button(button_frame, text="Explorar Arredores", command=lambda: controller.switch_view("exploracao"), width=25)
        btn_explorar.pack(pady=10)

        btn_personagem = ttk.Button(button_frame, text="Ver Personagem", command=lambda: controller.switch_view("personagem"), width=25)
        btn_personagem.pack(pady=10)

        btn_salvar = ttk.Button(button_frame, text="Salvar Jogo", command=controller.save_game, width=25)
        btn_salvar.pack(pady=10)

        btn_sair = ttk.Button(button_frame, text="Sair do Jogo", command=self.controller.destroy, width=25)
        btn_sair.pack(pady=(30, 10))

    def set_player(self, player):
        """
        Define o jogador para esta view e atualiza os elementos da UI.
        Este método é chamado pelo controller ao trocar para esta view.
        """
        self.player = player
        # Assumindo que o jogador tem um atributo 'localizacao_atual'
        cidade_nome = self.player.localizacao_atual.replace('_', ' ').title()
        self.lbl_welcome.config(text=f"Bem-vindo a {cidade_nome}, {self.player.nome}!")
