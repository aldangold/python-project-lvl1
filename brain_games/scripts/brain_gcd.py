#!/usr/bin/python3
from brain_games.engine.flow import game_launch
from brain_games.games.gcd import gcd


def main():
    game_launch(gcd)


if __name__ == '__main__':
    main()
