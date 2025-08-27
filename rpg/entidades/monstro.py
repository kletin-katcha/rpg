import random
from typing import List, Dict, Any, Optional, TYPE_CHECKING

from .personagem import Personagem
from ..dados.habilidades import TODAS_HABILIDADES
from ..dados.ataques_base import ATAQUES_BASE

if TYPE_CHECKING:
    from .item import Item

class Monstro(Personagem):
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

        self.id_monstro = id_monstro
        self.familia = familia
        self.xp_recompensa = xp_recompensa
        self.ouro = ouro_recompensa
        self.loot_table = loot_table
        self.aplicar_stats_base(stats_base)
        self.habilidades = habilidades_ids
        self.habilidades_completas = [TODAS_HABILIDADES[id_h] for id_h in habilidades_ids if id_h in TODAS_HABILIDADES]
        self.ataques_base = [ATAQUES_BASE[id_a] for id_a in ataques_base_ids if id_a in ATAQUES_BASE]
        self.comportamento_ia = comportamento_ia
        self.cooldowns_habilidades: Dict[str, int] = {h['nome']: 0 for h in self.habilidades_completas}
        self.memoria_combate: Dict[str, Any] = {}
        self.foco_atual: Optional['Personagem'] = None

        self.recalcular_stats_completos()
        self.hp_atual = self.hp_max
        self.mp_atual = self.mp_max

    def aplicar_stats_base(self, stats: Dict[str, int]):
        self.base_forca = stats.get("forca", 5)
        self.base_destreza = stats.get("destreza", 5)
        self.base_constituicao = stats.get("constituicao", 5)
        self.base_inteligencia = stats.get("inteligencia", 5)
        self.base_sabedoria = stats.get("sabedoria", 5)
        self.base_carisma = stats.get("carisma", 1)
        self.base_sorte = stats.get("sorte", 5)

    def decidir_acao(self, aliados: List['Personagem'], inimigos: List['Personagem']) -> Dict[str, Any]:
        # Reduzir cooldowns no início do turno
        for hab_nome in self.cooldowns_habilidades:
            if self.cooldowns_habilidades[hab_nome] > 0:
                self.cooldowns_habilidades[hab_nome] -= 1

        inimigos_vivos = [i for i in inimigos if i.esta_vivo()]
        if not inimigos_vivos:
            return {"tipo": "passar_turno"}

        if not self.foco_atual or not self.foco_atual.esta_vivo():
            self.foco_atual = random.choice(inimigos_vivos)

        if self.nivel >= 15 and self.comportamento_ia != "suporte":
            alvo_oportunista = min(inimigos_vivos, key=lambda i: i.hp_atual / i.hp_max)
            if self.foco_atual != alvo_oportunista:
                print(f"[IA Escalável] {self.nome} reavalia a situação e foca em {alvo_oportunista.nome}!")
                self.foco_atual = alvo_oportunista

        if self.hp_atual / self.hp_max < 0.3:
            habilidade_cura = self.encontrar_habilidade_por_efeito("cura", "self")
            if habilidade_cura:
                print(f"[IA - Autopreservação] {self.nome} está com pouca vida e decide se curar.")
                self.cooldowns_habilidades[habilidade_cura['nome']] = habilidade_cura.get('cooldown', 2)
                return {"tipo": "usar_habilidade", "habilidade": habilidade_cura, "alvo": self}

        if self.comportamento_ia == "suporte":
            aliado_ferido = self.encontrar_aliado_ferido(aliados)
            if aliado_ferido:
                habilidade_cura_aliado = self.encontrar_habilidade_por_efeito("cura", "aliado_unico")
                if habilidade_cura_aliado:
                    print(f"[IA - Suporte] {self.nome} decide curar seu aliado {aliado_ferido.nome}.")
                    self.cooldowns_habilidades[habilidade_cura_aliado['nome']] = habilidade_cura_aliado.get('cooldown', 2)
                    return {"tipo": "usar_habilidade", "habilidade": habilidade_cura_aliado, "alvo": aliado_ferido}

        if hasattr(self.foco_atual, 'efeitos_ativos'):
            efeitos_alvo = self.foco_atual.efeitos_ativos
            if any(e.id_efeito == "buff_defesa_grande" for e in efeitos_alvo):
                habilidade_debuff = self.encontrar_habilidade_por_efeito("debuff", "inimigo_unico")
                if habilidade_debuff:
                    print(f"[IA - Análise] {self.nome} vê a defesa do alvo e tenta aplicar um debuff.")
                    self.cooldowns_habilidades[habilidade_debuff['nome']] = habilidade_debuff.get('cooldown', 3)
                    return {"tipo": "usar_habilidade", "habilidade": habilidade_debuff, "alvo": self.foco_atual}

        habilidade_ofensiva = self.encontrar_habilidade_por_efeito("dano", "inimigo_unico")
        if habilidade_ofensiva:
            chance_usar_habilidade = 0.5 if self.nivel < 25 else 0.8
            if random.random() < chance_usar_habilidade:
                print(f"[IA - Ofensiva] {self.nome} decide usar uma habilidade de ataque: {habilidade_ofensiva['nome']}.")
                self.cooldowns_habilidades[habilidade_ofensiva['nome']] = habilidade_ofensiva.get('cooldown', 2)
                return {"tipo": "usar_habilidade", "habilidade": habilidade_ofensiva, "alvo": self.foco_atual}

        ataque_escolhido = random.choice(self.ataques_base) if self.ataques_base else None
        if ataque_escolhido:
            print(f"[IA - Padrão] {self.nome} recorre a um ataque básico: {ataque_escolhido['nome']}.")
            return {"tipo": "ataque_basico", "ataque": ataque_escolhido, "alvo": self.foco_atual}
        else:
            print(f"[IA - Padrão] {self.nome} tenta atacar mas não tem ações disponíveis e passa o turno.")
            return {"tipo": "passar_turno"}

    def encontrar_habilidade_por_efeito(self, tipo_efeito: str, tipo_alvo: str) -> Optional[Dict]:
        habilidades_disponiveis = []
        for h in self.habilidades_completas:
            custo_valor = h.get('custo_valor', 0)
            custo_tipo = h.get('custo_tipo')
            pode_pagar = False
            if custo_tipo == 'mp':
                if self.mp_atual >= custo_valor: pode_pagar = True
            elif custo_tipo == 'stamina':
                if self.stamina_atual >= custo_valor: pode_pagar = True
            else:
                pode_pagar = True

            # Verifica se a habilidade não está em cooldown
            em_cooldown = self.cooldowns_habilidades.get(h.get('nome'), 0) > 0

            if pode_pagar and not em_cooldown:
                habilidades_disponiveis.append(h)

        for h in habilidades_disponiveis:
            if h.get("tipo_alvo") == tipo_alvo:
                for efeito in h.get("efeitos", []):
                    if efeito.get("tipo", "").startswith(tipo_efeito):
                        return h
        return None

    def encontrar_aliado_ferido(self, aliados: List['Personagem']) -> Optional['Personagem']:
        aliados_feridos = [a for a in aliados if a is not self and (a.hp_atual / a.hp_max) < 0.5]
        if not aliados_feridos:
            return None
        return min(aliados_feridos, key=lambda a: a.hp_atual / a.hp_max)

    def gerar_loot(self) -> Dict[str, Any]:
        loot_gerado = {"ouro": self.ouro, "xp": self.xp_recompensa, "itens": []}
        for item_drop in self.loot_table:
            if random.random() < item_drop["chance"]:
                quantidade = random.randint(item_drop["quantidade"][0], item_drop["quantidade"][1])
                loot_gerado["itens"].append({"id_item": item_drop["id_item"], "quantidade": quantidade})
        return loot_gerado

    def __str__(self) -> str:
        return f"MONSTRO: {self.nome} (Nível {self.nivel}) | HP: {self.hp_atual}/{self.hp_max}"
