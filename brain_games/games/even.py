#!/usr/bin/python3
import random
import prompt


def even(name):
    i = 0
    while i < 3:
        num = random.randint(1, 100)
        print('Question: ', num)
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if num % 2 == 0 else 'no'
        if answer.lower() == correct_answer:
            print('Correct!')
            i += 1
        else:
            print('\'{}\' is wrong answer ;(. Correct answer was \'{}\''.format(answer, correct_answer))  # noqa E501
            print('Let\'s try again, ', name, '!')
    return print('Congratulations, ', name, '!')
