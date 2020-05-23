import random


RULE = 'What is the result of the expression?'


def match_build():
    num1 = str(random.randint(1, 100))
    num2 = str(random.randint(1, 100))
    operator = random.choice(['*', '+', '-'])
    question = '{} {} {}'.format(num1, operator, num2)
    correct_answer = str(eval(num1 + operator + num2))
    return (question, correct_answer)
