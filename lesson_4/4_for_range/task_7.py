#!/usr/bin/python3

"""
С помощью конструкции for in range() выведите первые пять элементов списка.

Пример вывода:
Alpha
Bravo
...
...
Echo
"""

# Задача
"""
words = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", 
         "Foxtrot", "Golf", "Hotel", "India", "Juliett", 
         "Kilo", "Lima", "Mike", "November", "Oscar",
         "Papa", "Quebec", "Romeo", "Sierra", "Tango",
         "Uniform", "Victor", "Whiskey", "X-ray", "Yankee",
         "Zulu"]
"""

# Решение
words = ["Alpha", "Bravo", "Charlie", "Delta", "Echo",
         "Foxtrot", "Golf", "Hotel", "India", "Juliett",
         "Kilo", "Lima", "Mike", "November", "Oscar",
         "Papa", "Quebec", "Romeo", "Sierra", "Tango",
         "Uniform", "Victor", "Whiskey", "X-ray", "Yankee",
         "Zulu"]

for i in range(0, 5):
    print(words[i])