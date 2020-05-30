#!/usr/bin/env python3
import prompt


def request_name():
    name = prompt.string("May I have your name? ")
    return name


def request_answer():
    answer = prompt.string("Your answer: ")
    return answer


GENERAL_GREET = "Welcome to the Brain Games!"

USER_GREET = "Hello, {} !"

QUESTION = "Question: {}"

CORRECT_ANSWER = "Correct!"

WRONG_ANSWER = "'{}' is wrong answer ;(. Correct answer was '{}'"

TRY_AGAIN = "Let's try again, {}!"

MESSAGE_WINNER = "Congratulations, {}!"
