import pytest
import requests
from selenium import webdriver
from data.urls import BASE_URL, USER_REGISTER_API_URL, USER_API_URL
from data.helpers import Helpers

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver_instance = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver_instance = webdriver.Firefox(options=options)
    
    driver_instance.get(BASE_URL)
    yield driver_instance
    driver_instance.quit()

@pytest.fixture
def create_user_and_delete(driver): # передаем driver внутрь фикстуры
    user_data = {
        "email": Helpers.generate_random_email(),
        "password": "Password123!",
        "name": "SultanTest"
    }
    response = requests.post(USER_REGISTER_API_URL, json=user_data)
    response_json = response.json()
    token = response_json.get("accessToken")
    refresh_token = response_json.get("refreshToken")

    # Авторизуем пользователя в браузере через localStorage, чтобы интерфейс "видел" сессию
    if token:
        driver.get(BASE_URL)
        driver.execute_script(
            f"window.localStorage.setItem('accessToken', '{token}');"
            f"window.localStorage.setItem('refreshToken', '{refresh_token}');"
        )
        driver.refresh()

    yield user_data, token

    if token:
        requests.delete(USER_API_URL, headers={"Authorization": token})