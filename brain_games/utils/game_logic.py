from brain_games.utils import cli

ROUND_NUMBER = 3


def compare_answer(answer: str, answer_correct: str) -> bool:
    if answer == answer_correct:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{answer_correct}'.")
        return False


def start_game(game_rule: str, questions: list, answer_correct: list):
    """Implements all game algorithm:
    1. welcome user
    2. display game rules
    3. ask 3 questions
    3.1. if answer is right - go next question
    3.2. if false - game over
    Args:
        game_rule (str): game rules for user
        questions (list): questions text for user, 3 elements
        answer_correct (list): correct answers for comparation, shoud be string, 3 elements
    """
    print("Welcome to the Brain Games!")
    username = cli.welcome_user()
    print(game_rule)

    for round_num in range(ROUND_NUMBER):
        cli.ask_question(question=questions[round_num])
        answer = cli.get_answer()
        result = compare_answer(
            answer=answer, answer_correct=answer_correct[round_num])

        if not result:
            # user game over
            print(f"Let's try again, {username}!")
            return

    # user win!
    print(f"Congratulations, {username}!")
