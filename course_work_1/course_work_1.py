import random

code_morse = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}

answers = []

words = ['code', 'bit', 'list', 'soul', 'next']

hello = input('Сегодня мы потренируемся расшифровать морзянку.\n'
              'Нажмите Enter и начнем: ')


def get_morse_encode(word: str, code: dict) -> str:
    """
    Принимает на вход слово, возвращает закодированное слово
    :param word: (str) слово
    :param code: (str) код морзе
    :return: (str) закодированное слово
    """
    morse_code = ''
    for letter in word:
        morse_code += code[letter] + ' '

    return morse_code


def get_random_word(list_words: list) -> str:
    """
    Получает на вход список слов, возвращает случайное слово из списка
    :param list_words: (list) список слов
    :return: (str) случайное слово
    """
    new_list = list_words
    use_word = random.choice(new_list)
    new_list.remove(use_word)

    return use_word


def statistics(list_bool: list) -> str:
    """
    Принимает список булевых значений, возвращает строку со статистикой ответов
    :param list_bool: (list) список булевых значений
    :return: (str) статистика
    """
    yes = 0
    for item in list_bool:
        if item:
            yes += 1

    return (f'Всего задачек: {len(list_bool)}\n'
            f'Отвечено верно: {yes}\n'
            f'Отвечено неверно: {len(list_bool) - yes}')


for i in range(len(words)):
    random_word = get_random_word(words)
    answer = input(f'Слово {i + 1} - {get_morse_encode(random_word, code_morse)} : ').lower()
    if answer == random_word:
        answers.append(True)
        print(f'Верно, {random_word.title()}!\n')
    else:
        answers.append(False)
        print(f'Неверно, {random_word.title()}!\n')

print(statistics(answers))
