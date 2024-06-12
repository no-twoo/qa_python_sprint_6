from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.questions_locators import *
from pages.base_page import *
import allure


class QuestionsPage(BasePage):

    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Находим и кликаем по вопросу. Метод возвращает текстовое значения ответа на вопрос.')
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(TestQuestionLocators.search_question, num)
        locator_a_formatted = self.format_locators(TestQuestionLocators.search_answer, num)
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(
            TestQuestionLocators.img_scooter))
        element = self.driver.find_element(*TestQuestionLocators.search_question_8)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(
            TestQuestionLocators.search_question_8))

        self.driver.find_element(*locator_q_formatted).click()
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(
            locator_a_formatted))

        return self.driver.find_element(*locator_a_formatted).text
