# -*- coding: utf-8 -*-
"""
================================================================================================
CLASSE: MONSTRO
================================================================================================
Este arquivo define a classe `Monstro`, que representa os inimigos que o jogador
enfrentará no mundo de Aetheria.

-------------------------
-- HERANÇA E DESIGN --
-------------------------
A classe `Monstro` herda da `entidade_base.Entidade`, utilizando a mesma base de
HP, atributos e métodos de dano. A especialização do Monstro reside em sua IA de
combate (o campo `comportamento`) e na sua tabela de loot.

Diferente do `Personagem`, que é complexo e persistente, um objeto `Monstro` é
geralmente mais simples e "descartável", existindo apenas durante um encontro de
combate.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
from typing import Dict, Any, List, Optional
import random

# Importa a classe base para herança.
from .entidade_base import Entidade

# ==============================================================================================
# == SEÇÃO 2: DEFINIÇÃO DA CLASSE MONSTRO ======================================================
# ==============================================================================================
class Monstro(Entidade):
    """
    Representa um monstro ou inimigo no jogo.

    Herda de `Entidade` e adiciona lógica específica para combate, como IA de
    comportamento e recompensas (loot).

    Attributes:
        comportamento (str): A estratégia de IA que o monstro usará em combate.
        loot_table (List[Dict]): A lista de itens que podem ser dropados ao morrer.
        habilidades (List[str]): Lista de IDs de habilidades que o monstro pode usar.
    """

    def __init__(self, dados_monstro: Dict[str, Any]):
        """
        Inicializa um novo objeto Monstro a partir de um dicionário de dados.

        Args:
            dados_monstro (Dict[str, Any]): O dicionário de dados completo do
                                           monstro, vindo de um dos arquivos
                                           de banco de dados de monstros.
        """
        # Chama o construtor da classe pai `Entidade`.
        super().__init__(
            id_entidade=dados_monstro.get("id", "monstro_desconhecido"),
            nome=dados_monstro.get("nome", "Monstro Desconhecido"),
            nivel=dados_monstro.get("nivel", 1),
            hp=dados_monstro.get("hp", 10),
            atributos=dados_monstro.get("atributos", {})
        )

        # Atributos específicos do Monstro
        self.comportamento: str = dados_monstro.get("comportamento", "agressivo")
        self.loot_table: List[Dict] = dados_monstro.get("drops", [])
        self.habilidades: List[str] = dados_monstro.get("habilidades", [])

    def __str__(self) -> str:
        """Retorna uma representação em string do monstro."""
        return f"[MONSTRO] {self.nome} (Nível {self.nivel}) - HP: {self.hp_atual}/{self.hp_max}"

    def decidir_acao(self, grupo_jogador: List['Entidade'], aliados_monstro: List['Monstro']) -> Dict[str, Any]:
        """
        Simula a "IA" do monstro para decidir qual ação tomar em seu turno.

        Esta é uma função placeholder. A lógica real seria complexa, baseada no
        campo `comportamento`.

        Args:
            grupo_jogador (List['Entidade']): A lista de alvos inimigos (o grupo do jogador).
            aliados_monstro (List['Monstro']): A lista de aliados do monstro no combate.

        Returns:
            Dict[str, Any]: Um dicionário representando a ação escolhida,
                            contendo, por exemplo, o ID da habilidade e o alvo.
        """
        # Lógica de IA muito simplificada para fins de demonstração.
        acao_escolhida = {
            "habilidade_id": None,
            "alvo_id": None
        }

        # Se tiver habilidades, escolhe uma aleatoriamente.
        if self.habilidades:
            acao_escolhida["habilidade_id"] = random.choice(self.habilidades)
        else:
            # Se não, usa um ataque básico genérico.
            acao_escolhida["habilidade_id"] = "sk_geral_ataque_basico"

        # Escolhe um alvo aleatório do grupo do jogador.
        if grupo_jogador:
            alvo = random.choice(grupo_jogador)
            acao_escolhida["alvo_id"] = alvo.id_entidade

        print(f"IA de {self.nome}: Decide usar '{acao_escolhida['habilidade_id']}' em '{acao_escolhida['alvo_id']}'.")
        return acao_escolhida

    def ao_morrer(self) -> List[str]:
        """
        Sobrescreve o método da classe base para lidar com a morte de um monstro,
        retornando logs do processo, incluindo o loot.
        """
        logs = super().ao_morrer()

        logs.append(f"{self.nome} deixa para trás algum loot...")
        loot_encontrado = False
        for item_drop in self.loot_table:
            if random.random() < item_drop.get("chance", 0):
                logs.append(f"    - Você encontrou: {item_drop.get('item_id')}!")
                loot_encontrado = True

        if not loot_encontrado:
            logs.append("    - ...mas não era nada de valor.")

        return logs

# Fim da definição da classe Monstro.
