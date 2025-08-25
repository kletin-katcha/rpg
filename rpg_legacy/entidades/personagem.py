# rpg_legacy/entidades/personagem.py (fully documented version)
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
from rpg_legacy.dados.ataques_base import ATAQUES_BASE
from ..dados.itens import TODOS_OS_ITENS
from ..dados.habilidades_passivas_efeitos import HABILIDADES_PASSIVAS_EFEITOS
from .item import Item


class Personagem:
    """
    A classe Personagem é o coração de todas as entidades vivas e interativas no mundo do jogo.
    Ela representa o jogador, NPCs importantes, e até mesmo inimigos complexos que podem
    usar inventário, habilidades e equipamentos.

    Esta classe é projetada para ser extremamente flexível e data-driven, onde os
    atributos, habilidades e status são modificados dinamicamente por um sistema
    robusto de recálculo que leva em conta bônus de equipamentos, efeitos de status
    temporários (buffs/debuffs) e habilidades passivas.

    Atributos:
        nome (str): O nome do personagem.
        raca (Optional[str]): O ID da raça do personagem, que influencia atributos base.
        classe (Optional[str]): O ID da classe do personagem, que define habilidades e progressão.
        nivel (int): O nível atual do personagem.
        xp_atual (int): A quantidade de experiência atual.
        xp_para_proximo_nivel (int): A quantidade de experiência necessária para o próximo nível.
        pontos_de_atributo_para_distribuir (int): Pontos acumulados ao subir de nível para gastar.

        base_forca (int): Força inerente, sem modificadores.
        base_destreza (int): Destreza inerente, sem modificadores.
        base_constituicao (int): Constituição inerente, sem modificadores.
        base_inteligencia (int): Inteligência inerente, sem modificadores.
        base_sabedoria (int): Sabedoria inerente, sem modificadores.
        base_carisma (int): Carisma inerente, sem modificadores.
        base_sorte (int): Sorte inerente, sem modificadores.

        forca (int): Força total, incluindo todos os bônus.
        # ... (e assim por diante para todos os outros atributos totais)

        hp_max (int): Pontos de vida máximos.
        hp_atual (int): Pontos de vida atuais.
        # ... (e assim por diante para mp e stamina)

        inventario (Dict): Dicionário que armazena os itens do personagem.
        equipamentos (Dict): Dicionário que representa os slots de equipamento do personagem.
        habilidades (List): Lista de IDs das habilidades que o personagem conhece.
        efeitos_ativos (List): Lista de objetos de Efeito atualmente aplicados ao personagem.
    """
    def __init__(self, nome: str, nivel: int = 1):
        """
        Inicializa um novo objeto Personagem.

        Args:
            nome (str): O nome para o personagem.
            nivel (int, optional): O nível inicial do personagem. Defaults to 1.
        """
        # ======================================================================
        # SEÇÃO 1: IDENTIFICAÇÃO E PROGRESSÃO
        # Atributos que definem quem o personagem é e como ele progride no jogo.
        # ======================================================================
        self.nome: str = nome
        self.raca: Optional[str] = None # ID da raça (ex: "humano", "elfo_da_floresta")
        self.classe: Optional[str] = None # ID da classe (ex: "guerreiro", "mago_arcano")
        self.nivel: int = nivel
        self.xp_atual: int = 0
        self.xp_para_proximo_nivel: int = self.calcular_xp_necessario(nivel)
        self.pontos_de_atributo_para_distribuir: int = 0 # Pontos para gastar ao subir de nível

        # ======================================================================
        # SEÇÃO 2: ATRIBUTOS PRIMÁRIOS
        # A base para todos os cálculos de combate e interação. Divididos em
        # 'base' (valor inerente) e 'total' (valor com bônus).
        # ======================================================================
        # --- Atributos Base (Inerentes) ---
        self.base_forca: int = 5
        self.base_destreza: int = 5
        self.base_constituicao: int = 5
        self.base_inteligencia: int = 5
        self.base_sabedoria: int = 5
        self.base_carisma: int = 5
        self.base_sorte: int = 5

        # --- Atributos Totais (com bônus de equipamentos, buffs, etc.) ---
        self.forca: int = 0
        self.destreza: int = 0
        self.constituicao: int = 0
        self.inteligencia: int = 0
        self.sabedoria: int = 0
        self.carisma: int = 0
        self.sorte: int = 0

        # ======================================================================
        # SEÇÃO 3: RECURSOS VITAIS
        # Pontos de vida, mana e stamina.
        # ======================================================================
        self.hp_max: int = 0
        self.hp_atual: int = 0
        self.mp_max: int = 0
        self.mp_atual: int = 0
        self.stamina_max: int = 100  # Stamina pode ter uma lógica diferente, começando fixa.
        self.stamina_atual: int = 100

        # ======================================================================
        # SEÇÃO 4: ATRIBUTOS DE COMBATE DERIVADOS
        # Stats calculados a partir dos atributos primários e equipamentos.
        # ======================================================================
        self.dano_arma_bonus: int = 0       # Bônus de dano direto da arma equipada.
        self.ataque_fisico: int = 0         # Poder de ataque físico geral.
        self.poder_magico: int = 0          # Poder de ataque mágico geral.
        self.defesa_fisica: int = 0         # Capacidade de reduzir dano físico.
        self.defesa_magica: int = 0         # Capacidade de reduzir dano mágico.
        self.precisao: int = 0              # Influencia a chance de acertar ataques.
        self.esquiva: int = 0               # Influencia a chance de evitar ataques.
        self.chance_critico: float = 0.05   # Chance base de 5% de causar um acerto crítico.
        self.multiplicador_critico: float = 1.5 # Dano de um acerto crítico é 150% do normal.

        # ======================================================================
        # SEÇÃO 5: RESISTÊNCIAS
        # Percentual de redução de dano de várias fontes.
        # ======================================================================
        self.resistencias: Dict[str, float] = {
            "fogo": 0.0, "gelo": 0.0, "raio": 0.0, "veneno": 0.0,
            "sagrado": 0.0, "sombra": 0.0, "fisico": 0.0, "magico": 0.0,
            "atordoamento": 0.0, "silencio": 0.0, "medo": 0.0
        }

        # ======================================================================
        # SEÇÃO 6: INVENTÁRIO E EQUIPAMENTOS
        # Itens que o personagem carrega e que estão em uso.
        # ======================================================================
        # O inventário usa um dicionário para empilhar itens de forma eficiente.
        # Estrutura: { "id_do_item": {"item": ObjetoItem, "quantidade": int} }
        self.inventario: Dict[str, Dict[str, Any]] = {}
        self.ouro: int = 100
        # Dicionário de slots de equipamento. A chave é o nome do slot, o valor é o objeto Item ou None.
        self.equipamentos: Dict[str, Optional['Item']] = {
            "arma_principal": None, "arma_secundaria": None,
            "elmo": None, "peitoral": None, "calcas": None, "botas": None,
            "luvas": None, "amuleto": None, "anel_1": None, "anel_2": None
        }

        # ======================================================================
        # SEÇÃO 7: HABILIDADES E EFEITOS
        # Capacidades ativas, passivas e status temporários.
        # ======================================================================
        self.habilidades: List[str] = [] # Lista de IDs de habilidades conhecidas
        self.ataques_base: List[Dict] = [ATAQUES_BASE["soco"], ATAQUES_BASE["chute"]] # Ataques básicos sempre disponíveis
        self.efeitos_ativos: List['Efeito'] = [] # Lista de buffs/debuffs ativos

        # ======================================================================
        # SEÇÃO 8: QUESTS E REPUTAÇÃO
        # Acompanhamento do progresso narrativo e social.
        # ======================================================================
        self.quests_ativas: List['Quest'] = []
        self.quests_concluidas: List[str] = [] # Armazena apenas os IDs das quests concluídas para referência
        self.reputacao: Dict[str, int] = { # Ex: "Guilda dos Ladrões": 50, "Reino de Eldoria": -20
            "cidade_inicial": 0,
        }

        # ======================================================================
        # INICIALIZAÇÃO FINAL
        # ======================================================================
        # Recalcula todos os stats derivados na criação do personagem para garantir consistência.
        self.recalcular_stats_completos()
        # Garante que o personagem começa com os recursos no máximo.
        self.hp_atual = self.hp_max
        self.mp_atual = self.mp_max
        self.stamina_atual = self.stamina_max

    def calcular_xp_necessario(self, nivel: int) -> int:
        """
        Calcula a quantidade de experiência (XP) necessária para atingir o próximo nível.
        A fórmula usa uma curva exponencial para que níveis mais altos exijam mais XP,
        tornando a progressão mais desafiadora no final do jogo.

        Args:
            nivel (int): O nível atual para o qual a necessidade de XP está sendo calculada.

        Returns:
            int: A quantidade total de XP necessária para passar para o próximo nível.
        """
        # Fórmula: 100 * (nivel ^ 1.5). O 'int' garante que o resultado seja um número inteiro.
        return int(100 * (nivel ** 1.5))

    def calcular_hp_max(self) -> int:
        """
        Calcula os pontos de vida (HP) máximos do personagem.
        O HP é determinado principalmente pela Constituição, mas também aumenta com o nível,
        refletindo a crescente resiliência do personagem.

        Returns:
            int: O total de pontos de vida máximos.
        """
        # Fórmula: 80 (base) + (Constituição * 10) + (Nível * 20)
        return 80 + (self.constituicao * 10) + (self.nivel * 20)

    def calcular_mp_max(self) -> int:
        """
        Calcula os pontos de mana (MP) máximos do personagem.
        O MP é determinado pela Inteligência (poder arcano bruto) e Sabedoria (eficiência e controle),
        e também aumenta com o nível.

        Returns:
            int: O total de pontos de mana máximos.
        """
        # Fórmula: 30 (base) + (Inteligência * 7) + (Sabedoria * 3) + (Nível * 10)
        return 30 + (self.inteligencia * 7) + (self.sabedoria * 3) + (self.nivel * 10)

    def recalcular_stats_completos(self):
        """
        Este é um dos métodos mais importantes da classe. Ele recalcula TODOS os atributos
        derivados e totais do personagem. Deve ser chamado sempre que um item é equipado/desequipado,
        um buff/debuff é aplicado/removido, ou o personagem sobe de nível.

        O processo é dividido em etapas para garantir a ordem correta de operações:
        1. Acumular todos os bônus de todas as fontes (itens, passivas, efeitos).
        2. Calcular os atributos primários totais (ex: Força total = Força base + bônus).
        3. Calcular os atributos secundários/derivados (ex: HP, ataque) com base nos primários totais.
        4. Adicionar bônus diretos (flat) aos atributos secundários.
        5. Ajustar os valores atuais de recursos (HP/MP) para refletir as mudanças nos máximos.
        """
        # Etapa 1: Acumular todos os bônus de equipamentos, habilidades passivas e efeitos ativos.
        # O dicionário 'bonus' serve como um acumulador temporário para todos os modificadores.
        bonus = {
            'forca': 0, 'destreza': 0, 'constituicao': 0, 'inteligencia': 0,
            'sabedoria': 0, 'carisma': 0, 'sorte': 0, 'hp_max': 0, 'mp_max': 0,
            'ataque_fisico': 0, 'poder_magico': 0, 'defesa_fisica': 0,
            'defesa_magica': 0, 'precisao': 0, 'esquiva': 0,
            'dano_arma_bonus': 0, 'chance_critico': 0,
            'resistencias': {}
        }

        # Acumula bônus de itens equipados.
        for item in self.equipamentos.values():
            if item and item.modificadores:
                for mod, valor in item.modificadores.items():
                    # 'dano_arma' é um caso especial que mapeia para 'dano_arma_bonus' no acumulador.
                    mod_real = 'dano_arma_bonus' if mod == 'dano_arma' else mod
                    if mod_real in bonus:
                        bonus[mod_real] += valor

        # Acumula bônus de habilidades passivas conhecidas.
        for hab_id in self.habilidades:
            if hab_id in HABILIDADES_PASSIVAS_EFEITOS:
                efeito = HABILIDADES_PASSIVAS_EFEITOS[hab_id]
                attr = efeito["atributo"]
                if attr in bonus:
                    # Lógica para atributos que são dicionários, como resistências.
                    if "chave" in efeito:
                        sub_chave = efeito["chave"]
                        if attr not in bonus: bonus[attr] = {}
                        bonus[attr][sub_chave] = bonus[attr].get(sub_chave, 0) + efeito["valor"]
                    else:
                        bonus[attr] += efeito["valor"]

        # Acumula bônus de efeitos temporários (buffs/debuffs).
        for efeito_ativo in self.efeitos_ativos:
            if efeito_ativo.modificadores:
                for mod, valor in efeito_ativo.modificadores.items():
                    if mod in bonus:
                        bonus[mod] += valor
                    # Caso especial para resistências, que não estão no dicionário 'bonus' principal.
                    elif mod.startswith("resistencia_"):
                         res_chave = mod.replace("resistencia_", "")
                         if res_chave in self.resistencias:
                            if 'resistencias' not in bonus: bonus['resistencias'] = {}
                            bonus['resistencias'][res_chave] = bonus['resistencias'].get(res_chave, 0) + valor


        # Etapa 2: Aplicar bônus acumulados aos atributos primários base para obter os totais.
        self.forca = self.base_forca + bonus['forca']
        self.destreza = self.base_destreza + bonus['destreza']
        self.constituicao = self.base_constituicao + bonus['constituicao']
        self.inteligencia = self.base_inteligencia + bonus['inteligencia']
        self.sabedoria = self.base_sabedoria + bonus['sabedoria']
        self.carisma = self.base_carisma + bonus['carisma']
        self.sorte = self.base_sorte + bonus['sorte']

        # Etapa 3: Salvar os valores antigos de HP/MP para ajustar os atuais mais tarde.
        hp_antigo = self.hp_max
        mp_antigo = self.mp_max

        # Etapa 4: Calcular os status derivados usando os atributos primários totais.
        self.hp_max = self.calcular_hp_max()
        self.mp_max = self.calcular_mp_max()
        self.ataque_fisico = self.forca * 2
        self.poder_magico = self.inteligencia * 2
        self.defesa_fisica = self.constituicao // 2
        self.defesa_magica = (self.inteligencia + self.sabedoria) // 2
        self.precisao = self.destreza * 3
        self.esquiva = self.destreza * 2
        # Chance de crítico base de 5% + 0.1% por ponto de Sorte.
        self.chance_critico = 0.05 + (self.sorte * 0.001)

        # Reseta as resistências para o valor base (0) antes de aplicar os bônus acumulados.
        for r in self.resistencias:
            self.resistencias[r] = 0.0

        # Agora, adicione os bônus diretos (flat bonuses) de equipamentos e passivas aos stats derivados.
        self.hp_max += bonus['hp_max']
        self.mp_max += bonus['mp_max']
        self.ataque_fisico += bonus['ataque_fisico']
        self.poder_magico += bonus['poder_magico']
        self.defesa_fisica += bonus['defesa_fisica']
        self.defesa_magica += bonus['defesa_magica']
        self.precisao += bonus['precisao']
        self.esquiva += bonus['esquiva']
        self.dano_arma_bonus = bonus['dano_arma_bonus']
        self.chance_critico += bonus['chance_critico'] # Adiciona bônus de itens/habilidades à chance de crítico.

        # Adiciona os bônus de resistência.
        for res, val in bonus['resistencias'].items():
            if res in self.resistencias:
                self.resistencias[res] += val

        # Etapa 5: Ajustar HP e MP atuais após mudança no máximo, para evitar ficar com HP baixo após
        # equipar um item de constituição, por exemplo.
        if self.hp_max > hp_antigo and hp_antigo != 0:
            self.hp_atual += self.hp_max - hp_antigo
        if self.mp_max > mp_antigo and mp_antigo != 0:
            self.mp_atual += self.mp_max - mp_antigo

        # Garante que os valores atuais não excedam os novos máximos.
        self.hp_atual = min(self.hp_atual, self.hp_max)
        self.mp_atual = min(self.mp_atual, self.mp_max)

    def esta_vivo(self) -> bool:
        """
        Verifica se o personagem ainda tem pontos de vida.

        Returns:
            bool: True se hp_atual for maior que 0, False caso contrário.
        """
        return self.hp_atual > 0

    def ganhar_xp(self, quantidade: int):
        """
        Adiciona uma quantidade de XP ao personagem e verifica se ele subiu de nível.
        Pode acionar múltiplas subidas de nível se o XP ganho for suficiente.

        Args:
            quantidade (int): A quantidade de experiência a ser adicionada.
        """
        if not self.esta_vivo():
            return

        self.xp_atual += quantidade
        print(f"{self.nome} ganhou {quantidade} de XP!")

        # Loop para permitir múltiplas subidas de nível de uma vez.
        while self.xp_atual >= self.xp_para_proximo_nivel:
            self.subir_nivel()

    def subir_nivel(self):
        """
        Executa a lógica de subida de nível. Aumenta o nível, ajusta o XP,
        e concede pontos de atributo para serem distribuídos pelo jogador,
        de acordo com as regras de progressão do jogo.
        """
        # Consome o XP necessário para o nível atual.
        self.xp_atual -= self.xp_para_proximo_nivel
        self.nivel += 1
        # Calcula o novo teto de XP para o próximo nível.
        self.xp_para_proximo_nivel = self.calcular_xp_necessario(self.nivel)

        # Concede pontos de atributo com base na faixa de nível do personagem.
        if 1 <= self.nivel <= 10:
            pontos_ganhos = 5
        elif 11 <= self.nivel <= 25:
            pontos_ganhos = 3
        elif 26 <= self.nivel <= 50:
            pontos_ganhos = 2
        else: # Nível 51+
            pontos_ganhos = 1

        self.pontos_de_atributo_para_distribuir += pontos_ganhos

        # Recalcula todos os stats e cura completamente o personagem.
        self.recalcular_stats_completos()
        self.hp_atual = self.hp_max
        self.mp_atual = self.mp_max

        print(f"🎉 {self.nome} subiu para o nível {self.nivel}! 🎉")
        print(f"Você ganhou {pontos_ganhos} pontos de atributo para distribuir!")
        print(f"HP: {self.hp_max} | MP: {self.mp_max}")

    def distribuir_pontos_de_atributo(self, distribuicao: Dict[str, int]) -> bool:
        """
        Distribui os pontos de atributo que o personagem acumulou ao subir de nível.
        A interface do usuário (em `io` ou `ui`) será responsável por coletar
        a 'distribuicao' do jogador e chamar este método.

        Args:
            distribuicao (Dict[str, int]): Um dicionário onde as chaves são os nomes dos
                                           atributos (ex: 'forca') e os valores são
                                           quantos pontos alocar.

        Returns:
            bool: True se a distribuição for bem-sucedida, False caso contrário
                  (ex: não há pontos suficientes).
        """
        pontos_a_gastar = sum(distribuicao.values())

        # Validação: Verifica se o jogador tem pontos suficientes.
        if pontos_a_gastar > self.pontos_de_atributo_para_distribuir:
            print("Você não tem pontos de atributo suficientes.")
            return False

        # Validação: Impede a alocação de pontos negativos.
        if any(v < 0 for v in distribuicao.values()):
            print("Não é possível alocar um número negativo de pontos.")
            return False

        # Aplica os pontos aos atributos base.
        if 'forca' in distribuicao: self.base_forca += distribuicao['forca']
        if 'destreza' in distribuicao: self.base_destreza += distribuicao['destreza']
        if 'constituicao' in distribuicao: self.base_constituicao += distribuicao['constituicao']
        if 'inteligencia' in distribuicao: self.base_inteligencia += distribuicao['inteligencia']
        if 'sabedoria' in distribuicao: self.base_sabedoria += distribuicao['sabedoria']
        if 'carisma' in distribuicao: self.base_carisma += distribuicao['carisma']
        if 'sorte' in distribuicao: self.base_sorte += distribuicao['sorte']

        # Subtrai os pontos gastos do total disponível.
        self.pontos_de_atributo_para_distribuir -= pontos_a_gastar
        # Recalcula todos os stats para refletir as mudanças.
        self.recalcular_stats_completos()

        print("Pontos de atributo distribuídos com sucesso!")
        return True

    def tomar_dano(self, quantidade_dano: int, tipo_dano: str = "fisico"):
        """
        Aplica dano ao HP do personagem. Esta função recebe o valor final do dano,
        já calculado pelo sistema de combate (que considera defesa, resistências, etc.).

        Args:
            quantidade_dano (int): O montante de dano a ser subtraído do HP.
            tipo_dano (str, optional): O tipo de dano (não usado aqui, mas útil para logs
                                       ou efeitos que reagem a tipos de dano). Defaults to "fisico".
        """
        dano_final = max(0, quantidade_dano) # Garante que o dano não seja negativo.
        self.hp_atual = max(0, self.hp_atual - dano_final)
        print(f"{self.nome} tomou {dano_final} de dano. HP restante: {self.hp_atual}/{self.hp_max}")
        if not self.esta_vivo():
            print(f"💀 {self.nome} foi derrotado. 💀")

    def curar(self, quantidade: int):
        """
        Restaura os pontos de vida do personagem.

        Args:
            quantidade (int): A quantidade de HP a ser restaurada.
        """
        # Garante que a cura não exceda o HP máximo.
        self.hp_atual = min(self.hp_max, self.hp_atual + quantidade)
        print(f"{self.nome} recuperou {quantidade} de HP. HP atual: {self.hp_atual}/{self.hp_max}")

    def adicionar_item(self, id_item: str, quantidade: int = 1):
        """
        Adiciona um item ao inventário do personagem. Se o item já existir e for
        empilhável, a quantidade é incrementada. Caso contrário, uma nova entrada é criada.

        Args:
            id_item (str): O ID único do item a ser adicionado.
            quantidade (int, optional): A quantidade do item a ser adicionada. Defaults to 1.
        """
        dados_item = TODOS_OS_ITENS.get(id_item)
        if not dados_item:
            print(f"ALERTA DE SISTEMA: Tentativa de adicionar item desconhecido: {id_item}")
            return

        # Se o item já está no inventário, apenas aumenta a quantidade.
        if id_item in self.inventario:
            self.inventario[id_item]["quantidade"] += quantidade
        else:
            # Se não, cria o objeto Item e o adiciona ao dicionário.
            novo_item = Item(id_item=id_item, **dados_item)
            self.inventario[id_item] = {"item": novo_item, "quantidade": quantidade}

        print(f"{quantidade}x {dados_item['nome']} adicionado(s) ao inventário.")

    def remover_item(self, id_item: str, quantidade: int = 1) -> bool:
        """
        Remove uma quantidade de um item do inventário.

        Args:
            id_item (str): O ID do item a ser removido.
            quantidade (int, optional): A quantidade a ser removida. Defaults to 1.

        Returns:
            bool: True se a remoção foi bem-sucedida, False caso contrário.
        """
        if id_item not in self.inventario:
            return False

        if self.inventario[id_item]["quantidade"] < quantidade:
            return False

        self.inventario[id_item]["quantidade"] -= quantidade
        nome_item = self.inventario[id_item]["item"].nome
        print(f"{quantidade}x {nome_item} removido(s) do inventário.")

        # Se a quantidade chegar a zero, remove completamente a entrada do item.
        if self.inventario[id_item]["quantidade"] <= 0:
            del self.inventario[id_item]

        return True

    def usar_item(self, id_item: str):
        """
        Usa um item consumível do inventário, aplicando seu efeito.

        Args:
            id_item (str): O ID do item a ser usado.
        """
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

        # Aplica o efeito com base no seu tipo.
        if tipo_efeito == "cura_hp":
            self.curar(quantidade_efeito)
        elif tipo_efeito == "cura_mp":
            self.mp_atual = min(self.mp_max, self.mp_atual + quantidade_efeito)
            print(f"{self.nome} recuperou {quantidade_efeito} de Mana. MP atual: {self.mp_atual}/{self.mp_max}")
        # TODO: Adicionar mais tipos de efeitos (ex: remover_debuff, buff_temporario, etc.)
        else:
            print("Este item não tem um efeito conhecido.")
            return # Não remove o item se o efeito não for aplicado com sucesso.

        # Remove uma unidade do item do inventário após o uso.
        self.remover_item(id_item, 1)

    def equipar_item(self, id_item: str):
        """
        Equipa um item do inventário em seu slot correspondente.
        Se já houver um item no slot, ele é desequipado primeiro.

        Args:
            id_item (str): O ID do item do inventário a ser equipado.
        """
        if id_item not in self.inventario:
            print("Você não possui este item para equipar.")
            return

        item_para_equipar = self.inventario[id_item]["item"]

        if not item_para_equipar.é_equipavel():
            print(f"{item_para_equipar.nome} não é um item equipável.")
            return

        # Verifica se o personagem cumpre os requisitos de nível, força, etc.
        if not item_para_equipar.pode_equipar(self):
            print(f"Você não cumpre os requisitos para equipar {item_para_equipar.nome}.")
            return

        slot = item_para_equipar.slot_equipamento

        # Se já houver um item no slot, o desequipa primeiro, movendo-o para o inventário.
        if self.equipamentos.get(slot) is not None:
            self.desequipar_item(slot)

        # Remove o item do inventário e o coloca no slot de equipamento.
        if self.remover_item(id_item, 1):
            self.equipamentos[slot] = item_para_equipar
            print(f"{item_para_equipar.nome} equipado no slot {slot.replace('_', ' ')}.")
            # É crucial recalcular os stats após qualquer mudança de equipamento.
            self.recalcular_stats_completos()
        else:
            # Esta verificação é uma segurança extra.
            print(f"Erro inesperado ao tentar equipar {item_para_equipar.nome}.")

    def desequipar_item(self, slot: str):
        """
        Desequipa um item de um slot específico, movendo-o de volta para o inventário.

        Args:
            slot (str): O nome do slot de equipamento a ser esvaziado (ex: "arma_principal").
        """
        if slot not in self.equipamentos or self.equipamentos[slot] is None:
            print(f"Nenhum item equipado no slot {slot.replace('_', ' ')}.")
            return

        item_para_desequipar = self.equipamentos[slot]

        # Adiciona o item de volta ao inventário.
        self.adicionar_item(item_para_desequipar.id_item, 1)

        # Limpa o slot de equipamento.
        self.equipamentos[slot] = None

        print(f"{item_para_desequipar.nome} desequipado.")
        # Recalcula os stats para remover os bônus do item desequipado.
        self.recalcular_stats_completos()

    def __str__(self) -> str:
        """
        Fornece uma representação em string do estado atual do personagem,
        útil para depuração e para exibir informações ao jogador.

        Returns:
            str: Uma string formatada com os principais status do personagem.
        """
        return (
            f"--- {self.nome} (Nível {self.nivel}) ---\n"
            f"HP: {self.hp_atual}/{self.hp_max} | MP: {self.mp_atual}/{self.mp_max}\n"
            f"XP: {self.xp_atual}/{self.xp_para_proximo_nivel}\n"
            f"Pontos para Distribuir: {self.pontos_de_atributo_para_distribuir}\n"
            f"Força: {self.forca} | Destreza: {self.destreza} | Constituição: {self.constituicao}\n"
            f"Inteligência: {self.inteligencia} | Sabedoria: {self.sabedoria} | Carisma: {self.carisma} | Sorte: {self.sorte}\n"
        )
