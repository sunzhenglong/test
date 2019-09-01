# !/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
# 清理测试环境的一个机制
# 第一步：在用例执行之前进行环境清理
# 第二步：在用例执行之后，进行环境的清理
#1. 脚本级别的清理
# setup_module    用例执行之前的
# teardown_module   用例执行之后
# module:本脚本所有的用例执行前，后均执行一次

# import pytest
# def setup_module():
#     print("所有用例执行之前执行一次")
# def test_1():
#     print("用例1执行")
# def test_2():
#     print("用例2执行")
# def test_3():
#     print("用例3执行")
# def teardown_module():
#     print("用例执行之后")

# setup_function:每个测试用例运行之前都要执行一次
# teardown_function:每个测试用例运行之后都要执行一次
# def setup_function():
#     print("每个用例执行之前执行一次")
# def test_1():
#     print("用例1执行")
# def test_2():
#     print("用例2执行")
# def test_3():
#     print("用例3执行")
# def teardown_function():
#     print("每个用例执行之后")

# setup_teardown 在类的范围内使用
# class Test_one(object):
#     def setup(self):
#         print("执行setup")
#     def teardown(self):
#         print("执行teardown")
#     def test_4(self):
#         print("用例执行4")
#     def test_5(self):
#         print("用例5执行")
#     def test_6(self):
#         print("用例6执行")
# setup --->  每个测试用例执行之前运行一次
# teardown --->  每个测试用例执行之后执行一次

# setup_class ---> 类中的所有测试用例执行前运行一次
# teardown_class ----> 类中的所有测试用例执行后运行一次
# class Test_one(object):
#     def setup_class(self):
#         print("执行setup")
# #     def teardown_class(self):
# #         print("执行teardown")
# #     def test_4(self):
# #         print("用例执行4")
# #     def test_5(self):
# #         print("用例5执行")
# #     def test_6(self):
# #         print("用例6执行")

# setup_method,teardown_method ---> 方法级别,每个测试用例运行之前/后执行一次
# class Test_one(object):
#     def setup_method(self):
#         print("执行setup_method")
#     def teardown_method(self):
#         print("执行teardown_method")
#     def test_4(self):
#         print("用例执行4")
#     def test_5(self):
#         print("用例5执行")
#     def test_6(self):
#         print("用例6执行")

# 测试夹具fixture
# @pytest.fixture()
# 1.scope:装饰器的作用范围
#     a.function  方法级别的/函数级别的
#     b.class  类级别
#     c.moudle  脚本级别的：脚本级别的，所有测试用例执行之前，之后运行一次
#     d.packages  包级别/目录级别
#     e.session  会话级别的
#
# @pytest.fixture()
# def login():
#         print("login函数开始执行")
# def test_1(login):
#         print("执行用例1")
# def test_2(login):
#         print("执行用例2")
# def test_3(login):
#         print("执行用例3")


# 类方法写：
# class Testtwo(object):
#     @pytest.fixture(scope="class")
#     def login(self):
#             print("login函数开始执行")
#     def test_1(self):
#             print("执行用例1")
#     def test_2(self,login):
#             print("执行用例2")
#     def test_3(self):
#             print("执行用例3")

# import pytest
# 8.13
# module:脚本级别的，所有测试用例执行之前运行一次
# @pytest.fixture(scope="module")
# def start():
#     print("所有用例执行之前运行一次")
# # @pytest.fixture(scope="module")
# # def closs():
# #     print("所有用例执行之前运行一次")
# def test_01():
#     print(1)
# def test_02():
#     print(2)
# def test_03(start):
#     print(3)

# conftest.py
# python文件，存放公共方法的/函数,必须放在当前测试用例所在目录下面
# @pytest.fixture(a)
# def clean():
#     print("当账号密码输入错误，执行删除数据的操作")
# def test_1():
#     print("输入账号，密码")
# def test_2(clean):
#     print("输入账号，密码")
# def test_3(clean):
#     print("输入账号，密码")
# def test_4(clean):
#     print("输入账号，密码")
# def test_5(clean):
#     print("输入账号，密码")

# conftest作用
# def test_1():
#     print("输入账号，密码")
# def test_2(clean):
#     print("输入账号，密码")
# def test_3(clean):
#     print("输入账号，密码")

"""
参数化----》向测试用例中传入参数的过程

"""
# 1.传一个参数
d = [1,2,3,4,5,6,7]
@pytest.fixture(scope="function",params=d)
def read_data(request):
    """
    request固定格式
    request.param:固定写法
    :param request:
    :return:
    """
    print(f"当前的传入的参数值是{request.param}")
    return request.param
def test_1(read_data):
    t = read_data    #实际结果
    # 预期结果:6
    assert t < 6

# 2.传两个参数
# import pytest
# import allure
# d2=[(1,2),(2,2),(5,6)]
# @pytest.mark.parametrize("y1,y2",d2)
# def test_2(y1,y2):
#     print(f"y1的值是{y1}")
#     print(f"y2的值是{y2}")
#     assert y1 == y2
# py.test test_1.py/ --alluredir ./result/
# allure generate ./result/ -o ./report/ --clean
# allure open -h 127.0.0.1 -p 8083 ./report/


# 三种方法：
# 1.
# import pytest
# @pytest.fixture()
# def myfix():
#     print("每个测试用例都要执行myfix")
# @pytest.mark.usefixtures("myfix")
# def test_1():
#     pass
# def test_2():
#     pass

# 2.
# @pytest.fixture(autouse="true")
# def myfix():
#     print("每个测试用例都要执行myfix")
# pytestmark=pytest.mark.usefixtures("myfix")  #固定格式
# def test_1():
#     pass
# def test_2():
#     pass
# def test_3():
#     pass


# 扩展知识
# ids
# name
# pytest  跳过某些用例，失败重跑，统计测试覆盖率，等


# from appium import webdriver
# from time import sleep
# # import yaml
# # with open(file="F:\QQ\element\login.yaml",mode="r",encoding="utf-8") as fb:
# #     el = yaml.load(fb,Loader=yaml.FullLoader)
# #     print(el)
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
# sleep(2)
# dr.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱").clear()
# sleep(2)
# dr.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱").send_keys(111111)
# sleep(1)
# dr.find_element_by_id("com.tencent.mobileqq:id/password").clear()
# sleep(2)
# dr.find_element_by_id("com.tencent.mobileqq:id/password").send_keys("adadwd")
# sleep(2)
# dr.find_element_by_id("com.tencent.mobileqq:id/login").click()
# sleep(8)

# from selenium.webdriver import ActionChains
# action = ActionChains(dr)
# source = dr.
# action.click_and_hold(source).perform()
# action.move_by_offset(298, 0)
# action.release().perform()

# time.sleep(1)
# def get_size():
#     x = dr.get_window_size()
#     return x
# size = get_size()
# sleep(0.5)
# x = size['width']
# y = size['height']
# sleep(1)
# dr.swipe(x * 0.2, y * 0.56, x * 0.8, y * 0.56, 300)
# sleep(30)

# json 是一种轻量级的数据交互格式
# iavascript语言中的一种数据表现形式
# python中没有json这种格式
# import json
# a_1 = {'hh':123,'gg':456}
# print(a_1)
# b = json.dumps(a_1)
# print(b)
# c = json.loads(b)
# print(type(c))
# print(c)
