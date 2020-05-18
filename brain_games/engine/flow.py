#!/usr/bin/python3
import prompt


def game_launch(game):
    (rule, _, _) = game()
    print('Welcome to the Brain Games!')
    print(rule)
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!')
    print()
    number_of_round = 3
    i = 0
    while i < number_of_round:
        (_, question, correct_answer) = game()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            print('\'{}\' is wrong answer ;(. Correct answer was \'{}\''.format(answer, correct_answer))  # noqa E501
            print('Let\'s try again, ', name, '!')
    return print('Congratulations, ', name, '!')
