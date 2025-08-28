import random
from typing import List, Dict, Optional, TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .item import Item
    from .efeito import Efeito
    from .quest import Quest

from rpg.dados.ataques_base import ATAQUES_BASE
from rpg.dados.itens import TODOS_OS_ITENS
from rpg.dados.habilidades_passivas_efeitos import HABILIDADES_PASSIVAS_EFEITOS
from .item import Item


class Personagem:
    def __init__(self, nome: str, nivel: int = 1):
        self.nome: str = nome
        self.raca: Optional[str] = None
        self.classe: Optional[str] = None
        self.nivel: int = nivel
        self.xp_atual: int = 0
        self.xp_para_proximo_nivel: int = self.calcular_xp_necessario(nivel)
        self.pontos_de_atributo_para_distribuir: int = 0

        self.base_forca: int = 5
        self.base_destreza: int = 5
        self.base_constituicao: int = 5
        self.base_inteligencia: int = 5
        self.base_sabedoria: int = 5
        self.base_carisma: int = 5
        self.base_sorte: int = 5

        self.forca: int = 0
        self.destreza: int = 0
        self.constituicao: int = 0
        self.inteligencia: int = 0
        self.sabedoria: int = 0
        self.carisma: int = 0
        self.sorte: int = 0

        self.hp_max: int = 0
        self.hp_atual: int = 0
        self.mp_max: int = 0
        self.mp_atual: int = 0
        self.stamina_max: int = 100
        self.stamina_atual: int = 100

        self.dano_arma_bonus: int = 0
        self.ataque_fisico: int = 0
        self.poder_magico: int = 0
        self.defesa_fisica: int = 0
        self.defesa_magica: int = 0
        self.precisao: int = 0
        self.esquiva: int = 0
        self.chance_critico: float = 0.05
        self.multiplicador_critico: float = 1.5

        self.resistencias: Dict[str, float] = {
            "fogo": 0.0, "gelo": 0.0, "raio": 0.0, "veneno": 0.0,
            "sagrado": 0.0, "sombra": 0.0, "fisico": 0.0, "magico": 0.0,
            "atordoamento": 0.0, "silencio": 0.0, "medo": 0.0
        }

        self.inventario: Dict[str, Dict[str, Any]] = {}
        self.ouro: int = 100
        self.equipamentos: Dict[str, Optional['Item']] = {
            "arma_principal": None, "arma_secundaria": None,
            "elmo": None, "peitoral": None, "calcas": None, "botas": None,
            "luvas": None, "amuleto": None, "anel_1": None, "anel_2": None
        }

        self.habilidades: List[str] = []
        self.ataques_base: List[Dict] = [ATAQUES_BASE["soco"], ATAQUES_BASE["chute"]]
        self.postura_combate: str = "equilibrada" # equilibrada, ofensiva, defensiva
        self.efeitos_ativos: List['Efeito'] = []
        self.quests_ativas: List['Quest'] = []
        self.quests_concluidas: List[str] = []
        self.reputacao: Dict[str, int] = {"cidade_inicial": 0}

        self.recalcular_stats_completos()
        self.hp_atual = self.hp_max
        self.mp_atual = self.mp_max
        self.stamina_atual = self.stamina_max

    def calcular_xp_necessario(self, nivel: int) -> int:
        return int(100 * (nivel ** 1.5))

    def calcular_hp_max(self) -> int:
        return 80 + (self.constituicao * 10) + (self.nivel * 20)

    def calcular_mp_max(self) -> int:
        return 30 + (self.inteligencia * 7) + (self.sabedoria * 3) + (self.nivel * 10)

    def recalcular_stats_completos(self):
        bonus = {
            'forca': 0, 'destreza': 0, 'constituicao': 0, 'inteligencia': 0,
            'sabedoria': 0, 'carisma': 0, 'sorte': 0, 'hp_max': 0, 'mp_max': 0,
            'ataque_fisico': 0, 'poder_magico': 0, 'defesa_fisica': 0,
            'defesa_magica': 0, 'precisao': 0, 'esquiva': 0,
            'dano_arma_bonus': 0, 'chance_critico': 0.0,
            'resistencias': {k: 0.0 for k in self.resistencias}
        }

        for item in self.equipamentos.values():
            if item and item.modificadores:
                for mod, valor in item.modificadores.items():
                    mod_real = 'dano_arma_bonus' if mod == 'dano_arma' else mod
                    if mod_real in bonus:
                        bonus[mod_real] += valor

        for hab_id in self.habilidades:
            if hab_id in HABILIDADES_PASSIVAS_EFEITOS:
                efeito = HABILIDADES_PASSIVAS_EFEITOS[hab_id]
                attr = efeito["atributo"]
                if attr in bonus:
                    if "chave" in efeito:
                        sub_chave = efeito["chave"]
                        if attr not in bonus: bonus[attr] = {}
                        bonus[attr][sub_chave] = bonus[attr].get(sub_chave, 0) + efeito["valor"]
                    else:
                        bonus[attr] += efeito["valor"]

        for efeito_ativo in self.efeitos_ativos:
            if efeito_ativo.modificadores:
                for mod, valor in efeito_ativo.modificadores.items():
                    if mod in bonus:
                        bonus[mod] += valor
                    elif mod.startswith("resistencia_"):
                         res_chave = mod.replace("resistencia_", "")
                         if res_chave in self.resistencias:
                            bonus['resistencias'][res_chave] = bonus['resistencias'].get(res_chave, 0) + valor

        self.forca = self.base_forca + bonus['forca']
        self.destreza = self.base_destreza + bonus['destreza']
        self.constituicao = self.base_constituicao + bonus['constituicao']
        self.inteligencia = self.base_inteligencia + bonus['inteligencia']
        self.sabedoria = self.base_sabedoria + bonus['sabedoria']
        self.carisma = self.base_carisma + bonus['carisma']
        self.sorte = self.base_sorte + bonus['sorte']

        hp_antigo = self.hp_max
        mp_antigo = self.mp_max

        self.hp_max = self.calcular_hp_max() + bonus['hp_max']
        self.mp_max = self.calcular_mp_max() + bonus['mp_max']
        self.ataque_fisico = self.forca * 2 + bonus['ataque_fisico']
        self.poder_magico = self.inteligencia * 2 + bonus['poder_magico']
        self.defesa_fisica = self.constituicao // 2 + bonus['defesa_fisica']
        self.defesa_magica = (self.inteligencia + self.sabedoria) // 2 + bonus['defesa_magica']
        self.precisao = self.destreza * 3 + bonus['precisao']
        self.esquiva = self.destreza * 2 + bonus['esquiva']
        self.chance_critico = 0.05 + (self.sorte * 0.005) + bonus['chance_critico']
        self.dano_arma_bonus = bonus['dano_arma_bonus']

        for res, val in bonus['resistencias'].items():
            self.resistencias[res] = val

        if self.hp_max > hp_antigo and hp_antigo != 0:
            self.hp_atual += self.hp_max - hp_antigo
        if self.mp_max > mp_antigo and mp_antigo != 0:
            self.mp_atual += self.mp_max - mp_antigo

        self.hp_atual = min(self.hp_atual, self.hp_max)
        self.mp_atual = min(self.mp_atual, self.mp_max)

    def esta_vivo(self) -> bool:
        return self.hp_atual > 0

    def ganhar_xp(self, quantidade: int) -> list[str]:
        if not self.esta_vivo(): return []

        logs = []
        self.xp_atual += quantidade
        logs.append(f"{self.nome} ganhou {quantidade} de XP!")

        while self.xp_atual >= self.xp_para_proximo_nivel:
            logs.extend(self.subir_nivel())

        return logs

    def subir_nivel(self) -> list[str]:
        self.xp_atual -= self.xp_para_proximo_nivel
        self.nivel += 1
        self.xp_para_proximo_nivel = self.calcular_xp_necessario(self.nivel)

        pontos_ganhos = 5 if 1 <= self.nivel <= 10 else 3 if 11 <= self.nivel <= 25 else 2 if 26 <= self.nivel <= 50 else 1
        self.pontos_de_atributo_para_distribuir += pontos_ganhos

        self.recalcular_stats_completos()
        self.hp_atual = self.hp_max
        self.mp_atual = self.mp_max

        return [
            f"🎉 {self.nome} subiu para o nível {self.nivel}! 🎉",
            f"Você ganhou {pontos_ganhos} pontos de atributo para distribuir!"
        ]

    def distribuir_pontos_de_atributo(self, distribuicao: Dict[str, int]) -> bool:
        pontos_a_gastar = sum(distribuicao.values())
        if pontos_a_gastar > self.pontos_de_atributo_para_distribuir:
            print("Você não tem pontos de atributo suficientes.")
            return False
        if any(v < 0 for v in distribuicao.values()):
            print("Não é possível alocar um número negativo de pontos.")
            return False

        for attr, valor in distribuicao.items():
            if hasattr(self, f"base_{attr}"):
                setattr(self, f"base_{attr}", getattr(self, f"base_{attr}") + valor)

        self.pontos_de_atributo_para_distribuir -= pontos_a_gastar
        self.recalcular_stats_completos()
        print("Pontos de atributo distribuídos com sucesso!")
        return True

    def tomar_dano(self, quantidade_dano: int, tipo_dano: str = "fisico"):
        dano_final = max(0, quantidade_dano)
        self.hp_atual = max(0, self.hp_atual - dano_final)
        print(f"{self.nome} tomou {dano_final} de dano. HP restante: {self.hp_atual}/{self.hp_max}")
        if not self.esta_vivo():
            print(f"💀 {self.nome} foi derrotado. 💀")

    def curar(self, quantidade: int):
        self.hp_atual = min(self.hp_max, self.hp_atual + quantidade)
        print(f"{self.nome} recuperou {quantidade} de HP. HP atual: {self.hp_atual}/{self.hp_max}")

    def adicionar_item(self, id_item: str, quantidade: int = 1):
        # Evita importação circular
        from rpg.sistemas import quests

        dados_item = TODOS_OS_ITENS.get(id_item)
        if not dados_item: return
        if id_item in self.inventario:
            self.inventario[id_item]["quantidade"] += quantidade
        else:
            novo_item = Item(id_item=id_item, **dados_item)
            self.inventario[id_item] = {"item": novo_item, "quantidade": quantidade}
        print(f"{quantidade}x {dados_item['nome']} adicionado(s) ao inventário.")

        # Atualiza o progresso das quests de coleta
        quests.atualizar_progresso_quests(self, "coletar", id_item, quantidade)

    def remover_item(self, id_item: str, quantidade: int = 1) -> bool:
        if id_item not in self.inventario or self.inventario[id_item]["quantidade"] < quantidade:
            return False
        self.inventario[id_item]["quantidade"] -= quantidade
        nome_item = self.inventario[id_item]["item"].nome
        print(f"{quantidade}x {nome_item} removido(s) do inventário.")
        if self.inventario[id_item]["quantidade"] <= 0:
            del self.inventario[id_item]
        return True

    def equipar_item(self, id_item: str):
        if id_item not in self.inventario: return
        item_para_equipar = self.inventario[id_item]["item"]
        if not item_para_equipar.é_equipavel() or not item_para_equipar.pode_equipar(self): return
        slot = item_para_equipar.slot_equipamento
        if self.equipamentos.get(slot) is not None:
            self.desequipar_item(slot)
        if self.remover_item(id_item, 1):
            self.equipamentos[slot] = item_para_equipar
            print(f"{item_para_equipar.nome} equipado no slot {slot.replace('_', ' ')}.")
            self.recalcular_stats_completos()

    def usar_item(self, id_item: str):
        """Usa um item consumível do inventário, aplicando seu efeito."""
        if id_item not in self.inventario:
            print("Você não possui este item.")
            return

        item = self.inventario[id_item]["item"]
        if not item.é_consumivel():
            print(f"{item.nome} não pode ser usado desta forma.")
            return

        efeito = item.efeito_consumo
        tipo_efeito = efeito.get("tipo")
        quantidade_efeito = efeito.get("quantidade", 0)

        print(f"Você usa {item.nome}...")

        if tipo_efeito == "cura_hp":
            self.curar(quantidade_efeito)
        elif tipo_efeito == "cura_mp":
            self.mp_atual = min(self.mp_max, self.mp_atual + quantidade_efeito)
            print(f"{self.nome} recuperou {quantidade_efeito} de Mana. MP atual: {self.mp_atual}/{self.mp_max}")
        else:
            print("Este item não tem um efeito conhecido.")
            return

        self.remover_item(id_item, 1)

    def desequipar_item(self, slot: str):
        if slot not in self.equipamentos or self.equipamentos[slot] is None: return
        item_para_desequipar = self.equipamentos[slot]
        self.adicionar_item(item_para_desequipar.id_item, 1)
        self.equipamentos[slot] = None
        print(f"{item_para_desequipar.nome} desequipado.")
        self.recalcular_stats_completos()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "nome": self.nome, "raca": self.raca, "classe": self.classe, "nivel": self.nivel,
            "xp_atual": self.xp_atual, "pontos_de_atributo_para_distribuir": self.pontos_de_atributo_para_distribuir,
            "base_stats": {
                "forca": self.base_forca, "destreza": self.base_destreza, "constituicao": self.base_constituicao,
                "inteligencia": self.base_inteligencia, "sabedoria": self.base_sabedoria, "carisma": self.base_carisma,
                "sorte": self.base_sorte,
            },
            "hp_atual": self.hp_atual, "mp_atual": self.mp_atual, "stamina_atual": self.stamina_atual,
            "inventario": {k: v["quantidade"] for k, v in self.inventario.items()},
            "ouro": self.ouro,
            "equipamentos": {s: i.id_item if i else None for s, i in self.equipamentos.items()},
            "habilidades": self.habilidades,
            "ataques_base": [a["id_ataque"] for a in self.ataques_base],
            "efeitos_ativos": [e.to_dict() for e in self.efeitos_ativos],
            "quests_ativas": [q.to_dict() for q in self.quests_ativas],
            "quests_concluidas": self.quests_concluidas,
            "reputacao": self.reputacao,
        }

    @classmethod
    def from_dict(cls, dados: Dict[str, Any]) -> 'Personagem':
        from .efeito import Efeito
        from .quest import Quest, EstadoQuest
        from rpg.dados.quests_ato1 import QUESTS_ATO1
        from rpg.dados.efeitos import TODOS_OS_EFEITOS

        personagem = cls(nome=dados["nome"], nivel=dados["nivel"])
        personagem.raca = dados["raca"]
        personagem.classe = dados["classe"]
        personagem.xp_atual = dados["xp_atual"]
        personagem.pontos_de_atributo_para_distribuir = dados["pontos_de_atributo_para_distribuir"]
        personagem.ouro = dados["ouro"]

        for stat, valor in dados["base_stats"].items():
            setattr(personagem, f"base_{stat}", valor)

        for id_item, quantidade in dados["inventario"].items():
            personagem.adicionar_item(id_item, quantidade)

        for slot, id_item in dados["equipamentos"].items():
            if id_item:
                personagem.equipar_item(id_item)

        personagem.habilidades = dados["habilidades"]

        # Carrega os ataques base, com um fallback para os padrões
        personagem.ataques_base.clear()
        ataques_ids = dados.get("ataques_base", ["soco", "chute"])
        for id_ataque in ataques_ids:
            if id_ataque in ATAQUES_BASE:
                personagem.ataques_base.append(ATAQUES_BASE[id_ataque])

        personagem.quests_concluidas = dados["quests_concluidas"]
        personagem.reputacao = dados["reputacao"]

        for quest_data in dados.get("quests_ativas", []):
            id_quest = quest_data["id_quest"]
            dados_base_quest = QUESTS_ATO1.get(id_quest)
            if dados_base_quest:
                nova_quest = Quest(id_quest=id_quest, **dados_base_quest)
                nova_quest.estado = EstadoQuest(quest_data["estado"])
                nova_quest.objetivos = quest_data["objetivos"]
                personagem.quests_ativas.append(nova_quest)

        for efeito_data in dados.get("efeitos_ativos", []):
            id_efeito = efeito_data["id_efeito"]
            dados_base_efeito = TODOS_OS_EFEITOS.get(id_efeito)
            if dados_base_efeito:
                novo_efeito = Efeito(id_efeito=id_efeito, **dados_base_efeito)
                novo_efeito.turnos_restantes = efeito_data["turnos_restantes"]
                personagem.efeitos_ativos.append(novo_efeito)

        personagem.recalcular_stats_completos()
        personagem.hp_atual = dados["hp_atual"]
        personagem.mp_atual = dados["mp_atual"]
        personagem.stamina_atual = dados["stamina_atual"]
        return personagem

    def __str__(self) -> str:
        return (
            f"--- {self.nome} (Nível {self.nivel}) ---\n"
            f"HP: {self.hp_atual}/{self.hp_max} | MP: {self.mp_atual}/{self.mp_max}\n"
            f"XP: {self.xp_atual}/{self.xp_para_proximo_nivel}\n"
            f"Pontos para Distribuir: {self.pontos_de_atributo_para_distribuir}\n"
            f"Força: {self.forca} | Destreza: {self.destreza} | Constituição: {self.constituicao}\n"
            f"Inteligência: {self.inteligencia} | Sabedoria: {self.sabedoria} | Carisma: {self.carisma} | Sorte: {self.sorte}\n"
        )
