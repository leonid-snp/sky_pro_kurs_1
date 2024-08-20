#!/usr/bin/python3

"""
Алиса часто зависает в сообществах по криптографии и заметила интересную функцию.
Когда она пишет сообщение, в редакторе отображается, сколько в нем символов.
Алиса решает написать похожую программу для подсчета количества слов в тексте.

Со стандартного ввода подается длинная строка, в которой слова разделены пробелом.
Программа должна вывести общее количество слов в тексте.

Пример ввода:
Горизонтали на огромной шахматной доске отделены друг от друга ручейками.
Вертикали — живыми изгородями.
В продолжение всей игры Алиса остается позади Королевы — лишь последним ходом,
став сама королевой, она берет Черную Королеву,
чтобы поставить мат дремлющему Черному Королю.

Вывод:
Количество слов: 39
"""

# Задача
"""
text = input()

...

print('Количество слов: 39')
"""

# Решение
text = input()

count_words = 0
for letter in text:
    if letter == ' ':
        count_words += 1

print(f'Количество слов: {count_words + 1}')
