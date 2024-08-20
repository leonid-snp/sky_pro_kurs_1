#!/usr/bin/python3

"""
У вас есть словарь с баллами студентов, пользователь вводит имя студента.
Выведите оценку по формуле.

81 и выше — это A.
61–80 — это B.
0–60 — это C.

Пример ввода:
Алиса

Пример вывода:
70 баллов, оценка B
"""

# Задача
"""
students = {
  "Алиса": 70, 
  "Эльдар" : 20 , 
  "Агата": 40, 
  "Ярослав": 84,
}

user_input = input()
"""

# Решение
students = {
    "Алиса": 70,
    "Эльдар": 20,
    "Агата": 40,
    "Ярослав": 84,
}

user_input = input()

if students[user_input] >= 81:
    print(f'{students[user_input]} баллов, оценка A')
elif students[user_input] in range(61, 81):
    print(f'{students[user_input]} баллов, оценка B')
elif students[user_input] in range(61):
    print(f'{students[user_input]} баллов, оценка C')
