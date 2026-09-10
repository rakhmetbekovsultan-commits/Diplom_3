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
    BUN_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    BURGER_CONSTRUCTOR_BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")