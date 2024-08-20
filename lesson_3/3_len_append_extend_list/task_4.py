#!/usr/bin/python3

"""
У вас есть список букв.
Со стандартного ввода подаются три символа.
Добавьте их в конец списка с помощью метода extend.
"""

# Задача
"""
symbols = ["m", "o", "n"]


symbol_1 = input()
symbol_2 = input()
symbol_3 = input()

symbols...

# Не удаляйте код ниже, он нужен для проверки

print("".join(symbols))
"""

# Решение
symbols = ["m", "o", "n"]


symbol_1 = input()
symbol_2 = input()
symbol_3 = input()

symbols.extend([symbol_1, symbol_2, symbol_3])

# Не удаляйте код ниже, он нужен для проверки

print("".join(symbols))
