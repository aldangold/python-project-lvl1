import random


RULE = 'What number is missing in the progression?'


def build_match():
    start_value = random.randint(1, 50)
    step = random.randint(1, 10)
    progression_length = 10
    final_value = step * progression_length + start_value
    progression = list(range(start_value, final_value, step))
    hidden_index = random.randint(0, progression_length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = '{}'.format(' '.join(map(str, progression)))
    return (question, correct_answer)
