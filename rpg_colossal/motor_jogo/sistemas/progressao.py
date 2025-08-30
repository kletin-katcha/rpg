# -*- coding: utf-8 -*-
"""
================================================================================================
SISTEMA DE PROGRESSÃO
================================================================================================
Este arquivo define o sistema de progressão de personagem, que gerencia o ganho de
experiência (XP), o avanço de níveis (level up) e a evolução de classes e raças.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
O sistema é baseado em funções que operam sobre o objeto `Personagem`.

- **Experiência e Níveis:** Uma curva de XP exponencial garante que cada novo nível
  exija mais esforço que o anterior. Ao subir de nível, os atributos do personagem
  são melhorados.
- **Evolução de Classe:** O sistema verifica constantemente se o personagem cumpre os
  `requisitos` para evoluir para uma classe intermediária, avançada ou especial,
  consultando os bancos de dados de classes.
- **Evolução Racial:** Similar à de classe, mas mais rara, consulta o banco de dados
  de evoluções de raças.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
from typing import Dict, Any, List, Optional

# Importa as classes e dados necessários
try:
    from ..entidades.personagem import Personagem
    from ..banco_de_dados.classes.classes_intermediarias import CLASSES_INTERMEDIARIAS
    # Adicionar outros bancos de dados de classes conforme necessário
except ImportError:
    Personagem = object
    CLASSES_INTERMEDIARIAS = []

# ==============================================================================================
# == SEÇÃO 2: LÓGICA DE EXPERIÊNCIA E NÍVEIS ===================================================
# ==============================================================================================
XP_BASE = 100
FATOR_XP = 1.5

def calcular_xp_para_proximo_nivel(nivel: int) -> int:
    """
    Calcula a quantidade de XP necessária para alcançar o próximo nível.
    Usa uma fórmula exponencial simples.
    """
    return int(XP_BASE * (FATOR_XP ** (nivel - 1)))

def processar_ganho_xp(personagem: Personagem, quantidade: int) -> None:
    """
    Adiciona XP a um personagem e lida com o processo de level up.
    """
    if not personagem.esta_vivo():
        return # Personagens mortos não ganham XP.

    personagem.xp_atual += quantidade
    print(f"{personagem.nome} ganhou {quantidade} de XP! ({personagem.xp_atual}/{personagem.xp_para_proximo_nivel})")

    while personagem.xp_atual >= personagem.xp_para_proximo_nivel:
        xp_excedente = personagem.xp_atual - personagem.xp_para_proximo_nivel
        subir_de_nivel(personagem)
        personagem.xp_atual = xp_excedente # Mantém o XP excedente

def subir_de_nivel(personagem: Personagem) -> None:
    """
    Processa o level up de um personagem.
    """
    personagem.nivel += 1
    personagem.xp_para_proximo_nivel = calcular_xp_para_proximo_nivel(personagem.nivel)

    # Lógica de melhoria de atributos (simplificada)
    personagem.atributos["forca"] += 1
    personagem.atributos["destreza"] += 1
    personagem.atributos["constituicao"] += 1
    hp_ganho = 10 + personagem.atributos["constituicao"] // 2
    personagem.hp_max += hp_ganho
    personagem.hp_atual = personagem.hp_max # Cura total

    print(f"✨ {personagem.nome} alcançou o Nível {personagem.nivel}! ✨")
    print(f"HP Máximo aumentado para {personagem.hp_max}!")

# ==============================================================================================
# == SEÇÃO 3: LÓGICA DE EVOLUÇÃO ===============================================================
# ==============================================================================================
def verificar_evolucoes_disponiveis(personagem: Personagem) -> List[Dict]:
    """
    Verifica todos os bancos de dados de classes para encontrar evoluções disponíveis.

    Returns:
        List[Dict]: Uma lista de dicionários de classes para as quais o personagem é elegível.
    """
    evolucoes_possiveis = []

    # Exemplo de verificação para classes intermediárias
    for classe_ev in CLASSES_INTERMEDIARIAS:
        reqs = classe_ev.get("requisitos", {})
        if (personagem.nivel >= reqs.get("nivel_minimo", 999) and
            personagem.classe.get("id_classe") == reqs.get("classe_base")):
            evolucoes_possiveis.append(classe_ev)

    # Adicionar loops para classes avançadas, especiais, etc.
    return evolucoes_possiveis

def evoluir_personagem(personagem: Personagem, id_nova_classe: str) -> bool:
    """
    Evolui o personagem para uma nova classe.
    """
    # Lógica para encontrar os dados da nova classe e aplicá-los ao personagem.
    print(f"Parabéns! {personagem.nome} evoluiu para a classe '{id_nova_classe}'!")
    # personagem.classe = dados_nova_classe
    # Adicionar novas habilidades, etc.
    return True

# ==============================================================================================
# == SEÇÃO 4: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("== DEMONSTRAÇÃO DO SISTEMA DE PROGRESSÃO ==")
    print("="*80)

    class MockPersonagemProg:
        def __init__(self, nome, classe_data):
            self.nome = nome
            self.nivel = 1
            self.xp_atual = 0
            self.xp_para_proximo_nivel = calcular_xp_para_proximo_nivel(1)
            self.classe = classe_data
            self.hp_atual = 100
            self.hp_max = 100
            self.atributos = {"forca": 10, "destreza": 10, "constituicao": 10}
        def esta_vivo(self): return self.hp_atual > 0

    guerreiro_teste = MockPersonagemProg(
        "Novato",
        {"id_classe": "guerreiro", "nome": "Guerreiro"}
    )

    print(f"\n--- {guerreiro_teste.nome} começa sua jornada ---")
    print(f"Nível: {guerreiro_teste.nivel}, XP: {guerreiro_teste.xp_atual}/{guerreiro_teste.xp_para_proximo_nivel}")

    print("\n--- Ganhando XP ---")
    processar_ganho_xp(guerreiro_teste, 120)
    print(f"Nível: {guerreiro_teste.nivel}, XP: {guerreiro_teste.xp_atual}/{guerreiro_teste.xp_para_proximo_nivel}")

    # Simula o personagem chegando ao nível de evolução
    guerreiro_teste.nivel = 10
    print(f"\n--- {guerreiro_teste.nome} atinge o nível 10 ---")
    evolucoes = verificar_evolucoes_disponiveis(guerreiro_teste)

    if evolucoes:
        print("Evoluções de classe disponíveis:")
        for ev in evolucoes:
            print(f" - {ev['nome']}")
    else:
        print("Nenhuma evolução disponível no momento.")
