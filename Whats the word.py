import random
### PART 1 - random word ###

list_of_the_correct_length = []


def how_long_word_you_want():
    global how_long_word
    try:
        how_long_word = int(
            input('How long word you want? Give me the number: '))
        return import_words('words.txt')

    except ValueError:
        print('The given value must be a number!')
        return how_long_word_you_want()


def import_words(file):
    x = open(file, 'r')
    return read_words(x)


def read_words(x):
    WORDS = x.read().splitlines()
    return create_list_with_words(WORDS, how_long_word)


def create_list_with_words(list_word, length_you_want):
    for line in list_word:
        if len(line) == length_you_want:
            list_of_the_correct_length.append(line)

        else:
            pass

    return check_list(list_of_the_correct_length)


def check_list(words_list):
    if len(words_list) == 0:
        print('There are no words with the given length!')
        return how_long_word_you_want()

    else:
        random_choice(words_list)


def random_choice(list_word):
    global random_word
    random_word = random.choice(list_word)
    return random_word.lower()


how_long_word_you_want()


### PART 2 ###

def guess_word(word, word_think):
    guess_word = ''
    for character in word:
        if character in word_think:
            guess_word = guess_word + character

        else:
            guess_word = guess_word + '_'

    return guess_word


def complete_the_word(word):
    character_guess = []
    total_chances = int(len(word) * 2)
    print('The word you are going to guess is ' +
          str(len(word)) + ' characters long')

    while True:
        if total_chances != 0:
            print(f"\nYou are still left with {total_chances}")
            print("Word is: " + guess_word(word, character_guess))
            print("Letters guessed: " + str(character_guess))
            try:
                guessing = input("Guess is: ").lower()[0]
            except IndexError:
                print('You must enter a letter!')
                guessing = input("Guess is: ").lower()[0]

            if guessing not in character_guess:
                character_guess.append(guessing)

            elif guess_word(word, character_guess) == word:
                print("Hurray!!")
                print("Congrats you got the correct word")
                break

            else:
                total_chances = total_chances - 1
                if guessing in word:
                    print("You have entered the correct character! " + guessing)
                else:
                    print(guessing + " is not in the word!")

        else:
            if input("Do you want to continue: ").lower().startswith("n"):
                break
            else:
                print('New random word! Good Luck!')
                random_choice(list_of_the_correct_length)


complete_the_word(random_word)