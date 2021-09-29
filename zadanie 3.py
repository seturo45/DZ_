# Задание 1
eng_rus_dict = {
    'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
    'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
}
number_1 = input('1. Enter a number from one to ten with a word: ')


def num_translate(word_1):

    return eng_rus_dict.get(word_1)


print(num_translate(number_1))

# Задание 2

number_2 = input('2. Enter a number from one to ten with a word: ')


def num_translate_adv(word_2):
    if word_2[0].isupper():
        word_2 = word_2.lower()
        return eng_rus_dict[word_2].capitalize()
    else:
        return eng_rus_dict.get(word_2)


print(num_translate_adv(number_2))

# Задание 3


def my_function(*names):
    my_dict = {}
    for name in names:
        my_dict.setdefault(name[0], [])
        my_dict[name[0]].append(name)
    return my_dict


print(my_function('Артем', 'Александр', 'Михаил', 'Максим', 'Иван',
                'София', 'Виктория', 'Мария', 'Анна', 'Алиса'))

# Задание 5


import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num):

    joke = []
    for i in range(num):
        noun = random.choice(nouns)
        adverb = random.choice(adverbs)
        adjective = random.choice(adjectives)
        joke.append(f'{noun} {adverb} {adjective}')
    return joke

print(get_jokes(3))