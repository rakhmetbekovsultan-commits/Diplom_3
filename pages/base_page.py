import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элемента с ожиданием присутствия")
    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    @allure.step("Клик по элементу")
    def click(self, locator, time=15):
        element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получение текущего URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Обновление страницы")
    def refresh_page(self):
        self.driver.refresh()

    @allure.step("Выполнение JavaScript скрипта")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor_button(self):
        self.click(BasePageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик по кнопке 'Лента Заказов'")
    def click_feed_button(self):
        self.click(BasePageLocators.FEED_BUTTON)

    @allure.step("Ожидание присутствия всех элементов")
    def find_elements(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator)
        )

    @allure.step("Ожидание невидимости элемента")
    def wait_for_invisibility(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Ожидание выполнения произвольного условия")
    def wait_for_condition(self, condition_func, time=15):
        return WebDriverWait(self.driver, time).until(condition_func)