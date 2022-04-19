"""Домашняя работа, лекция №4"""

index1 = ''
index2 = ''

name = input('Введите ваше имя: ')
if name:
    index1 = f'Привет, {name} !' .title()
if not name:
    index1 = 'Ошибка: пустое имя!'
elif len(name) < 3:
    index1 = 'Ошибка: Имя cлишком короткое!'

age = int(input('Введите ваш возраст: '))
if age >= 14:
    index2 = f'{age} - отличный возраст!'
elif age > 0:
    index2 = 'Ошибка: Минимальный возраст — 14 лет.'
else:
    index2 = 'Ошибка: Несуществующий возраст!'
if age == 16 or age == 17:
    index2 = 'Вам пора получить паспорт.'
    if not name:
        index2 = ''
    elif len(name) < 3:
        index2 = ''
if age == 25 or age == 26:
    index2 = 'Вам пора получить паспорт.'
    if not name:
        index2 = ''
    elif len(name) < 3:
        index2 = ''
if age == 45 or age == 46:
    index2 = 'Вам пора получить паспорт.'
    if not name:
        index2 = ''
    elif len(name) < 3:
        index2 = ''

print(index1, index2)
