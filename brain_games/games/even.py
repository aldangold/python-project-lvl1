#!/usr/bin/python3
import random


def even():
    rule = 'Answer "yes" if number even otherwise answer "no".'
    num = random.randint(1, 100)
    question = 'Question: {}'.format(num)
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return (rule, question, correct_answer)
