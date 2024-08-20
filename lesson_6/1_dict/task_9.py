#!/usr/bin/python3

"""
Пользователь вводит со стандартного ввода по очереди год, месяц и день рождения.
Запишите в словарь в формате:

{
    "year": 2000,
    "month": 6,
    "day": 6,
}

Не печатайте словарь самостоятельно, код для проверки, который его распечатывает, уже написан.
"""

# Задача
"""
year = input()
month = input()
day = input()

birth_date = ...

# Не удаляйте код ниже: он нужен для проверки.

print(" ".join([x for x in birth_date.keys()]))
print(" ".join([str(x) for x in birth_date.values()]))
"""

# Решение
year = input()
month = input()
day = input()

birth_date = {
    'year': year,
    'month': month,
    'day': day
}

# Не удаляйте код ниже: он нужен для проверки.

print(" ".join([x for x in birth_date.keys()]))
print(" ".join([str(x) for x in birth_date.values()]))
