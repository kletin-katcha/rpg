import json
from pathlib import Path

from rpg.core.errors import RegraNegocioError
from rpg.game import Game, GameState
from rpg.systems.city import CityState
from rpg.core.types import CharacterState


def _to_dict(game: Game) -> dict:
    p = game.state.jogador
    return {
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
        },
    }


def save_game(game: Game, path: str = "savegame.json") -> Path:
    data = _to_dict(game)
    out = Path(path)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return out


def load_game(path: str = "savegame.json") -> Game:
    p = Path(path)
    if not p.exists():
        raise RegraNegocioError(f"Save não encontrado: {path}")

    raw = json.loads(p.read_text(encoding="utf-8"))
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
    )
    return game
