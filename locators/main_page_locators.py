from selenium.webdriver.common.by import By

class MainPageLocators:
    INGREDIENT_CARD = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    INGREDIENT_MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'close')]",
    )
    INGREDIENT_COUNTER = (
        By.XPATH,
        ".//p[contains(@class, 'counter_counter__num') or contains(@class, 'counter')]",
    )
    # Избавились от жесткого индекса [1], find_element автоматически берет первый элемент
    BUN_INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    BURGER_CONSTRUCTOR_BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    ORDER_ID_MODAL = (By.XPATH, "//p[contains(text(), 'идентификатор заказа')]")
    ORDER_NUMBER = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//h2[contains(@class, 'text_type_digits-large')]")
    CLOSE_ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'close')]")