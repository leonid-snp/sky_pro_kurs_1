#!/usr/bin/python3

"""
Возраст жильцов в доме варьируется от 0 до 99 лет.
Вычислите средний возраст жильцов и выведите в виде целого числа.

Пример ответа:
25
"""

# Задача
"""
residents = [5, 3, 2, 20, 5, 30, 5, 34]
residents_count = 0
age_sum = 0

1_for ... in ... :
    ...
"""

# Решение
residents = [5, 3, 2, 20, 5, 30, 5, 34]
residents_count = 0
age_sum = 0

for resident in residents:
    age_sum += resident
    residents_count += 1

print(age_sum // residents_count)