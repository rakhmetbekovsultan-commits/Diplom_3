from selenium.webdriver.common.by import By

class BasePageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")