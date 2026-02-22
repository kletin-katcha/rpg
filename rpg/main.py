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
        print("Dica: contrato_aleatorio -> concluir_contrato/falhar_contrato -> resgatar_beneficio_faccao; atalhos: lobo, goblin, forjar, oficina, automacao, dia, status, historico, arvore, help + salvar/carregar (novo: cacar_boss, ver_mercado, vender_sucata, produzir_liga_metal)")
        acao = input("Ação: ").strip()
        try:
            print(game.executar_acao_cidade(acao))
        except RegraNegocioError as exc:
            print(f"Erro: {exc}")


if __name__ == "__main__":
    main()
