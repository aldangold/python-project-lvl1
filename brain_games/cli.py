#!/usr/bin/env python3
import prompt


def welcome(game_rule):
    print('Welcome to the Brain Games!')
    print(game_rule)
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!')
    print()
    return name


def request_answer(question):
    print('Question: {}'.format(question))
    answer = prompt.string('Your answer: ')
    return answer


def show_message_correct_answer():
    print('Correct!')


def show_message_wrong_answer(answer, correct_answer, name):
    format_message = "'{}' is wrong answer ;(. Correct answer was '{}'"
    print(format_message.format(answer, correct_answer))
    print("Let's try again, {}!".format(name))


def show_message_winner(name):
    print('Congratulations, {}!'.format(name))
