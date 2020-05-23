import random


RULE = 'Answer "yes" if number even otherwise answer "no".'


def match_build():
    num = random.randint(1, 100)
    question = num
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return (question, correct_answer)
