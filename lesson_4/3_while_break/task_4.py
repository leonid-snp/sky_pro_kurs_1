#!/usr/bin/python3

"""
При открытии вклада сумма на счете равна 0.
Каждый месяц пользователь пополняет свой вклад на одну и ту же сумму — 1500.

Выводите баланс счета за каждый месяц, пока сумма не начнет превышать 10 000.

Пример вывода:
Баланс счета = 1500
Баланс счета = 3000
...
Баланс счета = 10500
"""

# Задача
"""
deposit = 0
replenishment = 1500
...
   print(f"Баланс счета = {deposit}")
"""

# Решение
deposit = 0
replenishment = 1500
while deposit < 10000:
    print(f"Баланс счета = {deposit + 1500}")
    deposit += 1500
