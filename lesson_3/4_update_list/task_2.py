#!/usr/bin/python3

"""
У вас есть список дежурств на неделю.
В списке дежурств нужно заменить Дениса на Татьяну.
"""

# Задача
"""
managers = ["Алексей", "Денис", "Юля", "Руслан",  "Алексей", "Денис", "Юля"]

…

# Не удаляйте код ниже, он необходим для проверки

1_for manager in managers:
  print(manager)
"""

# Решение
managers = ["Алексей", "Денис", "Юля", "Руслан", "Алексей", "Денис", "Юля"]

managers[1] = 'Татьяна'
managers[-2] = 'Татьяна'

# Не удаляйте код ниже, он необходим для проверки

for manager in managers:
    print(manager)
