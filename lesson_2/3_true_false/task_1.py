#!/usr/bin/python3
"""
Со стандартного ввода подается скорость автомобиля и максимально разрешенная скорость.
Если скорость автомобиля не превышает максимальную (меньше или равна максимальной),
выведите True, иначе — False.

Пример вывода:
True, False
"""

# Задача
"""
our_speed = int(input())
max_speed = int(input())
"""

# Решение
our_speed = int(input())
max_speed = int(input())
print('True' if our_speed <= max_speed else 'False')
