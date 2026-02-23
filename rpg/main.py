from rpg.core.errors import RegraNegocioError
from rpg.content.loader import load_catalog

from .game import Game


def _normalizar_escolha(valor: str) -> str:
    return valor.strip().lower().replace(" ", "_")


def _listar_numerado(opcoes: list[dict], titulo: str) -> None:
    print(f"\n=== {titulo} ===")
    for idx, item in enumerate(opcoes, start=1):
        desc = item.get("descricao") or item.get("papel", "")
        sufixo = f" — {desc}" if desc else ""
        print(f"{idx:>2}) {item['nome']} [{item['id']}]" + sufixo)


def _escolher_item_numerado(label: str, opcoes: list[dict]) -> dict | None:
    mapa_por_id = {_normalizar_escolha(item["id"]): item for item in opcoes}
    while True:
        try:
            valor = input(label).strip()
        except EOFError:
            print("Entrada encerrada. Saindo do jogo.")
            return None

        if not valor:
            print("Entrada vazia. Informe número ou id.")
            continue

        if valor.isdigit():
            idx = int(valor)
            if 1 <= idx <= len(opcoes):
                return opcoes[idx - 1]
            print(f"Número fora do intervalo (1..{len(opcoes)}).")
            continue

        valor_norm = _normalizar_escolha(valor)
        if valor_norm in mapa_por_id:
            return mapa_por_id[valor_norm]

        print("Valor inválido. Use número da lista ou id mostrado entre colchetes.")


def _render_hud(game: Game) -> str:
    jogador = game.state.jogador
    acoes = game.opcoes_cidade()

    grupos = {
        "Combate": [a for a in acoes if a.startswith("cacar_") or a.startswith("desbloquear_") or a in {"ver_arvore", "ver_log_combate"}],
        "Economia/Cidade": [
            a
            for a in acoes
            if a.startswith("construir_")
            or a.startswith("melhorar_")
            or a.startswith("forjar_")
            or a in {"ativar_automacao", "avancar_dia", "ver_mercado", "vender_sucata", "produzir_liga_metal", "descansar", "coletar_item_inicial"}
        ],
        "Mundo/Meta": [
            a
            for a in acoes
            if a.startswith("ver_")
            or a.startswith("gerar_")
            or a.startswith("iniciar_")
            or a.startswith("avancar_")
            or a in {"aplicar_mutador", "evento_mundo", "contrato_aleatorio", "concluir_contrato", "falhar_contrato", "resgatar_beneficio_faccao", "faccao_status", "rodar_agenda_faccoes", "viajar_fronteira_norte", "viajar_ruinas_antigas", "explorar_dungeon", "explorar_fora_cidade"}
        ],
        "Sistema": [a for a in acoes if a in {"ajuda", "buscar_acoes:<termo>", "salvar", "carregar", "rollback_criacao", "sair"}],
    }

    grupos = {k: v for k, v in grupos.items() if v}

    atributos_ordenados = sorted(jogador.atributos.items())
    atributos_fmt = " | ".join(f"{k}:{v}" for k, v in atributos_ordenados)

    linhas = [
        "=" * 88,
        f"RPG Surreal | Cidade: {game.state.cidade_atual} | Região: {game.state.regiao_atual}",
        (
            f"Jogador: {jogador.nome} | Raça: {jogador.raca_id} | Sub-raça: {jogador.sub_raca_id} | "
            f"Classe: {jogador.classe_id} | Nível {jogador.nivel}"
        ),
        f"HP {jogador.hp_atual}/{jogador.hp_max} | Ouro {game.state.cidade.ouro} | Clima {game.state.clima} | Hora {game.state.hora:02d}h",
        "-" * 88,
        "ATRIBUTOS / STATUS:",
        atributos_fmt,
        "-" * 88,
        "Comandos (número no setup; aqui use nome exato ou atalhos):",
    ]

    for grupo, comandos in grupos.items():
        preview = ", ".join(comandos[:6])
        extra = " ..." if len(comandos) > 6 else ""
        linhas.append(f"[{grupo}] {preview}{extra}")

    linhas.append("Atalhos: lobo | goblin | forjar | oficina | automacao | dia | status | help")
    linhas.append("=" * 88)
    return "\n".join(linhas)


def main() -> None:
    game = Game()
    print(game.start_message())

    racas_catalog = list(load_catalog("racas").values())
    classes_catalog = list(load_catalog("classes").values())

    racas_catalog.sort(key=lambda x: x["nome"])
    classes_catalog.sort(key=lambda x: x["nome"])

    print("\n=== Criação de Personagem ===")
    try:
        nome = input("Nome do personagem: ").strip()
    except EOFError:
        print("Entrada encerrada. Saindo do jogo.")
        return

    if not nome:
        print("Nome inválido. Encerrando criação.")
        return

    _listar_numerado(racas_catalog, "Escolha sua raça")
    raca = _escolher_item_numerado("Raça (número/id): ", racas_catalog)
    if raca is None:
        return

    sub_racas = list(game.opcoes_sub_raca(raca["id"]).values())
    sub_racas.sort(key=lambda x: x["nome"])
    _listar_numerado(sub_racas, f"Sub-raças de {raca['nome']}")
    sub_raca = _escolher_item_numerado("Sub-raça (número/id): ", sub_racas)
    if sub_raca is None:
        return

    _listar_numerado(classes_catalog, "Escolha sua classe")
    classe = _escolher_item_numerado("Classe (número/id): ", classes_catalog)
    if classe is None:
        return

    try:
        jogador = game.criar_jogador(nome, raca["id"], classe["id"], sub_raca_id=sub_raca["id"])
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
