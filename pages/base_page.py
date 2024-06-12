import allure


class BasePage:

    @allure.step('Метод форматирует локатор, предоставляя возможность добавлять в конец локатора необходимое число')
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)

        return [method, locator]
