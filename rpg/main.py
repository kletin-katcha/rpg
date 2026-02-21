"""Entrypoint do pacote reboot."""

from console_client import main_loop


def main() -> None:
    main_loop()


if __name__ == "__main__":
    main()
