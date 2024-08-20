#!/usr/bin/python3

"""
Напишите цикл, который выведет 18 этажей, пропустив номера 4 и 13.

Пример вывода:
1 этаж
2 этаж
...
18 этаж
"""

# Задача
"""
for floor in range(1, 19):
    ...
    print(f"{floor} этаж")
"""

# Решение
for floor in range(1, 19):
    if floor == 4 or floor == 13:
        continue
    print(f"{floor} этаж")
