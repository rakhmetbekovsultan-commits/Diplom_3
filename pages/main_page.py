import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

HTML5_DRAG_AND_DROP_JS = """
var src = arguments[0], tgt = arguments[1];
var dataTransfer = new DataTransfer();
src.dispatchEvent(new DragEvent('dragstart', {dataTransfer: dataTransfer, bubbles: true}));
tgt.dispatchEvent(new DragEvent('drag', {dataTransfer: dataTransfer, bubbles: true}));
tgt.dispatchEvent(new DragEvent('dragover', {dataTransfer: dataTransfer, bubbles: true}));
tgt.dispatchEvent(new DragEvent('drop', {dataTransfer: dataTransfer, bubbles: true}));
src.dispatchEvent(new DragEvent('dragend', {dataTransfer: dataTransfer, bubbles: true}));
"""

class MainPage(BasePage):
    @allure.step("Клик по первому ингредиенту")
    def click_first_ingredient(self):
        self.click(MainPageLocators.INGREDIENT_CARD)

    @allure.step("Проверка отображения модального окна ингредиента")
    def is_ingredient_modal_displayed(self):
        return self.find_element(MainPageLocators.INGREDIENT_MODAL).is_displayed()

    @allure.step("Закрытие модального окна ингредиента")
    def close_ingredient_modal(self):
        self.click(MainPageLocators.INGREDIENT_MODAL_CLOSE_BUTTON)

    @allure.step("Проверка закрытия модального окна ингредиента")
    def is_ingredient_modal_closed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_MODAL)
        )

    @allure.step("Перетаскивание ингредиента в корзину конструктора")
    def drag_ingredient_to_basket(self):
        ingredient = self.find_element(MainPageLocators.BUN_INGREDIENT)
        basket = self.find_element(MainPageLocators.BURGER_CONSTRUCTOR_BASKET)
        self.execute_script(HTML5_DRAG_AND_DROP_JS, ingredient, basket)

    @allure.step("Получение значения счетчика ингредиента")
    def get_ingredient_count(self):
        element = self.find_element(MainPageLocators.BUN_INGREDIENT)
        try:
            counter_element = element.find_element(*MainPageLocators.INGREDIENT_COUNTER)
            return int(counter_element.text)
        except Exception:
            return 0

    @allure.step("Оформление заказа через интерфейс с получением его номера")
    def create_order_via_ui(self):
        self.drag_ingredient_to_basket()
        self.click(MainPageLocators.CONFIRM_ORDER_BUTTON)
        
        # Ожидаем появления модального окна с подтверждением заказа
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_ID_MODAL)
        )
        
        # Забираем точный номер заказа из модального окна (форматируем под формат ленты, например, с ведущими нулями или без)
        order_number_text = self.find_element(MainPageLocators.ORDER_NUMBER).text
        # При необходимости убираем лишние знаки, если в модалке выводится с хэшем (например, "#03482" -> "03482")
        formatted_order_number = order_number_text.strip().replace("#", "")
        
        # Закрываем модальное окно заказа
        self.click(MainPageLocators.CLOSE_ORDER_MODAL)
        WebDriverWait(self.driver, 15).until(
            EC.invisibility_of_element_located(MainPageLocators.ORDER_ID_MODAL)
        )
        return formatted_order_number