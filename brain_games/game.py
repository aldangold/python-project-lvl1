#!/usr/bin/python3
import random
import prompt


def quest(name):
    i = 0
    while i < 3:
        num = random.randint(1, 100)
        print('Question: ', num)
        answer = prompt.string('Your answer: ')
        if num % 2 == 0 and answer.lower() == 'yes':
            print('Correct!')
            i += 1
        elif num % 2 != 0 and answer.lower() == 'no':
            print('Correct!')
            i += 1
        else:
            print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
            print('Let\'s try again, ', name, '!')
    return print('Congratulations, ', name, '!')
