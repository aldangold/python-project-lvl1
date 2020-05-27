from brain_games import cli


def play(game):
    name = cli.welcome(game.RULE)
    number_of_rounds = 3
    counter = 0
    while counter < number_of_rounds:
        (question, correct_answer) = game.match_build()
        answer = cli.request_answer(question)
        if answer == correct_answer:
            cli.show_message_correct_answer()
            counter += 1
        else:
            cli.show_message_wrong_answer(answer, correct_answer, name)
    cli.show_message_winner(name)
