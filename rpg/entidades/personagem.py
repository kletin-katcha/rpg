import random
from typing import List, Dict, Optional, TYPE_CHECKING

# Usamos TYPE_CHECKING para evitar importações circulares em tempo de execução,
# já que outras entidades podem depender de Personagem e vice-versa.
if TYPE_CHECKING:
    from .item import Item
    from .efeito import Efeito
    from .quest import Quest
    # Supondo que teremos classes para Habilidade, Raça e Classe também
    # from ..dados.habilidades import Habilidade
    # from ..dados.racas import Raca
    # from ..dados.classes import Classe

class Personagem:
    """
    A classe base para qualquer personagem controlável ou não-controlável no jogo.
    Engloba jogadores, NPCs e potencialmente até certas criaturas com características complexas.
    """
    def __init__(self, nome: str, nivel: int = 1):
        # --- Identificação Básica ---
        self.nome: str = nome
        self.raca: Optional[str] = None # ID da raça
        self.classe: Optional[str] = None # ID da classe
        self.nivel: int = nivel
        self.xp_atual: int = 0
        self.xp_para_proximo_nivel: int = self.calcular_xp_necessario(nivel)

        # --- Atributos Primários ---
        self.forca: int = 10         # Dano físico, capacidade de carga
        self.destreza: int = 10      # Precisão, esquiva, dano à distância
        self.constituicao: int = 10  # Pontos de vida, resistência a dano físico
        self.inteligencia: int = 10  # Dano mágico, mana, resistência mágica
        self.sabedoria: int = 10     # Poder de cura, resistência a debuffs, percepção
        self.carisma: int = 10       # Interação com NPCs, preços em lojas, liderança

        # --- Recursos (HP, MP, Stamina) ---
        self.hp_max: int = self.calcular_hp_max()
        self.hp_atual: int = self.hp_max
        self.mp_max: int = self.calcular_mp_max()
        self.mp_atual: int = self.mp_max
        self.stamina_max: int = 100
        self.stamina_atual: int = self.stamina_max

        # --- Atributos de Combate Derivados ---
        # Estes serão recalculados com base nos atributos primários e equipamentos
        self.ataque_fisico: int = 0
        self.poder_magico: int = 0
        self.defesa_fisica: int = 0
        self.defesa_magica: int = 0
        self.precisao: int = 0
        self.esquiva: int = 0
        self.chance_critico: float = 0.05  # 5% base
        self.multiplicador_critico: float = 1.5 # 150% de dano base

        # --- Resistências Elementais e de Status ---
        self.resistencias: Dict[str, float] = {
            "fogo": 0.0, "gelo": 0.0, "raio": 0.0, "veneno": 0.0,
            "sagrado": 0.0, "sombra": 0.0, "fisico": 0.0, "magico": 0.0,
            "atordoamento": 0.0, "silencio": 0.0, "medo": 0.0
        }

        # --- Inventário e Equipamentos ---
        self.inventario: List['Item'] = []
        self.ouro: int = 100
        self.equipamentos: Dict[str, Optional['Item']] = {
            "arma_principal": None, "arma_secundaria": None,
            "elmo": None, "peitoral": None, "calcas": None, "botas": None,
            "luvas": None, "amuleto": None, "anel_1": None, "anel_2": None
        }

        # --- Habilidades e Efeitos ---
        self.habilidades: List[str] = [] # Lista de IDs de habilidades
        self.efeitos_ativos: List['Efeito'] = []

        # --- Quests ---
        self.quests_ativas: List['Quest'] = []
        self.quests_concluidas: List[str] = [] # Armazena IDs das quests concluídas

        # --- Reputação ---
        self.reputacao: Dict[str, int] = { # Ex: "Guilda dos Ladrões": 50
            "cidade_inicial": 0,
        }

        # Recalcular todos os stats derivados na inicialização
        self.recalcular_stats_completos()

    def calcular_xp_necessario(self, nivel: int) -> int:
        """Calcula o XP necessário para o próximo nível com base em uma curva exponencial."""
        return int(100 * (nivel ** 1.5))

    def calcular_hp_max(self) -> int:
        """Calcula os pontos de vida máximos com base na constituição e nível."""
        return 80 + (self.constituicao * 10) + (self.nivel * 20)

    def calcular_mp_max(self) -> int:
        """Calcula os pontos de mana máximos com base na inteligência/sabedoria e nível."""
        return 30 + (self.inteligencia * 7) + (self.sabedoria * 3) + (self.nivel * 10)

    def recalcular_stats_completos(self):
        """
        Recalcula todos os atributos derivados do personagem.
        Deve ser chamado ao subir de nível, equipar/desequipar itens ou ao receber buffs/debuffs permanentes.
        """
        # Resetar stats base
        self.hp_max = self.calcular_hp_max()
        self.mp_max = self.calcular_mp_max()

        # Stats de combate baseados nos atributos primários
        self.ataque_fisico = self.forca * 2
        self.poder_magico = self.inteligencia * 2
        self.defesa_fisica = self.constituicao // 2
        self.defesa_magica = self.inteligencia // 2 + self.sabedoria // 2
        self.precisao = self.destreza * 3
        self.esquiva = self.destreza * 2

        # TODO: Adicionar lógica para aplicar modificadores de equipamentos
        # for slot, item in self.equipamentos.items():
        #     if item:
        #         # Aplicar item.modificadores
        #         pass

        # TODO: Adicionar lógica para aplicar modificadores de efeitos ativos (buffs/debuffs)
        # for efeito in self.efeitos_ativos:
        #     # Aplicar efeito.modificadores
        #     pass

        # Garantir que HP/MP atuais não excedam o novo máximo
        self.hp_atual = min(self.hp_atual, self.hp_max)
        self.mp_atual = min(self.mp_atual, self.mp_max)

    def esta_vivo(self) -> bool:
        """Verifica se o personagem ainda tem pontos de vida."""
        return self.hp_atual > 0

    def ganhar_xp(self, quantidade: int):
        """Adiciona XP ao personagem e verifica se ele subiu de nível."""
        if not self.esta_vivo():
            return

        self.xp_atual += quantidade
        print(f"{self.nome} ganhou {quantidade} de XP!")

        while self.xp_atual >= self.xp_para_proximo_nivel:
            self.subir_nivel()

    def subir_nivel(self):
        """
        Executa a lógica de subida de nível.
        Aumenta o nível, reseta o XP, calcula o novo XP necessário e melhora os atributos.
        """
        self.xp_atual -= self.xp_para_proximo_nivel
        self.nivel += 1
        self.xp_para_proximo_nivel = self.calcular_xp_necessario(self.nivel)

        # Lógica de ganho de atributos (exemplo simples, pode ser baseado na classe)
        self.forca += 1
        self.destreza += 1
        self.constituicao += 2
        self.inteligencia += 1
        self.sabedoria += 1
        self.carisma += 1

        # Recalcula tudo e cura o personagem
        self.recalcular_stats_completos()
        self.hp_atual = self.hp_max
        self.mp_atual = self.mp_max

        print(f"🎉 {self.nome} subiu para o nível {self.nivel}! 🎉")
        print(f"HP: {self.hp_max} | MP: {self.mp_max}")

    def tomar_dano(self, quantidade_dano: int, tipo_dano: str = "fisico"):
        """
        Aplica uma quantidade de dano já calculada ao HP do personagem.
        A lógica de cálculo (com defesa/resistências) acontece no sistema de combate.
        """
        dano_final = max(0, quantidade_dano)
        self.hp_atual -= dano_final
        print(f"{self.nome} tomou {dano_final} de dano. HP restante: {self.hp_atual}/{self.hp_max}")
        if not self.esta_vivo():
            print(f"{self.nome} foi derrotado.")

    def curar(self, quantidade: int):
        """Cura o personagem, sem exceder o HP máximo."""
        self.hp_atual = min(self.hp_max, self.hp_atual + quantidade)
        print(f"{self.nome} recuperou {quantidade} de HP. HP atual: {self.hp_atual}/{self.hp_max}")

    def __str__(self) -> str:
        return (
            f"--- {self.nome} (Nível {self.nivel}) ---\n"
            f"HP: {self.hp_atual}/{self.hp_max} | MP: {self.mp_atual}/{self.mp_max}\n"
            f"XP: {self.xp_atual}/{self.xp_para_proximo_nivel}\n"
            f"Força: {self.forca} | Destreza: {self.destreza} | Constituição: {self.constituicao}\n"
            f"Inteligência: {self.inteligencia} | Sabedoria: {self.sabedoria} | Carisma: {self.carisma}\n"
        )
