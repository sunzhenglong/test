# !/usr/bin/env python
# -*- coding:utf-8 -*-
# from appium import webdriver
from time import sleep
# import yaml
# with open(file="F:\QQ\element\login.yaml",mode="r",encoding="utf-8") as fb:
#     el = yaml.load(fb,Loader=yaml.FullLoader)
#     print(el)
# d = {
#   "platformName": "Android",
#   "platformVersion": "5.1.1",
#   "deviceName": "emulator-5554",
#   "appPackage": "com.tencent.mobileqq",
#   "appActivity": ".activity.SplashActivity",
#   "noReset": "true",
#   'unicodeKeyboard': "true",
#   'resetKeyboard': "true"
# }
# dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
# sleep(7)
# dr.find_element_by_xpath(el["tou"]).click()
# sleep(2)
# dr.find_element_by_id(el["seting"]).click()
# sleep(2)
# dr.find_element_by_id(el["zhanghao"]).click()
# sleep(2)
# dr.find_element_by_id(el["out"]).click()
# sleep(2)
# dr.find_element_by_id(el["sure"]).click()
# sleep(2)
# b = dr.find_element_by_accessibility_id(el["xyh"]).text
# print(b)
# if b == "用户注册":
#     print("退出成功")


# 类方法写
# class A(object):
#     def __init__(self):
#         with open(file="F:\QQ\element\login.yaml",mode="r",encoding="utf-8") as fb:
#             el = yaml.load(fb,Loader=yaml.FullLoader)
#             print(el)
#         d = {
#           "platformName": "Android",
#           "platformVersion": "5.1.1",
#           "deviceName": "emulator-5554",
#           "appPackage": "com.tencent.mobileqq",
#           "appActivity": ".activity.SplashActivity",
#           "noReset": "true",
#           'unicodeKeyboard': "true",
#           'resetKeyboard': "true"
#         }
#         dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
#     def aa(self):
#             sleep(7)
#             dr.find_element_by_xpath(el["tou"]).click()
#             sleep(2)
#             dr.find_element_by_id(el["seting"]).click()
#             sleep(2)
#             dr.find_element_by_id(el["zhanghao"]).click()
#             sleep(2)
#             dr.find_element_by_id(el["out"]).click()
#             sleep(2)
#             dr.find_element_by_id(el["sure"]).click()
#             sleep(2)
#             b = dr.find_element_by_accessibility_id(el["xyh"]).text
#             print(b)
#             if b == "用户注册":
#                 print("退出成功")
# c = A()
# c.aa()

# 使用conftest
# def test_1(cl):
#     el,dr = cl
#     dr.find_element_by_xpath(el["tou"]).click()
#     sleep(2)
#     dr.find_element_by_id(el["seting"]).click()
#     sleep(2)
#     dr.find_element_by_id(el["zhanghao"]).click()
#     sleep(2)
#     dr.find_element_by_id(el["out"]).click()
#     sleep(2)
#     dr.find_element_by_id(el["sure"]).click()
#     sleep(2)
#     b = dr.find_element_by_accessibility_id(el["xyh"]).text
#     print(b)
#     assert b == "用户注册"


import pytest
from until.readdata import g
from until.phlog import get_logger
log = get_logger(filename="test_01.py")
# from until.ciliu import hd
@pytest.mark.parametrize("y1,y2",g)
def test_3(y1,y2,cl):
        el,dr = cl
        # #清空
        # dr.find_element_by_accessibility_id(el["dl"]).clear()
        # #账号
        # sleep(1)
        # dr.find_element_by_accessibility_id(el["dl"]).send_keys(y1)
        # #日志
        # log.info(f"账号是{y1}")
        # sleep(1)
        # # 清空
        # dr.find_element_by_id(el["pwd"]).clear()
        # sleep(1)
        # # 密码
        # dr.find_element_by_id(el["pwd"]).send_keys(y2)
        # #日志
        # log.info(f"密码是{y2}")
        # sleep(1)
        # dr.find_element_by_id(el["sures"]).click()


#         sleep(6)
        # from selenium.common.exceptions import NoSuchElementException
        # from selenium.common.exceptions import InvalidElementStateException
        # try:
        #     f = dr.find_element_by_accessibility_id("新用户注册").text
        #     assert f == "用户注册"
        # except:
        #     h = dr.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn").text
        #     assert h == "确定"
        # try:
        #     f = dr.find_element_by_id("com.tencent.mobileqq:id/ivTitleName").text
        #     assert f == "消息"
        # except:
        #     pass
        # try:
        #     dr.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()  # 捕获登陆失败弹框确认
        # except:
        #     sleep(1)
        #     try:
        #         dr.find_element_by_id('com.tencent.mobileqq:id/ivTitleName').text == '消息'  # 捕获登陆成功信息
        #     except:
        #         assert dr.find_element_by_accessibility_id(el['newuser']).text == '用户注册'  # 断言错误账号密码登陆失败（无弹框）
        #     else:
        #         assert dr.find_element_by_id('com.tencent.mobileqq:id/ivTitleName').text == '消息'  # 断言正确账号登陆成功
        # else:
        #     sleep(2)
        #     assert dr.find_element_by_accessibility_id(el['newuser']).text == '用户注册'  # 断言错误账号登陆失败（有弹框）

