#!/usr/bin/python3
import random
import prompt
import math


def prime():
    num1 = random.randint(3, 500)
    limit = math.sqrt(num1)
    i = 2
    correct_answer = 'yes'
    while i <= limit:
        if num1 % i == 0:
            correct_answer = 'no'
            break
        i += 1
    print('Question: {}'.format(num1))
    answer = prompt.string('Your answer: ')
    return (answer, correct_answer)
