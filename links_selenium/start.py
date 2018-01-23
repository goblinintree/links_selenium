# -*- coding: UTF-8 -*-

from selenium import webdriver
from auto.driver import AutoDriver
from auto.driver import get_type_driver
from auto import work
from xls import xls
from svn import svnclient
import os

def check_url_xls(workbook, Auto):
    count = 0
    for m_n_url in xls.xls_url_generator(workbook=workbook):
        count = count + 1
        # moudle    name    url    member
        print ">>>  ", (m_n_url["moudle"] +"___"+ m_n_url["name"] ).encode("GB2312","ignore") ,  m_n_url["member"]
        try:
            member = m_n_url["member"]
            if int(member) > 0:
                xls_member = xls.xls_member_dict(workbook=workbook, member=member)
                work.miccn_redo_logon(Auto.driver, xls_member["username"], xls_member["password"])
            Auto.driver_get(m_n_url["url"]).show_title()
        except UnicodeEncodeError:
            print UnicodeEncodeError.encoding
            file_name = m_n_url["moudle"] +"___"+ m_n_url["name"]+".png"
            Auto.driver_save_screenshot(file_name)
        finally:
            Auto.driver_quit()
            print "*" * 50

def check_yewu_xls(workbook, Auto):
    count = 0
    print workbook
    for m_n_yewu in xls.xls_yewu_generator(workbook=workbook):
        count = count + 1
        # moudle    name    url    member
        print ">>>  ", (m_n_yewu["moudle"] +"___"+ m_n_yewu["name"] ).encode("GB2312","ignore") ,  m_n_yewu["member"]
        try:
            member = m_n_yewu["member"]
            if int(member) > 0:
                xls_member = xls.xls_member_dict(workbook=workbook, member=member)
                work.miccn_redo_logon(Auto.driver, xls_member["username"], xls_member["password"])
            exec_script(m_n_yewu["yewu"], Auto)
        except UnicodeEncodeError:
            print UnicodeEncodeError.encoding
            file_name = m_n_yewu["moudle"] +"___"+ m_n_yewu["name"]+".png"
            Auto.driver_save_screenshot(file_name)
        finally:
            print "*" * 50

def exec_script(moudle_script, Auto):
    #  script\test01.py 
    m = __import__(moudle_script, fromlist=True)
    print m
    if hasattr(m,"exec_case"):  # 判断在commons模块中是否存在inp这个字符串
        target_func = getattr(m,"exec_case")  # 获取inp的引用
        target_func(Auto)  # 执行

    else:
        print(u"404, CASE ERROR!!" )
    pass

def initcode():
    print svnclient.svn_export()
    pass

if __name__ == "__main__":
    try:
        initcode()
    except (IOError):
        print "ERROR!!"
        pass
    try:
        # u"打开Excel文件"
        xls_file = u'file\\cases\\case01.xls'
        print ">>> ",os.path.realpath(__file__)
        Auto = AutoDriver("chrome")
        workbook = xls.get_workbook(xls_file=xls_file)
        # u"检查xls文件中的URL业务"
        # check_url_xls(workbook, Auto)
        # u"检查xls文件中的业务流程"
        check_yewu_xls(workbook, Auto)
    # except (IOError) as e:
    #     print "ERROR!!"
    #     print e
    #     pass
    finally:
        Auto.driver_quit()
