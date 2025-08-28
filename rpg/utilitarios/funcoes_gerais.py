import os
import sys
import time

def limpar_tela():
    """Limpa o console, compatível com Windows, macOS e Linux."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar(mensagem: str = "Pressione ENTER para continuar..."):
    """Pausa a execução e espera que o usuário pressione Enter."""
    input(mensagem)

def imprimir_cabecalho(titulo: str, nivel: int = 1):
    """
    Imprime um cabeçalho formatado.
    Nível 1 é para títulos principais, Nível 2 para subtítulos.
    """
    if nivel == 1:
        print("\n" + "=" * 60)
        print(f" {titulo.upper()} ".center(60, "="))
        print("=" * 60 + "\n")
    elif nivel == 2:
        print("\n" + "-" * 40)
        print(f" {titulo} ".center(40, "-"))
        print("-" * 40 + "\n")
    else:
        print(f"\n--- {titulo} ---\n")

def animacao_simples(texto: str, duracao: float = 1.0):
    """Exibe uma animação de carregamento simples."""
    frames = ["|", "/", "-", "\\"]
    tempo_final = time.time() + duracao
    while time.time() < tempo_final:
        for frame in frames:
            print(f"\r{texto} {frame}", end="")
            time.sleep(0.1)
    print(f"\r{texto}... Concluído! ")
