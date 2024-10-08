#!/usr/bin/python3

"""
У вас есть список гостей с отметкой о том, кто придет.
Выведите только тех, кто придет.

Пример вывода:
Эльдар
Алиса
"""

# Задача
"""
guests = {
  "Алиса": True, 
  "Эльдар" : False, 
  "Агата": False, 
  "Ярослав": True,
}
"""

# Решение
guests = {
    "Алиса": True,
    "Эльдар": False,
    "Агата": False,
    "Ярослав": True,
}

for k, v in guests.items():
    if v:
        print(k)