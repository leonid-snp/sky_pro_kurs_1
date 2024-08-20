#!/usr/bin/python3
"""
У вас в группе X студентов, из них Y пришли на онлайн-встречу.
Выведите, сколько процентов пришло. Проценты округлите до целого числа.
"""

# Задача
"""
students_count = int(input())
students_online = int(input())

online_percent = ...

print(f"На встречу пришло {online_percent} процентов")
"""

# Решение
students_count = int(input())
students_online = int(input())

online_percent = int(students_online * 100 / students_count)

print(f"На встречу пришло {online_percent} процентов")
