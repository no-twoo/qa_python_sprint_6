from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.dzen_locators import *
import allure


class TransitionDzen:

    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Находим логотип Яндекса и кликаем по нему')
    def check_transition_dzen(self):
        self.driver.find_element(*TestDzenLocators.search_button_yandex).click()

    @allure.step('Переходим на страницу Яндекса и возвращаем значение url')
    def check_main_yandex(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(
            TestDzenLocators.search_main_yandex))
        current_url = self.driver.current_url
        return current_url
