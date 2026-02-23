import compileall

if __name__ == "__main__":
    ok = compileall.compile_dir(".", quiet=1, maxlevels=10)
    if ok:
        print("Sintaxe OK em todos os arquivos Python.")
        raise SystemExit(0)
    print("Erros de sintaxe encontrados.")
    raise SystemExit(1)
