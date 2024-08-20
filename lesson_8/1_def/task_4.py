#!/usr/bin/python3

"""
Напишите функцию, которая получает несколько элементов через пробел и суммирует их.

Пример вызова функции:
lost_time(1,2,3) # Вернет 6
lost_time(3, 3, 3, 3) # Вернет 12
"""

# Задача
"""
def lost_time(...):
  pass


# Не удаляйте код ниже, он нужен для проверки

numbers = [int(x) for x in input().split(" ")]
print(lost_time(*numbers))
"""


# Решение
def lost_time(*args: int) -> int:
    summ = 0
    for num in args:
        summ += num
    return summ


# Не удаляйте код ниже, он нужен для проверки

numbers = [int(x) for x in input().split(" ")]
print(lost_time(*numbers))
