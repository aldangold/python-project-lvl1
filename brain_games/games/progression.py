import random


RULE = 'What number is missing in the progression?'


def build_match():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 10)
    progression_length = 10
    progression = list(range(num1, num2 * progression_length + num1, num2))
    hidden_index = random.randint(0, progression_length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = '{}'.format(' '.join(map(str, progression)))
    return (question, correct_answer)
