# -*- coding: utf-8 -*-
"""
################################################################################################
##                                                                                            ##
##     ██████╗ ██████╗ ███╗   ███╗██████╗  █████╗ ████████╗    ██████╗  ██████╗  █████╗ ████████╗ ##
##    ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝    ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝ ##
##    ██║     ██║   ██║██╔████╔██║██████╔╝███████║   ██║       ██████╔╝██║   ██║███████║   ██║    ##
##    ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██╔══██║   ██║       ██╔══██╗██║   ██║██╔══██║   ██║    ##
##    ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ██║  ██║   ██║       ██║  ██║╚██████╔╝██║  ██║   ██║    ##
##     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ##
##                                                                                            ##
################################################################################################
################################################################################################

================================================================================================
SISTEMA DE COMBATE
================================================================================================
Este arquivo contém o `CombatManager`, o coração do sistema de combate por turnos de
Aetheria. Ele é responsável por gerenciar o fluxo de uma batalha, desde sua
inicialização até a determinação de um vencedor.

-------------------------
-- FLUXO DE UM COMBATE --
-------------------------
1.  **Inicialização:** Um combate é iniciado com dois grupos de entidades: o grupo do
    jogador e o grupo inimigo.
2.  **Ordem de Turno:** A ordem de ação é determinada, geralmente com base no atributo
    de 'destreza' ou 'velocidade' de cada entidade.
3.  **Loop de Turnos:** O combate prossegue em turnos. A cada turno de uma entidade:
    a. Efeitos de status (como veneno, regeneração) são aplicados.
    b. Se for um jogador, a interface pede uma ação. Se for um monstro, a IA decide.
    c. A ação (ataque, magia, item) é executada e seus resultados são calculados.
4.  **Fim de Combate:** O loop continua até que todas as entidades de um dos grupos
    sejam derrotadas.
5.  **Resolução:** Recompensas (XP, loot) são distribuídas ao grupo vencedor.

---------------------------------
-- INTEGRAÇÃO COM OUTROS MÓDULOS --
---------------------------------
- **entidades/:** O `CombatManager` manipula instâncias das classes `Personagem`,
  `Monstro` e `Boss`, chamando seus métodos (ex: `receber_dano`) e lendo seus
  atributos.
- **banco_de_dados/habilidades/:** As ações de combate são baseadas nos dados das
  habilidades. O `CombatManager` lê os dados de uma habilidade para calcular seu
  dano, custo, efeitos, etc.
- **sistemas/ia_adaptativa.py:** A decisão de ação de um monstro ou boss pode ser
  delegada a este sistema para um comportamento mais complexo.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import random
import time
from typing import List, Dict, Any, Optional

# Importa as classes de entidade para type hinting e instanciação
try:
    from ..entidades.entidade_base import Entidade
    from ..entidades.personagem import Personagem
    from ..entidades.monstro import Monstro
    from ..entidades.boss import Boss

    # Importa o grimório completo de habilidades
    from ..banco_de_dados.habilidades.grimorio_completo import GRIMORIO_COMPLETO
except ImportError:
    # Fallback para testes isolados
    print("DEBUG: Falha ao importar módulos do motor para combate.py. Usando mocks.")
    Entidade = object
    Personagem = object
    Monstro = object
    Boss = object
    GRIMORIO_COMPLETO = {}


# ==============================================================================================
# == SEÇÃO 2: CLASSE COMBATMANAGER =============================================================
# ==============================================================================================
class CombatManager:
    """
    Gerencia uma instância única de um encontro de combate de forma interativa.
    """
    def __init__(self, grupo_jogador: List[Entidade], grupo_inimigos: List[Entidade]):
        self.grupo_jogador = grupo_jogador
        self.grupo_inimigos = grupo_inimigos
        self.ordem_de_turno: List[Entidade] = []
        self.turno_atual: int = 0
        self.log_combate: List[str] = []
        self.estado_combate: str = "em_andamento" # em_andamento, vitoria_jogador, derrota_jogador

        self.iniciar_novo_combate()

    def iniciar_novo_combate(self):
        """Prepara o estado inicial do combate."""
        self.log_combate.append("="*30 + " COMBATE INICIADO " + "="*30)
        self._determinar_ordem_de_turno()
        self.estado_combate = "em_andamento"
        self.turno_atual = 0

    def _determinar_ordem_de_turno(self):
        """Calcula a ordem de ação para todas as entidades no combate."""
        todas_entidades = self.grupo_jogador + self.grupo_inimigos
        self.ordem_de_turno = sorted(
            todas_entidades,
            key=lambda e: e.atributos.get("destreza", 10) + random.uniform(0, 1), # Fator aleatório para desempate
            reverse=True
        )
        ordem_nomes = " -> ".join([e.nome for e in self.ordem_de_turno])
        self.log_combate.append(f"Ordem de turno: {ordem_nomes}")

    def obter_estado_atual(self) -> Dict:
        """Retorna o estado atual do combate para a UI renderizar."""
        return {
            "grupo_jogador": self.grupo_jogador,
            "grupo_inimigos": self.grupo_inimigos,
            "log_combate": self.log_combate,
            "entidade_da_vez": self.get_entidade_da_vez(),
            "estado_combate": self.estado_combate,
        }

    def get_entidade_da_vez(self) -> Optional[Entidade]:
        """Retorna a entidade cujo turno está ativo."""
        if not self.ordem_de_turno:
            return None
        return self.ordem_de_turno[self.turno_atual % len(self.ordem_de_turno)]

    def processar_proximo_turno(self) -> Dict:
        """
        Processa o combate turno a turno até que seja a vez de um jogador
        ou o combate termine.
        """
        if self.estado_combate != "em_andamento":
            return self.obter_estado_atual()

        while self.estado_combate == "em_andamento":
            entidade_da_vez = self.get_entidade_da_vez()

            if not entidade_da_vez.esta_vivo():
                self.turno_atual += 1
                continue

            self.log_combate.append("\n" + "-"*25 + f" TURNO DE {entidade_da_vez.nome.upper()} " + "-"*25)
            entidade_da_vez.atualizar_efeitos() # Aplica DoTs, HoTs, etc.

            if not entidade_da_vez.esta_vivo(): # Verifica de novo caso um DoT mate a entidade
                self.turno_atual += 1
                self._verificar_fim_de_combate()
                continue

            # Se for um PNJ (monstro), a IA age e o loop continua.
            if entidade_da_vez in self.grupo_inimigos:
                acao = entidade_da_vez.decidir_acao(self.grupo_jogador, self.grupo_inimigos)
                self._executar_acao(entidade_da_vez, acao)
                self.turno_atual += 1
                self._verificar_fim_de_combate()
            # Se for um jogador, o loop para e espera a ação da UI.
            else:
                self.log_combate.append(f"Aguardando ação de {entidade_da_vez.nome}...")
                break

        return self.obter_estado_atual()

    def executar_acao_jogador(self, jogador: Entidade, acao: Dict):
        """
        Executa a ação fornecida pelo jogador e avança o combate.
        """
        if jogador != self.get_entidade_da_vez() or self.estado_combate != "em_andamento":
            self.log_combate.append("ERRO: Não é o turno deste jogador ou o combate já terminou.")
            return

        self._executar_acao(jogador, acao)
        self.turno_atual += 1
        self._verificar_fim_de_combate()

        # Após a ação do jogador, processa os turnos dos PNJs até o próximo jogador
        self.processar_proximo_turno()

    def _executar_acao(self, atacante: Entidade, acao: Dict):
        """Lógica interna para processar uma ação de qualquer entidade."""
        habilidade_id = acao.get("habilidade_id")
        alvo_id = acao.get("alvo_id")

        if not habilidade_id or not alvo_id:
            self.log_combate.append(f"{atacante.nome} não faz nada.")
            return

        habilidade_data = GRIMORIO_COMPLETO.get(habilidade_id)
        if not habilidade_data:
            self.log_combate.append(f"DEBUG: Habilidade '{habilidade_id}' não encontrada no Grimório Completo!")
            return

        alvo = next((e for e in self.grupo_jogador + self.grupo_inimigos if e.id_entidade == alvo_id), None)
        if not alvo or not alvo.esta_vivo():
            self.log_combate.append(f"{atacante.nome} tenta atacar, mas o alvo não é válido.")
            return

        self.log_combate.append(f"{atacante.nome} usa '{habilidade_data.get('nome', 'Habilidade Desconhecida')}' em {alvo.nome}!")

        if random.random() > habilidade_data.get("precisao", 1.0):
            self.log_combate.append(f"O ataque de {atacante.nome} errou!")
            return

        dano_base = atacante.atributos.get(habilidade_data.get("atributo_chave", "forca"), 10) * habilidade_data.get("multiplicador", 1.0)
        defesa_alvo = alvo.atributos.get("defesa", 0)
        dano_final = max(1, int(dano_base - defesa_alvo))

        # A lógica de dano agora também deve retornar logs
        log_dano = alvo.receber_dano(dano_final)
        self.log_combate.extend(log_dano) # Supondo que receber_dano retorne uma lista de strings

    def _verificar_fim_de_combate(self):
        """Verifica e atualiza o estado do combate se um dos grupos foi derrotado."""
        if all(not p.esta_vivo() for p in self.grupo_jogador):
            self.estado_combate = "derrota_jogador"
            self.log_combate.append("FIM DE COMBATE! Resultado: DERROTA DO JOGADOR")
        elif all(not i.esta_vivo() for i in self.grupo_inimigos):
            self.estado_combate = "vitoria_jogador"
            self.log_combate.append("FIM DE COMBATE! Resultado: VITÓRIA DO JOGADOR")

# ==============================================================================================
# == SEÇÃO 3: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
if __name__ == "__main__":
    # Este bloco serve como um teste rápido e uma demonstração de como o sistema funciona.
    print("="*80)
    print("== DEMONSTRAÇÃO DO SISTEMA DE COMBATE ==")
    print("="*80)

    # --- Mocks e Stubs para Teste ---
    # Como não podemos importar os bancos de dados e outras classes facilmente aqui,
    # criamos "dublês" (mocks) para simular o comportamento.
    class MockEntidadeParaTeste:
        def __init__(self, id_entidade, nome, nivel, hp, atributos):
            self.id_entidade = id_entidade
            self.nome = nome
            self.nivel = nivel
            self.hp_max = hp
            self.hp_atual = hp
            self.atributos = atributos

        def esta_vivo(self):
            return self.hp_atual > 0

        def receber_dano(self, quantidade):
            self.hp_atual -= quantidade
            print(f"{self.nome} recebe {quantidade} de dano! HP restante: {self.hp_atual}")
            if not self.esta_vivo():
                print(f"{self.nome} foi derrotado!")

        def atualizar_efeitos(self): pass # Placeholder

        def decidir_acao(self, grupo_jogador, *args, **kwargs):
            alvo = next((p for p in grupo_jogador if p.esta_vivo()), None)
            return {"habilidade_id": "sk_geral_ataque_basico", "alvo_id": alvo.id_entidade if alvo else None}

    # Criando um personagem jogador mock
    jogador_mock = MockEntidadeParaTeste(
        id_entidade="player_1",
        nome="Herói Valente",
        nivel=5,
        hp=100,
        atributos={"forca": 15, "destreza": 12, "defesa": 10}
    )

    # Criando um monstro mock
    monstro_mock = MockEntidadeParaTeste(
        id_entidade="goblin_1",
        nome="Goblin Guerreiro",
        nivel=3,
        hp=40,
        atributos={"forca": 12, "destreza": 10, "defesa": 8}
    )

    # Adicionando uma habilidade mock ao grimório para o teste
    GRIMORIO_COMPLETO["ataque_basico"] = {
        "nome": "Ataque Básico Teste",
        "precisao": 0.95,
        "multiplicador": 1.0,
        "atributo_chave": "forca"
    }

    # --- Iniciando o Combate ---
    grupo_jogador_teste = [jogador_mock]
    grupo_inimigos_teste = [monstro_mock]

    combate = CombatManager(grupo_jogador_teste, grupo_inimigos_teste)
    resultado_final = combate.iniciar_combate()

    print(f"\nO combate terminou. O jogador alcançou: {resultado_final}")
