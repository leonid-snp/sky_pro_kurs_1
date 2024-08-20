#!/usr/bin/python3

"""
У вас есть словарь, который содержит перевод цифр в слова.
Дополните его, не редактируя первую строчку кода.

Данные для добавления:

4: "four",
5: "five",
6: "six",
7: "seven",
8: "eight",
9: "nine",
"""

# Задача
"""
numbers = {
  1: "one",
  2: "two",
  3: "three",
}

numbers[...] = ...
...

# Не удаляйте код ниже: он нужен для проверки.

print("_".join([str(x) for x in numbers]))
print("_".join(numbers.values()))
"""

# Решение
numbers = {
    1: "one",
    2: "two",
    3: "three"
}

numbers[4] = 'four'
numbers[5] = 'five'
numbers[6] = 'six'
numbers[7] = 'seven'
numbers[8] = 'eight'
numbers[9] = 'nine'

# Не удаляйте код ниже: он нужен для проверки.

print("_".join([str(x) for x in numbers]))
print("_".join(numbers.values()))
