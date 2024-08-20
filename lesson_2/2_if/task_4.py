#!/usr/bin/python3
"""
Пользователь вводит со стандартного ввода вес своей сумки в килограммах:
Если вес меньше 5 килограмм включительно, сумку можно взять в салон самолета.
Если больше, то сумку взять в салон нельзя, придется сдавать в багаж.

Создайте в задаче два условия:
Если вес 5 или меньше кг, выведите «Можно взять в салон».
Если вес больше 5 кг, выведите «Нужно сдать в багаж».

Пример вывода:
Можно взять в салон, Нужно сдать в багаж
"""

# Задача
"""
luggage_weight = int(input())

2_if ...
    print(...)

2_if ...
    print(...)
"""

# Решение
luggage_weight = int(input())

if luggage_weight <= 5:
    print('Можно взять в салон')

if luggage_weight > 5:
    print('Нужно сдать в багаж')
