import random

capabilities = ['rock', 'paper', 'scissors']


def how_many_game_func():
    try:
        how_many_game = int(input('How many are we playing to? '))
        return how_many_game
    except ValueError:
        print('Please, enter number!')
        return how_many_game_func()


def turn_computer(possibilities):
    computer = random.choice(possibilities)
    print(computer)

    return computer


def turn_user():
    try:
        user = str(input('Rock, paper or scissors? What do you choice: '))
        return check_user(user.lower())

    except ValueError:
        print('Provide one of the possible options listed!')
        return turn_user(possibilities)

    return check_user(user)


def check_user(user):
    if user == 'paper' or user == 'rock' or user == 'scissors':
        return user

    else:
        print('Provide one of the possible options listed!')
        return turn_user()


def value_comparison(comp, user):
    if comp == 'paper' and user == 'paper':
        return 'draw'

    elif comp == 'scissors' and user == 'scissors':
        return 'draw'

    elif comp == 'rock' and user == 'rock':
        return 'draw'

    elif comp == 'rock' and user == 'scissors':
        return 'win comp'

    elif comp == 'paper' and user == 'rock':
        return 'win comp'

    elif comp == 'scissors' and user == 'paper':
        return 'win comp'

    elif comp == 'scissors' and user == 'rock':
        return 'win user'

    elif comp == 'rock' and user == 'paper':
        return 'win user'

    elif comp == 'paper' and user == 'scissors':
        return 'win user'

    else:
        print('An unexpected error has occurred')


points_user = 0
points_comp = 0
how_many_game = how_many_game_func()

while True:
    if points_comp < how_many_game and points_user < how_many_game:

        game = value_comparison(turn_user(), turn_computer(capabilities))

        if game == 'win comp':
            print('The computer wins the round!')
            points_comp += 1

        elif game == 'win user':
            print('The user wins the round!')
            points_user += 1

        elif game == 'draw':
            print('Draw!')

        print('User: ', points_user, 'Comp: ', points_comp)

    else:
        print('Game over!')
        if points_user == how_many_game:
            print('The user wins the game!')
        elif points_comp == how_many_game:
            print('The computer wins the game!')
        break
