# !/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
from time import sleep
from until.loger import get_logger
log = get_logger(filename="test_01.py")
# 使用conftest
# def test_1(cl):
#     el,dr = cl
#     sleep(3)
#     c = dr.find_element_by_id(el["a7"]).text
#     log.info("切换皮肤")
#     assert c == "超级皮肤"
# def test_2(cl):
#     el,dr = cl
#     sleep(3)
#     def get_size():
#         x = dr.get_window_size()
#         return x
#     size = get_size()
#     sleep(0.5)
#     x = size['width']
#     y = size['height']
#     sleep(1)
#     dr.swipe(x*0.5, y*0.75, x*0.5, y*0.25, 1000)
#     dr.find_element_by_id(el["a6"]).find_element_by_xpath("//*[@index='2']").click()
#     dr.find_element_by_id(el["a8"]).click()
#     sleep(4)
#     log.info("皮肤下载成功")
#     a = dr.find_element_by_id(el["a7"]).text
#     assert a == "皮肤启用成功"
# def test_3(cl):   #超级皮肤搜索引擎验证
#         el,dr = cl
#         sleep(3)
#         dr.find_element_by_id(el["a9"]).click()   #点击搜索按键
#         sleep(2)
#         dr.find_element_by_id("com.baidu.input:id/store_hot_search").find_element_by_xpath("//*[@index='1']").click()
#         a = dr.find_element_by_id("com.baidu.input:id/ID_PULLTOREFRESH_GRIDVIEW").find_elements_by_class_name("android.widget.RelativeLayout")
#         for i in a:
#             i.click()
#             sleep(3)
#             break
#         log.info("搜索到皮肤")
#         dr.find_element_by_id(el["a8"]).click()
#         sleep(4)
#         b = dr.find_element_by_id(el["a7"]).text
#         assert b == "皮肤启用成功"
# def test_4(cl):
#     el,dr = cl
#     sleep(3)
#     dr.find_element_by_id(el["a9"]).click()
#     sleep(2)
#     dr.find_element_by_id("com.baidu.input:id/store_hot_search").find_element_by_xpath("//*[@index='1']").click()
#     a = dr.find_element_by_id("com.baidu.input:id/ID_PULLTOREFRESH_GRIDVIEW").find_elements_by_class_name("android.widget.RelativeLayout")
#     for i in a:
#         i.click()
#         sleep(3)
#         break
#     dr.find_element_by_id("com.baidu.input:id/share_list").find_element_by_xpath("//*[@index='2']").click()
#     sleep(7)
#     b = dr.find_element_by_id("com.tencent.mobileqq:id/listView1").find_elements_by_class_name("android.widget.RelativeLayout")
#     c = 0
#     for i in b:
#         c += 1
#         if c == 2:
#             i.click()
#             sleep(3)
#             break
#         else:
#             continue
#     dr.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn").click()
#     sleep(4)
#     d = dr.find_element_by_id("com.baidu.input:id/share_title").text
#     assert d == "分享到"
# def test_5(cl):
#     el,dr = cl
#     dr.find_element_by_id("com.baidu.input:id/banner_settings_frame").click()
#     sleep(2)
#     dr.find_element_by_id("android:id/list").find_element_by_xpath("//*[@index='0']").click()
#     sleep(5)
#     dr.find_element_by_accessibility_id("QQ").click()
#     sleep(2)
#     dr.find_element_by_class_name("android.widget.Button").click()
#     sleep(2)
#     a = dr.find_element_by_id("android:id/action_bar").find_element_by_class_name("android.widget.TextView").text
#     assert a == "百度输入法"

# def test_6(cl):
#     el, dr = cl
#     sleep(3)
#     dr.find_element_by_id(el["a9"]).click()  # 点击搜索按键
#     sleep(1)
#     dr.press_keycode("7")
    # sleep(10)
    # dr.find_element_by_id("com.baidu.input:id/store_hot_search").find_element_by_xpath("//*[@index='1']").click()
    # a = dr.find_element_by_id("com.baidu.input:id/ID_PULLTOREFRESH_GRIDVIEW").find_elements_by_class_name(
    #     "android.widget.RelativeLayout")
    # for i in a:
    #     i.click()
    #     sleep(3)
    #     break
    # log.info("搜索到皮肤")
    # dr.find_element_by_id(el["a8"]).click()
    # sleep(4)
    # b = dr.find_element_by_id(el["a7"]).text
    # assert b == "皮肤启用成功"





# py.test test
# _1.py/ --alluredir ./result/
# allure generate ./result/ -o ./report/ --clean
# allure open -h 127.0.0.1 -p 8083 ./report/






# def get_size():
#     x = dr.get_window_size()
#     return x
# size = get_size()
# time.sleep(0.5)
# x = size['width']
# y = size['height']
# time.sleep(1)
# dr.swipe(x*0.5, y*0.65, x*0.5, y*0.35, 600)
# dr.find_element_by_id("com.baidu.input:id/ID_PULLTOREFRESH_GRIDVIEW").find_element_by_xpath("//*[@index='4']").click()
# dr.find_element_by_id("com.baidu.input:id/apply_btn").click()
# time.sleep(10)






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

