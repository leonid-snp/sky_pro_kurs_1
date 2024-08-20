#!/usr/bin/python3

"""
С помощью конструкции for in range() выведите последние пять элементов списка.

Пример вывода:

Victor
Whiskey
...
...
Zulu
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

for i in range(len(words) - 5, len(words)):
    print(words[i])
