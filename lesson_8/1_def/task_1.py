#!/usr/bin/python3

"""
По умолчанию в земных сутках 24 часа, но,
например, на Меркурии сутки длятся 1392 часа,
а на Сатурне 10 часов. Напишите функцию,
которая переводит часы в количество полных суток и возвращает полученное значение.
Функция может принимать вторым аргументом длительность суточного цикла, а может и не принимать.

Пример работы функции:
print(hours_to_days(48)) # Вернет 2
print(hours_to_days(12)) # Вернет 0
print(hours_to_days(36, 12))  # Вернет 3
"""

# Задача
"""
def hours_to_days( … ):
  pass


# не изменяйте код дальше, это проверка
values = [int(x) for x in input().split(" ")]
print(hours_to_days(*values))
"""


# Решение
def hours_to_days(hour: int, hour_day=24) -> int:
    return hour // hour_day


# не изменяйте код дальше, это проверка
values = [int(x) for x in input().split(" ")]
print(hours_to_days(*values))
