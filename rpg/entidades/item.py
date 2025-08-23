from typing import Dict, Any, Optional
from enum import Enum

class TipoItem(Enum):
    ARMA = "Arma"
    ARMADURA = "Armadura"
    POCAO = "Poção"
    INGREDIENTE = "Ingrediente"
    MATERIAL_CRAFTING = "Material de Crafting"
    ITEM_QUEST = "Item de Missão"
    GENERICO = "Genérico"

class RaridadeItem(Enum):
    COMUM = "Comum"
    INCOMUM = "Incomum"
    RARO = "Raro"
    EPICO = "Épico"
    LENDARIO = "Lendário"
    UNICO = "Único"

class Item:
    """
    Representa qualquer item que pode existir no jogo, desde equipamentos a consumíveis.
    Esta classe é primariamente um contêiner de dados.
    """
    def __init__(self,
                 id_item: str,
                 nome: str,
                 descricao: str,
                 tipo: TipoItem,
                 raridade: RaridadeItem,
                 valor: int,
                 empilhavel: bool = False,
                 max_pilha: int = 1,
                 lore: str = "",
                 # Atributos específicos
                 slot_equipamento: Optional[str] = None, # "arma_principal", "elmo", etc.
                 modificadores: Optional[Dict[str, Any]] = None, # {"forca": 10, "resistencia_fogo": 0.15}
                 efeito_consumo: Optional[Dict[str, Any]] = None, # {"tipo": "cura_hp", "quantidade": 100}
                 requisitos: Optional[Dict[str, Any]] = None): # {"nivel": 10, "forca": 20}

        # --- Identificação ---
        self.id_item = id_item
        self.nome = nome
        self.descricao = descricao
        self.lore = lore

        # --- Classificação ---
        self.tipo = tipo
        self.raridade = raridade
        self.valor = valor # Valor base em ouro
        self.empilhavel = empilhavel
        self.max_pilha = max_pilha if empilhavel else 1

        # --- Dados de Jogo ---
        # Para itens equipáveis
        self.slot_equipamento = slot_equipamento
        self.modificadores = modificadores if modificadores is not None else {}
        self.requisitos = requisitos if requisitos is not None else {}

        # Para itens consumíveis
        self.efeito_consumo = efeito_consumo if efeito_consumo is not None else {}

    def é_equipavel(self) -> bool:
        """Verifica se o item pode ser equipado."""
        return self.slot_equipamento is not None

    def é_consumivel(self) -> bool:
        """Verifica se o item pode ser consumido."""
        return self.efeito_consumo is not None

    def pode_equipar(self, personagem: 'Personagem') -> bool:
        """Verifica se o personagem cumpre os requisitos para equipar o item."""
        if not self.é_equipavel():
            return False

        for req, valor in self.requisitos.items():
            if getattr(personagem, req, 0) < valor:
                return False
        return True

    def __str__(self) -> str:
        return f"[{self.raridade.value}] {self.nome}"

    def info_detalhada(self) -> str:
        """Retorna uma string com todos os detalhes do item."""
        info = (
            f"--- {self.nome} ---\n"
            f"Tipo: {self.tipo.value} | Raridade: {self.raridade.value}\n"
            f"Valor: {self.valor} Ouro\n"
            f'"{self.descricao}"\n'
        )
        if self.requisitos:
            reqs = ", ".join([f"{k.capitalize()} {v}" for k, v in self.requisitos.items()])
            info += f"Requisitos: {reqs}\n"
        if self.modificadores:
            mods = ", ".join([f"{k.replace('_', ' ').capitalize()} +{v}" for k, v in self.modificadores.items()])
            info += f"Bônus: {mods}\n"
        if self.efeito_consumo:
            efeito = self.efeito_consumo
            info += f"Uso: {efeito.get('tipo', '').replace('_', ' ').capitalize()} em {efeito.get('quantidade', 0)}\n"
        if self.lore:
            info += f'\n"{self.lore}"'

        return info
