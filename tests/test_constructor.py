import allure
from pages.main_page import MainPage
from data.urls import BASE_URL, FEED_URL

class TestConstructor:
    @allure.title("Переход по клику на 'Конструктор'")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_feed_button()
        main_page.click_constructor_button()
        current_url = main_page.get_current_url()
        assert current_url == BASE_URL or current_url == f"{BASE_URL}/"

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_navigate_to_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_feed_button()
        assert FEED_URL in main_page.get_current_url()

    @allure.title("Появление всплывающего окна с деталями при клике на ингредиент")
    def test_ingredient_modal_open(self, driver):
        main_page = MainPage(driver)
        main_page.click_first_ingredient()
        assert main_page.is_ingredient_modal_displayed()

    @allure.title("Закрытие всплывающего окна кликом по крестику")
    def test_ingredient_modal_close(self, driver):
        main_page = MainPage(driver)
        main_page.click_first_ingredient()
        main_page.close_ingredient_modal()
        assert main_page.is_ingredient_modal_closed()

    @allure.title("Увеличение счетчика ингредиента при добавлении в заказ")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.drag_ingredient_to_basket()
        count = main_page.get_ingredient_count()
        assert count > 0