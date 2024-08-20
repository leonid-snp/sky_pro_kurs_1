#!/usr/bin/python3
"""
Известно, что чем меньше ваш опыт вождения,
чем хуже погода и видимость и чем больше вы устали, тем медленнее нужно ехать.

Мы придумали небольшой алгоритм вычисления рекомендуемой скорости,
которая завязана на булевых значениях:

Изначальное максимальное значение равно 90 км.
Если сейчас темно — вычтите 20 км.
Если ваш стаж вождения меньше года — вычтите 10 км.
Если на улице дождь — вычтите 10 км.
Если вы устали — вычтите 10 км.

Пример ввода:
1
0
1
1

Пример вывода:
50
"""

# Задача
"""
is_dark = bool(int(input()))
is_experience_less_1y = bool(int(input()))
is_raining = bool(int(input()))
is_driver_tired = bool(int(input()))

max_speed = 90

speed = max_speed - is_dark * 20 - ...

print(speed)
"""

# Решение
is_dark = bool(int(input()))
is_experience_less_1y = bool(int(input()))
is_raining = bool(int(input()))
is_driver_tired = bool(int(input()))

max_speed = 90

speed = max_speed - is_dark * 20 - is_experience_less_1y * 10 - is_raining * 10 - is_driver_tired * 10

print(speed)
