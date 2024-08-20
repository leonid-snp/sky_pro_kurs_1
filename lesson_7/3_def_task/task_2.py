#!/usr/bin/python3

"""
Напишите функцию has_rrr(word),
которая проверяет картавость слова (содержит ли слово маленькие или большие буквы «Р»),
а возвращает булево значение. В качестве аргумента в функцию всегда передается строка.

Пример ввода:
has_rrr("Речка") # Вернет True
has_rrr("ручка") # Вернет True
has_rrr("уточка") # Вернет False
has_rrr("птичка") # Вернет False
has_rrr("") # Вернет False
"""

# Задача
"""
def has_rrr(word):

    return ...

# Не удаляйте код ниже, он нужен для проверки

word = input()
result = has_rrr(word)
print(result)
"""


# Решение
def has_rrr(word):
    return True if 'р' in word.lower() else False


# Не удаляйте код ниже, он нужен для проверки

word = input()
result = has_rrr(word)
print(result)
