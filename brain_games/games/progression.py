import random


RULE = 'What number is missing in the progression?'


def match_build():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 10)
    hidden_element = random.randint(0, 9)
    progression_length = 10
    progression = list(range(num1, num2 * progression_length + num1, num2))
    correct_answer = str(progression[hidden_element])
    progression[hidden_element] = '..'
    question = '{}'.format(' '.join(map(str, progression)))
    return (question, correct_answer)
