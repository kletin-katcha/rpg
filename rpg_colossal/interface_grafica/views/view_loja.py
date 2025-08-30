# -*- coding: utf-8 -*-
"""
================================================================================================
GUI: VIEW - LOJA
================================================================================================
Este arquivo define a classe LojaView, a tela para interação com uma loja.
"""

import tkinter as tk
from tkinter import ttk

class LojaView(ttk.Frame):
    """
    A tela (view) que representa uma loja onde o jogador pode comprar e vender itens.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.player = None
        self.shop_inventory = [ # Inventário da loja (placeholder)
            "pocao_cura_fraca", "pocao_cura_normal", "arma_adaga_ferro"
        ]

        # --- Layout Principal ---
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- Header ---
        header_frame = ttk.Frame(self)
        header_frame.grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(header_frame, text="Loja de Itens", font=("Trajan Pro", 24, "bold")).pack(side="left", padx=20)
        self.lbl_money = ttk.Label(header_frame, text="Dinheiro: 0g", font=("Arial", 14))
        self.lbl_money.pack(side="right", padx=20)

        # --- Painel da Loja (Esquerda) ---
        shop_frame = ttk.LabelFrame(self, text="Itens à Venda")
        shop_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        shop_frame.grid_rowconfigure(0, weight=1)
        shop_frame.grid_columnconfigure(0, weight=1)
        self.shop_list = tk.Listbox(shop_frame, bg="#1e1e1e", fg="white", exportselection=False)
        self.shop_list.grid(row=0, column=0, sticky="nsew")
        self.shop_list.bind("<<ListboxSelect>>", self._on_shop_select)

        # --- Painel do Jogador (Direita) ---
        player_frame = ttk.LabelFrame(self, text="Seu Inventário")
        player_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)
        player_frame.grid_rowconfigure(0, weight=1)
        player_frame.grid_columnconfigure(0, weight=1)
        self.player_list = tk.Listbox(player_frame, bg="#1e1e1e", fg="white", exportselection=False)
        self.player_list.grid(row=0, column=0, sticky="nsew")
        self.player_list.bind("<<ListboxSelect>>", self._on_player_select)

        # --- Botões de Ação ---
        action_frame = ttk.Frame(self)
        action_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.btn_buy = ttk.Button(action_frame, text="Comprar", state="disabled", width=20, command=self._buy_selected)
        self.btn_buy.pack(side="left", padx=20)

        self.btn_sell = ttk.Button(action_frame, text="Vender", state="disabled", width=20, command=self._sell_selected)
        self.btn_sell.pack(side="left", padx=20)

        btn_back = ttk.Button(action_frame, text="Sair da Loja", command=lambda: controller.switch_view("cidade"), width=20)
        btn_back.pack(side="right", padx=20)

    def _on_shop_select(self, event=None):
        self.btn_buy.config(state="normal")
        self.btn_sell.config(state="disabled")
        self.player_list.selection_clear(0, tk.END)

    def _on_player_select(self, event=None):
        self.btn_buy.config(state="disabled")
        self.btn_sell.config(state="normal")
        self.shop_list.selection_clear(0, tk.END)

    def _buy_selected(self):
        selected_indices = self.shop_list.curselection()
        if not selected_indices: return

        item_id = self.shop_inventory[selected_indices[0]]
        self.controller.player_buy_item(item_id)

    def _sell_selected(self):
        selected_indices = self.player_list.curselection()
        if not selected_indices: return

        # Precisamos mapear o texto da lista de volta para um ID de item
        selected_text = self.player_list.get(selected_indices[0])
        item_name = selected_text.split(" (x")[0]

        found_item = next((item for item in self.player.inventario if item.get("nome") == item_name), None)
        if found_item:
            self.controller.player_sell_item(found_item.get("id"))

    def set_player(self, player):
        self.player = player
        self.update_ui()

    def update_ui(self):
        if not self.player: return

        self.lbl_money.config(text=f"Dinheiro: {self.player.dinheiro}g")

        # Popula a lista da loja
        self.shop_list.delete(0, tk.END)
        for item_id in self.shop_inventory:
            item_data = self.controller.INDICE_ITENS_COMPLETO.get(item_id, {})
            display_text = f"{item_data.get('nome', '???')} ({item_data.get('preco_base', 0)}g)"
            self.shop_list.insert(tk.END, display_text)

        # Popula a lista do jogador
        self.player_list.delete(0, tk.END)
        self.player_inventory_map = [] # Mapeia índice da lista para ID do item
        item_counts = {}
        for item in self.player.inventario:
            item_id = item.get("id")
            if item_id:
                item_counts[item_id] = item_counts.get(item_id, 0) + 1

        for item_id, count in item_counts.items():
            item_data = self.controller.INDICE_ITENS_COMPLETO.get(item_id, {})
            display_text = f"{item_data.get('nome', '???')} (x{count})"
            self.player_list.insert(tk.END, display_text)
            self.player_inventory_map.append(item_id)

        self.btn_buy.config(state="disabled")
        self.btn_sell.config(state="disabled")
