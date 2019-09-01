# !/usr/bin/env python
# -*- coding:utf-8 -*-
from appium import webdriver
import time
d = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "emulator-5554",
  "appPackage": "com.baidu.input",
  "appActivity": ".ImeAppMainActivity",
  # "noReset": "true",
  'unicodeKeyboard': "true",
  'resetKeyboard': "true"
}
dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)

dr.find_element_by_id("com.baidu.input:id/setdefault").click()
time.sleep(2)
a = dr.find_elements_by_class_name("android.widget.RadioButton")
b = 0
for i in a:
    b += 1
    if b == 2:
        i.click()
        break
    else:
        continue
time.sleep(2)
dr.find_element_by_id("com.baidu.input:id/finishsetting").click()
def get_size():
    x = dr.get_window_size()
    return x
size = get_size()
time.sleep(0.5)
x = size['width']
y = size['height']
time.sleep(1)
dr.swipe(x*0.5, y*0.65, x*0.5, y*0.35, 600)
dr.find_element_by_id("com.baidu.input:id/ID_PULLTOREFRESH_GRIDVIEW").find_element_by_xpath("//*[@index='4']").click()
dr.find_element_by_id("com.baidu.input:id/apply_btn").click()
time.sleep(10)
