import prompt


def game_launch(game):
    print('Welcome to the Brain Games!')
    print(game.RULE)
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!')
    print()
    number_of_round = 3
    i = 0
    while i < number_of_round:
        (question, correct_answer) = game.match_build()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            print('\'{}\' is wrong answer ;(. Correct answer was \'{}\''.format(answer, correct_answer))  # noqa E501
            print('Let\'s try again, {}!'.format(name))
    print('Congratulations, {}!'.format(name))
