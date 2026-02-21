"""Validação rápida de sintaxe para todos os módulos Python do repositório."""

from pathlib import Path
import py_compile


EXCLUIR_PARTES = {".git", "__pycache__", ".venv", "venv"}


def iter_python_files(base: Path):
    for path in base.rglob("*.py"):
        if any(parte in EXCLUIR_PARTES for parte in path.parts):
            continue
        yield path


def main():
    raiz = Path(__file__).resolve().parents[1]
    erros = []
    for arquivo in iter_python_files(raiz):
        try:
            py_compile.compile(str(arquivo), doraise=True)
        except py_compile.PyCompileError as exc:
            erros.append((arquivo, exc.msg))

    if erros:
        print("Falhas de sintaxe encontradas:")
        for arquivo, msg in erros:
            print(f"- {arquivo}: {msg}")
        raise SystemExit(1)

    print("Sintaxe OK em todos os arquivos Python.")


if __name__ == "__main__":
    main()
