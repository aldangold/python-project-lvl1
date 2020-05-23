import random
import math


RULE = 'Find the greatest common divisor of given numbers.'


def match_build():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = '{} {}'.format(num1, num2)
    correct_answer = str(math.gcd(num1, num2))
    return (question, correct_answer)
