#!/usr/bin/python3
from brain_games.scripts.brain_games import welcome
from brain_games.engine.cli import welcome_user
from brain_games.engine.flow import flow
from brain_games.games.even import even


def rule():
    print('Answer "yes" if number even otherwise answer "no".')


def main():
    welcome()  # Привествие
    rule()  # Правила игры
    print()
    flow(even, welcome_user())  # Флоу вызывает игру и имя пользователя


if __name__ == '__main__':
    main()
