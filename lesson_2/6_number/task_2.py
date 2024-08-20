#!/usr/bin/python3
"""
На жестком диске 110 гигабайт.
30 занимает операционная система, 22 занимают документы.
Посчитайте остаток.
"""

# Задача
"""
space_total = 110
space_os = 30
space_docs = 22
space_free = ...

print(space_free)
"""

# Решение
space_total = 110
space_os = 30
space_docs = 22
space_free = space_total - space_os - space_docs

print(space_free)
