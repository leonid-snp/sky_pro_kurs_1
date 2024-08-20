#!/usr/bin/python3

"""
Напишите функцию avg(items),
которая принимает список и вычисляет среднее арифметическое элементов.

Среднее арифметическое — это сумма всех чисел (sum),
разделенная на их количество (len).

Пример:
avg([1,2,3]) # Вернет 2.0
avg([5,5,5,5]) # Вернет 5.0
avg([2,8]) # Вернет 5.0
"""

# Задача
"""
def avg(items):

  return ...

# Не удаляйте код ниже, он нужен для проверки

items = [int(x) for x in input().split(" ")]
items_avg = avg(items)
print(items_avg)
"""


# Решение
def avg(items: list) -> float:
    return sum(items) / len(items)


# Не удаляйте код ниже, он нужен для проверки

items = [int(x) for x in input().split(" ")]
items_avg = avg(items)
print(items_avg)
