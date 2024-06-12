from selenium.webdriver.common.by import By


class TestOrderLocators:
    create_order_button_header = [By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"]
    create_order_button_footer = [By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"]

    search_input_name = [By.XPATH, ".//*[@placeholder='* Имя']"]
    search_input_surname = [By.XPATH, ".//*[@placeholder='* Фамилия']"]
    search_input_address = [By.XPATH, ".//*[@placeholder='* Адрес: куда привезти заказ']"]
    search_input_metro = [By.XPATH, ".//*[@placeholder='* Станция метро']"]
    search_button_metro_station = [By.XPATH, ".//button[@value='3']"]
    search_input_phone_number = [By.XPATH, ".//*[@placeholder='* Телефон: на него позвонит курьер']"]
    search_button_next = [By.XPATH, ".//button[text()='Далее']"]
    search_text = [By.XPATH, ".//*[text()='Про аренду']"]

    search_input_date = [By.XPATH, ".//*[@placeholder='* Когда привезти самокат']"]
    search_date_selector = [By.XPATH, ".//*[@aria-label='Choose воскресенье, 16-е июня 2024 г.']"]
    search_input_rental = [By.XPATH, ".//*[text()='* Срок аренды']"]
    search_rental_selector = [By.XPATH, ".//*[@class='Dropdown-menu']/div[text()='трое суток']"]
    search_input_color = [By.XPATH, ".//input[@id='black']"]
    search_input_comment = [By.XPATH, ".//*[@placeholder='Комментарий для курьера']"]
    search_button_order = [By.XPATH, ".//button[contains(@class, 'Button_Middle')][text()='Заказать']"]

    search_text_order = [By.XPATH, ".//div[text()='Хотите оформить заказ?']"]
    search_button_yes = [By.XPATH, ".//button[text()='Да']"]

    search_button_completed = [By.XPATH, ".//button[text()='Посмотреть статус']"]
