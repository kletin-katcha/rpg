import random
from typing import List, Dict, Optional, TYPE_CHECKING, Any

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
from rpg.dados.ataques_base import ATAQUES_BASE
from ..dados.itens import TODOS_OS_ITENS
from ..dados.habilidades_passivas_efeitos import HABILIDADES_PASSIVAS_EFEITOS
from .item import Item


class Personagem:
    """
    A classe base para qualquer personagem controlável ou não-controlável no jogo.
    Engloba jogadores, NPCs e potencialmente até certas criaturas com características complexas.
    """
    def __init__(self, nome: str, nivel: int = 1):
        # --- Identificação Básica ---
        self.nome: str = nome
        self.raca: Optional[str] = None # ID da raça
        self.sub_raca: Optional[str] = None # ID da sub-raça/variação
        self.classe: Optional[str] = None # ID da classe
        self.classe_secundaria: Optional[str] = None # ID da classe secundária
        self.nivel: int = nivel
        self.xp_atual: int = 0
        self.xp_para_proximo_nivel: int = self.calcular_xp_necessario(nivel)

        # --- Atributos Primários (Base) ---
        # Estes são os atributos inerentes do personagem, sem modificadores.
        self.base_forca: int = 5
        self.base_destreza: int = 5
        self.base_constituicao: int = 5
        self.base_inteligencia: int = 5
        self.base_sabedoria: int = 5
        self.base_carisma: int = 5

        # --- Atributos Primários (Totais) ---
        # Estes incluem bônus de equipamentos e outros efeitos. São recalculados.
        self.forca: int = 0
        self.destreza: int = 0
        self.constituicao: int = 0
        self.inteligencia: int = 0
        self.sabedoria: int = 0
        self.carisma: int = 0

        # --- Recursos (HP, MP, Stamina) ---
        self.hp_max: int = 0
        self.hp_atual: int = 0
        self.mp_max: int = 0
        self.mp_atual: int = 0
        self.stamina_max: int = 100
        self.stamina_atual: int = 100

        # --- Atributos de Combate Derivados ---
        # Estes serão recalculados com base nos atributos primários e equipamentos
        self.dano_arma_bonus: int = 0
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
        # O inventário agora é um dicionário para empilhar itens.
        # Estrutura: { "id_item": {"item": ObjetoItem, "quantidade": int} }
        self.inventario: Dict[str, Dict[str, Any]] = {}
        self.ouro: int = 100
        self.equipamentos: Dict[str, Optional['Item']] = {
            "arma_principal": None, "arma_secundaria": None,
            "elmo": None, "peitoral": None, "calcas": None, "botas": None,
            "luvas": None, "amuleto": None, "anel_1": None, "anel_2": None
        }

        # --- Habilidades e Efeitos ---
        self.habilidades: List[str] = [] # Lista de IDs de habilidades
        self.ataques_base: List[Dict] = [ATAQUES_BASE["soco"], ATAQUES_BASE["chute"]] # Ataques básicos disponíveis
        self.efeitos_ativos: List['Efeito'] = []

        # --- Quests ---
        self.quests_ativas: List['Quest'] = []
        self.quests_concluidas: List[str] = [] # Armazena IDs das quests concluídas

        # --- Localização e Reputação ---
        self.cidade_atual: str = "vila_aurora"
        self.reino_atual: str = "valedourado"

        # --- Reputação ---
        self.reputacao: Dict[str, int] = { # Ex: "Guilda dos Ladrões": 50
            "cidade_inicial": 0,
        }

        # --- Construções / Automação ---
        self.estruturas_construidas: set[str] = set()
        self.niveis_estruturas: Dict[str, int] = {}
        self.plano_producao_ativo: Optional[str] = None

        # Recalcular todos os stats derivados na inicialização
        self.recalcular_stats_completos()
        # Garante que o personagem começa com os recursos no máximo
        self.hp_atual = self.hp_max
        self.mp_atual = self.mp_max
        self.stamina_atual = self.stamina_max

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
        # Etapa 1: Acumular todos os bônus de equipamentos e habilidades passivas.
        bonus = {
            'forca': 0, 'destreza': 0, 'constituicao': 0, 'inteligencia': 0,
            'sabedoria': 0, 'carisma': 0, 'hp_max': 0, 'mp_max': 0,
            'ataque_fisico': 0, 'poder_magico': 0, 'defesa_fisica': 0,
            'defesa_magica': 0, 'precisao': 0, 'esquiva': 0,
            'dano_arma_bonus': 0, 'chance_critico': 0,
            'resistencias': {}
        }

        # Acumula bônus de itens
        for item in self.equipamentos.values():
            if item and item.modificadores:
                for mod, valor in item.modificadores.items():
                    mod_real = 'dano_arma_bonus' if mod == 'dano_arma' else mod
                    if mod_real in bonus:
                        bonus[mod_real] += valor

        # Acumula bônus de habilidades passivas
        for hab_id in self.habilidades:
            if hab_id in HABILIDADES_PASSIVAS_EFEITOS:
                efeito = HABILIDADES_PASSIVAS_EFEITOS[hab_id]
                attr = efeito["atributo"]
                if attr in bonus:
                    if "chave" in efeito: # Para atributos que são dicionários, como resistências
                        sub_chave = efeito["chave"]
                        if attr not in bonus: bonus[attr] = {}
                        bonus[attr][sub_chave] = bonus[attr].get(sub_chave, 0) + efeito["valor"]
                    else:
                        bonus[attr] += efeito["valor"]

        # Acumula bônus de efeitos temporários (buffs/debuffs)
        for efeito_ativo in self.efeitos_ativos:
            if efeito_ativo.modificadores:
                for mod, valor in efeito_ativo.modificadores.items():
                    if mod in bonus:
                        bonus[mod] += valor
                    # Caso especial para resistências
                    elif mod.startswith("resistencia_"):
                         res_chave = mod.replace("resistencia_", "")
                         if res_chave in self.resistencias:
                            if 'resistencias' not in bonus: bonus['resistencias'] = {}
                            bonus['resistencias'][res_chave] = bonus['resistencias'].get(res_chave, 0) + valor


        # Etapa 2: Aplicar bônus aos atributos primários.
        self.forca = self.base_forca + bonus['forca']
        self.destreza = self.base_destreza + bonus['destreza']
        self.constituicao = self.base_constituicao + bonus['constituicao']
        self.inteligencia = self.base_inteligencia + bonus['inteligencia']
        self.sabedoria = self.base_sabedoria + bonus['sabedoria']
        self.carisma = self.base_carisma + bonus['carisma']

        # Etapa 3: Manter controle do HP/MP para ajustar o valor atual.
        hp_antigo = self.hp_max
        mp_antigo = self.mp_max

        # Etapa 4: Calcular os status derivados usando os atributos finais e os bônus diretos.
        # Primeiro, o cálculo base a partir dos atributos primários.
        self.hp_max = self.calcular_hp_max() # Supondo que isso use self.constituicao
        self.mp_max = self.calcular_mp_max() # Supondo que isso use self.inteligencia/sabedoria
        self.ataque_fisico = self.forca * 2
        self.poder_magico = self.inteligencia * 2
        self.defesa_fisica = self.constituicao // 2
        self.defesa_magica = (self.inteligencia + self.sabedoria) // 2
        self.precisao = self.destreza * 3
        self.esquiva = self.destreza * 2

        # Reseta as resistências para o valor base (0) antes de aplicar bônus
        for r in self.resistencias:
            self.resistencias[r] = 0.0

        # Agora, adicione os bônus diretos (flat bonuses) de equipamentos e passivas.
        self.hp_max += bonus['hp_max']
        self.mp_max += bonus['mp_max']
        self.ataque_fisico += bonus['ataque_fisico']
        self.poder_magico += bonus['poder_magico']
        self.defesa_fisica += bonus['defesa_fisica']
        self.defesa_magica += bonus['defesa_magica']
        self.precisao += bonus['precisao']
        self.esquiva += bonus['esquiva']
        self.dano_arma_bonus = bonus['dano_arma_bonus'] # É um valor direto, não somado.

        for res, val in bonus['resistencias'].items():
            if res in self.resistencias:
                self.resistencias[res] += val

        # Etapa 5: Ajustar HP e MP atuais após mudança no máximo.
        if self.hp_max > hp_antigo and hp_antigo != 0:
            self.hp_atual += self.hp_max - hp_antigo
        if self.mp_max > mp_antigo and mp_antigo != 0:
            self.mp_atual += self.mp_max - mp_antigo

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
        self.base_forca += 1
        self.base_destreza += 1
        self.base_constituicao += 2
        self.base_inteligencia += 1
        self.base_sabedoria += 1
        self.base_carisma += 1

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
        self.hp_atual = max(0, self.hp_atual - dano_final)
        print(f"{self.nome} tomou {dano_final} de dano. HP restante: {self.hp_atual}/{self.hp_max}")
        if not self.esta_vivo():
            print(f"{self.nome} foi derrotado.")

    def curar(self, quantidade: int):
        """Cura o personagem, sem exceder o HP máximo."""
        self.hp_atual = min(self.hp_max, self.hp_atual + quantidade)
        print(f"{self.nome} recuperou {quantidade} de HP. HP atual: {self.hp_atual}/{self.hp_max}")

    def adicionar_item(self, id_item: str, quantidade: int = 1):
        """Adiciona um item ao inventário, empilhando se já existir."""
        dados_item = TODOS_OS_ITENS.get(id_item)
        if not dados_item:
            print(f"ALERTA: Tentativa de adicionar item desconhecido: {id_item}")
            return

        if id_item in self.inventario:
            self.inventario[id_item]["quantidade"] += quantidade
        else:
            novo_item = Item(id_item=id_item, **dados_item)
            self.inventario[id_item] = {"item": novo_item, "quantidade": quantidade}

        # O narrador seria melhor aqui, mas print para consistência com outras funções.
        print(f"{quantidade}x {dados_item['nome']} adicionado(s) ao inventário.")

    def remover_item(self, id_item: str, quantidade: int = 1) -> bool:
        """Remove uma quantidade de um item do inventário. Retorna True se bem-sucedido."""
        if id_item not in self.inventario:
            # print(f"ALERTA: Tentativa de remover item que não está no inventário: {id_item}")
            return False

        if self.inventario[id_item]["quantidade"] < quantidade:
            # print(f"ALERTA: Não há quantidade suficiente de {id_item} para remover.")
            return False

        self.inventario[id_item]["quantidade"] -= quantidade
        nome_item = self.inventario[id_item]["item"].nome
        print(f"{quantidade}x {nome_item} removido(s) do inventário.")

        if self.inventario[id_item]["quantidade"] <= 0:
            del self.inventario[id_item]

        return True

    def usar_item(self, id_item: str):
        """Usa um item do inventário, aplicando seu efeito."""
        if id_item not in self.inventario:
            print("Você não possui este item.")
            return

        item = self.inventario[id_item]["item"]
        if not item.é_consumivel():
            print(f"{item.nome} não pode ser usado.")
            return

        efeito = item.efeito_consumo
        tipo_efeito = efeito.get("tipo")
        quantidade_efeito = efeito.get("quantidade", 0)

        print(f"Você usa {item.nome}...")

        if tipo_efeito == "cura_hp":
            self.curar(quantidade_efeito)
        elif tipo_efeito == "cura_mp":
            # Precisamos de um método para restaurar mana, similar ao curar()
            self.mp_atual = min(self.mp_max, self.mp_atual + quantidade_efeito)
            print(f"{self.nome} recuperou {quantidade_efeito} de Mana. MP atual: {self.mp_atual}/{self.mp_max}")
        # TODO: Adicionar outros tipos de efeitos (ex: remover_efeito, buff_temporario)
        else:
            print("Este item não tem um efeito conhecido.")
            return # Não remove o item se o efeito não for aplicado

        # Remove o item do inventário após o uso
        self.remover_item(id_item, 1)

    def equipar_item(self, id_item: str):
        """Equipa um item do inventário."""
        if id_item not in self.inventario:
            print("Você não possui este item para equipar.")
            return

        item_para_equipar = self.inventario[id_item]["item"]

        if not item_para_equipar.é_equipavel():
            print(f"{item_para_equipar.nome} não é um item equipável.")
            return

        # Verifica se o personagem cumpre os requisitos
        if not item_para_equipar.pode_equipar(self):
            print(f"Você não cumpre os requisitos para equipar {item_para_equipar.nome}.")
            return

        slot = item_para_equipar.slot_equipamento

        # Se já houver um item no slot, desequipa primeiro
        if self.equipamentos.get(slot) is not None:
            self.desequipar_item(slot)

        # Remove o item do inventário e o coloca no slot de equipamento
        if self.remover_item(id_item, 1):
            self.equipamentos[slot] = item_para_equipar
            print(f"{item_para_equipar.nome} equipado no slot {slot.replace('_', ' ')}.")
            self.recalcular_stats_completos()
        else:
            # Isso não deveria acontecer se a verificação inicial passou, mas é uma segurança
            print(f"Erro ao tentar equipar {item_para_equipar.nome}.")

    def desequipar_item(self, slot: str):
        """Desequipa um item, movendo-o de volta para o inventário."""
        if slot not in self.equipamentos or self.equipamentos[slot] is None:
            print(f"Nenhum item equipado no slot {slot.replace('_', ' ')}.")
            return

        item_para_desequipar = self.equipamentos[slot]

        # Adiciona o item de volta ao inventário
        self.adicionar_item(item_para_desequipar.id_item, 1)

        # Limpa o slot de equipamento
        self.equipamentos[slot] = None

        print(f"{item_para_desequipar.nome} desequipado.")
        self.recalcular_stats_completos()

    def __str__(self) -> str:
        return (
            f"--- {self.nome} (Nível {self.nivel}) ---\n"
            f"HP: {self.hp_atual}/{self.hp_max} | MP: {self.mp_atual}/{self.mp_max}\n"
            f"XP: {self.xp_atual}/{self.xp_para_proximo_nivel}\n"
            f"Força: {self.forca} | Destreza: {self.destreza} | Constituição: {self.constituicao}\n"
            f"Inteligência: {self.inteligencia} | Sabedoria: {self.sabedoria} | Carisma: {self.carisma}\n"
        )
