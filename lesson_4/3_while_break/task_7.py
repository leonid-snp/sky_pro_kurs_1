#!/usr/bin/python3

"""
В первый день спортсмен пробежал 2 километра,
затем он каждый день увеличивал пробег на 20% от предыдущего значения.

Определите номер дня, когда пробег спортсмена составит не менее 5 километров.
Выведите ответ в формате целого числа.
"""

# Задача
"""
day = 1
distance = 2.0

while ...
"""

# Решение
day = 1
distance = 2.0

while distance < 5:
    up_dist = distance * 0.2
    distance += up_dist
    day += 1

print(day)
