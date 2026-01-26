import prompt

ROUNDS_COUNT = 3


def run_game(game_name, user_name, get_game_data):

    print(game_name)
    
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = get_game_data()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return False
        
        print('Correct!')
    
    print(f'Congratulations, {user_name}!')
    return True