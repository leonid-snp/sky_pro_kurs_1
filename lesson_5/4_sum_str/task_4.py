#!/usr/bin/python3

"""
Со стандартного ввода подается строка.
Запишите ее в новую переменную,
удалив пробелы и символы подчеркивания (если очередной символ — символ подчеркивания,
то не добавляйте его в новую строку).

Пример ввода:
python_variables are_awesome

Пример вывода:
pythonvariablesareawesome
"""

# Задача
"""
line = input()

line_spaceless = ...

# Не удаляйте этот код: он нужен для проверки.

print("".join(line_spaceless))
"""

# Решение
line = input()

line_spaceless = [letter for letter in line if letter not in [' ', '_']]

# Не удаляйте этот код: он нужен для проверки.

print("".join(line_spaceless))
