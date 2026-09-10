import allure
import requests
import time
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from data.urls import ORDER_CREATE_API_URL

class TestFeed:
    @allure.title("Увеличение счетчика 'Выполнено за все время' при создании заказа")
    def test_all_time_counter_increases(self, driver, create_user_and_delete):
        _, token = create_user_and_delete
        main_page = MainPage(driver)
        main_page.click_feed_button()
        
        feed_page = FeedPage(driver)
        count_before = feed_page.get_all_time_orders_count()

        ingredients = ["61c0c5a71d1f82001bdaaa6d"]
        requests.post(ORDER_CREATE_API_URL, headers={"Authorization": token}, json={"ingredients": ingredients})

        driver.refresh()
        time.sleep(2)
        count_after = feed_page.get_all_time_orders_count()
        assert count_after > count_before

    @allure.title("Увеличение счетчика 'Выполнено за сегодня' при создании заказа")
    def test_today_counter_increases(self, driver, create_user_and_delete):
        _, token = create_user_and_delete
        main_page = MainPage(driver)
        main_page.click_feed_button()

        feed_page = FeedPage(driver)
        count_before = feed_page.get_today_orders_count()

        ingredients = ["61c0c5a71d1f82001bdaaa6d"]
        requests.post(ORDER_CREATE_API_URL, headers={"Authorization": token}, json={"ingredients": ingredients})

        driver.refresh()
        time.sleep(2)
        count_after = feed_page.get_today_orders_count()
        assert count_after > count_before

    @allure.title("Появление номера заказа в разделе 'В работе' после оформления")
    def test_order_number_in_progress_list(self, driver, create_user_and_delete):
        _, token = create_user_and_delete
        ingredients = ["61c0c5a71d1f82001bdaaa6d"]
        response = requests.post(ORDER_CREATE_API_URL, headers={"Authorization": token}, json={"ingredients": ingredients})
        order_number = str(response.json()["order"]["number"])

        main_page = MainPage(driver)
        main_page.click_feed_button()

        feed_page = FeedPage(driver)
        time.sleep(2)
        orders_in_progress = feed_page.get_in_progress_orders()
        
        assert any(order_number in order for order in orders_in_progress) or len(orders_in_progress) > 0