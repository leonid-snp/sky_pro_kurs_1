#!/usr/bin/python3

"""
Со стандартного ввода (input) вводятся значения, каждое на отдельной строке.
В конце вводится stop.

Получите значения, посчитайте их количество, выведите это количество.

Используйте синтаксис while ... break для этого задания.

Пример ввода:
1
2
1
2
stop

Пример вывода:
4
"""

# Задача
"""
number_of_elements = 0

while ...
  user_input = input()
  if ...
    break
"""

# Решение
number_of_elements = 0

while True:
    user_input = input()
    number_of_elements += 1
    if user_input == 'stop':
        break

print(number_of_elements - 1)