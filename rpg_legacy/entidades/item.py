# rpg_legacy/entidades/item.py (fully documented)
from typing import Dict, Any, Optional, TYPE_CHECKING
from enum import Enum

# A checagem de tipo para 'Personagem' é movida para dentro dos métodos
# que a utilizam para evitar importação circular, já que Personagem também importa Item.
if TYPE_CHECKING:
    from .personagem import Personagem

class TipoItem(Enum):
    """
    Enumeração para os diferentes tipos de itens no jogo.
    Ajuda a classificar e a aplicar lógicas específicas para cada tipo.
    """
    ARMA = "Arma"
    ARMADURA = "Armadura"
    POCAO = "Poção"
    INGREDIENTE = "Ingrediente"
    MATERIAL_CRAFTING = "Material de Crafting"
    ITEM_QUEST = "Item de Missão"
    GENERICO = "Genérico"

class RaridadeItem(Enum):
    """
    Enumeração para as diferentes raridades de itens.
    Influencia a cor do nome do item, seu valor e, potencialmente, a força de seus bônus.
    """
    COMUM = "Comum"
    INCOMUM = "Incomum"
    RARO = "Raro"
    EPICO = "Épico"
    LENDARIO = "Lendário"
    UNICO = "Único"

class Item:
    """
    Representa qualquer item que pode existir no jogo, desde equipamentos a consumíveis e materiais.
    Esta classe é projetada para ser um contêiner de dados flexível, instanciado a partir
    de definições em arquivos de dados (ex: dados/itens_comuns.py).

    Atributos:
        id_item (str): O identificador único e interno do item.
        nome (str): O nome do item exibido para o jogador.
        descricao (str): Uma breve descrição do que o item é ou faz.
        lore (str): Uma descrição mais longa ou um texto de ambientação para o item.
        tipo (TipoItem): A categoria do item (ex: Arma, Poção).
        raridade (RaridadeItem): A raridade do item (ex: Comum, Lendário).
        valor (int): O valor base do item em moedas de ouro.
        empilhavel (bool): Se o item pode ser agrupado em um único slot de inventário.
        max_pilha (int): O número máximo de unidades que podem ser empilhadas.
        slot_equipamento (Optional[str]): Se for um equipamento, o slot que ele ocupa (ex: "arma_principal").
        modificadores (Dict): Dicionário com os bônus de stats que o item concede quando equipado.
        efeito_consumo (Dict): Dicionário que descreve o que acontece quando o item é usado/consumido.
        requisitos (Dict): Dicionário com os requisitos para equipar o item.
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
                 # Atributos específicos para diferentes tipos de itens
                 slot_equipamento: Optional[str] = None, # Ex: "arma_principal", "elmo", etc.
                 modificadores: Optional[Dict[str, Any]] = None, # Ex: {"forca": 10, "resistencia_fogo": 0.15}
                 efeito_consumo: Optional[Dict[str, Any]] = None, # Ex: {"tipo": "cura_hp", "quantidade": 100}
                 requisitos: Optional[Dict[str, Any]] = None): # Ex: {"nivel": 10, "forca": 20}
        """
        Inicializa um novo objeto Item a partir de seus dados.

        Args:
            id_item (str): O ID único do item.
            nome (str): O nome do item.
            descricao (str): A descrição curta do item.
            tipo (TipoItem): O tipo do item.
            raridade (RaridadeItem): A raridade do item.
            valor (int): O valor em ouro.
            empilhavel (bool, optional): Se o item pode ser empilhado. Defaults to False.
            max_pilha (int, optional): Tamanho máximo da pilha se empilhável. Defaults to 1.
            lore (str, optional): Texto de ambientação do item. Defaults to "".
            slot_equipamento (Optional[str], optional): Slot de equipamento. Defaults to None.
            modificadores (Optional[Dict[str, Any]], optional): Bônus de stats. Defaults to None.
            efeito_consumo (Optional[Dict[str, Any]], optional): Efeito ao consumir. Defaults to None.
            requisitos (Optional[Dict[str, Any]], optional): Requisitos para equipar. Defaults to None.
        """

        # --- Seção de Identificação e Lore ---
        self.id_item: str = id_item
        self.nome: str = nome
        self.descricao: str = descricao
        self.lore: str = lore

        # --- Seção de Classificação e Valor ---
        self.tipo: TipoItem = tipo
        self.raridade: RaridadeItem = raridade
        self.valor: int = valor # Valor base em ouro para compra/venda.
        self.empilhavel: bool = empilhavel
        self.max_pilha: int = max_pilha if empilhavel else 1

        # --- Seção de Dados de Jogo ---
        # Para itens equipáveis:
        self.slot_equipamento: Optional[str] = slot_equipamento
        self.modificadores: Dict[str, Any] = modificadores if modificadores is not None else {}
        self.requisitos: Dict[str, Any] = requisitos if requisitos is not None else {}

        # Para itens consumíveis:
        self.efeito_consumo: Dict[str, Any] = efeito_consumo if efeito_consumo is not None else {}

    def é_equipavel(self) -> bool:
        """
        Verifica se o item é do tipo que pode ser equipado por um personagem.

        Returns:
            bool: True se o item tem um `slot_equipamento` definido, False caso contrário.
        """
        return self.slot_equipamento is not None

    def é_consumivel(self) -> bool:
        """
        Verifica se o item é do tipo que pode ser consumido (usado).

        Returns:
            bool: True se o item tem um `efeito_consumo` definido, False caso contrário.
        """
        return self.efeito_consumo is not None

    def pode_equipar(self, personagem: 'Personagem') -> bool:
        """
        Verifica se um personagem específico cumpre os requisitos para equipar este item.

        Args:
            personagem (Personagem): O objeto do personagem que está tentando equipar o item.

        Returns:
            bool: True se o personagem cumpre todos os requisitos, False caso contrário.
        """
        # Um item não equipável nunca pode ser equipado.
        if not self.é_equipavel():
            return False

        # Itera sobre todos os requisitos definidos para o item.
        for req, valor_req in self.requisitos.items():
            # Usa getattr para pegar o valor do atributo correspondente no personagem.
            # Se o personagem não tiver o atributo, retorna 0 como padrão.
            valor_personagem = getattr(personagem, req, 0)
            if valor_personagem < valor_req:
                # Se qualquer requisito não for cumprido, retorna False imediatamente.
                return False
        # Se o loop terminar sem retornar, todos os requisitos foram cumpridos.
        return True

    def __str__(self) -> str:
        """
        Retorna uma representação curta e simples do item, ideal para listas de inventário.

        Returns:
            str: Uma string formatada como "[Raridade] Nome do Item".
        """
        return f"[{self.raridade.value}] {self.nome}"

    def info_detalhada(self) -> str:
        """
        Retorna uma string formatada com todos os detalhes do item,
        perfeita para ser exibida em uma tela de "inspecionar item".

        Returns:
            str: Uma string multi-linha com todas as informações relevantes do item.
        """
        info = (
            f"--- {self.nome} ---\n"
            f"Tipo: {self.tipo.value} | Raridade: {self.raridade.value}\n"
            f"Valor: {self.valor} Ouro\n"
            f'"{self.descricao}"\n'
        )
        # Adiciona a seção de Requisitos se houver alguma.
        if self.requisitos:
            # Formata o dicionário de requisitos em uma string legível.
            reqs = ", ".join([f"{k.capitalize()} {v}" for k, v in self.requisitos.items()])
            info += f"Requisitos: {reqs}\n"
        # Adiciona a seção de Bônus se houver algum.
        if self.modificadores:
            # Formata o dicionário de modificadores em uma string legível.
            mods = ", ".join([f"{k.replace('_', ' ').capitalize()} +{v}" for k, v in self.modificadores.items()])
            info += f"Bônus: {mods}\n"
        # Adiciona a seção de Efeito de Uso se houver.
        if self.efeito_consumo:
            efeito = self.efeito_consumo
            info += f"Uso: {efeito.get('tipo', '').replace('_', ' ').capitalize()} em {efeito.get('quantidade', 0)}\n"
        # Adiciona a lore do item se existir.
        if self.lore:
            info += f'\n"{self.lore}"\n'

        return info
