#!/usr/bin/python3

"""
У вас есть прогноз погоды на 3 дня с температурой и описанием погоды.

Выведите прогноз на 3 дня в формате:

Понедельник +10 ясно
Вторник +13 дождь
Среда +9 град
"""

# Задача
"""
temp = ["+10", "+8", "+7"]
weather = ["ясно", "дождь", "град"]

print("Понедельник", temp[0], ...)
print("Вторник", ...)
print("Среда", ...)
"""

# Решение
temp = ["+10", "+8", "+7"]
weather = ["ясно", "дождь", "град"]

print("Понедельник", temp[0], weather[0])
print("Вторник", temp[1], weather[1])
print("Среда", temp[2], weather[2])
