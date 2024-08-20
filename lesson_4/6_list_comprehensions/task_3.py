#!/usr/bin/python3

"""
Отфильтруйте список из строк, которые содержат "р".
"""

# Задача
"""
words = ["ракушка", "кукушка", "рыбка"]
words_with_r = ...

# Не удаляйте этот код, он нужен для проверки 

[print(w) for w in words_with_r]
"""

# Решение
words = ["ракушка", "кукушка", "рыбка"]
words_with_r = [word for word in words if 'р' in word]

# Не удаляйте этот код, он нужен для проверки

[print(w) for w in words_with_r]