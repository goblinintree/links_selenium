# -*- coding: UTF-8 -*-
import sys
sys.path.append("..")
from auto.driver import AutoDriver

import time

def print_test():
    print "MICCN 03 "
    pass

def exec_case(driver):
    Auto = driver
    Auto.driver_get("http://cn.made-in-china.com/prod/catlist/").show_title()
    search_input = Auto.find_element_by_xpath('//*[@id="inputWord"]')
    search_input.send_keys("LED")
    search_button = Auto.find_element_by_xpath('//*[@id="searchBtn"]')
    search_button.click()
    time.sleep(10)
    pass