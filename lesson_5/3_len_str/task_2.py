#!/usr/bin/python3

"""
У вас есть три строки.
Выведите среднюю длину слов.
Округлять значение не нужно.

Пример вывода:
8.0
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

len_string = [len(line) for line in [line_1, line_2, line_3]]
print(sum(len_string) / 3)
