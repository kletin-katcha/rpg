"""Ponto de entrada do pacote para executar o cliente de console via `python -m rpg.main`."""

from console_client import main_loop


def main():
    """Inicia o loop principal do cliente de console."""
    main_loop()


if __name__ == "__main__":
    main()
