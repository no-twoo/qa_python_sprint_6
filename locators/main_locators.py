from selenium.webdriver.common.by import By


class TestMainLocators:
    create_order_button_header = [By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"]
    create_order_button_footer = [By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"]

    img_scooter = [By.XPATH, ".//*[@alt='Scooter blueprint']"]
    search_question = [By.XPATH, ".//div[@id='accordion__heading-{}']"]
    search_answer = [By.XPATH, ".//div[@id='accordion__panel-{}']"]
    search_question_8 = [By.XPATH, ".//div[@id='accordion__heading-7']"]
