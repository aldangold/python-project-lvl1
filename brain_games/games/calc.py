#!/usr/bin/python3
import random


def calc():
    rule = 'What is the result of the expression?'
    num1 = str(random.randint(1, 100))
    num2 = str(random.randint(1, 100))
    oper = random.choice(['*', '+', '-'])
    question = 'Question: {} {} {}'.format(num1, oper, num2)
    correct_answer = str(eval(num1 + oper + num2))
    return (rule, question, correct_answer)
