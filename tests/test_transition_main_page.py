from conftest import *
from pages.transition_main_page import *
import allure


class TestTransitionMain:

    @allure.description('Тест проверяет, что значение возвращаемого текста соответствует ожидаемому значению')
    def test_transition_main(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/order')
        transition_main = TransitionMain(driver)
        transition_main.check_transition_main()

        assert transition_main.check_text_main() == 'Привезём его прямо к вашей двери,\nа когда накатаетесь — заберём'
