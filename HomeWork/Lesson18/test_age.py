from age import *
import unittest


class TestHomeWork18(unittest.TestCase):

    def setUp(self) -> None:
        self.name = validate_name
        self.age = validate_age
        self.passport = validate_passport
        self.clean = clean
        self.main = main

    def test_name(self):
        self.assertEqual(self.name(""), "Ошибка: Пустое имя. ")
        self.assertEqual(self.name("Ян"), "Ошибка: В имени меньше трех символов. ")
        self.assertEqual(self.name("Жан Клод Ван-Дам"), "Ошибка: Cлишком много пробелов! ")

    def test_name_neg(self):
        self.assertNotEqual(self.name("Ярик"), "Привет, !")
        self.assertNotEqual(self.name("Ярослав"), "Привет, ЯРОСЛАВ")
        self.assertNotEqual(self.name(""), "Привет! ")

    def test_age(self):
        self.assertEqual(self.age(3), "Ошибка: Возраст меньше 14 лет")
        self.assertEqual(self.age(-9), "Ошибка: неверное значение возраста")
        self.assertEqual(self.age(18), "")

    def test_age_neg(self):
        self.assertNotEqual(self.age(5), "Тебе 5 лет.")
        self.assertNotEqual(self.age(0), "Тебе 0 лет.")
        self.assertNotEqual(self.age(10), "Тебе 10 лет.")

    def test_passport(self):
        self.assertEqual(self.passport(16), "Не забудьте получить первый паспорт. ")
        self.assertEqual(self.passport(25), "Не забудьте заменить паспорт. ")
        self.assertEqual(self.passport(46), "Не забудьте еще раз заменить паспорт. ")

    def test_passport_neg(self):
        self.assertNotEqual(self.passport(17), "Тебе 17 лет")
        self.assertNotEqual(self.passport(26), "Тебе 26 лет.")
        self.assertNotEqual(self.passport(45), "")

    def test_clean(self):
        self.assertEqual(self.clean(" Ярик"), "Ярик")
        self.assertEqual(self.clean("Ярик "), "Ярик")
        self.assertEqual(self.clean(" Ярослав "), "Ярослав")

    def test_clean_neg(self):
        self.assertNotEqual(self.clean("Ярослав"), " Ярослав")
        self.assertNotEqual(self.clean("Ярик "), "Ярик ")
        self.assertNotEqual(self.clean("Саня"), " Саня ")

    def test_main(self):
        self.assertEqual(self.main("Ярик", 31), "Привет, Ярик! Тебе 31 лет. ")
        self.assertEqual(self.main("Ярик", 25), "Привет, Ярик! Тебе 25 лет. Не забудьте заменить паспорт. ")
        self.assertEqual(self.main("Ярик", 50), "Привет, Ярик! Тебе 50 лет. ")

    def test_main_neg(self):
        self.assertNotEqual(self.main("Ярик", 0), "Привет, Ярик! Тебе 0 лет.")
        self.assertNotEqual(self.main("Яр", -11), "Привет, Яр! Тебе -11 лет.")
        self.assertNotEqual(self.main("Ярослав", 25), "Привет, Ярослав!")
        self.assertNotEqual(self.main("Ярослав", 13), "Привет, Ярослав! Не забудьте получить первый паспорт. ")
        self.assertNotEqual(self.main("Ярик Ярослав Яр", 7), "Привет, Ярослав! Тебе 7 лет!")

# В последнем в голову пришлось чуть больше вариаций тестов, решил их записать, почему бы и нет)
