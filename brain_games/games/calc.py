import random

DESCRIPTION = 'What is the result of the expression?'

OPERATORS = ['+', '-', '*']


def generate_expression():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(OPERATORS)
    expression = f'{num1} {operator} {num2}'
    return expression


def calculate_expression(expression):
    parts = expression.split()
    num1 = int(parts[0])
    operator = parts[1]
    num2 = int(parts[2])
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    else:
        raise ValueError(f'Unknown operator: {operator}')
    
    return str(result)


def get_game_data():
    expression = generate_expression()
    correct_answer = calculate_expression(expression)
    return expression, correct_answer