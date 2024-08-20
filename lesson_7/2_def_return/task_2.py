#!/usr/bin/python3

"""
Напишите три функции:

text_length() — вернет количество символов без пробелов,
text_length_full() — вернет количество символов c пробелами,
text_word_count() — вернет количество слов (количество пробелов + 1).

Примеры вызова функций (значения приведены для примера):
text_length() # Вернет 200
text_length_full() # Вернет 220
text_word_count() # Вернет 80
"""

# Задача
"""
text = "The quick brown fox jumps over the lazy dog"


def text_length():
    ...

def text_length_full()
    ...

def text_word_count()
    ...

# Не удаляйте код ниже, он нужен для вызова и тестирования функции

print(text_length())
print(text_length_full())
print(text_word_count())
"""


# Решение
text = "The quick brown fox jumps over the lazy dog"


def text_length():
    return len(text.replace(' ', ''))

def text_length_full():
    return len(text)

def text_word_count():
    return text.count(' ') + 1

# Не удаляйте код ниже, он нужен для вызова и тестирования функции

print(text_length())
print(text_length_full())
print(text_word_count())
