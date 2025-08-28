from typing import TYPE_CHECKING
from ..utilitarios import funcoes_gerais
from ..sistemas import evolucao as sistema_evolucao

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem

def evolucao_ui(jogador: 'Personagem'):
    """
    Interface para o jogador evoluir sua classe.
    """
    funcoes_gerais.limpar_tela()
    funcoes_gerais.imprimir_cabecalho("Mestre de Classe")

    evolucoes = sistema_evolucao.get_evolucoes_disponiveis(jogador)

    if not evolucoes:
        print("'Você tem potencial, jovem, mas ainda não está pronto para o próximo passo.'")
        print("'Volte quando tiver mais experiência.'")
        funcoes_gerais.pausar()
        return

    print("'Vejo que você trilhou um longo caminho. Chegou a hora de escolher uma especialização.'")
    print("'Seu futuro está em suas mãos. Escolha com sabedoria.'\n")

    evolucoes_listadas = list(evolucoes.items())

    for i, (id_classe, dados) in enumerate(evolucoes_listadas, 1):
        print(f"{i}. Tornar-se um {dados['nome']}")
        print(f"   \"{dados['descricao']}\"\n")

    print(f"{len(evolucoes_listadas) + 1}. 'Ainda não estou pronto.' (Sair)")

    while True:
        escolha_str = input("\nQual caminho você seguirá? > ").strip()
        if not escolha_str.isdigit():
            print("Por favor, insira um número.")
            continue

        idx_escolha = int(escolha_str) - 1

        if 0 <= idx_escolha < len(evolucoes_listadas):
            id_escolhido, dados_escolhidos = evolucoes_listadas[idx_escolha]

            confirmar = input(f"Você tem certeza que deseja se tornar um {dados_escolhidos['nome']}? Esta decisão é permanente. (s/n): ").lower()
            if confirmar == 's':
                logs = sistema_evolucao.evoluir_classe(jogador, id_escolhido)
                funcoes_gerais.limpar_tela()
                funcoes_gerais.imprimir_cabecalho("EVOLUÇÃO DE CLASSE")
                for log in logs:
                    print(f">> {log}")
                    funcoes_gerais.pausar()
                return
            else:
                print("'A sabedoria está em ponderar suas escolhas. Volte quando estiver decidido.'")
                funcoes_gerais.pausar()
                return

        elif idx_escolha == len(evolucoes_listadas):
            print("'O caminho sempre estará aqui para quando você estiver pronto.'")
            funcoes_gerais.pausar()
            return
        else:
            print("Opção inválida.")
