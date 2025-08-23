from ..utilitarios import funcoes_gerais
from . import salvar_carregar

def exibir_menu_principal() -> str:
    """
    Exibe o menu principal e solicita a escolha do jogador.
    Retorna a ação escolhida ('novo_jogo', 'carregar_jogo', 'sair').
    """
    while True:
        funcoes_gerais.limpar_tela()
        funcoes_gerais.imprimir_cabecalho("RPG TEXTUAL COLOSSAL", nivel=1)
        print("1. Novo Jogo")
        print("2. Carregar Jogo")
        print("3. Sair")
        print("\n" + "="*20)

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            return "novo_jogo"
        elif escolha == '2':
            return "carregar_jogo"
        elif escolha == '3':
            return "sair"
        else:
            print("\nOpção inválida. Tente novamente.")
            funcoes_gerais.pausar()

def menu_carregar_jogo() -> str:
    """
    Exibe os saves disponíveis e permite que o jogador escolha um.
    Retorna o nome do arquivo de save escolhido ou None se cancelar.
    """
    saves = salvar_carregar.listar_saves()

    while True:
        funcoes_gerais.limpar_tela()
        funcoes_gerais.imprimir_cabecalho("Carregar Jogo", nivel=2)

        if not saves:
            print("Nenhum jogo salvo encontrado.")
            funcoes_gerais.pausar()
            return None

        for i, nome_save in enumerate(saves, 1):
            print(f"{i}. {nome_save}")

        print("\n0. Voltar ao Menu Principal")

        escolha = input("Escolha um save para carregar: ")

        if not escolha.isdigit():
            print("\nEntrada inválida. Digite o número correspondente.")
            funcoes_gerais.pausar()
            continue

        escolha_int = int(escolha)
        if escolha_int == 0:
            return None
        elif 1 <= escolha_int <= len(saves):
            return saves[escolha_int - 1]
        else:
            print("\nOpção inválida. Tente novamente.")
            funcoes_gerais.pausar()
