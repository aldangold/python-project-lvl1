import random


RULE = 'Find the greatest common divisor of given numbers.'


def match_build():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = '{} {}'.format(num1, num2)
    correct_answer = str(gcd(num1, num2))
    return (question, correct_answer)


def gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1
