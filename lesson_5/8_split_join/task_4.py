#!/usr/bin/python3

"""
Со стандартного ввода поступает в виде строки последовательность чисел, разделенная пробелами.
Разделите строку по пробелам и найдите самое большое и самое маленькое число.

Пример ввода:
2 3 4 5

Пример вывода:
min: 2
max: 5
"""

# Задача
"""
numbers = input()
"""

# Решение
numbers = input()
new_number = [int(number) for number in numbers.split(' ')]
print(f'min: {min(new_number)}\n'
      f'max: {max(new_number)}')
