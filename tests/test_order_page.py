from conftest import *
from pages.order_page import *
from data import *
import allure


class TestCreateOrder:

    @allure.description('Тест проверяет успешное оформление заказа. Точка входа вверху страницы')
    @pytest.mark.parametrize(
        'name, surname, address, phone_number, comment',
        [
            (name_1, surname_1, address_1, phone_number_1, comment_1),
        ]
    )
    def test_create_order_header_button(self, driver, name, surname, address, phone_number, comment):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        create_order = OrderPageScooter(driver)
        create_order.check_order_header()
        create_order.check_personal_form(name, surname, address, phone_number)
        create_order.check_scooter_form(comment)
        create_order.check_submit_button_yes()

        assert create_order.check_status_order() == 'Посмотреть статус'

    @allure.description('Тест проверяет успешное оформление заказа. Точка входа внизу страницы')
    @pytest.mark.parametrize(
        'name, surname, address, phone_number, comment',
        [
            (name_2, surname_2, address_2, phone_number_2, comment_2),
        ]
    )
    def test_create_order_footer_button(self, driver, name, surname, address, phone_number, comment):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        create_order = OrderPageScooter(driver)
        create_order.check_order_footer()
        create_order.check_personal_form(name, surname, address, phone_number)
        create_order.check_scooter_form(comment)
        create_order.check_submit_button_yes()

        assert create_order.check_status_order() == 'Посмотреть статус'
