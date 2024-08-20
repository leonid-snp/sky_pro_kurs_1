#!/usr/bin/python3

"""
Напишите функцию, которая возвращает площадь круга, принимая его радиус.

Формула вычисления площади:
радиус ** 2 * Пи.

Пи в этом задании можно считать равным 3.14.
get_square(1) # Вернет 3.14
get_square(2) # Вернет 12.56
get_square(3) # Вернет 28.26
"""

# Задача
"""
def get_square(radius):
   ...


# Не удаляйте код ниже, он нужен для проверки

radius = int(input())
square = get_square(radius)
print(square)
"""


# Решение
def get_square(radius: int) -> float:
    return round(radius ** 2 * 3.14, 2)


# Не удаляйте код ниже, он нужен для проверки

radius = int(input())
square = get_square(radius)
print(square)
