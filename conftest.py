# фикстура для открытия и закрытия браузера
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service # as ChromeService

@pytest.fixture(scope="function")
def driver():
    print("Start browser")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()