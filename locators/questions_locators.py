from selenium.webdriver.common.by import By


class TestQuestionLocators:
    img_scooter = [By.XPATH, ".//*[@alt='Scooter blueprint']"]
    search_question = [By.XPATH, ".//div[@id='accordion__heading-{}']"]
    search_answer = [By.XPATH, ".//div[@id='accordion__panel-{}']"]
    search_question_8 = [By.XPATH, ".//div[@id='accordion__heading-7']"]
