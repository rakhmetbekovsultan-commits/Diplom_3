from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators

class FeedPage(BasePage):
    def get_all_time_orders_count(self):
        return int(self.find_element(FeedPageLocators.ALL_TIME_ORDERS_COUNT).text)

    def get_today_orders_count(self):
        return int(self.find_element(FeedPageLocators.TODAY_ORDERS_COUNT).text)

    def get_in_progress_orders(self):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(FeedPageLocators.IN_PROGRESS_ORDERS_LIST)
        )
        elements = self.driver.find_elements(*FeedPageLocators.IN_PROGRESS_ORDERS_LIST)
        return [el.text for el in elements]