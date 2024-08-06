#!/usr/bin/python3
"""
Со стандартного ввода подается количество студентов.
В одной учебной группе должно быть 4 студента.
Сколько полных групп из 4 студентов можно создать?
"""

# Задача
"""
number_of_students = int(input())

number_of_groups =     

print(f"Получится {number_of_groups} полных групп")
"""

# Решение
number_of_students = int(input())

number_of_groups = number_of_students // 4

print(f"Получится {number_of_groups} полных групп")
