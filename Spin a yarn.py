import random
import copy

story = ("Lorem Ipsum is simply dummy - {} - text of the printing and typesetting industry.\n" +
         "Lorem Ipsum has been the industry's standard dummy - {} - text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. \n" +
         "It has survived not only five - {} - centuries, but also the leap into electronic typesetting, remaining essentially unchanged.\n" +
         "It was popularised - {} - in the 1960s with the release of Letraset - {} - sheets containing Lorem Ipsum passages.")

words_dict = {
    'number': [1, 2, 3, 4, 5],
    'adjective': ['Warm', 'Talkative', 'Cheerful', 'Shy', 'Smart'],
    'body': ['Brain', 'Leg', 'Hand', 'Wrist', 'Elbow'],
    'profession': ['Mechanic', 'Cook', 'Ski Jumper', 'Skater', 'Writer'],
    'color': ['Green', 'Pink', 'Navy blue', 'Yellow', 'Red'],
}

'''
def randomchoice(dic):
    number = random.choice(words['number'])
    adjective = random.choice(words['adjective'])
    body = random.choice(words['body'])
    profession = random.choice(words['profession'])
    color = random.choice(words['color'])

    randomlist = [number, adjective, body, profession, color]
    return insert_values_to_text(randomlist)


def insert_values_to_text(list):
    my_story = copy.deepcopy(story)
    return my_story.format(list[0], list[1], list[2], list[3], list[4])


print(randomchoice(words))
'''


def choicetype(type, dictionary):
    try:
        words = dictionary[type]
        count = len(words) - 1
        index = random.randint(0, count)
        return dictionary[type].pop(index)

    except ValueError:
        print('All words have been exhausted!')
        exit()


def insert_text_to_story():
    dictionary = copy.deepcopy(words_dict)
    return story.format(
        choicetype('number', dictionary),
        choicetype('adjective', dictionary),
        choicetype('body', dictionary),
        choicetype('profession', dictionary),
        choicetype('color', dictionary)
    )


print(insert_text_to_story())
