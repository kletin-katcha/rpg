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


def _agrupar_acoes(acoes: list[str]) -> dict[str, list[str]]:
    grupos: dict[str, list[str]] = {
        "Combate": [],
        "Economia/Cidade": [],
        "Mundo/Meta": [],
        "Sistema": [],
        "Outros": [],
    }

    for acao in acoes:
        if acao.startswith("cacar_") or acao.startswith("desbloquear_") or acao in {"ver_arvore", "ver_log_combate"}:
            grupos["Combate"].append(acao)
        elif acao.startswith("construir_") or acao.startswith("melhorar_") or acao.startswith("forjar_") or acao in {
            "ativar_automacao",
            "avancar_dia",
            "ver_mercado",
            "vender_sucata",
            "produzir_liga_metal",
            "descansar",
            "coletar_item_inicial",
        }:
            grupos["Economia/Cidade"].append(acao)
        elif acao.startswith("ver_") or acao.startswith("gerar_") or acao.startswith("iniciar_") or acao.startswith("avancar_") or acao in {
            "aplicar_mutador",
            "evento_mundo",
            "contrato_aleatorio",
            "concluir_contrato",
            "falhar_contrato",
            "resgatar_beneficio_faccao",
            "faccao_status",
            "rodar_agenda_faccoes",
            "viajar_fronteira_norte",
            "viajar_ruinas_antigas",
            "explorar_dungeon",
        }:
            grupos["Mundo/Meta"].append(acao)
        elif acao in {"ajuda", "buscar_acoes:<termo>", "salvar", "carregar", "rollback_criacao", "sair"}:
            grupos["Sistema"].append(acao)
        else:
            grupos["Outros"].append(acao)

    return {k: v for k, v in grupos.items() if v}


def _render_hud(game: Game) -> str:
    jogador = game.state.jogador
    acoes = game.opcoes_cidade()
    grupos = _agrupar_acoes(acoes)
    linhas = [
        "=" * 72,
        f"RPG Surreal | {game.state.cidade_atual} | Região: {game.state.regiao_atual}",
        f"Jogador: {jogador.nome} | Nível {jogador.nivel} | HP {jogador.hp_atual}/{jogador.hp_max} | Ouro {game.state.cidade.ouro}",
        f"Clima: {game.state.clima} | Hora: {game.state.hora:02d}h | Energia viagem: {game.state.energia_viagem}",
        "-" * 72,
        "Comandos (use o nome exato; `ajuda` mostra visão detalhada):",
    ]

    for grupo, comandos in grupos.items():
        preview = ", ".join(comandos[:6])
        extra = " ..." if len(comandos) > 6 else ""
        linhas.append(f"[{grupo}] {preview}{extra}")

    linhas.append("Atalhos: lobo | goblin | forjar | oficina | automacao | dia | status | help")
    linhas.append("=" * 72)
    return "\n".join(linhas)


def main() -> None:
    game = Game()
    print(game.start_message())

    opcoes = game.opcoes_criacao()
    print("\n=== Criação de Personagem ===")
    print(f"Raças disponíveis : {', '.join(opcoes['racas'])}")
    print(f"Classes disponíveis: {', '.join(opcoes['classes'])}")

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

    print(f"\nBem-vindo, {jogador.nome}! Você está em {game.state.cidade_atual}.\n")

    while game.running:
        print(_render_hud(game))
        try:
            acao = input("Ação > ").strip()
        except EOFError:
            print("Entrada encerrada. Saindo do jogo.")
            break

        try:
            print(f"\n{game.executar_acao_cidade(acao)}\n")
        except RegraNegocioError as exc:
            game.state.metricas_onboarding["erros_regra_negocio"] += 1
            print(f"\nErro: {exc}\n")


if __name__ == "__main__":
    main()
