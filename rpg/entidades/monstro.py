import random
from typing import List, Dict, Any, Optional, TYPE_CHECKING

from .personagem import Personagem
from ..dados.habilidades import TODAS_HABILIDADES
from ..dados.ataques_base import ATAQUES_BASE

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
                 ataques_base_ids: List[str],
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
        # Converte os IDs de ataques básicos em objetos de ataque completos
        self.ataques_base = [ATAQUES_BASE[id_a] for id_a in ataques_base_ids if id_a in ATAQUES_BASE]


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
        # Como monstros não usam equipamentos, seus stats base são seus stats totais.
        # Nós os atribuímos aos `base_` atributos para consistência com a classe Personagem.
        self.base_forca = stats.get("forca", 10)
        self.base_destreza = stats.get("destreza", 10)
        self.base_constituicao = stats.get("constituicao", 10)
        self.base_inteligencia = stats.get("inteligencia", 10)
        self.base_sabedoria = stats.get("sabedoria", 10)
        self.base_carisma = stats.get("carisma", 1) # Geralmente baixo para monstros

    def decidir_acao(self, aliados: List['Monstro'], inimigos: List['Personagem']) -> Dict[str, Any]:
        """
        O cérebro do monstro. Decide qual ação tomar com base na IA.
        Esta é a primeira implementação da IA adaptativa.
        """
        # Define o alvo principal se não tiver um, ou se o alvo atual estiver morto.
        if not self.foco_atual or not self.foco_atual.esta_vivo():
            # Comportamento de foco: 'oportunista' foca no inimigo com menos HP.
            if self.comportamento_ia == "oportunista":
                self.foco_atual = min(inimigos, key=lambda i: i.hp_atual)
            else:
                self.foco_atual = random.choice(inimigos)

        # --- Lógica de Decisão Baseada em Regras ---

        # 1. Autopreservação (Prioridade Alta)
        if self.hp_atual / self.hp_max < 0.3: # Se com menos de 30% de vida
            habilidade_cura = self.encontrar_habilidade_por_efeito("cura", "self")
            if habilidade_cura:
                print(f"[IA - Autopreservação] {self.nome} está com pouca vida e decide se curar.")
                return {"tipo": "usar_habilidade", "habilidade": habilidade_cura, "alvo": self}

        # 2. Sinergia / Suporte (Prioridade Média)
        if self.comportamento_ia == "suporte":
            aliado_ferido = self.encontrar_aliado_ferido(aliados)
            if aliado_ferido:
                habilidade_cura_aliado = self.encontrar_habilidade_por_efeito("cura", "aliado_unico")
                if habilidade_cura_aliado:
                    print(f"[IA - Suporte] {self.nome} decide curar seu aliado {aliado_ferido.nome}.")
                    return {"tipo": "usar_habilidade", "habilidade": habilidade_cura_aliado, "alvo": aliado_ferido}

        # 3. Análise do Jogador (Prioridade Média)
        # Exemplo simples: se o jogador estiver com um buff de defesa, usar um debuff em vez de ataque direto.
        efeitos_alvo = self.foco_atual.efeitos_ativos
        if any(e.id_efeito == "buff_defesa_grande" for e in efeitos_alvo):
            habilidade_debuff = self.encontrar_habilidade_por_efeito("debuff", "inimigo_unico")
            if habilidade_debuff:
                print(f"[IA - Análise] {self.nome} vê a defesa do alvo e tenta aplicar um debuff.")
                return {"tipo": "usar_habilidade", "habilidade": habilidade_debuff, "alvo": self.foco_atual}

        # 4. Ofensiva Padrão (Prioridade Baixa)
        habilidade_ofensiva = self.encontrar_habilidade_por_efeito("dano", "inimigo_unico")
        if habilidade_ofensiva:
            print(f"[IA - Ofensiva] {self.nome} decide usar uma habilidade de ataque.")
            return {"tipo": "usar_habilidade", "habilidade": habilidade_ofensiva, "alvo": self.foco_atual}

        # 5. Ação Padrão: Ataque Básico
        ataque_escolhido = random.choice(self.ataques_base) if self.ataques_base else None
        if ataque_escolhido:
            print(f"[IA - Padrão] {self.nome} recorre a um ataque básico: {ataque_escolhido['nome']}.")
            return {"tipo": "ataque_basico", "ataque": ataque_escolhido, "alvo": self.foco_atual}
        else:
            # Caso o monstro não tenha ataques básicos definidos (fallback de segurança)
            print(f"[IA - Padrão] {self.nome} tenta atacar mas não tem ações disponíveis.")
            return {"tipo": "passar_turno"}


    def encontrar_habilidade_por_efeito(self, tipo_efeito: str, tipo_alvo: str) -> Optional[Dict]:
        """Encontra a primeira habilidade disponível que corresponde a um tipo de efeito e alvo."""
        habilidades_disponiveis = [h for h in self.habilidades if self.mp_atual >= h.get('custo_valor', 0)]
        for h in habilidades_disponiveis:
            if h.get("tipo_alvo") == tipo_alvo:
                for efeito in h.get("efeitos", []):
                    if efeito.get("tipo", "").startswith(tipo_efeito):
                        return h
        return None

    def encontrar_aliado_ferido(self, aliados: List['Monstro']) -> Optional['Monstro']:
        """Encontra o aliado (excluindo a si mesmo) com a menor porcentagem de vida, se abaixo de 50%."""
        aliados_feridos = [a for a in aliados if a is not self and (a.hp_atual / a.hp_max) < 0.5]
        if not aliados_feridos:
            return None
        return min(aliados_feridos, key=lambda a: a.hp_atual / a.hp_max)

    def gerar_loot(self) -> Dict[str, Any]:
        """Gera loot para o jogador com base na tabela de loot."""
        loot_gerado = {"ouro": self.ouro, "xp": self.xp_recompensa, "itens": []}
        for item_drop in self.loot_table:
            if random.random() < item_drop["chance"]:
                quantidade = random.randint(item_drop["quantidade"][0], item_drop["quantidade"][1])
                loot_gerado["itens"].append({"id_item": item_drop["id_item"], "quantidade": quantidade})

        return loot_gerado

    def __str__(self) -> str:
        return f"MONSTRO: {self.nome} (Nível {self.nivel}) | HP: {self.hp_atual}/{self.hp_max}"
