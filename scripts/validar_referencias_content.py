"""Valida referências cruzadas entre catálogos para suportar conteúdo massivo."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from rpg.content.loader import load_all_catalogs
from rpg.content.schemas.common import ContentValidationError


def validar_referencias() -> None:
    data = load_all_catalogs()
    itens = set(data["itens"].keys())
    racas = set(data["racas"].keys())

    faccoes = set(data["faccoes"].keys())
    estruturas = set(data["estruturas"].keys())

    for sid, sub_raca in data["sub_racas"].items():
        if sub_raca.get("raca_id") not in racas:
            raise ContentValidationError(f"sub_racas.{sid}: raca_id inexistente '{sub_raca.get('raca_id')}'")

    for mid, monstro in data["monstros"].items():
        for item_id in monstro.get("loot", {}).keys():
            if item_id not in itens:
                raise ContentValidationError(f"monstros.{mid}: loot referencia item inexistente '{item_id}'")

    for rid, receita in data["receitas"].items():
        for item_id in list(receita.get("insumos", {}).keys()) + list(receita.get("resultado", {}).keys()):
            if item_id not in itens:
                raise ContentValidationError(f"receitas.{rid}: referencia item inexistente '{item_id}'")

    for cid, contrato in data["contratos"].items():
        if contrato.get("faccao_id") not in faccoes:
            raise ContentValidationError(f"contratos.{cid}: faccao_id inexistente '{contrato.get('faccao_id')}'")

    for pid, plano in data["planos_automacao"].items():
        if plano.get("estrutura_requerida") not in estruturas:
            raise ContentValidationError(
                f"planos_automacao.{pid}: estrutura_requerida inexistente '{plano.get('estrutura_requerida')}'"
            )
        for item_id in plano.get("ganhos", {}).keys():
            if item_id not in itens:
                raise ContentValidationError(f"planos_automacao.{pid}: ganho referencia item inexistente '{item_id}'")


if __name__ == "__main__":
    try:
        validar_referencias()
        print("Referências de conteúdo: OK")
    except ContentValidationError as exc:
        print(f"Falha de referência de conteúdo: {exc}")
        raise SystemExit(1)
