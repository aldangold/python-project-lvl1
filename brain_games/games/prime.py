import random
import math


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def match_build():
    num1 = random.randint(0, 200)
    question = num1
    correct_answer = 'yes' if is_prime(num1) else 'no'
    return (question, correct_answer)


def is_prime(num1):
    if num1 < 2:
        return False
    elif num1 == 2:
        return True
    limit = math.sqrt(num1)
    i = 2
    while i <= limit:
        if num1 % i == 0:
            return False
            break
        i += 1
    return True
