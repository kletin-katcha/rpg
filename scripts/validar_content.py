"""Valida todos os catálogos de conteúdo usando o loader oficial."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from rpg.content.loader import load_all_catalogs
from rpg.content.schemas.common import ContentValidationError


if __name__ == "__main__":
    try:
        data = load_all_catalogs()
        total = sum(len(v) for v in data.values())
        print(f"Conteúdo válido. Catálogos: {list(data.keys())}. Entradas: {total}")
    except ContentValidationError as exc:
        print(f"Falha de validação de conteúdo: {exc}")
        raise SystemExit(1)
