#!/usr/bin/python3


def flow(game, name):
    i = 0
    while i < 3:
        (answer, correct_answer) = game()
        if answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            print('\'{}\' is wrong answer ;(. Correct answer was \'{}\''.format(answer, correct_answer))  # noqa E501
            print('Let\'s try again, ', name, '!')
    return print('Congratulations, ', name, '!')
