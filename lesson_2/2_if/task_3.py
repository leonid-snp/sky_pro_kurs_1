#!/usr/bin/python3
"""
Напишите примитивный калькулятор, который увеличивает счетчик на 1 за каждый утвердительный ответ.
Финальный рейтинг должен получиться от 0 до 3.

Пример вывода:
0, 1, 2, 3

Переменная          Расшифровка                         Должно быть
residency           Время жизни на одном месте          >= 2 года
salary              Зарплата                            >= 50000
experience          Стаж работы                         >= 2 года
"""

# Задача
"""
residency = input()
salary = input()
experience = input()


counter = ...


2_if …
 counter += 1
2_if …
 counter += 1
2_if …
 counter += 1

print(f"Ваш кредитный рейтинг - X")
"""

# Решение
residency = input()
salary = input()
experience = input()

counter = 0

if int(residency) >= 2:
    counter += 1
if int(salary) >= 50000:
    counter += 1
if int(experience) >= 2:
    counter += 1

print(f"Ваш кредитный рейтинг - {counter}")
