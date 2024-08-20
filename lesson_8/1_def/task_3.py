#!/usr/bin/python3

"""
Напишите функцию count_successful(students, score),
которая считает, сколько студентов прошли тестирование.

Функция получает список оценок студентов (students)
и возвращает количество студентов, которые набрали проходной балл (score).
По умолчанию проходной балл равен 50, но мы можем передать и другое значение score.

Пример ввода:
count_successful([]) # Возвращает 0
count_successful([50, 50]) # Возвращает 2
count_successful([20, 20]) # Возвращает 0
count_successful([40, 40], 40) # Возвращает 2
count_successful([80, 40]) # Возвращает 1
count_successful([80, 40], 40) # Возвращает 2
count_successful([60, 60], 90) # Возвращает 0
"""

# Задача
"""
def count_successful():
    return ...


# не изменяйте код дальше, это проверка

values = [int(x) for x in input().split(" ")]
score = input()

print(count_successful(values, int(score)) if score.isdigit() else count_successful(values))
"""


# Решение
def count_successful(students_ball: list[int, ...], score=50) -> int:
    count_students = 0
    for ball in students_ball:
        if ball >= score:
            count_students += 1
    return count_students


# не изменяйте код дальше, это проверка

values = [int(x) for x in input().split(" ")]
score = input()

print(count_successful(values, int(score)) if score.isdigit() else count_successful(values))
