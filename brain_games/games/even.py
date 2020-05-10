#!/usr/bin/python3
import random
import prompt


def even():
    num = random.randint(1, 100)
    print('Question: ', num)
    answer = prompt.string('Your answer: ')
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return (answer.lower(), correct_answer)
