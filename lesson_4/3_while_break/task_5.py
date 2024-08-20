#!/usr/bin/python3

"""
При открытии вклада сумма на счете равна 0.
Каждый месяц пользователь пополняет свой вклад на одну и ту же сумму,
ее нужно получить со стандартного ввода (input()).

Выводите баланс счета за каждый месяц, пока сумма не достингет 12 000.

Пример вывода:
Баланс счета = 2000
Баланс счета = 4000
...
Баланс счета = 12000
"""

# Задача
"""
deposit = 0
replenishment = ...
while ...
    print(f"Баланс счета = {deposit}")  
    ...
"""

# Решение
deposit = 0
replenishment = int(input('Введите сумму пополнений: '))
while deposit + replenishment <= 12000:
    deposit += replenishment
    print(f"Баланс счета = {deposit}")
