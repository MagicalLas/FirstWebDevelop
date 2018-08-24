import selenium as sl
from selenium import webdriver


def test():
    assert 1


def test_server():
    driver = webdriver.Chrome()
    driver.get('http://localhost')
    assert 1