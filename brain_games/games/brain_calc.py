import random

from brain_games.utils.game_logic import ROUND_NUMBER, start_game


def start_brain_calc():
    """ Generate data for game and start game algorithm """
    rules = 'What is the result of the expression?'
    questions = []
    answers_correct = []

    # generate questions and answers
    for round in range(ROUND_NUMBER):
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        operation = random.randint(1, 3)

        if operation == 1:
            question_text = str(number_1) + " + " + str(number_2)
            questions.append(question_text)
            result = str(number_1 + number_2)
            answers_correct.append(result)
        elif operation == 2:
            question_text = str(number_1) + " - " + str(number_2)
            questions.append(question_text)
            result = str(number_1 - number_2)
            answers_correct.append(result)
        else:
            question_text = str(number_1) + " * " + str(number_2)
            questions.append(question_text)
            result = str(number_1 * number_2)
            answers_correct.append(result)

    start_game(game_rule=rules,
               questions=questions,
               answer_correct=answers_correct)
