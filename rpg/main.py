from rpg.core.errors import RegraNegocioError

from .game import Game


def main() -> None:
    game = Game()
    print(game.start_message())

    opcoes = game.opcoes_criacao()
    print(f"Raças: {', '.join(opcoes['racas'])}")
    print(f"Classes: {', '.join(opcoes['classes'])}")

    nome = input("Nome do personagem: ").strip()
    raca = input("Escolha raça: ").strip()
    classe = input("Escolha classe: ").strip()

    try:
        jogador = game.criar_jogador(nome, raca, classe)
    except RegraNegocioError as exc:
        print(f"Erro na criação: {exc}")
        return

    print(f"Bem-vindo, {jogador.nome}! Você está em {game.state.cidade_atual}.")

    while game.running:
        print(f"Ações da cidade: {', '.join(game.opcoes_cidade())}")
        acao = input("Ação: ").strip()
        try:
            print(game.executar_acao_cidade(acao))
        except RegraNegocioError as exc:
            print(f"Erro: {exc}")


if __name__ == "__main__":
    main()
