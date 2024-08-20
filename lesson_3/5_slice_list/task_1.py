#!/usr/bin/python3

"""
У вас есть список дней недели на иностранном языке.
Создайте новый список, в котором будут только будние дни.
"""

# Задача
"""
weekdays = [
"pirmdiena", 
"otrdiena", 
"trešdiena",
"ceturtdiena", 
"piektdiena", 
"sestdiena", 
"svētdiena"]


workdays = ...


# Не удаляйте код ниже, он нужен для проверки

1_for workday in workdays:
  print(workday)
"""

# Решение
weekdays = [
    "pirmdiena",
    "otrdiena",
    "trešdiena",
    "ceturtdiena",
    "piektdiena",
    "sestdiena",
    "svētdiena"]

workdays = weekdays[:5]

# Не удаляйте код ниже, он нужен для проверки

for workday in workdays:
    print(workday)
