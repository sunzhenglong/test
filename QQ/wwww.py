#appium的三种等待
# 1.sleep---> 强制等待
# 2.隐性等待--->implicitly_wait(time_to_wait)
# 设置最大等待时间，关键字参数：time_to_wait=10，超过最大等待时间后则会抛出异常
# 3.安卓独有的--->等待某一个activity出现,设置最大等待时间，超出最大等待时间，就会抛出异常
# 在设置的时间内没间隔指定的时间扫描activity是否被找到，找到则执行下面的代码，超过最大等待时间则抛出异常
# activity: 安卓活动名，tiemout：超时时间
# 4.智能等待--->

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#WebDriverWait  等待某一个元素加载出来
#expected_conditions 的异常处理类   （预期条件）
#By 指的是通过什么方式进行定位  By.ID---->通过ID的方式定位
WebDriverWait("参数一","参数二","参数三").until(EC.presence_of_element_located("参数四"))
#参数一：我们与手机建立的会话 --->dr
#参数二：最大等待时间，单位是s
#参数三：刷新页面的时间间隔，单位s
#until 直到某个元素被找到，就停止等待
#参数四：一个由定位方法和元素组成的元组
#例如：(By.ID,"元素")
