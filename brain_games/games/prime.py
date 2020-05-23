import random
import math


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def match_build():
    num1 = random.randint(3, 500)
    question = num1
    correct_answer = check_on_prime(num1)
    return (question, correct_answer)


def check_on_prime(num1):
    limit = math.sqrt(num1)
    i = 2
    correct_answer = 'yes'
    while i <= limit:
        if num1 % i == 0:
            correct_answer = 'no'
            break
        i += 1
    return correct_answer
