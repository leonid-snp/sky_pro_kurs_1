#!/usr/bin/python3

"""
У вас есть список лекарств.
Со стандартного ввода подаются два индекса.
Нумерация в передаваемых индексах начинается с нуля.

Удалите с помощью оператора del соответствующие лекарства.
Выведите оставшиеся лекарства.

Обратите внимание, после удаления нумерация элемента может поменяться.
"""

# Задача
"""
medications = ["Пепамицин", "Дилитарил", "Флоутолар", "Россум-лайт"]

index_to_remove_1 = input()
index_to_remove_2 = input()

...

print(medications)
"""

# Решение
medications = ["Пепамицин", "Дилитарил", "Флоутолар", "Россум-лайт"]

index_to_remove_1 = int(input())
index_to_remove_2 = int(input())

del medications[index_to_remove_1]
del medications[index_to_remove_2]

print(medications)
