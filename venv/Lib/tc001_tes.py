# chorme path
import time
import pytest
from selenium.webdriver import Chrome
a=101
@pytest.mark.skipif(a>100,reason="don't want to execute this function")
def test_registration_valid_data():
    path = "C:/Program Files/JetBrains/geckodriver-v0.26.0-win64/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.testingworld.com/testing")
    driver.maximize_window()
    time.sleep(15)

def test_registration_invalid_data():
    path = "C:/Program Files/JetBrains/geckodriver-v0.26.0-win64/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.testingworld.com/testing")
    driver.maximize_window()
    time.sleep(3)
