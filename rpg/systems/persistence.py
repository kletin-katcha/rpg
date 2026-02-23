import json
from pathlib import Path
from tempfile import NamedTemporaryFile

from rpg.core.errors import RegraNegocioError
from rpg.game import Game, GameState
from rpg.systems.city import CityState
from rpg.core.types import CharacterState


SAVE_VERSION = 2


def _to_dict(game: Game) -> dict:
    p = game.state.jogador
    return {
        "save_version": SAVE_VERSION,
        "etapa": game.state.etapa,
        "cidade_atual": game.state.cidade_atual,
        "inventario": game.state.inventario,
        "log": game.state.log,
        "cidade": {
            "ouro": game.state.cidade.ouro,
            "estruturas": game.state.cidade.estruturas,
            "plano_automacao_ativo": game.state.cidade.plano_automacao_ativo,
        },
        "reputacoes": game.state.reputacoes,
        "contrato_ativo": game.state.contrato_ativo,
        "mercado": game.state.mercado,
        "dia_economico": game.state.dia_economico,
        "hora": game.state.hora,
        "clima": game.state.clima,
        "jornal_cidade": game.state.jornal_cidade,
        "codex": sorted(game.state.codex),
        "mutador_ativo": game.state.mutador_ativo,
        "memoria_faccoes": game.state.memoria_faccoes,
        "cadeia_contratos": game.state.cadeia_contratos,
        "cadeia_resolvidos": game.state.cadeia_resolvidos,
        "tensao_faccoes": game.state.tensao_faccoes,
        "crise_urbana": game.state.crise_urbana,
        "regiao_atual": game.state.regiao_atual,
        "energia_viagem": game.state.energia_viagem,
        "regioes_descobertas": sorted(game.state.regioes_descobertas),
        "dungeon_ativa": game.state.dungeon_ativa,
        "agenda_faccoes": game.state.agenda_faccoes,
        "arco_longo": game.state.arco_longo,
        "checkpoint_criacao": game.state.checkpoint_criacao,
        "ultimo_log_combate": game.state.ultimo_log_combate,
        "metricas_onboarding": game.state.metricas_onboarding,
        "jogador": None
        if p is None
        else {
            "id": p.id,
            "nome": p.nome,
            "nivel": p.nivel,
            "xp": p.xp,
            "atributos": p.atributos,
            "hp_atual": p.hp_atual,
            "hp_max": p.hp_max,
            "habilidades_desbloqueadas": p.habilidades_desbloqueadas,
        },
    }


def save_game(game: Game, path: str = "savegame.json") -> Path:
    data = _to_dict(game)
    out = Path(path)
    backup = out.with_suffix(f"{out.suffix}.bak")

    if out.exists():
        backup.write_text(out.read_text(encoding="utf-8"), encoding="utf-8")

    with NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=out.parent) as handle:
        handle.write(json.dumps(data, ensure_ascii=False, indent=2))
        temp_path = Path(handle.name)

    temp_path.replace(out)
    return out


def _read_save_file(p: Path) -> dict:
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RegraNegocioError(f"Save corrompido em {p}: {exc}") from exc


def _build_game_from_raw(raw: dict) -> Game:
    save_version = int(raw.get("save_version", 1))
    if save_version > SAVE_VERSION:
        raise RegraNegocioError(
            f"Save versão {save_version} não suportado nesta build (máx: {SAVE_VERSION})."
        )

    game = Game()

    jogador_raw = raw.get("jogador")
    jogador = None
    if jogador_raw:
        jogador = CharacterState(
            id=jogador_raw["id"],
            nome=jogador_raw["nome"],
            nivel=jogador_raw["nivel"],
            xp=jogador_raw["xp"],
            atributos=jogador_raw["atributos"],
            hp_atual=jogador_raw["hp_atual"],
            hp_max=jogador_raw["hp_max"],
            habilidades_desbloqueadas=jogador_raw.get("habilidades_desbloqueadas", []),
        )

    cidade_raw = raw.get("cidade", {})
    cidade = CityState(
        ouro=cidade_raw.get("ouro", 400),
        estruturas=cidade_raw.get("estruturas", {}),
        plano_automacao_ativo=cidade_raw.get("plano_automacao_ativo"),
    )

    game.state = GameState(
        etapa=raw.get("etapa", "criacao"),
        cidade_atual=raw.get("cidade_atual", "Vila Aurora"),
        jogador=jogador,
        inventario=raw.get("inventario", {}),
        log=raw.get("log", []),
        cidade=cidade,
        reputacoes=raw.get("reputacoes", {}),
        contrato_ativo=raw.get("contrato_ativo"),
        mercado=raw.get("mercado", {}),
        dia_economico=raw.get("dia_economico", 0),
        hora=raw.get("hora", 8),
        clima=raw.get("clima", "ensolarado"),
        jornal_cidade=raw.get("jornal_cidade", []),
        codex=set(raw.get("codex", [])),
        mutador_ativo=raw.get("mutador_ativo"),
        memoria_faccoes=raw.get("memoria_faccoes", {}),
        cadeia_contratos=raw.get("cadeia_contratos", []),
        cadeia_resolvidos=raw.get("cadeia_resolvidos", 0),
        tensao_faccoes=raw.get("tensao_faccoes", {}),
        crise_urbana=raw.get("crise_urbana", {}),
        regiao_atual=raw.get("regiao_atual", "vila_aurora"),
        energia_viagem=raw.get("energia_viagem", 6),
        regioes_descobertas=set(raw.get("regioes_descobertas", ["vila_aurora"])),
        dungeon_ativa=raw.get("dungeon_ativa"),
        agenda_faccoes=raw.get("agenda_faccoes", []),
        arco_longo=raw.get("arco_longo"),
        checkpoint_criacao=raw.get("checkpoint_criacao"),
        ultimo_log_combate=raw.get("ultimo_log_combate", []),
        metricas_onboarding=raw.get(
            "metricas_onboarding",
            {"erros_criacao": 0, "comandos_invalidos": 0, "erros_regra_negocio": 0},
        ),
    )
    return game


def load_game(path: str = "savegame.json") -> Game:
    p = Path(path)
    if not p.exists():
        raise RegraNegocioError(f"Save não encontrado: {path}")

    try:
        raw = _read_save_file(p)
    except RegraNegocioError:
        backup = p.with_suffix(f"{p.suffix}.bak")
        if not backup.exists():
            raise
        raw = _read_save_file(backup)

    return _build_game_from_raw(raw)
