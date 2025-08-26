from typing import List, Dict, Any, Optional

from .monstro import Monstro
from .personagem import Personagem

class Boss(Monstro):
    """
    Representa um chefe, um adversário significativamente mais poderoso e complexo.
    Herda de Monstro, mas adiciona mecânicas de fases e uma IA mais sofisticada.
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
                 habilidades: List[Any],
                 mecanicas_fases: Dict[int, Dict[str, Any]], # Ex: {1: {"limite_hp": 0.7}, 2: {"limite_hp": 0.3, "novas_habilidades": [...]}}
                 dialogo_batalha: Optional[Dict[str, str]] = None): # Ex: {"fase_2": "Agora você verá meu verdadeiro poder!"}

        super().__init__(nome, nivel, id_monstro, familia, xp_recompensa,
                         ouro_recompensa, loot_table, stats_base, habilidades,
                         comportamento_ia="chefe")

        # --- Mecânicas de Chefe ---
        self.fase_atual = 1
        self.mecanicas_fases = mecanicas_fases
        self.dialogo_batalha = dialogo_batalha if dialogo_batalha is not None else {}

    def verificar_mudanca_fase(self):
        """Verifica se o chefe deve transicionar para a próxima fase."""
        proxima_fase = self.fase_atual + 1
        if proxima_fase in self.mecanicas_fases:
            limite_hp = self.mecanicas_fases[proxima_fase].get("limite_hp_percent", 0)
            if (self.hp_atual / self.hp_max) <= limite_hp:
                self.mudar_fase(proxima_fase)

    def mudar_fase(self, nova_fase: int):
        """
        Muda o chefe para uma nova fase, alterando sua IA, habilidades e stats.
        """
        self.fase_atual = nova_fase
        print(f"!!! {self.nome} entra na Fase {self.fase_atual} !!!")

        # Falar diálogo da nova fase, se houver
        dialogo = self.dialogo_batalha.get(f"fase_{self.fase_atual}")
        if dialogo:
            print(f"[{self.nome}]: {dialogo}")

        # Aplicar mecânicas da nova fase
        mecanicas = self.mecanicas_fases[self.fase_atual]

        # Adicionar novas habilidades
        novas_habilidades = mecanicas.get("novas_habilidades", [])
        if novas_habilidades:
            # self.habilidades.extend(novas_habilidades)
            print(f"{self.nome} aprende novas habilidades!")

        # Mudar comportamento da IA
        novo_comportamento = mecanicas.get("novo_comportamento_ia")
        if novo_comportamento:
            self.comportamento_ia = novo_comportamento
            print(f"O comportamento de {self.nome} mudou para {novo_comportamento}!")

        # Pode haver outros efeitos, como curar, invocar minions, etc.
        # Estes serão implementados no sistema de combate.

    def decidir_acao(self, aliados: List['Monstro'], inimigos: List['Personagem']) -> Dict[str, Any]:
        """
        IA do chefe, sobrescrevendo a do Monstro para ser sensível a fases.
        """
        # Primeiro, verifica se precisa mudar de fase
        self.verificar_mudanca_fase()

        # A lógica da IA pode depender da fase atual
        # Placeholder para a lógica complexa da Fase 4
        print(f"[IA Chefe - Fase {self.fase_atual}] {self.nome} está planejando seu próximo movimento...")

        # Chama a IA base de Monstro, que pode ser modificada pelo comportamento
        return super().decidir_acao(aliados, inimigos)

    def __str__(self) -> str:
        return f"CHEFE: {self.nome} (Nível {self.nivel}) | Fase: {self.fase_atual} | HP: {self.hp_atual}/{self.hp_max}"
