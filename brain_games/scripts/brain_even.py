#!/usr/bin/env python3
import random

import prompt

from brain_games.cli import welcome_user


def main():
    """ user"""
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        number = random.randint(1, 100)
        print(f'Question: {number}')

        answer = prompt.string('Your answer: ')
        if (number % 2 == 0 and answer == 'yes') or \
           (number % 2 != 0 and answer == 'no'):
            print('Correct!')
            print(f'Congratulations, {name}!')
        else:
            correct_answer = 'yes' if number % 2 == 0 else 'no'
            print(f"'{answer}' is wrong answer ;(. \
                Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return


if __name__ == "__main__":
    main()
