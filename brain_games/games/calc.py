import random

OPERATORS = ['+', '-', '*']


def generate_expression():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(OPERATORS)
    expression = f'{num1} {operator} {num2}'
    return expression


def calculate_expression(expression):
    return str(eval(expression))


def get_game_data():
    expression = generate_expression()
    correct_answer = calculate_expression(expression)
    return expression, correct_answer