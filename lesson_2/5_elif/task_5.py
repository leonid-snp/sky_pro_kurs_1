#!/usr/bin/python3
"""
Посчитайте размер бонуса курьера питьевой воды. Норма составляет 20 тысяч литров в квартал.

Если курьер выполняет норму, то получает бонус 10%.
Если доставляет 30 тысяч литров и больше, то получает 20%.
Если курьер не выполняет норму, то не получает никакой премии.

Со стандартного ввода подается объем доставленной воды. Посчитайте процент бонуса.

Ввод:
22000

Вывод:
Бонус = 10%
"""

# Задача
"""
water_delivered = int(input())

2_if ...
bonus_percent = ...
elif ... :
bonus_percent = ...
else:
bonus_percent = ... 


print("")
"""

# Решение
water_delivered = int(input())

if 20_000 <= water_delivered < 30_000:
    bonus_percent = '10%'
elif water_delivered >= 30_000:
    bonus_percent = '20%'
else:
    bonus_percent = '0%'

print(f"Бонус = {bonus_percent}")
