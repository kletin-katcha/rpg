import random
from typing import List, Dict, Any, Optional, TYPE_CHECKING

from .personagem import Personagem
from ..dados.habilidades import TODAS_HABILIDADES

if TYPE_CHECKING:
    from .item import Item

class Monstro(Personagem):
    """
    Representa um adversário no jogo. Herda muitas características de Personagem,
    mas tem lógica própria para IA, loot e comportamento.
    """
    def __init__(self,
                 nome: str,
                 nivel: int,
                 id_monstro: str,
                 familia: str,
                 xp_recompensa: int,
                 ouro_recompensa: int,
                 loot_table: List[Dict[str, Any]],
                 stats_base: Dict[str, int],
                 habilidades_ids: List[str],
                 comportamento_ia: str = "agressivo"):

        super().__init__(nome, nivel)

        # --- Identificação do Monstro ---
        self.id_monstro = id_monstro
        self.familia = familia # Ex: "Goblin", "Lobo", "Elemental"

        # --- Recompensas ---
        self.xp_recompensa = xp_recompensa
        self.ouro = ouro_recompensa # Sobrescreve o ouro base de Personagem
        self.loot_table = loot_table # Ex: [{"id_item": "pocao_cura", "chance": 0.5, "quantidade": [1, 3]}]

        # --- Atributos e Habilidades Específicas ---
        self.aplicar_stats_base(stats_base)
        # Converte os IDs de habilidades em objetos de habilidade completos
        self.habilidades = [TODAS_HABILIDADES[id_h] for id_h in habilidades_ids if id_h in TODAS_HABILIDADES]

        # --- Inteligência Artificial ---
        self.comportamento_ia = comportamento_ia # "agressivo", "defensivo", "suporte", "oportunista"
        self.cooldowns_habilidades: Dict[str, int] = {h['nome']: 0 for h in self.habilidades}
        self.memoria_combate: Dict[str, Any] = {} # Para IA adaptativa (ex: "ultima_habilidade_jogador": "bola_de_fogo")
        self.foco_atual: Optional['Personagem'] = None

        # Recalcula os stats DEPOIS de aplicar os stats base do monstro
        self.recalcular_stats_completos()
        # Define o HP e MP atuais para o máximo recém-calculado
        self.hp_atual = self.hp_max
        self.mp_atual = self.mp_max

    def aplicar_stats_base(self, stats: Dict[str, int]):
        """Aplica os atributos base definidos para este tipo de monstro."""
        self.forca = stats.get("forca", 10)
        self.destreza = stats.get("destreza", 10)
        self.constituicao = stats.get("constituicao", 10)
        self.inteligencia = stats.get("inteligencia", 10)
        self.sabedoria = stats.get("sabedoria", 10)
        self.carisma = stats.get("carisma", 1) # Geralmente baixo para monstros

    def decidir_acao(self, aliados: List['Monstro'], inimigos: List['Personagem']) -> Dict[str, Any]:
        """
        O cérebro do monstro. Decide qual ação tomar com base na IA.
        Esta é uma implementação placeholder. A lógica complexa (B, C, D) será adicionada na Fase 4.
        """
        # Placeholder: Lógica de IA muito simples
        # Na Fase 4, isso será expandido para:
        # 1. Analisar status (HP baixo -> usar habilidade de cura ou fugir?)
        # 2. Analisar buffs/debuffs do inimigo (inimigo com reflexão de dano -> usar debuff em vez de ataque direto)
        # 3. Analisar ações do inimigo (inimigo usa muita magia de fogo -> usar habilidade de resistência a fogo)
        # 4. Coordenar com aliados (se HP do aliado X está baixo, usar habilidade de cura nele)
        # 5. Gerenciar cooldowns

        # Define o alvo principal se não tiver um
        if not self.foco_atual or not self.foco_atual.esta_vivo():
            self.foco_atual = random.choice(inimigos)

        acao_escolhida = {"tipo": "ataque_basico", "alvo": self.foco_atual}

        # Tenta usar uma habilidade se tiver MP e se houver habilidades
        if self.habilidades:
            # Agora 'h' é um dicionário, então h.get() funciona
            habilidades_disponiveis = [h for h in self.habilidades if self.mp_atual >= h.get('custo_valor', 0)]
            if habilidades_disponiveis:
                habilidade_aleatoria = random.choice(habilidades_disponiveis)
                acao_escolhida = {"tipo": "usar_habilidade", "habilidade": habilidade_aleatoria, "alvo": self.foco_atual}

        print(f"[IA] {self.nome} decide: {acao_escolhida['tipo']} em {acao_escolhida['alvo'].nome}")
        return acao_escolhida

    def gerar_loot(self) -> Dict[str, Any]:
        """Gera loot para o jogador com base na tabela de loot."""
        loot_gerado = {"ouro": self.ouro, "xp": self.xp_recompensa, "itens": []}
        for item_drop in self.loot_table:
            if random.random() < item_drop["chance"]:
                quantidade = random.randint(item_drop["quantidade"][0], item_drop["quantidade"][1])
                loot_gerado["itens"].append({"id_item": item_drop["id_item"], "quantidade": quantidade})

        print(f"{self.nome} deixou cair {loot_gerado['ouro']} de ouro e {len(loot_gerado['itens'])} item(s).")
        return loot_gerado

    def __str__(self) -> str:
        return f"MONSTRO: {self.nome} (Nível {self.nivel}) | HP: {self.hp_atual}/{self.hp_max}"
