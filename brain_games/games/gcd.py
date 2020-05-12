#!/usr/bin/python3
import random
import prompt
import math


def gcd():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print('Question: {} {}'.format(num1, num2))
    answer = prompt.string('Your answer: ')
    correct_answer = str(math.gcd(num1, num2))
    return (answer, correct_answer)
