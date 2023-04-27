from selenium import webdriver
import pytest


@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()