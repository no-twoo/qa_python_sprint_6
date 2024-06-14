from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:

    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод форматирует локатор, предоставляя возможность добавлять в конец локатора необходимое число')
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)

        return [method, locator]

    @allure.step('Ожидаем и находим элемент')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(
            locator))

        return self.driver.find_element(*locator)

    @allure.step('Кликаем по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 60).until(expected_conditions.element_to_be_clickable(
            locator))
        self.driver.find_element(*locator).click()

    @allure.step('Добавляем текст в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Возвращаем текст из элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Скролим страницу до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
