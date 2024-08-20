#!/usr/bin/python3

"""
У вас есть строка.
Выведите с помощью цикла все символы, кроме пробелов.
Чтобы вывести символы на одной строке, используйте print(..., end="").

Пример вывода:
THISISFINE
"""

# Задача
"""
line = "STRINGS ARE AWESOME"
"""

# Решение
line = "STRINGS ARE AWESOME"

for letter in line:
    if letter != ' ':
        print(letter, end='')
