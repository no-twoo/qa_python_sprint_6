from selenium.webdriver.common.by import By


class TestTransitionLocators:
    search_button_scooter = [By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]"]
    search_main_page = [By.XPATH, ".//*[text()='Привезём его прямо к вашей двери,']"]
