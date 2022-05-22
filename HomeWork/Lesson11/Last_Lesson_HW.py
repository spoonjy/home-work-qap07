from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import json
import os


@dataclass(order=True)
class CarBase(ABC):
    TOTAL_OBJECTS = 0
    current_speed = 0
    max_speed = 200
    label: str = field(compare=False)
    color: str = field(compare=False)
    year: int = field(compare=True)
    price: str = field(compare=False)
    TOTAL_OBJECTS += 1

    def info(self):
        """Информация о машине"""
        print(
            f'Машина - "{self.label}" \n'
            f'Цвет - {self.color} \n'
            f'Текущая скорость - {self.current_speed}  (макс. {self.max_speed}) км/ч.\n'
            f'Цена - {self.price}$ \n'
            f'Год выпуска - {self.year} \n'
        )

    def start_car(self):
        pass

    def dance_tesla(self):
        pass

    @staticmethod
    def stop_dance():
        pass

    @classmethod
    def total_objects(cls):
        print("Total objects: ", cls.TOTAL_OBJECTS)

    def drive(self, add_speed: int):
        """Увелечение скорости"""
        self.current_speed = min((self.calculate_speed(self.current_speed, add_speed), self.max_speed))
        print(f'{self.label} движется со скоростью  - {self.current_speed} км/ч.')

    @staticmethod
    def calculate_speed(current_speed, add_speed):
        return current_speed + add_speed

    def stop(self):
        """Остановка"""
        self.current_speed = 0
        print(f'{self.label} остановлена')


class Tesla(CarBase):
    def __init__(self, label, color, year, price):
        super().__init__(label, color, year, price)
        self.color = color
        self.label = label
        self.current_speed = 0
        self.year = year
        self.max_speed = 250

    def dance_tesla(self):
        """Режим Dancing mode"""
        print('Начинается Праздничное шоу Tesla, машина начинает сигналить, '
              'мигать фарами и открывать двери под музыку :)')

    @staticmethod
    def calculate_speed(current_speed, add_speed):
        return current_speed + add_speed - 10

    @staticmethod
    def stop_dance():
        return 'Шоу окончено'

    def start_car(self):
        print('Машина заведена')


class AirplaneBase(ABC):

    def __init__(self, label='', color='', year='', price=''):
        self.color = color
        self.label = label
        self.current_speed = 0
        self.year = year
        self.price = price
        self.max_speed = 800

    def info(self):
        """Информация о машине"""
        print(
            f'Самолет - "{self.label}" \n'
            f'Цвет - {self.color} \n'
            f'Текущая скорость - {self.current_speed}  (макс. {self.max_speed}) км/ч.\n'
            f'Цена - {self.price}$ \n'
            f'Год выпуска - {self.year} \n'
        )

    def drive(self, add_speed: int):
        """Увелечение скорости"""
        self.current_speed = min((self.current_speed + add_speed, self.max_speed))
        print(f'{self.label} движется со скоростью  - {self.current_speed} км/ч.')

    @abstractmethod
    def start_fly(self):
        pass

    @abstractmethod
    def duration(self):
        pass


class Jetcruzer(AirplaneBase):

    def __init__(self, label, color, year, price):
        super().__init__(label, color, year, price)
        self.color = color
        self.label = label
        self.current_speed = 0
        self.year = year
        self.max_speed = 590

    def start_fly(self):
        print(f'{self.label} набирает высоту')

    def duration(self):
        print(f'Дальность полета самолета {self.label} 1818 км.')


class Beechcraft(AirplaneBase):

    def __init__(self, label, color, year, price):
        super().__init__(label, color, year, price)
        self.color = color
        self.label = label
        self.current_speed = 0
        self.year = year
        self.max_speed = 620

    def start_fly(self):
        print(f'{self.label} набирает высоту')

    def duration(self):
        print(f'Дальность полета самолета {self.label} 2804 км.')


def main():
    car1 = Tesla(label='Tesla Model S', color='white', year='2012', price='70000$')
    car1.info()
    car1.start_car()
    car1.drive(180)
    car1.stop()
    car1.max_speed = 250
    print()

    car2 = Tesla(label='Tesla Model X', color='black', year='2017', price='130000$')
    car2.info()
    car2.start_car()
    car2.drive(235)
    car2.stop()
    car2.dance_tesla()
    car2.stop_dance()
    car2.max_speed = 300
    print()

    air1 = Jetcruzer(label='Jetcruzer 450', color='white', year='1994', price='1,6 millions')
    air1.info()
    air1.start_fly()
    air1.drive(520)
    air1.duration()
    air1.max_speed = 600
    print()

    air2 = Beechcraft(label='Beechcraft Starship', color='yellow', year='1995', price='3,9 millions')
    air2.info()
    air2.start_fly()
    air2.drive(610)
    air2.duration()
    air2.max_speed = 700
    print()

    lst = [car1, air1, air2]
    for i in lst:
        i.drive(250)

    a = Tesla.TOTAL_OBJECTS
    print(f'Количество созданных автомобилей Tesla = {a}')

    # Последняя часть домашки(Lesson11)
    """Сравниваем год выпуска через датакласс"""
    q1 = CarBase('a', 'b', 2012, 't')
    q2 = CarBase('v', 'x', 2017, 'u')
    print(f'{car1.label} старше чем {car2.label} = {q1 > q2}')


"""Создаем список json который сохраняется в другой файл"""
new_lst = {
    "Cars": [
        {
            "car1": "Tesla",
            "year": 2012,
            "model": "Tesla Model S",
            "color": "White",
            "price": 70000,
            "max_speed": 250
        },
        {
            "car2": "Tesla",
            "year": 2017,
            "model": "Tesla Model X",
            "color": "Black",
            "price": 130000,
            "max_speed": 300
        }

    ]
}

with open('vehicle.json', 'w') as f:
    json.dump(new_lst, f, indent=4)

"""загружаем файлы из json"""  # тут я не смог его вывести красиво и он пишется просто в строку
with open('vehicle.json') as json_file:
    data = json.load(json_file)
print(f'Список из json файла vehicle: {data}')
print()

"""функция которая сохраняет создает файл если его нет и сохраняет значения в json-формате """
filename = 'super_car.json'
my_file = open(filename, 'w', encoding='Latin-1')

new_car1 = {
    "car": "Tesla",
    "year": 2012,
    "model": "Tesla Model S",
    "color": "White",
    "price": 70000,
    "max_speed": 250
}

new_car2 = {
    "car": "Tesla",
    "year": 2017,
    "model": "Tesla Model X",
    "color": "Black",
    "price": 130000,
    "max_speed": 300
}

my_car = []  # тут я не понял из-за чего он ругается
my_car.append(new_car1)
my_car.append(new_car2)
json.dump(my_car, my_file)
my_file.close()

my_file = open(filename, 'r', encoding='Latin-1')
json_date = json.load(my_file)


def where_json(file_name):
    return os.path.exists(file_name)


# возможно здесь написано больше чем нужно, но зато в созданном файле все красиво выводится)
if os.path.isfile(filename) and os.access(filename, os.R_OK):
    print("File created and is readable")
else:
    print("Either file is missing or is not readable")

try:
    with open('super_car.json', 'r') as fp:
        accounts = json.load(fp)
except IOError:
    print('File not found, will create a new one.')
    accounts = {}
with open('super_car.json', 'w') as fp:
    json.dump(accounts, fp, indent=4)

for car in json_date:  # просто поболоваться, вывел отдельные атрибуты класса из json
    print('Car: ' + str(car["model"]))
    print('Year: ' + str(car["year"]))
    print('Max Speed : ' + str(car["max_speed"]))
print()

if __name__ == '__main__':
    main()

# Спасибо за обучение, Саша, надеюсь я не слишком тупил и не безнадежен, я правда старался)
