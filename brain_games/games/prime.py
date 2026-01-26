import random


def is_prime(number):
    if number < 2:
        return False
    
    if number == 2:
        return True
    
    if number % 2 == 0:
        return False
    
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False
    
    return True


def generate_number():
    return random.randint(2, 100)


def get_game_data():
    number = generate_number()
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    
    return question, correct_answer