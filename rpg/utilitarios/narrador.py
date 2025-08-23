import sys
import time
import random

def narrar(texto: str, velocidade: float = 0.04):
    """
    Imprime o texto lentamente, como se estivesse sendo narrado.
    """
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidade)
    print() # Pula para a próxima linha no final

def imprimir_dialogo(personagem: str, fala: str, velocidade: float = 0.03):
    """
    Imprime uma linha de diálogo formatada.
    """
    texto_formatado = f"[{personagem}]: "
    sys.stdout.write(texto_formatado)
    sys.stdout.flush()
    time.sleep(0.5) # Pequena pausa antes da fala

    for char in fala:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def imprimir_dado_rolando(texto_acao: str, resultado: int, max_dado: int = 20):
    """
    Mostra uma animação de "rolando o dado" e depois o resultado.
    """
    print(f"\nTentando... {texto_acao}")
    frames = [f"d{max_dado} [ {random.randint(1, max_dado)} ]",
              f"d{max_dado} [ {random.randint(1, max_dado)} ]",
              f"d{max_dado} [ {random.randint(1, max_dado)} ]",
              f"d{max_dado} [ {random.randint(1, max_dado)} ]",
              f"d{max_dado} [ {resultado} ]"]

    for i, frame in enumerate(frames):
        time.sleep(0.2 + i * 0.1)
        print(f"\r{frame}", end="")

    print(f"\rResultado: {resultado}/{max_dado}\n")
