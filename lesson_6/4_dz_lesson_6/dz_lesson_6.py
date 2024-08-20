tasks = {
    "easy": {
        "family": "семья",
        "hand": "рука",
        "people": "люди",
        "evening": "вечер",
        "minute": "минута",
    },
    "medium": {
        "believe": "верить",
        "feel": "чувствовать",
        "make": "делать",
        "open": "открывать",
        "think": "думать",
    },
    "hard": {
        "rural": "деревенский",
        "fortune": "удача",
        "exercise": "упражнение",
        "suggest": "предлагать",
        "except": "кроме",
    }
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

answers = {}
count_good_answer = 0

level = input('Выберите уровень сложности.\n'
              '`easy`, `medium`, `hard`.\n'
              'Ввод: ').lower()

user_input = input(f'Выбран уровень сложности `{level}`, '
                   f'мы предложим 5 слов, подберите перевод.\n'
                   f'Нажмите Enter.')

words = tasks[level]
for key, value in words.items():
    question = input(f'{key}, {len(value)} букв, начинается на {value[0]:.<4} : ').lower()
    if question == value:
        answers[key] = True
        print(f'Верно, {key} - это {value}.\n')
    else:
        answers[key] = False
        print(f'Неверно. {key} - это {value}.')

print('Правильно отвеченные слова:')
for key, value in answers.items():
        if value:
            count_good_answer += 1
            print(key)

print('Неправильно отвеченные слова:')
for key, value in answers.items():
        if not value:
            print(key)

print(f'Ваш ранг:\n'
      f'{levels[count_good_answer]}')
