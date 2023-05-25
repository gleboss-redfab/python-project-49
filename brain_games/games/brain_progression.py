import random

from brain_games.utils.game_logic import ROUND_NUMBER, start_game


def generate_progression(a0: int, difference: int, length: int) -> list:
    """Generate Arithmetic progression
    Args:
        a0 (int): first element
        difference (int): step
        length (int): number of elements
    Returns:
        list: progression
    """
    result = []
    for i in range(length):
        result.append(a0 + i * difference)

    return result


def start_brain_progression():
    """ Generate data for game and start game algorithm """
    rules = 'What number is missing in the progression?'
    questions = []
    answers_correct = []

    # generate questions and answers
    for round in range(ROUND_NUMBER):
        a0 = random.randint(1, 100)
        difference = random.randint(-10, 10)
        length = random.randint(5, 15)
        result_num = random.randint(0, length - 1)

        progression = generate_progression(a0, difference, length)
        answer = progression[result_num]
        answers_correct.append(str(answer))

        question = ""
        progression[result_num] = ".."
        for num in progression:
            question += str(num) + " "

        questions.append(question)

    start_game(game_rule=rules,
               questions=questions,
               answer_correct=answers_correct)
