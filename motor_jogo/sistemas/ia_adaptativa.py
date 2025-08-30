# -*- coding: utf-8 -*-
"""
================================================================================================
SISTEMA DE IA ADAPTATIVA
================================================================================================
Este arquivo define a classe `IAAdaptativa`, um sistema mais avançado para governar o
comportamento de NPCs e monstros, permitindo que eles "aprendam" e reajam às
estratégias do jogador.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
A IA Adaptativa é um conceito ambicioso. Nesta fase inicial, o objetivo não é
implementar um aprendizado de máquina complexo, mas sim criar a ESTRUTURA para tal.

- **Registro de Ações:** O sistema manterá um histórico das ações mais comuns ou
  eficazes do jogador (ex: "usou magia de fogo", "atacou alvo com HP baixo").
- **Análise de Padrões:** A IA analisará esse histórico para identificar padrões.
  Por exemplo, se o jogador usa consistentemente magias de fogo, a IA pode
  marcar o jogador como "vulnerável a gelo" ou "resistente a fogo".
- **Sugestão de Ação:** Com base na análise, o sistema pode sugerir uma contra-
  estratégia para a entidade de IA (monstro ou boss). Em vez de uma IA que sempre
  usa a habilidade mais forte, ela pode escolher uma que explore uma fraqueza
  percebida do jogador.
- **Memória de NPC:** Para NPCs, o sistema pode registrar decisões importantes do
  jogador, permitindo que os diálogos mudem no futuro.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
from typing import Dict, Any, List, Optional
from collections import Counter

# ==============================================================================================
# == SEÇÃO 2: CLASSE IAADAPTATIVA ==============================================================
# ==============================================================================================
class IAAdaptativa:
    """
    Gerencia o aprendizado e a adaptação da IA do jogo.
    """
    def __init__(self):
        """
        Inicializa o sistema de IA, criando estruturas para armazenar o histórico.
        """
        # Histórico de habilidades usadas pelo jogador.
        self.historico_habilidades_jogador: List[str] = []
        # Histórico de decisões em diálogos.
        self.memoria_decisoes: Dict[str, Any] = {}
        print("Sistema de IA Adaptativa inicializado.")

    def registrar_acao_jogador(self, acao: Dict):
        """
        Registra uma ação do jogador para análise futura.

        Args:
            acao (Dict): Um dicionário descrevendo a ação do jogador.
                         Ex: {"tipo": "habilidade", "id": "sk_mago_bola_de_fogo"}
                             {"tipo": "dialogo", "id_missao": "resgate_ferreiro", "decisao": "aceitou"}
        """
        tipo_acao = acao.get("tipo")
        if tipo_acao == "habilidade":
            self.historico_habilidades_jogador.append(acao.get("id"))
        elif tipo_acao == "dialogo":
            self.memoria_decisoes[acao.get("id_missao")] = acao.get("decisao")

        # Mantém o histórico com um tamanho gerenciável
        if len(self.historico_habilidades_jogador) > 100:
            self.historico_habilidades_jogador.pop(0)

    def analisar_padroes_jogador(self) -> Dict:
        """
        Analisa o histórico de ações para identificar padrões de jogo.

        Returns:
            Dict: Um dicionário com as tendências identificadas.
                  Ex: {"elemento_mais_usado": "fogo", "tipo_ataque_comum": "single-target"}
        """
        if not self.historico_habilidades_jogador:
            return {}

        # Usa collections.Counter para encontrar a habilidade mais usada.
        contador_habilidades = Counter(self.historico_habilidades_jogador)
        habilidade_mais_comum = contador_habilidades.most_common(1)[0][0]

        # Lógica placeholder para extrair o "tipo" da habilidade
        # (Em um sistema real, buscaria a tag da habilidade no grimório)
        tendencias = {}
        if "fogo" in habilidade_mais_comum:
            tendencias["elemento_mais_usado"] = "fogo"
        elif "gelo" in habilidade_mais_comum:
            tendencias["elemento_mais_usado"] = "gelo"

        print(f"IA analisou padrões: Jogador tende a usar '{habilidade_mais_comum}'.")
        return tendencias

    def sugerir_acao_adaptativa(self, monstro: 'Monstro', tendencias_jogador: Dict) -> Optional[str]:
        """
        Sugere uma contra-ação para um monstro com base nos padrões do jogador.

        Args:
            monstro ('Monstro'): A instância do monstro que vai agir.
            tendencias_jogador (Dict): As tendências identificadas pela análise.

        Returns:
            Optional[str]: O ID da habilidade sugerida, ou None se nenhuma
                           contra-estratégia for encontrada.
        """
        elemento_usado = tendencias_jogador.get("elemento_mais_usado")
        if elemento_usado == "fogo":
            # Se o jogador usa fogo, sugere usar uma habilidade de gelo, se disponível.
            for habilidade_id in monstro.habilidades:
                if "gelo" in habilidade_id:
                    print(f"IA sugere: Usar '{habilidade_id}' para contra-atacar o uso de fogo.")
                    return habilidade_id
        return None

# ==============================================================================================
# == SEÇÃO 3: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("== DEMONSTRAÇÃO DO SISTEMA DE IA ADAPTATIVA ==")
    print("="*80)

    class MockMonstro:
        def __init__(self, nome, habilidades):
            self.nome = nome
            self.habilidades = habilidades

    ia = IAAdaptativa()

    # Simula o jogador usando várias magias de fogo
    print("\n--- Jogador usa magias de fogo repetidamente ---")
    for _ in range(5):
        ia.registrar_acao_jogador({"tipo": "habilidade", "id": "sk_mago_bola_de_fogo"})
    ia.registrar_acao_jogador({"tipo": "habilidade", "id": "sk_mago_seta_de_fogo"})

    # A IA analisa o comportamento
    print("\n--- IA analisa o histórico ---")
    padroes = ia.analisar_padroes_jogador()
    print(f"Padrões identificados: {padroes}")

    # A IA sugere uma ação para um monstro que tem uma habilidade de gelo
    print("\n--- IA sugere uma contra-medida ---")
    monstro_teste = MockMonstro("Elemental de Gelo", ["sk_elemental_lanca_de_gelo_tripla"])
    acao_sugerida = ia.sugerir_acao_adaptativa(monstro_teste, padroes)

    if acao_sugerida:
        print(f"Ação final escolhida para {monstro_teste.nome}: {acao_sugerida}")
    else:
        print(f"{monstro_teste.nome} não tem uma boa contra-medida e usará sua IA padrão.")
