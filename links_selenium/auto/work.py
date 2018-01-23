# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
import tools
from selenium.common.exceptions import NoSuchElementException

def miccn_do_logon(driver, username, password):
    try:
        logon_flag = False
        driver.get("http://membercenter.cn.made-in-china.com/?_=1")
        time.sleep(5)
        username_element = driver.find_element_by_xpath("//*[@id=\"logonUserName\"]")
        username_element.clear()
        username_element.send_keys(username)
        password_element = driver.find_element_by_xpath("//*[@id=\"logonPassword\"]")
        password_element.send_keys(password)
        time.sleep(5)
        click_element = driver.find_element_by_xpath("//*[@id=\"micForm\"]/div/ul/li[5]/button")
        click_element.click()
        time.sleep(5)

        driver.get("http://membercenter.cn.made-in-china.com/member/main/")
        assert_element = driver.find_element_by_xpath("//*[@id=\"userName\"]")
        print assert_element.text + u"登陆成功！！"
        logon_flag = True
    except (NameError, NoSuchElementException) as Er:
        Er.message
    return logon_flag

def miccn_do_logout(driver):
    if miccn_check_logon(driver):
        try:
            logon_flag = False
            driver.get("http://membercenter.cn.made-in-china.com/logout/")
            time.sleep(10)
            logout_text_element = driver.find_element_by_xpath('//*[@id="main"]')
            print logout_text_element.text
            
        except Exception :
            print Exception.message
    print u"用户已成功登出！！"
    return driver


def miccn_check_logon(driver):
    logon_flag = True
    if not tools.contain_subString("cn.made-in-china.com", driver.current_url):
        driver.get("http://cn.made-in-china.com/")
    try:
        driver.find_element_by_xpath("//*[@id=\"userName\"]")
    except NoSuchElementException:
        # print NameError
        # print Exception
        print ">>> NoSuchElementException"
        logon_flag = False
    finally:
        if logon_flag: 
            print u"用户已登录" 
        else: 
            print u"用户未登录"
    return logon_flag

def miccn_ensure_logon(driver, username, password):
    if not miccn_check_logon(driver):
        miccn_do_logon(driver, username, password)
    return driver




def miccn_redo_logon(driver, username, password):
    print ">>>>>> ", username,password
    if miccn_check_logon(driver):
        miccn_do_logout(driver)
    miccn_do_logon(driver, username, password)
    return driver

if __name__ == "__main__":
    # 调试用
    driver = webdriver.Chrome()
    username = "yulikui2011"
    password = "654321b"
    if miccn_do_logon(driver, username, password) :
        print u">>  登陆成功..."
    print miccn_do_logout(driver)
    driver.quit()

