from selenium.webdriver.common.by import By

class FeedPageLocators:
    ALL_TIME_ORDERS_COUNT = (By.XPATH, "//p[contains(text(),'Выполнено за все время')]/following-sibling::p")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")
    IN_PROGRESS_ORDERS_LIST = (By.XPATH, "//ul[contains(@class, 'orderListReady')]//li")