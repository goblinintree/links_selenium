# -*- coding: UTF-8 -*-
from auto.pre import get_type_driver
from auto.pre import chose_driver
from selenium import webdriver
import pictools
import os


def prepDriver(driver_type="chrome"):
    if "chrome" == driver_type:
        PrepDriver = chose_driver("chrome")
        driver = PrepDriver()
    elif "mx" == driver_type:
        from selenium.webdriver.chrome.options import Options
        #360极速浏览器（基于chrome）
        browser_url = r'D:\apply\browers\Maxthon5\Bin\Maxthon.exe'
        chrome_options = Options()
        chrome_options.binary_location = browser_url
        PrepDriver = chose_driver("chrome")
        driver = PrepDriver(chrome_options=chrome_options)
    elif "ff" == driver_type:
        PrepDriver = chose_driver("ff")
        driver = PrepDriver()
    elif "ie" == driver_type:
        PrepDriver = chose_driver("ie")
        driver = PrepDriver()
    elif "chrome" == driver_type:
        PrepDriver = chose_driver("chrome")
        driver = PrepDriver()
    return driver


class AutoDriver(object):
    driver = None
    __driver_type = ""
    __instance = None

    def __init__(self, driver_type):
        print 444444
        print "__instance  ", AutoDriver.__driver_type
        if not AutoDriver.__driver_type:
            AutoDriver.__driver_type = driver_type
            self.driver = prepDriver(driver_type)
            print 555555
            # 调试使用
            # self.driver = webdriver.Chrome()
            
    def __new__(cls,*args, **kwd):
        print "111111"
        print args
        if (AutoDriver.__instance is None):
            print "222222"
            AutoDriver.__instance=object.__new__(cls,*args,**kwd)
            print "3333333"
        return AutoDriver.__instance

    def driver_get(self, url):
        self.driver.get(url)
        return self

    def show_title(self):
        print self.driver.title
        return self

    def driver_quit(self):
        self.driver.quit()
        self.driver = None
        return self

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def driver_save_screenshot(self, file_name):
        file_path ="Screenshots"
        self.driver.save_screenshot(os.path.join(file_path,file_name))
        return self

    def driver_save_screenshot_merge(self, file_name):
        file_path ="Screenshots"
        pictools.capture(self.driver, file_name)
        return self

    def driver_save_screenshot_canvas(self, file_name):
        """
        基于浏览器HTML5之canvas绘制的全屏截图，
        TODO
        """
        file_path ="Screenshots"
        pictools.capture(self.driver, file_name)
        return self

    def driver_save_screenshot_lazy(self, file_name):
        """
        基于浏览器JS滚屏的全屏截图，
        """
        file_path ="Screenshots"
        pictools.capture_lazy(self.driver, file_name)
        return self

    def driver_init(self, driver_type):
        self.driver_type = driver_type
        self.driver = prepDriver(driver_type)
        return self

    def driver_upate(self, driver):
        self.driver_type = "UPDATE"
        self.driver = driver
        return self
    pass

