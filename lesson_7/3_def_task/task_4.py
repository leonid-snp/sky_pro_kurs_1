#!/usr/bin/python3

"""
Напишите функцию get_grade(points),
которая принимает количество баллов и возвращает оценку.

Количество баллов — целое число от 0 до 100.
0–40 баллов — Плохо
41–60 баллов — Удовлетворительно
61–80 баллов — Хорошо
81–100 баллов — Отлично
get_grade(35) # Вернет Плохо
get_grade(45) # Вернет Удовлетворительно
get_grade(100) # Вернет Отлично
"""

# Задача
"""
def get_grade(points):

    return ...

# Не удаляйте код ниже, он нужен для проверки

points = int(input())
grade = get_grade(points)
print(grade)
"""


# Решение
def get_grade(points: int) -> str:
    if points in range(41):
        return 'Плохо'
    elif points in range(41, 61):
        return 'Удовлетворительно'
    elif points in range(61, 81):
        return 'Хорошо'
    elif points in range(81, 101):
        return 'Отлично'


# Не удаляйте код ниже, он нужен для проверки

points = int(input())
grade = get_grade(points)
print(grade)
