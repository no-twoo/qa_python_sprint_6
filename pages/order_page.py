from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_locators import *
import allure


class OrderPageScooter:
    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем по кнопке "Заказать" вверху страницы')
    def check_order_header(self):
        self.driver.find_element(*TestOrderLocators.create_order_button_header).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(TestOrderLocators.search_input_name))

    @allure.step('Кликаем по кнопке "Заказать" внизу страницы')
    def check_order_footer(self):
        element = self.driver.find_element(*TestOrderLocators.create_order_button_footer)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(
            TestOrderLocators.create_order_button_footer))

        self.driver.find_element(*TestOrderLocators.create_order_button_footer).click()

        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(TestOrderLocators.search_input_name))

    @allure.step('Находим и заполняем элемент Имя')
    def set_name(self, name):
        self.driver.find_element(*TestOrderLocators.search_input_name).send_keys(name)

    @allure.step('Находим и заполняем элемент Фамилия')
    def set_surname(self, surname):
        self.driver.find_element(*TestOrderLocators.search_input_surname).send_keys(surname)

    @allure.step('Находим и заполняем элемент Адрес')
    def set_address(self, address):
        self.driver.find_element(*TestOrderLocators.search_input_address).send_keys(address)

    @allure.step('Находим элемент со станциями метро и выбираем станцию')
    def set_metro(self):
        self.driver.find_element(*TestOrderLocators.search_input_metro).click()

        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            TestOrderLocators.search_button_metro_station))
        self.driver.find_element(*TestOrderLocators.search_button_metro_station).click()

    @allure.step('Находим и заполняем элемент Номер телефона')
    def set_phone_number(self, phone_number):
        self.driver.find_element(*TestOrderLocators.search_input_phone_number).send_keys(phone_number)

    @allure.step('Находим кнопку "Далее" и кликаем по ней')
    def check_button_next(self):
        self.driver.find_element(*TestOrderLocators.search_button_next).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            TestOrderLocators.search_text))

    @allure.description('Объединяем методы в шаг')
    def check_personal_form(self, name, surname, address, phone_number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro()
        self.set_phone_number(phone_number)
        self.check_button_next()

    @allure.step('Находим и заполняем поле с элементом дата доставки')
    def set_date(self):
        self.driver.find_element(*TestOrderLocators.search_input_date).click()

        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            TestOrderLocators.search_date_selector))

        self.driver.find_element(*TestOrderLocators.search_date_selector).click()

    @allure.step('Находим и заполняем поле с элементом срок аренды')
    def set_rental_days(self):
        self.driver.find_element(*TestOrderLocators.search_input_rental).click()

        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            TestOrderLocators.search_rental_selector))

        self.driver.find_element(*TestOrderLocators.search_rental_selector).click()

    @allure.step('Находим и выбираем цвет самоката')
    def set_color(self):
        self.driver.find_element(*TestOrderLocators.search_input_color).click()

    @allure.step('Находим и заполняем поле с комментарием')
    def set_comment(self, comment):
        self.driver.find_element(*TestOrderLocators.search_input_comment).send_keys(comment)

    @allure.step('Находим кнопку "Заказать" и нажимаем ее')
    def check_order(self):
        self.driver.find_element(*TestOrderLocators.search_button_order).click()

        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            TestOrderLocators.search_text_order))

    @allure.description('Объединяем методы в шаг')
    def check_scooter_form(self, comment):
        self.set_date()
        self.set_rental_days()
        self.set_color()
        self.set_comment(comment)
        self.check_order()

    @allure.step('Находим кнопку "Да" и нажимаем ее')
    def check_submit_button_yes(self):
        self.driver.find_element(*TestOrderLocators.search_button_yes).click()

        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            TestOrderLocators.search_button_completed))

    @allure.step('Находим кнопку "Просмотреть статус" и возвращаем текст из нее')
    def check_status_order(self):
        status_text = self.driver.find_element(*TestOrderLocators.search_button_completed).text
        return status_text
