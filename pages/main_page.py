from locators.main_locators import *
from pages.base_page import *
import allure


class MainPage(BasePage):

    @allure.step('Находим и кликаем по вопросу. Метод возвращает текстовое значения ответа на вопрос.')
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(TestMainLocators.search_question, num)
        locator_a_formatted = self.format_locators(TestMainLocators.search_answer, num)
        self.find_element_with_wait(TestMainLocators.img_scooter)
        self.scroll_to_element(TestMainLocators.search_question_8)
        self.find_element_with_wait(TestMainLocators.search_question_8)
        self.find_element_with_wait(locator_q_formatted).click()

        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Кликаем по кнопке "Заказать" вверху страницы')
    def check_order_header(self):
        self.click_to_element(TestMainLocators.create_order_button_header)

        return self.driver.current_url

    @allure.step('Кликаем по кнопке "Заказать" внизу страницы')
    def check_order_footer(self):
        self.scroll_to_element(TestMainLocators.create_order_button_footer)
        self.click_to_element(TestMainLocators.create_order_button_footer)

        return self.driver.current_url
