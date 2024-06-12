from conftest import *
from pages.transition_dzen_page import *
import allure


class TestTransitionDzen:

    @allure.description('Тест проверяет, что заданный текст входит в url главной станицы Яндекса')
    def test_transition_dzen(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        transition_dzen = TransitionDzen(driver)
        transition_dzen.check_transition_dzen()

        assert "dzen.ru" in transition_dzen.check_main_yandex()
