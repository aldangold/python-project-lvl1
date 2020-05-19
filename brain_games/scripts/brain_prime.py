#!/usr/bin/python3
from brain_games.engine.flow import game_launch
from brain_games.games.prime import prime


def main():
    game_launch(prime)


if __name__ == '__main__':
    main()
