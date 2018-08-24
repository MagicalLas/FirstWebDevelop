import selenium as sl
from selenium import webdriver


def test():
    assert 1


def test_server():
    driver = webdriver.Firefox()
    driver.get('https://naver.com/')
    assert 1