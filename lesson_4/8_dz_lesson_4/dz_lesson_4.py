hello = input('Привет!\n'
              'Предлагаю проверить твои знания английского!\n'
              'Наберите `ready`, чтобы начать!\n'
              'Ввод: ')

questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

correct_answer = 0
grade = 0
count_questions = len(questions)

if hello != 'ready':
    print('Кажется вы не хотите играть. Очень жаль.')
else:
    for i in range(count_questions):
        attempts = 3
        while attempts != 0:
            answer = input(f'{questions[i]}: ')
            if answer == answers[i]:
                correct_answer += 1
                grade += attempts
                print('Ответ верный!')
                break
            else:
                attempts -= 1
                if attempts != 0:
                    print(f'Осталось попыток {attempts}, попробуйте еще раз!')
                else:
                    print(f'Увы, но нет. Верный ответ {answers[i]}')

interest = (grade * 100) // (count_questions * 3)
word_1 = 'вопрос' if correct_answer == 1 else 'вопроса'
word_2 = 'процента' if interest == 1 else 'процентов'
word_3 = 'балл' if grade == 1 else 'баллов'

print(f'Вот и всё! Вы ответили на {correct_answer} '
      f'{word_1} из {count_questions} '
      f'верно, вы набрали {grade} {word_3} '
      f'это {interest} {word_2}.')
