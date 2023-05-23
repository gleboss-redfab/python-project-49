import prompt


def welcome_user() -> str:
    """Ask user name and print greeting.
    Returns:
        str: user name
    """
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
