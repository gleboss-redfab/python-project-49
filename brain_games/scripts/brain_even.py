#!/usr/bin/env python3
from brain_games.brain_even import start_game
from brain_games.cli import welcome_user


def main():
    """ user"""
    print("Welcome to the Brain Games!")
    username = welcome_user()
    start_game(username)


if __name__ == "__main__":
    main()
