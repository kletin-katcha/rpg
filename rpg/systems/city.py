from dataclasses import dataclass, field

from rpg.content.loader import load_catalog
from rpg.core.errors import RegraNegocioError
from rpg.systems.crafting import forjar_receita
from rpg.systems.inventory.rules import adicionar_item


@dataclass
class CityState:
    ouro: int = 400
    estruturas: dict[str, int] = field(default_factory=dict)
    plano_automacao_ativo: str | None = None


def construir_estrutura(state: CityState, estrutura_id: str) -> int:
    estruturas = load_catalog("estruturas")
    if estrutura_id not in estruturas:
        raise RegraNegocioError(f"Estrutura inválida: {estrutura_id}")

    atual = state.estruturas.get(estrutura_id, 0)
    if atual > 0:
        raise RegraNegocioError("Estrutura já construída")

    custo = estruturas[estrutura_id]["custo_base"]
    if state.ouro < custo:
        raise RegraNegocioError("Ouro insuficiente para construção")

    state.ouro -= custo
    state.estruturas[estrutura_id] = 1
    return state.estruturas[estrutura_id]


def melhorar_estrutura(state: CityState, estrutura_id: str) -> int:
    estruturas = load_catalog("estruturas")
    if estrutura_id not in estruturas:
        raise RegraNegocioError(f"Estrutura inválida: {estrutura_id}")

    atual = state.estruturas.get(estrutura_id, 0)
    if atual == 0:
        raise RegraNegocioError("Estrutura não construída")

    max_nivel = estruturas[estrutura_id]["max_nivel"]
    if atual >= max_nivel:
        raise RegraNegocioError("Estrutura já está no nível máximo")

    custo = estruturas[estrutura_id]["custo_base"] * (atual + 1)
    if state.ouro < custo:
        raise RegraNegocioError("Ouro insuficiente para melhoria")

    state.ouro -= custo
    state.estruturas[estrutura_id] = atual + 1
    return state.estruturas[estrutura_id]


def ativar_plano_automacao(state: CityState, plano_id: str) -> None:
    planos = load_catalog("planos_automacao")
    if plano_id not in planos:
        raise RegraNegocioError(f"Plano inválido: {plano_id}")

    req = planos[plano_id]["estrutura_requerida"]
    if state.estruturas.get(req, 0) == 0:
        raise RegraNegocioError(f"Estrutura requerida não construída: {req}")

    state.plano_automacao_ativo = plano_id


def processar_automacao(state: CityState, inventario: dict[str, int]) -> dict[str, int]:
    if not state.plano_automacao_ativo:
        return inventario

    planos = load_catalog("planos_automacao")
    plano = planos[state.plano_automacao_ativo]
    for item_id, qtd in plano["ganhos"].items():
        adicionar_item(inventario, item_id, qtd)

    if state.estruturas.get("oficina", 0) >= 1 and inventario.get("sucata_metal", 0) >= 3:
        forjar_receita(inventario, "refino_barra_metal")

    return inventario
