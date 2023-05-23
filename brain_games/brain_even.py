import random

import prompt


def start_game(username: str):
    """Implement full is even game logic.

    Args:
        username (str): user name
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for question_num in range(3):
        number = random.randint(1, 100)
        print(f'Question: {number}')

        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        if answer == correct_answer:
            print('Correct!')
            print(f'Congratulations, {username}!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            return
