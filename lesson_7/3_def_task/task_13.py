#!/usr/bin/python3

"""
Напишите функцию get_discount(summ),
которая возвращает уровень скидки или бонусной карты в зависимости от суммы покупок.

Уровень — это целое число!

Правила вычисления уровня:
до 5000 вернет 1
до 10000 вернет 2
до 20000 вернет 3
до 35000 вернет 4
до 50000 вернет 5
от 50000 и выше вернет 6

Примеры вызова функции:
get_discount(2000) # Вернет 1
get_discount(7500) # Вернет 2
get_discount(45000) # Вернет 5
get_discount(75000) # Вернет 6
"""

# Задача
"""
def get_discount(summ):

    return ...

# Не удаляйте код ниже, он нужен для проверки

value = int(input())
result = get_discount(value)  
print(result)
"""


# Решение
def get_discount(summ: int) -> int:
    if summ in range(5000):
        return 1
    elif summ in range(5001, 10001):
        return 2
    elif summ in range(10001, 20001):
        return 3
    elif summ in range(20001, 35001):
        return 4
    elif summ in range(35001, 50001):
        return 5
    else:
        return 6


# Не удаляйте код ниже, он нужен для проверки

value = int(input())
result = get_discount(value)
print(result)
