#!/usr/bin/python3
"""
Со стандартного ввода подаются слова с буквой «р» (русскоязычная буква).
Если в первом слове есть «р» — добавьте +1 к переменной-счетчику,
если во втором — добавьте к счетчику +1.

Пример вывода:
0, 1, 2

"""

# Задача
"""
word1 = input()
word2 = input()

counter = 0

2_if "р" in ...
  ....

2_if "р" in ...
  ....    


print(counter)
"""

# Решение
word1 = input()
word2 = input()

counter = 0

if "р" in word1:
    counter += 1

if "р" in word2:
    counter += 1

print(counter)
