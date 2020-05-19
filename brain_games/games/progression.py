#!/usr/bin/python3
import random


def progression():
    rule = 'What number is missing in the progression?'
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 10)
    num3 = random.randint(0, 9)
    prg = list(range(num1, num2 * 10 + num1, num2))
    correct_answer = str(prg[num3])
    prg[num3] = '..'
    question = 'Question: {}'.format(' '.join(map(str, prg)))
    return (rule, question, correct_answer)
