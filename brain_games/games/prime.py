import random
import math


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def build_match():
    question = random.randint(0, 200)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return (question, correct_answer)


def is_prime(question):
    if question < 2:
        return False
    elif question == 2:
        return True
    limit = math.sqrt(question)
    i = 2
    while i <= limit:
        if question % i == 0:
            return False
            break
        i += 1
    return True
