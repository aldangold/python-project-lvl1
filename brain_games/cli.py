import prompt


def ask_user(question):
    answer = prompt.string(question)
    return answer


NAME = "May I have your name? "

ANSWER = "Your answer: "

GENERAL_GREET = "Welcome to the Brain Games!"

USER_GREET = "Hello, {} !"

QUESTION = "Question: {}"

CORRECT_ANSWER = "Correct!"

WRONG_ANSWER = "'{}' is wrong answer ;(. Correct answer was '{}'"

TRY_AGAIN = "Let's try again, {}!"

MESSAGE_WINNER = "Congratulations, {}!"
