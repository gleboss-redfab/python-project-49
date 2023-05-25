import random

from brain_games.utils.game_logic import ROUND_NUMBER, start_game


def is_prime(number: int) -> bool:
    """Check if number is prime
    Args:
        number (int): number for checking
    Returns:
        bool: prime or not
    """
    if number == 1:
        return False

    for i in range(2, number):
        if (number % i) == 0:
            return False

    return True


def start_brain_prime():
    """ Generate data for game and start game algorithm """
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    questions = []
    answers_correct = []

    # generate questions and answers
    for round in range(ROUND_NUMBER):
        number = random.randint(1, 100)

        result = "yes" if is_prime(number) else "no"
        answers_correct.append(result)

        questions.append(str(number))

    start_game(game_rule=rules,
               questions=questions,
               answer_correct=answers_correct)
