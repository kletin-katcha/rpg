# -*- coding: utf-8 -*-
"""
================================================================================================
GUI: VIEW - PERSONAGEM
================================================================================================
Este arquivo define a classe PersonagemView, a tela para exibir os detalhes do personagem.
"""

import tkinter as tk
from tkinter import ttk

class PersonagemView(ttk.Frame):
    """
    A tela (view) que exibe os detalhes do personagem do jogador.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.player = None

        # --- Layout Principal ---
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=1)

        # --- Header com informações básicas ---
        header_frame = ttk.Frame(self)
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        self.lbl_name = ttk.Label(header_frame, text="Nome do Personagem", font=("Trajan Pro", 20, "bold"))
        self.lbl_name.pack(side="left")
        self.lbl_level = ttk.Label(header_frame, text="Nível 1", font=("Arial", 14))
        self.lbl_level.pack(side="left", padx=20)
        self.lbl_race_class = ttk.Label(header_frame, text="Humano Guerreiro", font=("Arial", 14, "italic"))
        self.lbl_race_class.pack(side="left")

        # --- Coluna da Esquerda: Atributos e Equipamento ---
        left_column = ttk.Frame(self)
        left_column.grid(row=1, column=0, sticky="nsew", padx=10)
        left_column.grid_rowconfigure(1, weight=1)

        # Atributos
        attr_frame = ttk.LabelFrame(left_column, text="Atributos")
        attr_frame.pack(fill="x", pady=5)
        self.attr_labels = {}
        for i, attr in enumerate(["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma", "sorte"]):
            ttk.Label(attr_frame, text=f"{attr.capitalize()}:").grid(row=i, column=0, sticky="w", padx=5, pady=2)
            self.attr_labels[attr] = ttk.Label(attr_frame, text="0")
            self.attr_labels[attr].grid(row=i, column=1, sticky="e", padx=5, pady=2)

        # Equipamento
        equip_frame = ttk.LabelFrame(left_column, text="Equipamento")
        equip_frame.pack(fill="both", expand=True, pady=5)
        self.equip_labels = {}
        slots = ["mao_principal", "mao_secundaria", "cabeca", "peito", "pernas", "pes", "amuleto", "anel_1", "anel_2"]
        for i, slot in enumerate(slots):
            display_name = slot.replace('_', ' ').title()
            ttk.Label(equip_frame, text=f"{display_name}:").grid(row=i, column=0, sticky="w", padx=5, pady=2)
            self.equip_labels[slot] = ttk.Label(equip_frame, text="Nenhum")
            self.equip_labels[slot].grid(row=i, column=1, sticky="w", padx=5, pady=2)

        # --- Coluna da Direita: Inventário ---
        inventory_frame = ttk.LabelFrame(self, text="Inventário")
        inventory_frame.grid(row=1, column=1, sticky="nsew", padx=10)
        inventory_frame.grid_rowconfigure(0, weight=1)
        inventory_frame.grid_columnconfigure(0, weight=1)

        self.inventory_list = tk.Listbox(inventory_frame, bg="#1e1e1e", fg="white", selectbackground="#4a4a4a")
        self.inventory_list.grid(row=0, column=0, sticky="nsew")

        # --- Botão de Voltar ---
        btn_back = ttk.Button(self, text="Voltar para a Cidade", command=lambda: controller.switch_view("cidade"))
        btn_back.grid(row=2, column=0, columnspan=2, pady=10)

    def set_player(self, player):
        """Define o jogador e atualiza a UI com seus dados."""
        self.player = player
        if not self.player:
            return

        # Atualiza Header
        self.lbl_name.config(text=self.player.nome)
        self.lbl_level.config(text=f"Nível {self.player.nivel}")
        self.lbl_race_class.config(text=f"{self.player.raca.get('nome')} {self.player.classe.get('nome')}")

        # Atualiza Atributos
        for attr, label in self.attr_labels.items():
            label.config(text=str(self.player.atributos.get(attr, 0)))

        # Atualiza Equipamento
        for slot, label in self.equip_labels.items():
            equip_item = self.player.equipamento.get(slot)
            label.config(text=equip_item.get("nome") if equip_item else "Nenhum")

        # Atualiza Inventário
        self.inventory_list.delete(0, tk.END)
        item_counts = {}
        for item in self.player.inventario:
            item_name = item.get("nome", "Item Desconhecido")
            item_counts[item_name] = item_counts.get(item_name, 0) + 1

        for name, count in item_counts.items():
            self.inventory_list.insert(tk.END, f"{name} (x{count})")
