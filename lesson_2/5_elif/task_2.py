#!/usr/bin/python3
"""
Со стандартного ввода подается цифрой число от 0 до 4. Выведите его прописью.

Ввод            Вывод
0               ноль
1               один
2               два
3               три
4               четыре

Пример вывода:
ноль, один, два, три, четыре
"""

# Задача
"""
number = input()
"""

# Решение
number = input()
item = {
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре'
}
print(item[number])
