from time import sleep

import allure
from selenium import webdriver

@allure.feature('test_module_01')
def test_baidu(selenium):
    # driver = webdriver.Chrome()

    selenium.get("https://www.baidu.com")   # selenium即driver
    selenium.find_element_by_id('kw').send_keys('Hello')
    selenium.find_element_by_id('su').click()

