import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators

class FeedPage(BasePage):
    @allure.step("Получение значения счетчика 'Выполнено за все время'")
    def get_all_time_orders_count(self):
        return int(self.find_element(FeedPageLocators.ALL_TIME_ORDERS_COUNT).text)

    @allure.step("Получение значения счетчика 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        return int(self.find_element(FeedPageLocators.TODAY_ORDERS_COUNT).text)

    @allure.step("Ожидание увеличения счетчика 'Выполнено за все время'")
    def wait_for_all_time_orders_to_increase(self, count_before):
        return self.wait_for_condition(
            lambda d: self.get_all_time_orders_count() > count_before
        )

    @allure.step("Ожидание увеличения счетчика 'Выполнено за сегодня'")
    def wait_for_today_orders_to_increase(self, count_before):
        return self.wait_for_condition(
            lambda d: self.get_today_orders_count() > count_before
        )

    @allure.step("Ожидание и проверка появления номера заказа в разделе 'В работе'")
    def is_order_in_progress(self, order_number):
        clean_order_number = order_number.strip().replace("#", "").lstrip("0")
        try:
            return self.wait_for_condition(
                lambda d: any(
                    clean_order_number in el.text.replace("#", "").lstrip("0") 
                    for el in self.find_elements(FeedPageLocators.IN_PROGRESS_ORDERS_LIST)
                ),
                time=20  # Увеличили таймаут
            )
        except Exception:
            return False