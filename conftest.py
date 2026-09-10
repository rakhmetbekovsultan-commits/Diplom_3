import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from data.urls import BASE_URL, USER_REGISTER_API_URL, USER_API_URL

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
def create_user_and_delete():
    user_data = {
        "email": f"sultan_test_{requests.get('https://httpbin.org/uuid').json()['uuid'][:8]}@yandex.ru",
        "password": "Password123!",
        "name": "SultanTest"
    }
    response = requests.post(USER_REGISTER_API_URL, json=user_data)
    token = response.json().get("accessToken")

    yield user_data, token

    if token:
        requests.delete(USER_API_URL, headers={"Authorization": token})