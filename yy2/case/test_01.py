import allure
from selenium import webdriver
import time

@allure.feature('test_module_01')
def test_001(browser):

    browser.get("https://www.baidu.com/")
    time.sleep(2)
    t = browser.title
    assert t == "百度一下，你知道"