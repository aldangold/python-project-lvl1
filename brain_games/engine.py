from brain_games import cli


def play(game):
    print(cli.GENERAL_GREET)
    print(game.RULE)
    print()
    name = cli.request_name()
    print(cli.USER_GREET.format(name))
    print()
    number_of_matches = 3
    counter = 0
    while counter < number_of_matches:
        (question, correct_answer) = game.build_match()
        print(cli.QUESTION.format(question))
        answer = cli.request_answer()
        if answer == correct_answer:
            print(cli.CORRECT_ANSWER)
            counter += 1
        else:
            print(cli.WRONG_ANSWER.format(answer, correct_answer))
            print(cli.TRY_AGAIN.format(name))
    print(cli.MESSAGE_WINNER.format(name))
