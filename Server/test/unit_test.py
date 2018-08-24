import selenium as sl
from selenium import webdriver


def test():
    assert 1


def test_server():
    driver_Path ="./chromedriver.exe"
    driver = webdriver.Firefox()

    driver.get("http://localhost:5000/")

    assert 'Hello World!' == driver.find_element_by_xpath('/html/body/pre').text
    
