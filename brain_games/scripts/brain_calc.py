#!/usr/bin/python3
from brain_games.scripts.brain_games import welcome
from brain_games.games.cli import welcome_user
from brain_games.games.calc import calc


def rule():
    print('What is the result of the expression?')


def main():
    welcome()
    rule()
    print()
    calc(name=welcome_user())


if __name__ == '__main__':
    main()
