# !/usr/bin/env python
# -*- coding:utf-8 -*-
from appium import webdriver
# python代码的客户端连接手机所需要的信息
d = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "emulator-5554",
  "appPackage": "com.tencent.mobileqq",
  "appActivity": ".activity.SplashActivity",
  "noReset": "true",
  'unicodeKeyboard': "true",
  'resetKeyboard': "true"
}
# 1.与手机建立连接
dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
# (将手机信息发送给appium服务器，使服务器和手机建立一个session，appium服务器和客户端建立连接)

# 1、python客户端与appium服务器建立一个连接
# 2、python代码中的命令由appium服务器转发
# 3、手机中bootstrap.jar服务器接收转发的命令
# 4、处理转发命令，将命令下发给uiautomatior（手机自带测试框架：执行类似于adb命令）
# 5、uiautomatior 生成一个执行后的结果
# 6、结果转发给bootstarp.jar微服务器
# 7、一直转发到python客户端，appium库解析转发的过来的结果
# 8、将结果输出

# appium选定的元素属性：
# id：一般是唯一的，标记一个元素
# class：标记一组元素，一般是多个
# text：是否可以获取文字，有文字代表可以获取
# clickable：判断是否可以被点击，true代表可以，false表示不可以

# 第二步，执行操作
# id不唯一，使用class定位
# 解决方法：
#     向上一级，或者更上一级，id唯一，class唯一
#     再使用class定位

import time
time.sleep(6)
# 联系人，看点，动态三个组成的列表：
# s = dr.find_element_by_id("android:id/tabs").find_elements_by_class_name("android.widget.FrameLayout")
# for i in s:
#     i.click()
# 消息的可点击定位：
# dr.find_element_by_id("android:id/tabs").find_element_by_class_name("android.widget.RelativeLayout").click()


# 打印text：
# a = dr.find_element_by_id("android:id/tabs").find_element_by_class_name("android.widget.RelativeLayout").find_elements_by_class_name("android.widget.TextView")
# # print(a)
# for i in a:
#     s = i.text
#     print(s)
# b = dr.find_element_by_id("android:id/tabs").find_elements_by_class_name("android.widget.FrameLayout")
# # print(b)
# for i in b:
#     g = i.find_element_by_class_name("android.widget.TextView").text
#     print(g)

# dr.find_element_by_id("dr.find_element_by_id").find_element_by_class_name("android.widget.RelativeLayout").find_element_by_class_name("android.widget.EditText").click()

# qq发送消息：
# dr.find_element_by_id("com.tencent.mobileqq:id/et_search_keyword").send_keys("嘻嘻嘻嘻嘻欢你")
# time.sleep(5)
# # aa = dr.find_element_by_id("com.tencent.mobileqq:id/et_search_keyword")
# f = dr.find_element_by_id("com.tencent.mobileqq:id/result_layout").find_element_by_class_name("android.widget.AbsListView").find_elements_by_class_name("android.widget.LinearLayout")
# g = 0
# for i in f:
#     g += 1
#     if g == 4:
#       i.click()
#       time.sleep(4)
#       break
#     else:
#       continue
# dr.find_element_by_id("com.tencent.mobileqq:id/input").send_keys("")
# time.sleep(2)
# dr.find_element_by_id("com.tencent.mobileqq:id/fun_btn").click()




# s = dr.find_element_by_id("android:id/tabs").find_elements_by_class_name("android.widget.FrameLayout")
# for i in s:
#     i.click()
#     break
# time.sleep(4)
# f = dr.find_element_by_class_name("android.support.v4.view.ViewPager").find_element_by_class_name("android.widget.FrameLayout").find_element_by_class_name("android.widget.AbsListView").find_elements_by_class_name("android.widget.RelativeLayout")
# n = 0
# for i in f:
#     n += 1
#     if n == 3:
#         i.click()
#         break
#     else:
#         continue
# def get_size():
#     x = dr.get_window_size()  #获取屏幕大小,返回dict
#     return x
# size = get_size()
# time.sleep(0.5)
# x = size['width']
# y = size['height']
# for i in range(50):
#     time.sleep(1)
#     dr.swipe(x*0.5, y*0.25, x*0.5, y*0.65, 600)
#     time.sleep(1)

#     for j in r:
#         j.click()


# s = dr.find_element_by_id("android:id/tabs").find_elements_by_class_name("android.widget.FrameLayout")
# y = 0
# for i in s:
#     y += 1
#     i.click()
#     if y == 2:
#         break
# time.sleep(10)
#
# gg = dr.find_element_by_class_name("android.support.v4.view.ViewPager").find_elements_by_class_name("android.widget.FrameLayout")
#
# uu = []
# for k in range(5):
#     time.sleep(3)
#     u = 0
#     for i in gg:
#         u += 1
#         if u == 2:
#             tt = i.find_element_by_class_name("android.widget.AbsListView").find_elements_by_class_name("android.widget.TextView")
#             for j in tt:
#                 m = j.text
#                 uu.append(m)
#             break
#         else:
#             continue
#     print(uu)
#     def get_size():
#         x = dr.get_window_size()
#         return x
#     size = get_size()
#     time.sleep(0.5)
#     x = size['width']
#     y = size['height']
#     time.sleep(1)
#     dr.swipe(x*0.5, y*0.25, x*0.5, y*0.55, 600)
#     time.sleep(3)
# hg = []
# q = -1
# for j in uu:
#     q += 1
#     if q%4 == 0:
#         hg.append(uu[q])
# print(hg)





