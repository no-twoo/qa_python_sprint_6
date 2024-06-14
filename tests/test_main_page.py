from conftest import *
import pytest

from data import *
from pages.main_page import *
import allure


class TestMainPage:

    @allure.title('Проверка соответствия ответов на вопросы ожидаемым значениям')
    @allure.description('Тест проверяет, что значение ответа на вопрос соответствует ожидаемому значению')
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, answer_1),
            (1, answer_2),
            (2, answer_3),
            (3, answer_4),
            (4, answer_5),
            (5, answer_6),
            (6, answer_7),
            (7, answer_8),
        ]
    )
    def test_question_and_answer(self, driver, num, result):
        driver.get(main_page_url)
        main_page = MainPage(driver)
        actual_result = main_page.get_answer_text(num)

        assert actual_result == result

    @allure.title('Проверка перехода по кнопке вверху страницы на страницу оформления заказа')
    @allure.description('Тест проверяет, что значение url соответствует ожидаемому значению')
    def test_button_order_header(self, driver):
        driver.get(main_page_url)
        button_order_header = MainPage(driver)

        assert button_order_header.check_order_header() == 'https://qa-scooter.praktikum-services.ru/order'

    @allure.title('Проверка перехода по кнопке внизу страницы на страницу оформления заказа')
    @allure.description('Тест проверяет, что значение url соответствует ожидаемому значению')
    def test_button_order_footer(self, driver):
        driver.get(main_page_url)
        button_order_footer = MainPage(driver)

        assert button_order_footer.check_order_header() == 'https://qa-scooter.praktikum-services.ru/order'
