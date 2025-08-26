from typing import TYPE_CHECKING
from ..entidades.monstro import Monstro
from ..dados.monstros_area1 import MONSTROS_AREA1

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem

def criar_monstro_por_id(id_monstro: str) -> Monstro:
    """Cria uma instância de Monstro a partir dos dados do dicionário."""
    dados_monstro = MONSTROS_AREA1.get(id_monstro)
    if not dados_monstro:
        raise ValueError(f"Monstro com ID '{id_monstro}' não encontrado.")

    habilidades = dados_monstro.get("habilidades", [])
    ataques_base = dados_monstro.get("ataques_base_ids", [])
    loot_table = dados_monstro.get("loot_table", [])

    return Monstro(
        id_monstro=id_monstro,
        nome=dados_monstro["nome"],
        nivel=dados_monstro["nivel"],
        familia=dados_monstro["familia"],
        xp_recompensa=dados_monstro["xp_recompensa"],
        ouro_recompensa=dados_monstro["ouro_recompensa"],
        stats_base=dados_monstro["stats_base"],
        habilidades_ids=habilidades,
        ataques_base_ids=ataques_base,
        loot_table=loot_table,
        comportamento_ia=dados_monstro.get("comportamento_ia", "agressivo")
    )
