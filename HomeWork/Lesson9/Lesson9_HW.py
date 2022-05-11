"""9 занятие"""

"""Проверка чилса на четность"""
func = lambda x=int(input('Введите ваше число: ')): print('Ваше число чётное') \
    if x % 2 == 0 else print('Ваше число нечётное')
func()
print()

"""Переводим список чисел в строку"""
lst = [1, 2, 3, 4, 5]
print(
    list(
        map(
            lambda x: str(x + 0), lst
        )
    )
)
print()

"""filter на слова-палиндромы"""
words = ["cat", "tenet", "phone", "топот", "level", "home", "music", "радар"]
palindromes = list(filter(lambda word: word == word[::-1], words))
print("Слова палиндромы: ", list(palindromes))
print()

"""Декоратор который выводит время выполнения функции"""
from datetime import datetime
import time


def test_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        elapsed = (end - start).total_seconds()
        print(f'>> функция {func.__name__} время выполнения: {elapsed}')

    return wrapper


@test_time
def test_time(a, b, delay=0):
    print('сложить', a, b, delay)
    time.sleep(delay)
    return a + b


print('старт программы')
test_time(10, 20, 1)
print('конец программы')
