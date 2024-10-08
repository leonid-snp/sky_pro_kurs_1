#!/usr/bin/python3

"""
Новая забава Алисы и Бориса — обмениваться сообщениями,
в которых много лишнего шума, например цифр.
Впрочем, это не проблема, если есть программа,
которая разделит строку по пробелам и оставит только слова (а цифры пропустит).
Чтобы проверить, является ли строка числом, используйте метод isdigit(),
а чтобы проверить, является ли строка набором букв, — isalpha().
"""

# Задача
"""
text = "734 122 мне 877 119 022 кажется 127 0 0 1 за 192 168 нами 255 255 следят 32 32 2 5"
just_words = []

...

print(text_cleaned)
"""

# Решение
text = "734 122 мне 877 119 022 кажется 127 0 0 1 за 192 168 нами 255 255 следят 32 32 2 5"
just_words = [word for word in text.split(' ') if word.isalpha()]



print(*just_words)