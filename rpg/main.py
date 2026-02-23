from rpg.core.errors import RegraNegocioError

from .game import Game


def _normalizar_escolha(valor: str) -> str:
    return valor.strip().lower().replace(" ", "_")


def _escolher_opcao(label: str, opcoes: list[str]) -> str | None:
    opcoes_norm = {o.lower(): o for o in opcoes}
    while True:
        try:
            valor = input(label).strip()
        except EOFError:
            print("Entrada encerrada. Saindo do jogo.")
            return None

        valor_norm = _normalizar_escolha(valor)
        if valor_norm in opcoes_norm:
            return opcoes_norm[valor_norm]

        print(f"Valor inválido: '{valor}'. Opções válidas: {', '.join(opcoes)}")


def main() -> None:
    game = Game()
    print(game.start_message())

    opcoes = game.opcoes_criacao()
    print(f"Raças: {', '.join(opcoes['racas'])}")
    print(f"Classes: {', '.join(opcoes['classes'])}")

    try:
        nome = input("Nome do personagem: ").strip()
    except EOFError:
        print("Entrada encerrada. Saindo do jogo.")
        return

    if not nome:
        print("Nome inválido. Encerrando criação.")
        return

    raca = _escolher_opcao("Escolha raça: ", opcoes["racas"])
    if raca is None:
        return

    classe = _escolher_opcao("Escolha classe: ", opcoes["classes"])
    if classe is None:
        return

    try:
        jogador = game.criar_jogador(nome, raca, classe)
    except RegraNegocioError as exc:
        game.state.metricas_onboarding["erros_criacao"] += 1
        print(f"Erro na criação: {exc}")
        return

    print(f"Bem-vindo, {jogador.nome}! Você está em {game.state.cidade_atual}.")

    while game.running:
        print(f"Ações da cidade: {', '.join(game.opcoes_cidade())}")
        print(
            "Dica: contrato_aleatorio -> concluir_contrato/falhar_contrato -> resgatar_beneficio_faccao; "
            "atalhos: lobo, goblin, forjar, oficina, automacao, dia, status, historico, arvore, help + salvar/carregar"
        )
        try:
            acao = input("Ação: ").strip()
        except EOFError:
            print("Entrada encerrada. Saindo do jogo.")
            break

        try:
            print(game.executar_acao_cidade(acao))
        except RegraNegocioError as exc:
            game.state.metricas_onboarding["erros_regra_negocio"] += 1
            print(f"Erro: {exc}")


if __name__ == "__main__":
    main()
