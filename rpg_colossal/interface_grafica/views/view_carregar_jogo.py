# -*- coding: utf-8 -*-
"""
================================================================================================
GUI: VIEW - CARREGAR JOGO
================================================================================================
Este arquivo define a classe CarregarJogoView, a tela para carregar um jogo salvo.
"""

import tkinter as tk
from tkinter import ttk

class CarregarJogoView(ttk.Frame):
    """
    A tela (view) para listar, carregar e apagar jogos salvos.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # --- Layout ---
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # --- Header ---
        ttk.Label(self, text="Carregar Jogo Salvo", font=("Trajan Pro", 24, "bold")).grid(row=0, column=0, pady=20)

        # --- Frame para a lista de saves ---
        self.saves_frame = ttk.Frame(self)
        self.saves_frame.grid(row=1, column=0, sticky="nsew", padx=20)

        # --- Botão de Voltar ---
        btn_back = ttk.Button(self, text="Voltar ao Menu", command=lambda: controller.switch_view("menu_principal"))
        btn_back.grid(row=2, column=0, pady=20)

    def set_player(self, player):
        """
        Este método é chamado pelo controller sempre que a view é exibida.
        Usamos isso para atualizar a lista de saves.
        """
        self.update_save_list()

    def update_save_list(self):
        """Busca os saves existentes e popula a UI."""
        # Limpa a lista antiga
        for widget in self.saves_frame.winfo_children():
            widget.destroy()

        # Acessa o gerenciador de saves através do controller
        if hasattr(self.controller, "save_manager"):
            save_files = self.controller.save_manager.listar_saves()

            if not save_files:
                ttk.Label(self.saves_frame, text="Nenhum jogo salvo encontrado.").pack()
                return

            for i, save_data in enumerate(save_files):
                slot = save_data.get('slot', '??')
                char_name = save_data.get('nome_personagem', 'Desconhecido')
                level = save_data.get('nivel', '??')
                timestamp = save_data.get('timestamp', '????-??-??')

                save_entry_frame = ttk.LabelFrame(self.saves_frame, text=f"Slot {slot}")
                save_entry_frame.pack(fill="x", padx=10, pady=5, expand=True)

                info_text = f"{char_name} - Nível {level}\nSalvo em: {timestamp}"
                ttk.Label(save_entry_frame, text=info_text).pack(side="left", padx=10, pady=5)

                # Botões de Ação para cada save
                btn_delete = ttk.Button(
                    save_entry_frame, text="Apagar",
                    command=lambda s=slot: self.controller.delete_save(s)
                )
                btn_delete.pack(side="right", padx=5)

                btn_load = ttk.Button(
                    save_entry_frame, text="Carregar",
                    command=lambda s=slot: self.controller.load_game(s)
                )
                btn_load.pack(side="right", padx=5)
        else:
            ttk.Label(self.saves_frame, text="Erro: Gerenciador de saves não encontrado.").pack()
