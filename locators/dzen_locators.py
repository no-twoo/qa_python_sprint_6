from selenium.webdriver.common.by import By


class TestDzenLocators:
    search_button_yandex = [By.XPATH, ".//*[@alt='Yandex']"]
    search_main_yandex = [By.XPATH, ".//*[@data-testid='logo']"]
