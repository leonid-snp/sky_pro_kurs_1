#!/usr/bin/python3

"""
Допишите функцию,
которая получает два числа и возвращает количество процентов,
которое составляет первое от второго.
Значение возвращается в виде строки со знаком процента.
Результат округляется до целого числа.

get_percent_rounded(10, 10) # Вернет "100%"
get_percent_rounded(5, 15) # Вернет "33%"
get_percent_rounded(0, 5)  # Вернет "0%"
"""

# Задача
"""
def get_percent_rounded(....):

    return ...

# Не удаляйте код ниже, он нужен для проверки

a = int(input())
b = int(input())
print(get_percent_rounded(a, b))
"""


# Решение
def get_percent_rounded(a: int, b: int) -> str:
    return f'{a / b:.0%}'


# Не удаляйте код ниже, он нужен для проверки

a = int(input())
b = int(input())
print(get_percent_rounded(a, b))
