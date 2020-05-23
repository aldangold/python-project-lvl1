#!/usr/bin/env python3
from brain_games.engine.flow import game_launch
from brain_games.games import calc


def main():
    game_launch(calc)


if __name__ == '__main__':
    main()
