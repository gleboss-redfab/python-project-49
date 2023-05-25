import random

from brain_games.utils.game_logic import ROUND_NUMBER, start_game


def start_brain_even():
    """ Generate data for game and start game algorithm """
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    questions = []
    answers_correct = []

    # generate questions and answers
    for round in range(ROUND_NUMBER):
        number = random.randint(1, 100)
        questions.append(str(number))
        if number % 2 == 0:
            answers_correct.append("yes")
        else:
            answers_correct.append("no")

    start_game(game_rule=rules,
               questions=questions,
               answer_correct=answers_correct)
