#!/usr/bin/python3

"""
Напишите функцию get_min_sec(sec),
которая принимает время в секундах, возвращает словарь в формате:

{"min": мин, "sec": сек}
Минуты и секунды — целые числа.

Подсказка: деление нацело — x//y , остаток от деления — x%y

get_min_sec(120) # Вернет {"min": 2, "sec": 0}
get_min_sec(150) # Вернет {"min": 2, "sec": 30}
get_min_sec(15) # Вернет {"min": 0, "sec": 15}
"""

# Задача
"""
def get_min_sec(sec):

    return ...

# Не удаляйте код ниже, он нужен для проверки

value = int(input())
result = get_min_sec(value)  
print(result)
"""


# Решение
def get_min_sec(sec: int) -> dict:
    return dict(min=sec // 60, sec=sec % 60)


# Не удаляйте код ниже, он нужен для проверки

value = int(input())
result = get_min_sec(value)
print(result)
