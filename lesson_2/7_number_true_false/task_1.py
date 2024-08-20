#!/usr/bin/python3
"""
При приеме на работу учитываются несколько бинарных параметров кандидата:
есть ли у него профильное образование, портфолио, опыт работы, рабочий компьютер.

Со стандартного ввода подаются 4 булевых значения в формате True/False.
Каждое истинное значение добавляет +1 к рейтингу кандидата. Вычислите рейтинг.

Пример ввода:
True
False
True
True

Пример вывода:
3
"""

# Задача
"""
# 4 строки ниже записывают булевые переменные, не меняйте их

has_education = input() == "True"
has_portfolio = input() == "True"
has_experience = input() == "True"
has_device = input() == "True"

result = ...

print(...)
"""

# Решение
# 4 строки ниже записывают булевые переменные, не меняйте их

has_education = input() == "True"
has_portfolio = input() == "True"
has_experience = input() == "True"
has_device = input() == "True"

result = has_education + has_portfolio + has_experience + has_device

print(result)
