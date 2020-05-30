import random


RULE = 'Answer "yes" if number even otherwise answer "no".'


def build_match():
    question = random.randint(1, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return (question, correct_answer)
