#!/usr/bin/python3

"""
У вас есть текст,
в котором встречаются #хештеги.
Напишите функцию get_hash(text).
Верните все хештеги одним списком.

get_hashtags("Котята #еда #закат море") # Вернет список ['еда', 'закат']
get_hashtags("#код #функция #решение") # Вернет ['код', 'функция', 'решение']
get_hashtags("Котята") # Вернет []
"""

# Задача
"""
def get_hashtags(text):

    words = text.split(" ")
    hashtags = []
    for word in words:
        if ... :
            pass
    return hashtags


# Не удаляйте код ниже, он нужен для проверки    

words = input()
result = get_hashtags(words)
print(result)
"""


# Решение
def get_hashtags(text: str) -> list:
    words = text.split(" ")
    hashtags = []
    for word in words:
        if word.startswith('#'):
            hashtags.append(word[1:])
    return hashtags


# Не удаляйте код ниже, он нужен для проверки

words = input()
result = get_hashtags(words)
print(result)
