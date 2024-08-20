#!/usr/bin/python3

"""
Напишите три функции:

get_first_element() — возвращает первый элемент из списка,
get_last_element() — последний,
get_list_length() — длину списка.

Примеры вызова функций:
get_first_element() вернет "Alpha"
get_last_element() вернет "Echo"
get_list_length() вернет 5
"""

# Задача
"""
letters = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]


def get_first_element():
  ...


def get_last_element():
  ...


def get_list_length():
  ...

# Не удаляйте код ниже, он нужен для проверки

print(get_first_element())
print(get_last_element())
print(get_list_length())
"""


# Решение
letters = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]


def get_first_element():
  return letters[0]


def get_last_element():
  return letters[-1]


def get_list_length():
  return len(letters)

# Не удаляйте код ниже, он нужен для проверки

print(get_first_element())
print(get_last_element())
print(get_list_length())
