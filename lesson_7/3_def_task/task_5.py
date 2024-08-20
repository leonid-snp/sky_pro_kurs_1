#!/usr/bin/python3

"""
Напишите функцию get_period(hour),
которая принимает час и возвращает время суток.

Час — это целое число в диапазоне от 0 до 23.
Если время 0–6 — ночь
Если время 7–11 — утро
Если время 12–17 — день
Если время 18–23 — вечер

Примеры вызова:
get_period(8) # Вернет "утро"
get_period(17) # Вернет "день"
get_period(0) # Вернет "ночь"
"""

# Задача
"""
def get_period(hour):

    return ...

# Не удаляйте код ниже, он нужен для проверки

hour = int(input())
time_of_day = get_period(hour)
print(time_of_day)
"""


# Решение
def get_period(hour: int) -> str:
    if hour in range(7):
        return 'ночь'
    elif hour in range(7, 12):
        return 'утро'
    elif hour in range(12, 18):
        return 'день'
    elif hour in range(18, 24):
        return 'вечер'


# Не удаляйте код ниже, он нужен для проверки

hour = int(input())
time_of_day = get_period(hour)
print(time_of_day)
