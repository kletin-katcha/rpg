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
        game.state.metricas_onboarding["erros_criacao"] += 1
        print(f"Erro na criação: {exc}")
        return

    print(f"Bem-vindo, {jogador.nome}! Você está em {game.state.cidade_atual}.")

    while game.running:
        print(f"Ações da cidade: {', '.join(game.opcoes_cidade())}")
        print("Dica: contrato_aleatorio -> concluir_contrato/falhar_contrato -> resgatar_beneficio_faccao; atalhos: lobo, goblin, forjar, oficina, automacao, dia, status, historico, arvore, help + salvar/carregar (novo: cacar_boss, ver_mercado, vender_sucata, produzir_liga_metal, ver_clima, ver_jornal, ver_codex, gerar_arco_mundo, aplicar_mutador, ver_memoria_faccoes, ver_condicoes_combate, iniciar_cadeia_contratos, ver_cadeia_contratos, gerar_tensao_faccoes, ver_tensao_faccoes, gerar_crise_urbana, ver_crise_urbana, ver_regiao, viajar_fronteira_norte, viajar_ruinas_antigas, gerar_dungeon, explorar_dungeon, rodar_agenda_faccoes, ver_agenda_faccoes, iniciar_arco_longo, avancar_arco_longo, ver_arco_longo, gerar_pacote_expansao, simular_balance_headless)")
        acao = input("Ação: ").strip()
        try:
            print(game.executar_acao_cidade(acao))
        except RegraNegocioError as exc:
            game.state.metricas_onboarding["erros_regra_negocio"] += 1
            print(f"Erro: {exc}")


if __name__ == "__main__":
    main()
