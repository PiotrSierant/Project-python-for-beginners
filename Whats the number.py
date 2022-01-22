''' What's the number?'''
import random
import time

print("Hello! - What's the number?")
print('We drew a random number between 0-100')
number_random = random.randint(0, 100)
print('_' * 50)


def how_many_function():
    try:
        how_many = int(input("How many times you are trying guess? I want: "))
        return check_how_many(how_many)
    except ValueError:
        print('The given value must be a number!')
        return how_many_function()


def check_how_many(how_many):
    if how_many > 100 or how_many < 0:
        print('The value given is outside the range, please try again!')
        return how_many_function()
    else:
        return how_many


def inputfunction():
    try:
        number_user = int(input("\nWhat's the number? Your number: "))
        return check_number(number_user)
    except ValueError:
        print('The given value must be a number!')
        return inputfunction()


def check_number(number_user):
    if number_user > 100 or number_user < 0:
        print('The value given is outside the range, please try again!')
        return inputfunction()
    else:
        return comparison_of_numbers(number_random, number_user)


def comparison_of_numbers(number_random, number_user):
    global z
    if number_random == number_user:
        print('Congratulations! You entered the correct one!')
        z = 'Congratulations! You entered the correct one!'
        return z
    elif number_random < number_user:
        print('The number given is too large!')
        z = 'The number given is too large!'
        return z
    elif number_random > number_user:
        print('The number given is too small!')
        z = 'The number given is too small!'
        return z


def your_trials(trials):
    if trials < (how_many - 1):
        print('You guessed the number in', trials, 'times!')
    elif trials == (how_many - 1):
        print("Unfortunately, you didn't make it! try again!")


how_many = how_many_function()
for i in range(how_many):
    try:
        inputfunction()
        x = 'Congratulations! You entered the correct one!'
        if x == z:
            your_trials(i)
            break

        elif i == (how_many - 1):
            your_trials(i)

    except:
        print('Thanks for game!')

for i in 'Thank you for the game!':
    print(i, end=' ')
    time.sleep(0.5)