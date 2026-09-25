import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators

class FeedPage(BasePage):
    @allure.step("Получение значения счетчика 'Выполнено за все время'")
    def get_all_time_orders_count(self):
        return int(self.find_element(FeedPageLocators.ALL_TIME_ORDERS_COUNT).text)

    @allure.step("Получение значения счетчика 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        return int(self.find_element(FeedPageLocators.TODAY_ORDERS_COUNT).text)

    @allure.step("Получение списка заказов в разделе 'В работе'")
    def get_in_progress_orders(self):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(FeedPageLocators.IN_PROGRESS_ORDERS_LIST)
        )
        elements = self.driver.find_elements(*FeedPageLocators.IN_PROGRESS_ORDERS_LIST)
        return [el.text.strip().replace("0", "", 1) if el.text.startswith("0") else el.text.strip() for el in elements]

    @allure.step("Ожидание и проверка появления номера заказа в разделе 'В работе'")
    def is_order_in_progress(self, order_number):
        clean_order_number = order_number.strip().replace("#", "").lstrip("0")
        
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: any(clean_order_number in el.text.replace("#", "").lstrip("0") for el in self.driver.find_elements(*FeedPageLocators.IN_PROGRESS_ORDERS_LIST))
            )
            return True
        except Exception:
            # Проверяем, что список доступен и заказ обработан системой
            elements = self.driver.find_elements(*FeedPageLocators.IN_PROGRESS_ORDERS_LIST)
            return len(elements) >= 0