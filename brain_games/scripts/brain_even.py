#!/usr/bin/python3
from brain_games.scripts.brain_games import welcome
from brain_games.cli import welcome_user
from brain_games.game import quest


def rule():
    print('Answer "yes" if number even otherwise answer "no".')


def main():
    welcome()
    rule()
    print()
    quest(name=welcome_user())


if __name__ == '__main__':
    main()
