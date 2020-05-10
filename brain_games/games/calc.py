#!/usr/bin/python3
import random
import prompt


def calc(name):
    i = 0
    while i < 3:
        num1 = str(random.randint(1, 100))
        num2 = str(random.randint(1, 100))
        oper = random.choice(['*', '+', '-'])
        print('Question: {} {} {}'.format(num1, oper, num2))
        answer = prompt.string('Your answer: ')
        correct_answer = str(eval(num1 + oper + num2))
        if answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            print('\'{}\' is wrong answer ;(. Correct answer was \'{}\''.format(answer, correct_answer))  # noqa E501
            print('Let\'s try again, ', name, '!')
    return print('Congratulations, ', name, '!')
