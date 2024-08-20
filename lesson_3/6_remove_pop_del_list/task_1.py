#!/usr/bin/python3

"""
У вас есть список покупок. Со стандартного ввода подаются три продукта.

С помощью метода remove удалите их из списка, затем выведите остальные продукты.

Пример ввода:
Хлопья
Молоко
Яблоки

Пример вывода:
["Печенье", "Шоколад"]
"""

# Задача
"""
shopping_list = ["Молоко", "Печенье", "Хлопья", "Шоколад", "Яблоки"]

item_to_remove_1 = input()
item_to_remove_2 = input()
item_to_remove_3 = input()

...

print(shopping_lis
"""

# Решение
shopping_list = ["Молоко", "Печенье", "Хлопья", "Шоколад", "Яблоки"]

item_to_remove_1 = input()
item_to_remove_2 = input()
item_to_remove_3 = input()

shopping_list.remove(item_to_remove_1)
shopping_list.remove(item_to_remove_2)
shopping_list.remove(item_to_remove_3)

print(shopping_list)
