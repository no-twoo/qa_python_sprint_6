from locators.order_locators import *
from pages.base_page import *
import allure


class OrderPageScooter(BasePage):

    @allure.step('Находим и заполняем элемент Имя')
    def set_name(self, name):
        self.add_text_to_element(TestOrderLocators.search_input_name, name)

    @allure.step('Находим и заполняем элемент Фамилия')
    def set_surname(self, surname):
        self.add_text_to_element(TestOrderLocators.search_input_surname, surname)

    @allure.step('Находим и заполняем элемент Адрес')
    def set_address(self, address):
        self.add_text_to_element(TestOrderLocators.search_input_address, address)

    @allure.step('Находим элемент со станциями метро и выбираем станцию')
    def set_metro(self):
        self.click_to_element(TestOrderLocators.search_input_metro)
        self.click_to_element(TestOrderLocators.search_button_metro_station)

    @allure.step('Находим и заполняем элемент Номер телефона')
    def set_phone_number(self, phone_number):
        self.add_text_to_element(TestOrderLocators.search_input_phone_number, phone_number)

    @allure.step('Находим кнопку "Далее" и кликаем по ней')
    def check_button_next(self):
        self.click_to_element(TestOrderLocators.search_button_next)

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
        self.click_to_element(TestOrderLocators.search_input_date)
        self.click_to_element(TestOrderLocators.search_date_selector)

    @allure.step('Находим и заполняем поле с элементом срок аренды')
    def set_rental_days(self):
        self.click_to_element(TestOrderLocators.search_input_rental)
        self.click_to_element(TestOrderLocators.search_rental_selector)

    @allure.step('Находим и выбираем цвет самоката')
    def set_color(self):
        self.click_to_element(TestOrderLocators.search_input_color)

    @allure.step('Находим и заполняем поле с комментарием')
    def set_comment(self, comment):
        self.add_text_to_element(TestOrderLocators.search_input_comment, comment)

    @allure.step('Находим кнопку "Заказать" и нажимаем ее')
    def check_order(self):
        self.click_to_element(TestOrderLocators.search_button_order)

    @allure.description('Объединяем методы в шаг')
    def check_scooter_form(self, comment):
        self.set_date()
        self.set_rental_days()
        self.set_color()
        self.set_comment(comment)
        self.check_order()

    @allure.step('Находим кнопку "Да" и нажимаем ее')
    def check_submit_button_yes(self):
        self.click_to_element(TestOrderLocators.search_button_yes)

    @allure.step('Находим кнопку "Просмотреть статус" и возвращаем текст из нее')
    def check_status_order(self):
        status_text = self.get_text_from_element(TestOrderLocators.search_button_completed)

        return status_text

    @allure.step('Находим логотип Самоката и кликаем по нему')
    def check_transition_main(self):
        self.click_to_element(TestOrderLocators.search_button_scooter)

    @allure.step('Метод возвращает текстовое значение с главной страницы')
    def check_text_main(self):
        text_main = self.get_text_from_element(TestOrderLocators.search_main_page)

        return text_main
