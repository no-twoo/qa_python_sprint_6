from conftest import *
import pytest

from data import *
from pages.questions_page import QuestionsPage
import allure


class TestQuestionPage:

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
        driver.get('https://qa-scooter.praktikum-services.ru/')
        question_page = QuestionsPage(driver)
        actual_result = question_page.get_answer_text(num)
        assert actual_result == result
