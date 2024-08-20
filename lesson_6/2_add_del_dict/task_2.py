#!/usr/bin/python3

"""
У вас есть словарь.
Со стандартного ввода подается сперва отдельной строкой ключ, затем отдельной строкой значение.
Добавьте новую пару «ключ-значение».
"""

# Задача
"""
shopping_list = {
  "Справочник по Python": 2200,
  "Блокнот в клеточку": 800,
  "Набор карандашей": 650
}

new_key = input()
new_value = input()

# Не удаляйте код ниже: он нужен для проверки.

print("_".join(shopping_list))
print("_".join([str(x) for x in shopping_list.values()]))
"""

# Решение
shopping_list = {
    "Справочник по Python": 2200,
    "Блокнот в клеточку": 800,
    "Набор карандашей": 650
}

new_key = input()
new_value = input()

shopping_list[new_key] = new_value

# Не удаляйте код ниже: он нужен для проверки.

print("_".join(shopping_list))
print("_".join([str(x) for x in shopping_list.values()]))
