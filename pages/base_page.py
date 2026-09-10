from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def click(self, locator, time=15):
        element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    def click_constructor_button(self):
        self.click(BasePageLocators.CONSTRUCTOR_BUTTON)

    def click_feed_button(self):
        self.click(BasePageLocators.FEED_BUTTON)