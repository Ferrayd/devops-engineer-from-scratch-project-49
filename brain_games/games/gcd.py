import math
import random


def find_gcd(num1, num2):
    return math.gcd(num1, num2)


def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2


def get_game_data():
    num1, num2 = generate_numbers()
    question = f'{num1} {num2}'
    correct_answer = str(find_gcd(num1, num2))
    return question, correct_answer