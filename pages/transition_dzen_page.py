from locators.dzen_locators import *
from pages.base_page import *
import allure


class TransitionDzen(BasePage):

    @allure.step('Находим логотип Яндекса и кликаем по нему')
    def check_transition_dzen(self):
        self.click_to_element(TestDzenLocators.search_button_yandex)

    @allure.step('Переходим на страницу Яндекса и возвращаем значение url')
    def check_main_yandex(self):
        self.switch_to_page()
        self.find_element_with_wait(TestDzenLocators.search_main_yandex)

        return self.current_url_page()
