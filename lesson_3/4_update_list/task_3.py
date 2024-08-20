#!/usr/bin/python3

"""
Со стандартного ввода подается номер месяца.

Выведите правильное название месяца на основе имеющегося списка.

Пример ввода:
2

Пример вывода:
февраль
"""

# Задача
"""
months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"] 

months_id = int(input())

...

print("принтабрь")
"""

# Решение
months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

months_id = int(input())

print(months[months_id - 1])
