import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent.parent.absolute().resolve()))
import play_game


def main():
    play_game.snakes_and_ladders()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\ngoodbye.")
