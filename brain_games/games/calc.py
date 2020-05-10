#!/usr/bin/python3
import random
import prompt


def calc():
    num1 = str(random.randint(1, 100))
    num2 = str(random.randint(1, 100))
    oper = random.choice(['*', '+', '-'])
    print('Question: {} {} {}'.format(num1, oper, num2))
    answer = prompt.string('Your answer: ')
    correct_answer = str(eval(num1 + oper + num2))
    return (answer, correct_answer)
