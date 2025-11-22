import pytest
from selenium import webdriver

@pytest.fixture
def set_up():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()

def test_form_fill(set_up):
    driver = set_up
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.find_element(By.)


