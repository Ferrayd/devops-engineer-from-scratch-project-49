ROUNDS_COUNT = 3


def run_game(user_name, game_module):
    print(game_module.DESCRIPTION)
    
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game_module.get_game_data()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
        
        print('Correct!')
    
    print(f'Congratulations, {user_name}!')