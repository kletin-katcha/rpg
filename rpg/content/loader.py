"""Loader único para catálogos de conteúdo com validação de schema e IDs únicos."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

from .schemas.common import ContentValidationError
from .schemas.raca import validate_raca
from .schemas.classe import validate_classe
from .schemas.item import validate_item
from .schemas.monstro import validate_monstro
from .schemas.receita import validate_receita
from .schemas.estrutura import validate_estrutura
from .schemas.automacao import validate_plano_automacao
from .schemas.arvore_habilidade import validate_arvore_habilidade
from .schemas.faccao import validate_faccao
from .schemas.evento_mundo import validate_evento_mundo
from .schemas.contrato import validate_contrato

Validator = Callable[[dict, str], None]


CATALOGS: dict[str, tuple[str, Validator]] = {
    "racas": ("racas.json", validate_raca),
    "classes": ("classes.json", validate_classe),
    "itens": ("itens.json", validate_item),
    "monstros": ("monstros.json", validate_monstro),
    "receitas": ("receitas.json", validate_receita),
    "estruturas": ("estruturas.json", validate_estrutura),
    "planos_automacao": ("planos_automacao.json", validate_plano_automacao),
    "arvores_habilidades": ("arvores_habilidades.json", validate_arvore_habilidade),
    "faccoes": ("faccoes.json", validate_faccao),
    "eventos_mundo": ("eventos_mundo.json", validate_evento_mundo),
    "contratos": ("contratos.json", validate_contrato),
}


def _base_data_dir() -> Path:
    return Path(__file__).resolve().parent / "data"


def load_catalog(catalog_name: str) -> dict[str, dict]:
    if catalog_name not in CATALOGS:
        raise ContentValidationError(f"Catálogo não registrado: {catalog_name}")

    file_name, validator = CATALOGS[catalog_name]
    path = _base_data_dir() / file_name
    if not path.exists():
        raise ContentValidationError(f"Arquivo de catálogo não encontrado: {path}")

    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ContentValidationError(f"{catalog_name}: raiz deve ser lista")

    by_id: dict[str, dict] = {}
    for idx, entry in enumerate(raw):
        context = f"{catalog_name}[{idx}]"
        if not isinstance(entry, dict):
            raise ContentValidationError(f"{context}: entrada deve ser objeto")

        validator(entry, context)
        entry_id = entry["id"]
        if entry_id in by_id:
            raise ContentValidationError(f"{catalog_name}: id duplicado '{entry_id}'")
        by_id[entry_id] = entry

    return by_id


def load_all_catalogs() -> dict[str, dict[str, dict]]:
    return {name: load_catalog(name) for name in CATALOGS}
