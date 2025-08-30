# -*- coding: utf-8 -*-
"""
################################################################################################
##                                                                                            ##
##    ███████╗███╗   ██╗████████╗██╗██████╗ █████╗ ██████╗                                       ##
##    ██╔════╝████╗  ██║╚══██╔══╝██║██╔══██╗██╔══██╗██╔══██╗                                      ##
##    █████╗  ██╔██╗ ██║   ██║   ██║██║  ██║███████║██║  ██║                                      ##
##    ██╔══╝  ██║╚██╗██║   ██║   ██║██║  ██║██╔══██║██║  ██║                                      ##
##    ███████╗██║ ╚████║   ██║   ██║██████╔╝██║  ██║██████╔╝                                      ##
##    ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═════╝ ╚═╝  ╚═╝╚═════╝                                       ##
##                                                                                            ##
################################################################################################
################################################################################################

================================================================================================
CLASSE BASE: ENTIDADE
================================================================================================
Este arquivo define a classe base `Entidade`, da qual todas as outras criaturas e
personagens do jogo herdarão. O objetivo de ter uma classe base é centralizar os
atributos e métodos que são comuns a todos os seres vivos em Aetheria.

-------------------------
-- PROPÓSITO E DESIGN --
-------------------------
A classe `Entidade` implementa o "mínimo denominador comum" de um ser no jogo:
- Possui um nome e um ID.
- Tem pontos de vida (HP) e sabe se está vivo ou morto.
- Possui um conjunto de atributos básicos (força, destreza, etc.).
- Pode receber dano e cura.
- Pode ter efeitos de status (buffs/debuffs) aplicados a si.

Classes mais específicas como `Personagem`, `Monstro`, e `NPC` herdarão de `Entidade`
e adicionarão suas próprias funcionalidades únicas sobre esta base sólida. Isso evita
a duplicação de código e garante que todas as entidades do jogo respondam de forma
consistente a interações fundamentais como o combate.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
from typing import Dict, Any, List

# ==============================================================================================
# == SEÇÃO 2: DEFINIÇÃO DA CLASSE ENTIDADE =====================================================
# ==============================================================================================
class Entidade:
    """
    Representa uma entidade viva no mundo do jogo.

    Esta é a superclasse para todos os personagens, monstros, NPCs e outras
    criaturas. Ela gerencia os atributos e o estado fundamental de um ser.

    Attributes:
        id_entidade (str): O identificador único da entidade (ex: "player_1", "goblin_batedor").
        nome (str): O nome de exibição da entidade.
        nivel (int): O nível da entidade, que influencia seu poder.
        hp_max (int): A quantidade máxima de pontos de vida.
        hp_atual (int): A quantidade atual de pontos de vida.
        atributos (Dict[str, int]): Um dicionário com os atributos base da entidade
                                    (forca, destreza, etc.).
        efeitos_ativos (List[Dict]): Uma lista dos efeitos de status (buffs/debuffs)
                                     atualmente afetando a entidade.
    """

    def __init__(self, id_entidade: str, nome: str, nivel: int, hp: int, atributos: Dict[str, int]):
        """
        Inicializa um novo objeto Entidade.

        Args:
            id_entidade (str): O ID único para esta instância da entidade.
            nome (str): O nome da entidade.
            nivel (int): O nível da entidade.
            hp (int): Os pontos de vida máximos da entidade.
            atributos (Dict[str, int]): O dicionário de atributos.
        """
        self.id_entidade: str = id_entidade
        self.nome: str = nome
        self.nivel: int = nivel
        self.hp_max: int = hp
        self.hp_atual: int = hp  # Começa com vida cheia
        self.atributos: Dict[str, int] = atributos
        self.efeitos_ativos: List[Dict] = []
        # Adicionar mais atributos comuns no futuro, como mana, stamina, etc.
        self.mana_max: int = atributos.get("inteligencia", 0) * 10
        self.mana_atual: int = self.mana_max

    def __str__(self) -> str:
        """Retorna uma representação em string da entidade, útil para debugging."""
        return f"{self.nome} (Nível {self.nivel}) - HP: {self.hp_atual}/{self.hp_max}"

    def esta_vivo(self) -> bool:
        """
        Verifica se a entidade ainda está viva.

        Returns:
            bool: True se hp_atual for maior que 0, False caso contrário.
        """
        return self.hp_atual > 0

    def receber_dano(self, quantidade: int) -> List[str]:
        """
        Aplica dano à entidade e retorna uma lista de logs sobre o que aconteceu.

        Args:
            quantidade (int): A quantidade de dano a ser recebida.

        Returns:
            List[str]: Uma lista de strings para o log de combate.
        """
        logs = []
        if quantidade < 0:
            quantidade = 0

        dano_real = min(self.hp_atual, quantidade)
        self.hp_atual -= dano_real

        if self.hp_atual < 0:
            self.hp_atual = 0

        logs.append(f"{self.nome} recebe {dano_real} de dano! HP restante: {self.hp_atual}")

        if not self.esta_vivo():
            logs.extend(self.ao_morrer())

        return logs

    def receber_cura(self, quantidade: int) -> List[str]:
        """
        Aplica cura à entidade e retorna uma lista de logs sobre o que aconteceu.

        Args:
            quantidade (int): A quantidade de cura a ser recebida.

        Returns:
            List[str]: Uma lista de strings para o log de combate.
        """
        logs = []
        if quantidade < 0:
            quantidade = 0

        cura_real = min(quantidade, self.hp_max - self.hp_atual)
        self.hp_atual += cura_real

        logs.append(f"{self.nome} recupera {cura_real} de vida! HP atual: {self.hp_atual}/{self.hp_max}")
        return logs

    def ao_morrer(self) -> List[str]:
        """
        Método chamado quando o HP da entidade chega a 0. Retorna logs do evento.
        """
        return [f"{self.nome} foi derrotado!"]

    def aplicar_efeito(self, efeito: Dict[str, Any]) -> None:
        """
        Adiciona um novo efeito de status (buff/debuff) à entidade.

        Args:
            efeito (Dict[str, Any]): Um dicionário representando o efeito,
                                     contendo chaves como 'nome_efeito', 'duracao', etc.
        """
        print(f"Efeito '{efeito.get('nome_efeito', 'Desconhecido')}' aplicado em {self.nome}.")
        self.efeitos_ativos.append(efeito)

    def atualizar_efeitos(self) -> None:
        """
        Processa todos os efeitos ativos no início do turno da entidade.

        Esta função deve ser chamada a cada turno. Ela aplica danos/curas por
        turno e decrementa a duração dos efeitos, removendo os que expiraram.
        """
        efeitos_a_remover = []
        for efeito in self.efeitos_ativos:
            # Aplica lógica do efeito (ex: dano de veneno)
            if efeito.get("tipo") == "dano_por_turno":
                dano_dot = int(self.atributos.get(efeito.get("atributo_chave", "forca"), 10) * efeito.get("valor", 0))
                self.receber_dano(dano_dot)

            # Decrementa a duração
            efeito["duracao"] -= 1
            if efeito["duracao"] <= 0:
                efeitos_a_remover.append(efeito)

        # Remove os efeitos expirados
        self.efeitos_ativos = [ef for ef in self.efeitos_ativos if ef not in efeitos_a_remover]

# Fim da definição da classe base.
