#!/usr/bin/python3

"""
У вас есть три строки.
Выведите длину каждой из них на новой строке,
затем выведите общую длину всех строк.

Пример ввода:
Alfa
Bravo
Uniform

Пример вывода:
4
5
7
16
"""

# Задача
"""
line_1 = "Python"
line_2 = "Java"
line_3 = "Go"
"""

# Решение
line_1 = "Python"
line_2 = "Java"
line_3 = "Go"

length_strings = [len(line) for line in [line_1, line_2, line_3]]
sum_length = sum(length_strings)
print(*length_strings, sum_length, sep='\n')
