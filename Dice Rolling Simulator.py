import random


def dice_rolling():
    x = random.randint(0, 6)
    return x


def how_many_time():
    try:
        how_many = int(input('How many times do you dice rolling?'))
        return how_many
    except ValueError:
        print('Please, enter number!')
        return how_many_time()


how_many = how_many_time()

for i in range(how_many):
    print(i+1, 'dice roll - result: ', dice_rolling())


while True:
    try:
        question = str(
            input("Do you dice roll again? Press 'y' or 'yes' or 'n' or 'no': "))
        if question == 'y' or question == 'yes':
            print('dice roll - result: ', dice_rolling())
        elif question == 'n' or question == 'no':
            print('Thanks for the game!')
            break
        else:
            print("Wrong value, press y or yes or 'n' or 'no'!")

    except ValueError:
        print('Provide one of the possible options listed!')
        continue
