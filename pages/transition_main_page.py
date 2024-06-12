from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.transition_main_locators import *
import allure


class TransitionMain:

    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Находим логотип Самоката и кликаем по нему')
    def check_transition_main(self):
        self.driver.find_element(*TestTransitionLocators.search_button_scooter).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            TestTransitionLocators.search_main_page))

    @allure.step('Метод возвращает текстовое значение с главной страницы')
    def check_text_main(self):
        text_main = self.driver.find_element(*TestTransitionLocators.search_main_page).text
        return text_main
