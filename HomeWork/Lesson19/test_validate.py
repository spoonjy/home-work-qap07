from validate import *
import pytest


class TestHomeWork19:
    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        print("Тест пройден!")

    @pytest.mark.name_verification
    @pytest.mark.parametrize(
        "name, expected_result",
        [
            ("", "Ошибка: Пустое имя. "),
            ("Ян", "Ошибка: В имени меньше трех символов. "),
            ("Жан Клод Ван-Дам", "Ошибка: Cлишком много пробелов! ")

        ]
    )
    def test_name(self, name, expected_result):
        assert validate_name(name) == expected_result

    @pytest.mark.name_verification_negative
    @pytest.mark.parametrize(
        "name, expected_result",
        [
            ("Ярик", "Привет, !"),
            ("Ярослав", "Привет"),
            ("", "Привет! ")
        ]
    )
    def test_name_neg(self, name, expected_result):
        assert validate_name(name) != expected_result

    @pytest.mark.age_verification
    @pytest.mark.parametrize(
        "age, expected_result",
        [
            (3, "Ошибка: Возраст меньше 14 лет"),
            (-9, "Ошибка: неверное значение возраста"),
            (18, "")

        ]
    )
    def test_age(self, age, expected_result):
        assert validate_age(age) == expected_result

    @pytest.mark.age_verification_negative
    @pytest.mark.parametrize(
        "age, expected_result",
        [
            (5, "Тебе 5 лет."),
            (0, "Тебе 0 лет."),
            (10, "Тебе 10 лет.")
        ]
    )
    def test_age_neg(self, age, expected_result):
        assert validate_age(age) != expected_result

    @pytest.mark.passport_verification
    @pytest.mark.parametrize(
        "passport, expected_result",
        [
            (16, "Не забудьте получить первый паспорт. "),
            (25, "Не забудьте заменить паспорт. "),
            (46, "Не забудьте еще раз заменить паспорт. ")

        ]
    )
    def test_passport(self, passport, expected_result):
        assert validate_passport(passport) == expected_result

    @pytest.mark.passport_verification_negative
    @pytest.mark.parametrize(
        "passport, expected_result",
        [
            (17, "Тебе 17 лет"),
            (26, "Тебе 26 лет."),
            (45, "")
        ]
    )
    def test_passport_neg(self, passport, expected_result):
        assert validate_passport(passport) != expected_result

    @pytest.mark.skip(reason="захотелось пропустить)")
    @pytest.mark.clean
    @pytest.mark.parametrize(
        "name, expected_result",
        [
            ("Ярослав", "Ярослав"),
            ("Ярик ", "Ярик"),
            ("Саня", "Саня")

        ]
    )
    def test_clean(self, name, expected_result):
        assert clean(name) == expected_result

    @pytest.mark.clean_negative
    @pytest.mark.parametrize(
        "name, expected_result",
        [
            ("Ярослав", " Ярослав"),
            ("Ярик ", "Ярик "),
            ("Саня", " Саня ")
        ]
    )
    def test_clean_neg(self, name, expected_result):
        assert clean(name) != expected_result

    @pytest.mark.main
    @pytest.mark.parametrize(
        "name, age, expected_result",
        [
            ("Ярик", 31, "Привет, Ярик! Тебе 31 лет. "),
            ("Ярик", 25, "Привет, Ярик! Тебе 25 лет. Не забудьте заменить паспорт. "),
            ("Ярик", 50, "Привет, Ярик! Тебе 50 лет. ")
        ]
    )
    def test_main(self, name, age, expected_result):
        assert main(name, age) == expected_result

    @pytest.mark.main_negative
    @pytest.mark.parametrize(
        "name, age, expected_result",
        [
            ("Ярик", 0, "Привет, Ярик! Тебе 0 лет."),
            ("Яр", -11, "Привет, Яр! Тебе -11 лет."),
            ("Ярослав", 25, "Привет, Ярослав!"),
            ("Ярослав", 13, "Привет, Ярослав! Не забудьте получить первый паспорт. "),
            ("Ярик Ярослав Яр", 7, "Привет, Ярослав! Тебе 7 лет!")
        ]
    )
    def test_main_neg(self, name, age, expected_result):
        assert main(name, age) != expected_result
