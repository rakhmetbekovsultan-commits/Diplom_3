import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from pages.feed_page import FeedPage

class TestFeed:
    @allure.title("Увеличение счетчика 'Выполнено за все время' при создании заказа")
    def test_all_time_counter_increases(self, driver, create_user_and_delete):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.click_feed_button()
        count_before = feed_page.get_all_time_orders_count()

        feed_page.click_constructor_button()
        main_page.create_order_via_ui()

        main_page.click_feed_button()
        feed_page.refresh_page()
        
        WebDriverWait(driver, 15).until(lambda d: feed_page.get_all_time_orders_count() > count_before)
        count_after = feed_page.get_all_time_orders_count()
        assert count_after > count_before

    @allure.title("Увеличение счетчика 'Выполнено за сегодня' при создании заказа")
    def test_today_counter_increases(self, driver, create_user_and_delete):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.click_feed_button()
        count_before = feed_page.get_today_orders_count()

        feed_page.click_constructor_button()
        main_page.create_order_via_ui()

        main_page.click_feed_button()
        feed_page.refresh_page()

        WebDriverWait(driver, 15).until(lambda d: feed_page.get_today_orders_count() > count_before)
        count_after = feed_page.get_today_orders_count()
        assert count_after > count_before

    @allure.title("Появление номера заказа в разделе 'В работе' после оформления")
    def test_order_number_in_progress_list(self, driver, create_user_and_delete):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        # Создаем заказ через интерфейс и перехватываем его номер
        order_number = main_page.create_order_via_ui()
        
        # Переходим в ленту заказов
        main_page.click_feed_button()
        
        # Строго проверяем, что в блоке "В работе" появился именно наш номер заказа
        assert feed_page.is_order_in_progress(order_number)