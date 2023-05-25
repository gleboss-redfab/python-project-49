import random

from brain_games.utils.game_logic import ROUND_NUMBER, start_game


def find_gcd(num_1: int, num_2: int) -> int:
    """Find GCD of two numbers
    Args:
        num_1 (int): number 1
        num_2 (int): number 2
    Returns:
        int: GCD of number 1 and number 2
    """
    while num_1 != num_2:
        if num_1 > num_2:
            num_1 = num_1 - num_2
        else:
            num_2 = num_2 - num_1
    return num_2


def start_brain_gcd():
    """ Generate data for game and start game algorithm """
    rules = 'Find the greatest common divisor of given numbers.'
    questions = []
    answers_correct = []

    # generate questions and answers
    for round in range(ROUND_NUMBER):
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)

        question = str(number_1) + " " + str(number_2)
        questions.append(question)

        answer = find_gcd(number_1, number_2)
        answers_correct.append(str(answer))

    start_game(game_rule=rules,
               questions=questions,
               answer_correct=answers_correct)
