import random

MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_START = 1
MAX_START = 100
MIN_STEP = 1
MAX_STEP = 10


def generate_progression():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    hidden_index = random.randint(0, length - 1)
    
    progression = [start + i * step for i in range(length)]
    hidden_number = progression[hidden_index]
    
    return progression, hidden_index, hidden_number


def format_progression(progression, hidden_index):
    formatted = []
    for i, num in enumerate(progression):
        if i == hidden_index:
            formatted.append('..')
        else:
            formatted.append(str(num))
    
    return ' '.join(formatted)


def get_game_data():
    progression, hidden_index, hidden_number = generate_progression()
    question = format_progression(progression, hidden_index)
    correct_answer = str(hidden_number)
    
    return question, correct_answer