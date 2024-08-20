#!/usr/bin/python3

"""
Функция get_distance(fuel, consumption) вычисляет,
сколько пролетит самолет в зависимости от объема
топлива на борту в литрах и расхода топлива на километр,
и возвращает количество километров.

По умолчанию каждый километр расходуется 20 литров,
но мы можем переопределить это значение (например, если самолет перегружен,
на каждый километр расходуется 25 литров).

Пример ввода:
get_distance(100) # Вернет 5.0
get_distance(200) # Вернет 10.0
get_distance(100, 20) # Вернет 5.0
get_distance(100, 50) # Вернет 2.0
get_distance(200, 50) # Вернет 4.0
"""

# Задача
"""
def get_distance(...) 
    ...

# не изменяйте код дальше, это проверка

values = [int(x) for x in input().split(" ")]
print(get_distance(*values))
"""


# Решение
def get_distance(fuel: int, consumption=20) -> float:
    return fuel / consumption


# не изменяйте код дальше, это проверка

values = [int(x) for x in input().split(" ")]
print(get_distance(*values))
