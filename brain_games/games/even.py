import random

ROUNDS_COUNT = 3


def is_even(number):
    return number % 2 == 0


def get_game_data():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer


def play_even_game(user_name):
    from brain_games.engine import run_game
    
    game_name = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(game_name, user_name, get_game_data)
