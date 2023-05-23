import prompt


def welcome_user():
    """Ask user name and print greeting."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
