import pytest
import allure

@allure.feature("Простая арифметика")
@allure.story("Сложение")
@allure.severity(allure.severity_level.NORMAL)
def test_addition():
    with allure.step("Сложение двух чисел"):
        result = 2 + 2
        assert result == 4, "Ошибка: 2 + 2 должно быть 4"

@allure.feature("Проверка строк")
@allure.story("Сравнение строк")
@allure.severity(allure.severity_level.CRITICAL)
def test_string():
    with allure.step("Сравниваем две строки"):
        assert "hello" == "hello", "Строки не совпадают"
