from operator import add, mul, sub
import random


RULE = 'What is the result of the expression?'


def build_match():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    sign, operation = random.choice([('+', add), ('*', mul), ('-', sub)])
    question = '{} {} {}'.format(num1, sign, num2)
    correct_answer = str(operation(num1, num2))
    return (question, correct_answer)
