# -*- coding: utf-8 -*-
"""
================================================================================================
GUI: VIEW - MENU PRINCIPAL
================================================================================================
Este arquivo define a classe `MenuPrincipalView`, que é a tela do menu principal.
"""

import tkinter as tk
from tkinter import ttk

class MenuPrincipalView(ttk.Frame):
    """
    A tela (view) que exibe as opções do menu principal.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # --- Layout e Estilo ---
        # Configura o grid para centralizar os elementos
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(6, weight=1) # Aumenta para 6 para novo botão
        self.grid_columnconfigure(0, weight=1)

        # --- Widgets ---
        # Título do Jogo
        lbl_title = ttk.Label(
            self,
            text="Ecos da Aetheria",
            font=("Trajan Pro", 36, "bold")
        )
        lbl_title.grid(row=0, column=0, pady=(20, 40))

        # Botão Novo Jogo
        btn_novo_jogo = ttk.Button(
            self,
            text="Novo Jogo",
            command=lambda: controller.switch_view("criacao_personagem"),
            width=20
        )
        btn_novo_jogo.grid(row=1, column=0, pady=10)

        # Botão Carregar Jogo
        btn_carregar_jogo = ttk.Button(
            self,
            text="Carregar Jogo",
            command=lambda: controller.switch_view("carregar_jogo"),
            width=20
        )
        btn_carregar_jogo.grid(row=2, column=0, pady=10)

        # Botão Configurações
        btn_config = ttk.Button(
            self,
            text="Configurações",
            command=lambda: controller.switch_view("configuracoes"),
            width=20
        )
        btn_config.grid(row=3, column=0, pady=10)

        # Botão Créditos
        btn_creditos = ttk.Button(
            self,
            text="Créditos",
            command=lambda: controller.switch_view("creditos"),
            width=20
        )
        btn_creditos.grid(row=4, column=0, pady=10)

        # Botão Sair
        btn_sair = ttk.Button(
            self,
            text="Sair",
            command=self.controller.destroy, # Fecha a janela principal
            width=20
        )
        btn_sair.grid(row=5, column=0, pady=10)
