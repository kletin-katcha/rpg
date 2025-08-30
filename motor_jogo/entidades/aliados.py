# -*- coding: utf-8 -*-
"""
================================================================================================
CLASSE: ALIADO
================================================================================================
Este arquivo define a classe `Aliado`, que representa entidades controladas pela IA
que ajudam o jogador, como familiares, invocações místicas ou seguidores de missões.

-------------------------
-- HERANÇA E DESIGN --
-------------------------
A classe `Aliado` herda da `entidade_base.Entidade`. Dependendo do tipo, um aliado
pode se comportar de maneira muito diferente:
- **Familiares/Animais de Estimação:** Podem fornecer buffs passivos ou ajudar a
  coletar itens.
- **Invocações (Summons):** Geralmente são entidades de combate temporárias,
  criadas por uma habilidade.
- **Seguidores (Followers):** NPCs que acompanham o jogador por um período,
  geralmente como parte de uma missão, e podem ou não participar do combate.

A classe é projetada para ser flexível e acomodar esses diferentes papéis.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
from typing import Dict, Any, List, Optional
import random

# Importa a classe base para herança.
try:
    from .entidade_base import Entidade
except ImportError:
    Entidade = object

# ==============================================================================================
# == SEÇÃO 2: DEFINIÇÃO DA CLASSE ALIADO =======================================================
# ==============================================================================================
class Aliado(Entidade):
    """
    Representa um companheiro ou invocação que ajuda o jogador.

    Herda de `Entidade` e pode ter um comportamento de combate ou de suporte.

    Attributes:
        tipo_aliado (str): O tipo do aliado ("Familiar", "Invocação", "Seguidor").
        dono (Entidade): A entidade que invocou ou comanda este aliado.
        duracao_turnos (int): Para invocações, quantos turnos ela permanecerá em combate.
                              -1 para permanente.
    """

    def __init__(self, dados_aliado: Dict[str, Any], dono: 'Entidade'):
        """
        Inicializa um novo objeto Aliado.

        Args:
            dados_aliado (Dict[str, Any]): O dicionário de dados do aliado.
            dono ('Entidade'): O personagem ou entidade que é o mestre deste aliado.
        """
        super().__init__(
            id_entidade=dados_aliado.get("id", "aliado_desconhecido"),
            nome=dados_aliado.get("nome", "Aliado"),
            nivel=dono.nivel, # O nível do aliado geralmente escala com o do dono.
            hp=dados_aliado.get("hp", 20) + (dono.nivel * 5),
            atributos=dados_aliado.get("atributos", {})
        )

        # Atributos específicos do Aliado
        self.tipo_aliado: str = dados_aliado.get("tipo", "Invocação")
        self.dono: 'Entidade' = dono
        self.duracao_turnos: int = dados_aliado.get("duracao", -1) # Permanente por padrão
        self.habilidades: List[str] = dados_aliado.get("habilidades", [])

    def __str__(self) -> str:
        """Retorna uma representação em string do aliado."""
        return f"[ALIADO] {self.nome} (Dono: {self.dono.nome}) - HP: {self.hp_atual}/{self.hp_max}"

    def decidir_acao(self, grupo_inimigos: List['Entidade']) -> Optional[Dict[str, Any]]:
        """
        Simula a "IA" do aliado para decidir qual ação tomar em seu turno de combate.

        Args:
            grupo_inimigos (List['Entidade']): A lista de alvos inimigos.

        Returns:
            Optional[Dict[str, Any]]: A ação escolhida ou None se nenhuma ação for tomada.
        """
        if not self.habilidades:
            return None # Aliados sem habilidades de combate não agem.

        acao_escolhida = {
            "habilidade_id": random.choice(self.habilidades),
            "alvo_id": random.choice(grupo_inimigos).id_entidade if grupo_inimigos else None
        }

        print(f"IA do Aliado {self.nome}: Decide usar '{acao_escolhida['habilidade_id']}' em '{acao_escolhida['alvo_id']}'.")
        return acao_escolhida

    def atualizar_duracao(self) -> None:
        """
        Decrementa a duração do aliado, se for uma invocação temporária.
        """
        if self.duracao_turnos > 0:
            self.duracao_turnos -= 1
            if self.duracao_turnos == 0:
                self.hp_atual = 0 # Desaparece ao fim da duração.
                print(f"{self.nome} desaparece, sua energia se esgotou.")

# Fim da definição da classe Aliado.
