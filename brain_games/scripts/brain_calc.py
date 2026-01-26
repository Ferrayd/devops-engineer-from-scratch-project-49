from brain_games.cli import welcome_user
from brain_games.engine import run_game
from brain_games.games.calc import get_game_data


def main():
    name = welcome_user()
    game_name = 'What is the result of the expression?'
    run_game(game_name, name, get_game_data)


if __name__ == '__main__':
    main()