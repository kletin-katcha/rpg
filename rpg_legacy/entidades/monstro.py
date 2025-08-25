# rpg_legacy/entidades/monstro.py (fully documented)
import random
from typing import List, Dict, Any, Optional, TYPE_CHECKING

from .personagem import Personagem
from ..dados.habilidades import TODAS_HABILIDADES
from ..dados.ataques_base import ATAQUES_BASE

if TYPE_CHECKING:
    from .item import Item

class Monstro(Personagem):
    """
    Representa um adversário no jogo, como um goblin, lobo ou dragão.
    Esta classe herda da classe base `Personagem`, o que significa que monstros
    compartilham muitas das mesmas características de um jogador ou NPC, como atributos,
    HP, e a capacidade de ter efeitos de status aplicados a eles.

    A classe `Monstro` se especializa em áreas como comportamento de IA (Inteligência Artificial),
    recompensas por derrota (XP, ouro) e a geração de loot (itens).

    Atributos:
        id_monstro (str): Um identificador único para o tipo de monstro (ex: "goblin_batedor").
        familia (str): A família à qual o monstro pertence (ex: "Goblinoid", "Besta", "Morto-vivo").
        xp_recompensa (int): A quantidade de experiência concedida ao derrotar o monstro.
        loot_table (List[Dict]): Uma lista que define os possíveis itens que o monstro pode dropar.
        comportamento_ia (str): Define o "cérebro" do monstro em combate.
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
        """
        Inicializa uma nova instância de Monstro.

        Args:
            nome (str): O nome do monstro (ex: "Goblin Batedor").
            nivel (int): O nível do monstro, que influencia seus stats.
            id_monstro (str): O ID único para este tipo de monstro.
            familia (str): A família do monstro.
            xp_recompensa (int): XP concedido pela derrota.
            ouro_recompensa (int): Ouro concedido pela derrota.
            loot_table (List[Dict[str, Any]]): A tabela de loot do monstro.
            stats_base (Dict[str, int]): Um dicionário com os atributos base do monstro.
            habilidades_ids (List[str]): Lista de IDs das habilidades que o monstro possui.
            ataques_base_ids (List[str]): Lista de IDs dos ataques básicos que o monstro pode usar.
            comportamento_ia (str, optional): O tipo de IA a ser usado. Defaults to "agressivo".
        """

        # Chama o inicializador da classe pai (Personagem) para configurar atributos comuns.
        super().__init__(nome, nivel)

        # --- Identificação Específica do Monstro ---
        self.id_monstro = id_monstro
        self.familia = familia

        # --- Recompensas por Derrota ---
        self.xp_recompensa = xp_recompensa
        self.ouro = ouro_recompensa # Sobrescreve o ouro base herdado de Personagem.
        self.loot_table = loot_table # Ex: [{"id_item": "pele_lobo", "chance": 0.75, "quantidade": [1, 2]}]

        # --- Configuração de Atributos e Habilidades ---
        self.aplicar_stats_base(stats_base)
        self.habilidades = habilidades_ids # Lista de IDs de habilidades.

        # Armazena os dados completos da habilidade (dicionários) para fácil acesso pela IA.
        self.habilidades_completas = [TODAS_HABILIDADES[id_h] for id_h in habilidades_ids if id_h in TODAS_HABILIDADES]
        # Converte os IDs de ataques básicos em objetos de ataque completos.
        self.ataques_base = [ATAQUES_BASE[id_a] for id_a in ataques_base_ids if id_a in ATAQUES_BASE]

        # --- Inteligência Artificial (IA) ---
        self.comportamento_ia = comportamento_ia # "agressivo", "defensivo", "suporte", "oportunista"
        # Dicionário para rastrear cooldowns de habilidades, prevenindo spam.
        self.cooldowns_habilidades: Dict[str, int] = {h['nome']: 0 for h in self.habilidades_completas}
        # Dicionário para IA adaptativa, pode armazenar informações sobre o combate.
        self.memoria_combate: Dict[str, Any] = {}
        # O alvo atual do monstro no combate.
        self.foco_atual: Optional['Personagem'] = None

        # --- Finalização da Inicialização ---
        # Recalcula todos os stats derivados DEPOIS de aplicar os stats base do monstro.
        self.recalcular_stats_completos()

        # Garante que o monstro comece com HP e MP no máximo.
        self.hp_atual = self.hp_max
        self.mp_atual = self.mp_max

    def aplicar_stats_base(self, stats: Dict[str, int]):
        """
        Aplica os atributos base definidos nos arquivos de dados para este tipo de monstro.
        Como monstros geralmente não usam equipamentos, seus stats base são a principal
        fonte de seu poder. Eles são atribuídos aos `base_` atributos para manter
        consistência com a classe Personagem, permitindo que buffs/debuffs funcionem da mesma forma.

        Args:
            stats (Dict[str, int]): Um dicionário contendo os valores para cada atributo base.
        """
        self.base_forca = stats.get("forca", 5)
        self.base_destreza = stats.get("destreza", 5)
        self.base_constituicao = stats.get("constituicao", 5)
        self.base_inteligencia = stats.get("inteligencia", 5)
        self.base_sabedoria = stats.get("sabedoria", 5)
        self.base_carisma = stats.get("carisma", 1) # Geralmente baixo para monstros.
        self.base_sorte = stats.get("sorte", 5)     # Sorte pode influenciar drops ou acertos críticos.

    def decidir_acao(self, aliados: List['Monstro'], inimigos: List['Personagem']) -> Dict[str, Any]:
        """
        O cérebro do monstro. Decide qual ação tomar com base em seu comportamento de IA.
        Esta é uma implementação de uma IA baseada em regras, com elementos escaláveis
        e adaptativos. A função retorna um dicionário representando a ação escolhida.

        Args:
            aliados (List['Monstro']): Uma lista de monstros aliados no combate.
            inimigos (List['Personagem']): Uma lista de inimigos (geralmente o jogador e seus aliados).

        Returns:
            Dict[str, Any]: Um dicionário descrevendo a ação a ser executada pelo sistema de combate.
                            Ex: {"tipo": "usar_habilidade", "habilidade": {...}, "alvo": <Personagem>}
        """
        inimigos_vivos = [i for i in inimigos if i.esta_vivo()]
        if not inimigos_vivos:
            return {"tipo": "passar_turno"} # Não há ninguém para atacar.

        # Define o alvo principal se não tiver um, ou se o alvo atual estiver morto.
        if not self.foco_atual or not self.foco_atual.esta_vivo():
            self.foco_atual = random.choice(inimigos_vivos)

        # --- IA ESCALÁVEL: Monstros de nível mais alto são mais espertos. ---
        if self.nivel >= 15 and self.comportamento_ia != "suporte":
            # Monstros de elite (nível 15+) focam no inimigo com a menor porcentagem de vida.
            alvo_oportunista = min(inimigos_vivos, key=lambda i: i.hp_atual / i.hp_max)
            if self.foco_atual != alvo_oportunista:
                print(f"[IA Escalável] {self.nome} reavalia a situação e foca em {alvo_oportunista.nome}!")
                self.foco_atual = alvo_oportunista

        # --- LÓGICA DE DECISÃO BASEADA EM REGRAS (Hierárquica) ---

        # 1. AUTOPRESERVAÇÃO (Prioridade Máxima)
        # Se com menos de 30% de vida, tenta usar uma habilidade de cura em si mesmo.
        if self.hp_atual / self.hp_max < 0.3:
            habilidade_cura = self.encontrar_habilidade_por_efeito("cura", "self")
            if habilidade_cura:
                print(f"[IA - Autopreservação] {self.nome} está com pouca vida e decide se curar.")
                return {"tipo": "usar_habilidade", "habilidade": habilidade_cura, "alvo": self}

        # 2. SINERGIA / SUPORTE (Apenas para IAs de Suporte)
        if self.comportamento_ia == "suporte":
            aliado_ferido = self.encontrar_aliado_ferido(aliados)
            if aliado_ferido:
                habilidade_cura_aliado = self.encontrar_habilidade_por_efeito("cura", "aliado_unico")
                if habilidade_cura_aliado:
                    print(f"[IA - Suporte] {self.nome} decide curar seu aliado {aliado_ferido.nome}.")
                    return {"tipo": "usar_habilidade", "habilidade": habilidade_cura_aliado, "alvo": aliado_ferido}

        # 3. ANÁLISE DO ALVO (Tenta ser esperto)
        # Exemplo: se o alvo estiver com um buff de defesa, tenta usar um debuff.
        efeitos_alvo = self.foco_atual.efeitos_ativos
        if any(e.id_efeito == "buff_defesa_grande" for e in efeitos_alvo): # Supondo que tal ID exista nos dados.
            habilidade_debuff = self.encontrar_habilidade_por_efeito("debuff", "inimigo_unico")
            if habilidade_debuff:
                print(f"[IA - Análise] {self.nome} vê a defesa do alvo e tenta aplicar um debuff.")
                return {"tipo": "usar_habilidade", "habilidade": habilidade_debuff, "alvo": self.foco_atual}

        # 4. OFENSIVA COM HABILIDADES (Ação principal)
        habilidade_ofensiva = self.encontrar_habilidade_por_efeito("dano", "inimigo_unico")
        if habilidade_ofensiva:
            # IA Escalável: Monstros de nível alto (25+) têm mais chance de usar habilidades poderosas.
            chance_usar_habilidade = 0.5 if self.nivel < 25 else 0.8
            if random.random() < chance_usar_habilidade:
                print(f"[IA - Ofensiva] {self.nome} decide usar uma habilidade de ataque: {habilidade_ofensiva['nome']}.")
                return {"tipo": "usar_habilidade", "habilidade": habilidade_ofensiva, "alvo": self.foco_atual}

        # 5. AÇÃO PADRÃO: ATAQUE BÁSICO (Fallback)
        # Se nenhuma outra lógica foi acionada, usa um ataque básico.
        ataque_escolhido = random.choice(self.ataques_base) if self.ataques_base else None
        if ataque_escolhido:
            print(f"[IA - Padrão] {self.nome} recorre a um ataque básico: {ataque_escolhido['nome']}.")
            return {"tipo": "ataque_basico", "ataque": ataque_escolhido, "alvo": self.foco_atual}
        else:
            # Fallback de segurança caso o monstro não tenha ataques definidos.
            print(f"[IA - Padrão] {self.nome} tenta atacar mas não tem ações disponíveis e passa o turno.")
            return {"tipo": "passar_turno"}


    def encontrar_habilidade_por_efeito(self, tipo_efeito: str, tipo_alvo: str) -> Optional[Dict]:
        """
        Busca nas habilidades do monstro uma que corresponda a um certo tipo de efeito e alvo.
        A IA usa isso para encontrar ações contextuais (ex: "encontre uma cura para mim mesmo").

        Args:
            tipo_efeito (str): O tipo de efeito desejado (ex: "cura", "dano", "debuff").
            tipo_alvo (str): O tipo de alvo da habilidade (ex: "self", "inimigo_unico").

        Returns:
            Optional[Dict]: O dicionário da habilidade encontrada, ou None se nenhuma for encontrada.
        """
        habilidades_disponiveis = []
        # Filtra habilidades que o monstro pode pagar o custo (MP/Stamina).
        for h in self.habilidades_completas:
            custo_valor = h.get('custo_valor', 0)
            custo_tipo = h.get('custo_tipo')

            pode_pagar = False
            if custo_tipo == 'mp':
                if self.mp_atual >= custo_valor: pode_pagar = True
            elif custo_tipo == 'stamina':
                if self.stamina_atual >= custo_valor: pode_pagar = True
            else: # Habilidades sem custo.
                pode_pagar = True

            if pode_pagar:
                habilidades_disponiveis.append(h)

        # Procura a primeira habilidade que corresponde aos critérios.
        for h in habilidades_disponiveis:
            if h.get("tipo_alvo") == tipo_alvo:
                for efeito in h.get("efeitos", []):
                    if efeito.get("tipo", "").startswith(tipo_efeito):
                        return h
        return None

    def encontrar_aliado_ferido(self, aliados: List['Monstro']) -> Optional['Monstro']:
        """
        Encontra o aliado (excluindo a si mesmo) com a menor porcentagem de vida,
        se essa porcentagem estiver abaixo de um limiar (50%).

        Args:
            aliados (List['Monstro']): A lista de aliados a serem verificados.

        Returns:
            Optional['Monstro']: O objeto do monstro aliado mais ferido, ou None se não houver.
        """
        aliados_feridos = [a for a in aliados if a is not self and (a.hp_atual / a.hp_max) < 0.5]
        if not aliados_feridos:
            return None
        # Retorna o aliado com a menor porcentagem de vida.
        return min(aliados_feridos, key=lambda a: a.hp_atual / a.hp_max)

    def gerar_loot(self) -> Dict[str, Any]:
        """
        Gera o loot (recompensas) para o jogador após a derrota do monstro.
        Processa a tabela de loot, rolando a chance para cada item possível.

        Returns:
            Dict[str, Any]: Um dicionário contendo o ouro, XP e uma lista de itens dropados.
        """
        loot_gerado = {"ouro": self.ouro, "xp": self.xp_recompensa, "itens": []}
        for item_drop in self.loot_table:
            # Rola um número aleatório entre 0.0 e 1.0 para cada item na tabela.
            if random.random() < item_drop["chance"]:
                # Se a chance for bem-sucedida, determina a quantidade a ser dropada.
                quantidade = random.randint(item_drop["quantidade"][0], item_drop["quantidade"][1])
                loot_gerado["itens"].append({"id_item": item_drop["id_item"], "quantidade": quantidade})

        return loot_gerado

    def __str__(self) -> str:
        """
        Fornece uma representação em string do monstro.

        Returns:
            str: Uma string formatada com o nome, nível e HP do monstro.
        """
        return f"MONSTRO: {self.nome} (Nível {self.nivel}) | HP: {self.hp_atual}/{self.hp_max}"
