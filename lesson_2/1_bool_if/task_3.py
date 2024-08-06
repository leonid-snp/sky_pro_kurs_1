#!/usr/bin/python3
"""
Со стандартного ввода подается слово, например locator.
В булевой переменной has_r запишите наличие буквы R.
В булевой переменной has_l запишите наличие буквы L.
В булевой переменной has_s запишите наличие буквы S.

Пример вывода:
Слово locator
Есть буква R
Есть буква L
"""

# Задача
"""
word = input()

has_r = "r" in word
has_l = ...
has_s = ...

print("Слово", word)

2_if has_r:
    print("Есть буква R")
...
"""

# Решение
word = input()

has_r = "r" in word
has_l = "l" in word
has_s = "s" in word

print("Слово", word)

if has_r:
    print("Есть буква R")
if has_l:
    print("Есть буква L")
if has_s:
    print("Есть буква S")
