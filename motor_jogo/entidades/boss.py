# -*- coding: utf-8 -*-
"""
================================================================================================
CLASSE: BOSS
================================================================================================
Este arquivo define a classe `Boss`, uma especialização da classe `Monstro`, projetada
para lidar com as complexidades das lutas contra chefes.

-------------------------
-- HERANÇA E DESIGN --
-------------------------
A classe `Boss` herda de `Monstro`, o que significa que ela já possui todos os
atributos e métodos de um inimigo padrão. A especialização aqui se concentra em
gerenciar mecânicas de luta mais elaboradas, principalmente:

- **Múltiplas Fases:** Um chefe pode ter vários estágios, cada um com seu próprio
  conjunto de habilidades, HP e comportamento.
- **Mecânicas Especiais:** Lógica para lidar com habilidades únicas que não se
  encaixam no sistema de combate padrão (ex: imunidade condicional, invocação
  de objetos de cenário, etc.).
- **Diálogos de Combate:** A capacidade de proferir falas em momentos específicos
  da luta para aumentar a imersão.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
from typing import Dict, Any, List

# Importa a classe Monstro para herança.
from .monstro import Monstro

# ==============================================================================================
# == SEÇÃO 2: DEFINIÇÃO DA CLASSE BOSS =========================================================
# ==============================================================================================
class Boss(Monstro):
    """
    Representa um chefe, um inimigo com múltiplas fases e mecânicas complexas.

    Herda de `Monstro` e adiciona a lógica para gerenciar o estado da luta
    através de diferentes fases.

    Attributes:
        dados_completos_boss (Dict): Armazena o dicionário de dados original do chefe.
        fase_atual_info (Dict): O dicionário de dados da fase atual da luta.
        fase_atual_num (int): O número da fase atual (1, 2, 3...).
    """

    def __init__(self, dados_boss: Dict[str, Any]):
        """
        Inicializa um novo objeto Boss.

        Args:
            dados_boss (Dict[str, Any]): O dicionário de dados completo do chefe.
        """
        # O chefe começa na primeira fase.
        fase_inicial = dados_boss.get("fases", [{}])[0]

        # Inicializa a classe pai (Monstro) com os dados da primeira fase.
        super().__init__(
            dados_monstro={
                "id": dados_boss.get("id"),
                "nome": dados_boss.get("nome"),
                "nivel": dados_boss.get("nivel", fase_inicial.get("nivel", 50)),
                "hp": fase_inicial.get("hp", 1000),
                "atributos": fase_inicial.get("atributos", dados_boss.get("atributos", {})),
                "habilidades": fase_inicial.get("habilidades", []),
                "comportamento": fase_inicial.get("comportamento", "agressivo"),
                "drops": dados_boss.get("loot_final", [])
            }
        )

        # Atributos específicos do Boss
        self.dados_completos_boss: Dict = dados_boss
        self.fase_atual_num: int = 1
        self.fase_atual_info: Dict = fase_inicial

        # Dispara o diálogo de início da fase, se houver.
        self.proferir_dialogo("inicio_fase")

    def receber_dano(self, quantidade: int) -> int:
        """
        Sobrescreve o método `receber_dano` para incluir a lógica de transição de fase.
        """
        # Chama o método original da superclasse para aplicar o dano.
        dano_real = super().receber_dano(quantidade)

        # Verifica se o limiar de HP para a próxima fase foi atingido.
        limiar_hp = self.fase_atual_info.get("limiar_hp", 0.0)
        hp_percentual_atual = self.hp_atual / self.hp_max

        if self.esta_vivo() and hp_percentual_atual <= limiar_hp:
            self.proxima_fase()

        return dano_real

    def proxima_fase(self) -> None:
        """
        Avança a luta para a próxima fase definida no banco de dados.
        """
        proxima_fase_num = self.fase_atual_num + 1
        fases = self.dados_completos_boss.get("fases", [])

        # Encontra os dados da próxima fase.
        nova_fase_info = next((f for f in fases if f.get("fase_id") == proxima_fase_num), None)

        if nova_fase_info:
            print(f"!!! {self.nome} entra na Fase {proxima_fase_num} !!!")
            self.fase_atual_num = proxima_fase_num
            self.fase_atual_info = nova_fase_info

            # Atualiza os stats do boss para os da nova fase.
            self.hp_max = self.fase_atual_info.get("hp", self.hp_max)
            self.hp_atual = self.hp_max # Geralmente, bosses recuperam a vida em uma nova fase.
            self.habilidades = self.fase_atual_info.get("habilidades", self.habilidades)

            self.proferir_dialogo("inicio_fase")
        else:
            # Se não houver próxima fase, a luta continua até a morte.
            pass

    def decidir_acao(self, grupo_jogador: List['Entidade'], aliados_monstro: List['Monstro']) -> Dict[str, Any]:
        """
        Sobrescreve a IA para usar as habilidades da fase atual.
        """
        # A IA de um chefe seria muito mais complexa, baseada nas mecânicas especiais.
        # Esta é uma simulação simplificada.
        habilidades_disponiveis = self.fase_atual_info.get("habilidades", [])
        if habilidades_disponiveis:
            habilidade_id = random.choice(habilidades_disponiveis)
            alvo_id = random.choice(grupo_jogador).id_entidade if grupo_jogador else None

            print(f"IA do BOSS {self.nome}: Decide usar '{habilidade_id}' em '{alvo_id}'.")
            return {"habilidade_id": habilidade_id, "alvo_id": alvo_id}
        else:
            # Fallback para o método do Monstro base se não houver habilidades na fase.
            return super().decidir_acao(grupo_jogador, aliados_monstro)

    def proferir_dialogo(self, gatilho: str) -> None:
        """
        Verifica e exibe um diálogo do chefe com base em um gatilho.
        """
        dialogo = self.fase_atual_info.get("dialogos", {}).get(gatilho)
        if isinstance(dialogo, str):
            print(f"[{self.nome}]: “{dialogo}”")
        elif isinstance(dialogo, dict) and dialogo.get("gatilho") == gatilho:
            print(f"[{self.nome}]: “{dialogo.get('fala')}”")

# Fim da definição da classe Boss.
