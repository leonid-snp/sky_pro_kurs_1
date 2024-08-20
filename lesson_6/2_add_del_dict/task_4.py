#!/usr/bin/python3

"""
У вас есть словарь со списком слов.
Со стандартного ввода подается ключ, соответствующий ключ нужно удалить из словаря.

Пример ввода:
mouse
"""

# Задача
"""
words = {
"owl":"сова",
"duck":"утка",
"mouse":"мышь",
"sheep":"овца",
"cat":"кошка",
}  

user_input = input()

...

# Не удаляйте код ниже: он нужен для проверки.

print("_".join([str(x) for x in words]))
print("_".join([str(x) for x in words.values()]))
"""

# Решение
words = {
    "owl": "сова",
    "duck": "утка",
    "mouse": "мышь",
    "sheep": "овца",
    "cat": "кошка",
}

user_input = input()

del words[user_input]

# Не удаляйте код ниже: он нужен для проверки.

print("_".join([str(x) for x in words]))
print("_".join([str(x) for x in words.values()]))
