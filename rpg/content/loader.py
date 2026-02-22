"""Loader único para catálogos de conteúdo com validação de schema e IDs únicos."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

from .schemas.common import ContentValidationError
from .schemas.raca import validate_raca
from .schemas.classe import validate_classe
from .schemas.item import validate_item

Validator = Callable[[dict, str], None]


CATALOGS: dict[str, tuple[str, Validator]] = {
    "racas": ("racas.json", validate_raca),
    "classes": ("classes.json", validate_classe),
    "itens": ("itens.json", validate_item),
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
