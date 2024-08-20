#!/usr/bin/python3

"""
Со стандартного ввода поступает фраза, разделенная пробелами.
Разделите фразу по пробелам и выведите каждое слово на отдельной строке.

Пример ввода:
Alfa Bravo Charlie Delta

Пример вывода:
Alfa
Bravo
Charlie
Delta
"""

# Задача
"""
words = input()
"""

# Решение
words = input()

print(*words.split(' '), sep='\n')