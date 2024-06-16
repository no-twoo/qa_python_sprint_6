from conftest import *
from pages.order_page import *
from data import *
import allure


class TestCreateOrder:

    @allure.title('Проверка успешного оформления заказа')
    @allure.description('Тест проверяет успешное оформление заказа')
    @pytest.mark.parametrize(
        'name, surname, address, phone_number, comment',
        [
            (name_1, surname_1, address_1, phone_number_1, comment_1),
            (name_2, surname_2, address_2, phone_number_2, comment_2),
        ]
    )
    def test_create_order(self, driver, name, surname, address, phone_number, comment):
        create_order = OrderPageScooter(driver, order_page_url)
        create_order.check_personal_form(name, surname, address, phone_number)
        create_order.check_scooter_form(comment)
        create_order.check_submit_button_yes()

        assert create_order.check_status_order() == 'Посмотреть статус'

    @allure.title('Проверка редиректа на главную страницу Самоката')
    @allure.description('Тест проверяет, что значение возвращаемого текста соответствует ожидаемому значению')
    def test_transition_main(self, driver):
        transition_main = OrderPageScooter(driver, order_page_url)
        transition_main.check_transition_main()

        assert transition_main.check_text_main() == actual_text
