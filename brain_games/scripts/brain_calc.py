from brain_games.cli import welcome_user
from brain_games.engine import run_game
from brain_games.games import calc


def main():
    name = welcome_user()
    run_game(name, calc)


if __name__ == '__main__':
    main()