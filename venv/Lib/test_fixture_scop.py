# chorme path
import time
import pytest
from selenium.webdriver import Chrome
a=101

#pytest fixture
@pytest.fixture(scope="module")
def setpath():
    global driver
    path = "C:/Program Files/JetBrains/geckodriver-v0.26.0-win64/chromedriver.exe"
    driver = Chrome(executable_path=path)
    yield
    driver.close()

#@pytest.mark.sanity
#@pytest.mark.skipif(a>100,reason="don't want to execute this function")
def test_registration_valid_data(setpath):
    driver.get("https://www.testingworld.com/testing")
    driver.maximize_window()
    time.sleep(2)
    assert driver.title == "Testingworld.com"
#@pytest.mark.smoke
def test_registration_invalid_data(setpath):
    driver.get("https://www.testingworld.com/testing")
    driver.maximize_window()
    time.sleep(2)
    assert driver.current_url == "http://ww25.testingworld.com/testing"


#@pytest.mark.sanity
def test_mixregistration_data(setpath):
    driver.get("https://www.testingworld.com/testing")
    driver.maximize_window()
    time.sleep(3)