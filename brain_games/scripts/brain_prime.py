from brain_games import games
from brain_games.cli import welcome_user
from brain_games.engine import run_game


def main():
    name = welcome_user()
    run_game(name, games.prime)


if __name__ == '__main__':
    main()