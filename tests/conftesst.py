from selenium import webdriver
import pytest
from selenium.webdriver.common.devtools.v115 import browser


@pytest.fixture()
def setup():
    if browser=="chrome":
        driver = webdriver.Chrome()
        print("launching chrome browser")
    else:
        driver = webdriver.Firefox()
    return driver
