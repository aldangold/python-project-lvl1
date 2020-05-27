from operator import add, mul, sub
import random


RULE = 'What is the result of the expression?'


def match_build():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    Addition = ('+', add)
    Multiplication = ('*', mul)
    Subtraction = ('-', sub)
    operator, function = random.choice([Addition, Multiplication, Subtraction])
    question = '{} {} {}'.format(num1, operator, num2)
    correct_answer = str(function(num1, num2))
    return (question, correct_answer)
