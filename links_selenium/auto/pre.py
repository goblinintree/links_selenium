# -*- coding: UTF-8 -*-
import os

from selenium import webdriver

def get_type_driver(driver_type="chrome", profile=""):
    TypeDriver = None
    print driver_type
    if "chrome" == driver_type:
        print 1
        from selenium.webdriver.chrome.webdriver import WebDriver as Chrome  # noqa
        TypeDriver = type('TypeDriver', (Chrome,), {})
        print TypeDriver
        # TypeDriver.get('https://www.baidu.com')
        # self.driver = webdriver.Chrome()  #调用chrome浏览器
    elif "ff" == driver_type:
        print 2
        from selenium.webdriver.firefox.webdriver import WebDriver as Firefox  # noqa
        TypeDriver = type('TypeDriver', (Firefox,), {"profile":profile})
        # self.driver = webdriver.Firefox()  #调用Firefox浏览器
    elif "ie" == driver_type:
        print 3
        from selenium.webdriver.ie.webdriver import WebDriver as Ie  # noqa
        TypeDriver = type('TypeDriver', (Ie,), {})
        # self.driver = webdriver.Ie()  #调用InternetExplorer浏览器
    return TypeDriver


def chose_driver(driver_type="chrome"):
    if "chrome" == driver_type:
        from selenium.webdriver.chrome.webdriver import WebDriver as Chrome  # noqa
        class TypeDriver(Chrome):
            pass
        return TypeDriver
    elif "ff" == driver_type:
        from selenium.webdriver.firefox.webdriver import WebDriver as Firefox  # noqa
        class TypeDriver(Firefox):
            pass
        return TypeDriver
    elif "ie" == driver_type:
        from selenium.webdriver.ie.webdriver import WebDriver as Ie  # noqa
        class TypeDriver(Ie):
            pass
        return TypeDriver
    else:
        from selenium.webdriver.chrome.webdriver import WebDriver as Chrome  # noqa
        class TypeDriver(Chrome):
            pass
        return TypeDriver


if __name__ == "__main__":
    PrepDriver = get_type_driver('chrome')
    driver = PrepDriver()
    print PrepDriver
