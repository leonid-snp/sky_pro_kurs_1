#!/usr/bin/python3

"""
Напишите функцию get_longest(words),
которая получает список строк и возвращает самое длинное слово из списка.
Список может быть пустым, но все элементы из списка — строки.

get_longest(["еж" , "мышь", "стриж"]) # Вернет "стриж"
get_longest(["aaa", "aa", "a"]) # Вернет "aaa"
get_longest(["——-", "—-", "-"]) # Вернет "——-"
get_longest(["a", "a", "a"]) # Вернет "a"
"""

# Задача
"""
def get_longest(words):
    return ...

# Не удаляйте код ниже, он нужен для проверки

words = input().split(" ")
result = get_longest(words)
print(result)
"""


# Решение
def get_longest(words: list) -> str:
    big_word = ''
    for word in words:
        if len(word) >= len(big_word):
            big_word = word
    return big_word


# Не удаляйте код ниже, он нужен для проверки

words = input().split(" ")
result = get_longest(words)
print(result)
