import selenium as sl
from selenium import webdriver


def test():
    assert 1


def test_server():
    driver = webdriver.Chrome()
    driver.get('http://localhost:5000')

    assert driver.find_element_by_xpath('/html/body').text == "Hello World!"
    
    driver.get('http://localhost:5000/project')

    assert driver.find_element_by_xpath('/html/body').text == 'This is FWD Project'
