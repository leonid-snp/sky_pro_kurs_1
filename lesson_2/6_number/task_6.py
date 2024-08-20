#!/usr/bin/python3
"""
Пользователь вводит три числа.
Найдите минимум, максимум, среднее арифметическое.
"""

# Задача
"""
number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

min_of = 
max_of = 
avg_of = 

print(f"Минимум: ...")
print(f"Максимум: ...")
print(f"Среднее: ...")
"""

# Решение
number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

min_of = min(number_1, number_2, number_3)
max_of = max(number_1, number_2, number_3)
avg_of = (number_1 + number_2 + number_3) // 3

print(f"Минимум: {min_of}")
print(f"Максимум: {max_of}")
print(f"Среднее: {avg_of}")
