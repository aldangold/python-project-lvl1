#!/usr/bin/python3
from brain_games.scripts.brain_games import welcome
from brain_games.engine.cli import welcome_user
from brain_games.engine.flow import flow
from brain_games.games.gcd import gcd


def rule():
    print('Find the greatest common divisor of given numbers')


def main():
    welcome()   # Привествие
    rule()  # Правила игры
    print()
    flow(gcd, welcome_user())  # Флоу вызывает игру и имя пользователя


if __name__ == '__main__':
    main()
