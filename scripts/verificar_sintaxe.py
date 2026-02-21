"""Compila todos os .py do projeto para validar sintaxe."""

import compileall
import sys

if __name__ == "__main__":
    ok = compileall.compile_dir(".", quiet=1, maxlevels=10)
    if ok:
        print("Sintaxe OK em todos os arquivos Python.")
        raise SystemExit(0)
    print("Foram encontrados erros de sintaxe.")
    raise SystemExit(1)
