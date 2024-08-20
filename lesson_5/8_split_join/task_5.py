#!/usr/bin/python3

"""
Со стандартного ввода поступает в виде строки пара «количество:цена», разделенная двоеточием.
Разделите строку по двоеточию и вычислите стоимость. Стоимость = количество * цена.

Пример ввода:
5:100

Пример вывода:
500
"""

# Задача
"""
data = input()
"""

# Решение
data = input()
number1, number2 = [int(num) for num in data.split(':')]
print(number1 * number2)
