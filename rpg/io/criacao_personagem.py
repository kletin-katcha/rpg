from typing import TYPE_CHECKING
from ..entidades.personagem import Personagem
from ..utilitarios import funcoes_gerais

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem

def iniciar_criacao_personagem() -> 'Personagem':
    """
    Guia o jogador através do processo de criação de personagem.
    Retorna um objeto Personagem totalmente inicializado.
    """
    funcoes_gerais.limpar_tela()
    funcoes_gerais.imprimir_cabecalho("Criação de Personagem", nivel=1)

    # 1. Obter o nome do personagem
    nome = ""
    while not nome:
        nome = input("Digite o nome do seu herói: ").strip()
        if not nome:
            print("O nome não pode estar em branco.")

    # --- Lógica de criação simplificada para a Fase 1 ---
    # Nas fases futuras, isso será expandido para permitir a escolha
    # de raças, classes, distribuição de atributos, etc.

    print(f"\nBem-vindo, {nome}!")
    print("Por enquanto, sua jornada começa como um Humano Guerreiro, forjado no básico.")
    funcoes_gerais.pausar()

    # Criar o objeto Personagem com valores padrão
    jogador = Personagem(nome=nome)

    # TODO: Implementar a escolha de raça e classe na Fase 2,
    # carregando os dados de rpg/dados/racas_base.py e classes_iniciais.py

    # TODO: Implementar a distribuição de pontos de atributo

    funcoes_gerais.limpar_tela()
    funcoes_gerais.imprimir_cabecalho("Personagem Criado", nivel=2)
    print(jogador) # Mostra o status inicial do personagem
    funcoes_gerais.pausar()

    return jogador
