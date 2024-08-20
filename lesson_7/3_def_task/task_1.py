#!/usr/bin/python3

"""
Функция get_distance(time, speed) вычисляет расстояние,
которое можно пройти за некоторое время.
Функция вызывается один раз с аргументами (1, 50).

Вызовите ее еще 2 раза с указанными в закомментированных строках параметрами.
"""

# Задача
"""
def get_distance(time, speed):
  distance = time*speed
  print(distance)


get_distance(1, 50)
# вызовите функцию 2 часа со скоростью 100 километров в час
# вызовите функцию 3 часа со скоростью 10 километров в час
"""


# Решение
def get_distance(time, speed):
    distance = time * speed
    print(distance)


get_distance(1, 50)
get_distance(2, 100)
get_distance(3, 10)
