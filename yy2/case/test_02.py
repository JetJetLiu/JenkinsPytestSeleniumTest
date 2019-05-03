import allure
from selenium import webdriver
import time

@allure.feature('test_module_02')
def test_002(browser):

    browser.get("https://www.baidu.com/")
    time.sleep(2)
    t = browser.title
    assert "百度一下" in t