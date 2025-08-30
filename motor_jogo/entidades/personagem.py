# -*- coding: utf-8 -*-
"""
################################################################################################
##                                                                                            ##
##    ██████╗ ███████╗██████╗  ███████╗ █████╗  ███╗   ██╗     █████╗  ██████╗  ██████╗ ███████╗  ##
##    ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗████╗  ██║    ██╔══██╗██╔═══██╗██╔════╝ ██╔════╝  ##
##    ██████╔╝█████╗  ██████╔╝███████╗███████║██╔██╗ ██║    ███████║██║   ██║██║  ███╗█████╗    ##
##    ██╔═══╝ ██╔══╝  ██╔══██╗╚════██║██╔══██║██║╚██╗██║    ██╔══██║██║   ██║██║   ██║██╔══╝    ##
##    ██║     ███████╗██║  ██║███████║██║  ██║██║ ╚████║    ██║  ██║╚██████╔╝╚██████╔╝███████╗  ##
##    ╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝  ##
##                                                                                            ##
################################################################################################
################################################################################################

================================================================================================
CLASSE: PERSONAGEM
================================================================================================
Este arquivo define a classe `Personagem`, que representa o avatar do jogador no mundo
de Aetheria. Esta é uma das classes mais complexas do motor, pois gerencia não apenas
o estado de combate, mas também a progressão, o inventário, as missões e outras
informações específicas do jogador.

-------------------------
-- HERANÇA E DESIGN --
-------------------------
A classe `Personagem` herda da `entidade_base.Entidade`, aproveitando todos os
atributos e métodos comuns (HP, atributos, receber_dano, etc.). Sobre essa base,
ela adiciona camadas de complexidade:

- **Dados de Origem:** Armazena informações sobre a raça e a classe do personagem,
  que são carregadas dos arquivos de banco de dados.
- **Progressão:** Gerencia a experiência (XP), o nível atual e o processo de
  subir de nível (`level up`).
- **Equipamento:** Possui "slots" de equipamento (mão principal, armadura, etc.) e
  um inventário para guardar itens.
- **Habilidades e Missões:** Mantém listas das habilidades conhecidas e das missões
  ativas ou concluídas.

O `__init__` da classe é projetado para ser flexível, aceitando dicionários de dados
brutos (vindos dos bancos de dados) para construir um objeto de personagem completo e
funcional.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
from typing import Dict, Any, List, Optional

# Importa a classe base para herança.
from .entidade_base import Entidade

# Importa os bancos de dados para consulta na criação do personagem.
# Usamos try-except para o caso de o módulo ser testado isoladamente.
try:
    from ..banco_de_dados.racas import racas_base
    from ..banco_de_dados.classes import classes_iniciais
except ImportError:
    print("DEBUG: Não foi possível importar os bancos de dados para a classe Personagem.", file=sys.stderr)


# ==============================================================================================
# == SEÇÃO 2: DEFINIÇÃO DA CLASSE PERSONAGEM ===================================================
# ==============================================================================================
class Personagem(Entidade):
    """
    Representa o personagem controlado pelo jogador.

    Herda de `Entidade` e adiciona sistemas de progressão, inventário,
    equipamento e missões.

    Attributes:
        raca (Dict[str, Any]): Dicionário com os dados da raça do personagem.
        classe (Dict[str, Any]): Dicionário com os dados da classe do personagem.
        xp_atual (int): A quantidade de experiência atual.
        xp_para_proximo_nivel (int): A quantidade de XP necessária para o próximo nível.
        inventario (List[Dict]): Lista de itens no inventário.
        equipamento (Dict[str, Any]): Dicionário com os itens equipados.
        missoes_ativas (List[str]): Lista de IDs de missões em andamento.
    """

    def __init__(self, id_entidade: str, nome: str, dados_raca: Dict, dados_classe: Dict):
        """
        Inicializa um novo objeto Personagem.

        Este construtor é mais complexo, pois combina os dados da raça e da classe
        para formar os atributos finais do personagem.

        Args:
            id_entidade (str): O ID único para esta instância de personagem.
            nome (str): O nome escolhido pelo jogador.
            dados_raca (Dict): O dicionário de dados completo da raça escolhida.
            dados_classe (Dict): O dicionário de dados completo da classe escolhida.
        """
        # Combina os atributos base da raça e da classe.
        # (Esta é uma lógica simplificada. Um sistema real poderia ter regras mais complexas).
        atributos_finais = dados_raca.get("atributos_base", {}).copy()

        # Inicializa a classe pai (Entidade) com os dados combinados.
        super().__init__(
            id_entidade=id_entidade,
            nome=nome,
            nivel=1,
            hp=atributos_finais.get("constituicao", 10) * 10, # HP inicial baseado na constituição
            atributos=atributos_finais
        )

        # Atributos específicos do Personagem
        self.raca: Dict[str, Any] = dados_raca
        self.classe: Dict[str, Any] = dados_classe
        self.xp_atual: int = 0
        self.xp_para_proximo_nivel: int = 100 # Exemplo de valor inicial
        self.dinheiro: int = 100 # Valor inicial para teste

        self.inventario: List[Dict] = []
        self.equipamento: Dict[str, Optional[Dict]] = {
            "mao_principal": None,
            "mao_secundaria": None,
            "cabeca": None,
            "peito": None,
            "pernas": None,
            "pes": None,
            "amuleto": None,
            "anel_1": None,
            "anel_2": None,
        }

        self.habilidades_conhecidas: List[str] = []
        self.habilidades_conhecidas.extend(dados_raca.get("habilidades_raciais", []))
        self.habilidades_conhecidas.extend(dados_classe.get("habilidades_iniciais", []))

        # Atributos para os sistemas de progressão
        self.historico_classes: List[str] = [dados_classe.get("id_classe")]
        self.alinhamento: str = "Neutro"
        self.reputacao: Dict[str, int] = {}
        self.boosts_legado: Dict[str, Any] = {}

        self.missoes_ativas: List[str] = []
        self.missoes_concluidas: List[str] = []

        # Atributos de estado do mundo
        self.localizacao_atual: str = "plains_de_havenwood" # Ponto de partida padrão

    def __str__(self) -> str:
        """Retorna uma representação mais detalhada para o personagem."""
        info_base = super().__str__()
        return f"{info_base} | Raça: {self.raca.get('nome')} | Classe: {self.classe.get('nome')}"

    # --- MÉTODOS DE INVENTÁRIO (PLACEHOLDERS) ---

    def adicionar_item(self, item_data: Dict) -> bool:
        """Adiciona um item ao inventário."""
        print(f"Item '{item_data.get('nome')}' adicionado ao inventário.")
        self.inventario.append(item_data)
        return True

    def remover_item(self, item_id: str, quantidade: int = 1) -> bool:
        """Remove uma certa quantidade de um item do inventário pelo seu ID."""
        itens_removidos = 0
        inventario_restante = []
        for item in self.inventario:
            if item.get("id") == item_id and itens_removidos < quantidade:
                itens_removidos += 1
                print(f"Item '{item.get('nome')}' removido do inventário.")
            else:
                inventario_restante.append(item)

        if itens_removidos > 0:
            self.inventario = inventario_restante
            return True
        else:
            print(f"AVISO: Tentativa de remover o item '{item_id}', mas ele não foi encontrado.")
            return False

    def equipar_item(self, item_data: Dict, slot: str) -> bool:
        """Equipa um item em um slot específico."""
        if slot not in self.equipamento:
            print(f"Erro: Slot de equipamento '{slot}' inválido.")
            return False

        # Lógica para desequipar o item antigo, se houver
        if self.equipamento[slot]:
            self.adicionar_item(self.equipamento[slot])

        print(f"Item '{item_data.get('nome')}' equipado no slot '{slot}'.")
        self.equipamento[slot] = item_data
        # Lógica para aplicar/remover bônus de atributos do item
        return True

    # --- MÉTODOS DE MISSÃO (PLACEHOLDERS) ---

    def iniciar_missao(self, id_missao: str) -> None:
        """Adiciona uma nova missão à lista de missões ativas."""
        if id_missao not in self.missoes_ativas:
            self.missoes_ativas.append(id_missao)
            print(f"Nova missão iniciada: {id_missao}")

# Fim da definição da classe Personagem.
