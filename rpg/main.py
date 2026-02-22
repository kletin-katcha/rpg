from .game import Game


def main() -> None:
    game = Game()
    print(game.start_message())


if __name__ == "__main__":
    main()
