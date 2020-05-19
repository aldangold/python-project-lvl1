#!/usr/bin/python3
import random
import math


def gcd():
    rule = 'Find the greatest common divisor of given numbers.'
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = 'Question: {} {}'.format(num1, num2)
    correct_answer = str(math.gcd(num1, num2))
    return (rule, question, correct_answer)
