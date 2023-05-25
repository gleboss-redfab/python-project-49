import prompt


def welcome_user() -> str:
    """Ask user name and print greeting.
    Returns:
        str: user name
    """
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    return username


def ask_question(question: str):
    """Simple ask question with right formating
    Args:
        question (str): question text
    """
    print(f'Question: {question}')


def get_answer() -> str:
    """Get answer from user
    Returns:
        str: answer 
    """
    answer = prompt.string('Your answer: ')
    return answer
