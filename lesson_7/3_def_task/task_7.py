#!/usr/bin/python3

"""
Напишите функцию get_rur_kop(value),
которая получает сумму в копейках, а возвращает количество полных рублей.
В качестве value всегда передается целое число.

Подсказка: деление нацело — x // y
get_rur_kop(100) # Возвращает 1
get_rur_kop(755) # Возвращает 7
get_rur_kop(1234) # Возвращает 12
get_rur_kop(99) # Возвращает 0
"""

# Задача
"""
def get_rur_kop(value):  
    return ...


# Не удаляйте код ниже, он нужен для проверки

value = int(input())
result = get_rur_kop(value)
print(result)
"""


# Решение
def get_rur_kop(value: int) -> int:
    return value // 100


# Не удаляйте код ниже, он нужен для проверки

value = int(input())
result = get_rur_kop(value)
print(result)
