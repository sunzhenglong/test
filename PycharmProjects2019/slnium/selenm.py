# 环境搭建
# 1.到网上下载webdriver驱动
# 2.将下载好的驱动，放在python安装目录下
# 3.python需要下载selenium模块
import pytest
from time import sleep
from selenium import webdriver
dr = webdriver.Chrome()
# 访问网址
# dr.get("https://www.baidu.com/")
# 获取当前访问的页面
# assert dr.title == "百度一下，你就知道"
# 获取访问的网址
# assert dr.current_url == "https://www.baidu.com/"
# 设置浏览器窗口大小
# dr.set_window_size(400,400)
# 设置浏览器产生的位置
# dr.set_window_position(400,400)
# 最大化浏览器
# dr.maximize_window()
# 最小化浏览器
# dr.minimize_window()
# sleep(2)
# dr.get("https://www.jd.com/")
# sleep(2)
# dr.back()
# sleep(2)
# 前进到第二个页面
# dr.forward()



# 核心：定位
# 1.id   2.class  3.name  4.link_text   5.tag_name  6.xpath  7.css  8.partial_link_text
# 1.id定位     动作：1.click  2.send_keys
# dr.find_element_by_id("kw").send_keys("知乎")
# sleep(1)
# dr.find_element_by_id("su").click()
# 2.class定位
# dr.find_element_by_class_name("")
# 3.name定位
# dr.find_element_by_name("")
# 4.link_text定位    #准确文本
# dr.find_element_by_link_text("新闻").click()
# 5.partial_link_text定位     #模糊文本
# dr.find_element_by_partial_link_text("中央全面依法治国").click()
# 6.tag_name标签定位   通常定位一组
# 7.xpath   路径标记语言(绝对路径和相对路径)
# XML:可扩展标记语言===HTML(内容和HTML一样)   作用：储存数据
# dr.find_element_by_xpath('//*[@id="u1"]/a[1]').click()
# 8.css定位
# dr.find_element_by_css_selector('#u1 > a:nth-child(1)').click()

# https://mail.qq.com/cgi-bin/frame_html?sid=R6VL73Hl1K7OUhNO&r=e87c9806c97427025303d7b7810d3bfb

# qq邮箱发邮件
# dr.get('https://mail.qq.com/cgi-bin/frame_html?sid=qkhCMqwFLVcICEkU&r=92a7c775c842ba458e6c684bde66e5d2')
# sleep(2)
# ww = dr.find_element_by_id('login_frame')
# print(ww)
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_id('u').send_keys('1098555106')
# dr.find_element_by_id('p').send_keys('a1098555106')
# dr.find_element_by_id("login_button").click()
# sleep(10)
# dd = dr.window_handles
# dr.switch_to.window(dd[-1])
# dr.find_element_by_id('composebtn').click()
# sleep(2)
# dr.switch_to.parent_frame()
# dr.switch_to.frame('mainFrame')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('1170339464@qq.com')
# sleep(1)
# dr.find_element_by_id("subject").send_keys('haha')
# sleep(2)
# ww = dr.find_elements_by_class_name('qmEditorIfrmEditArea')[0]
# # ww = dr.find_element_by_xpath('//*[@id="_156664726215107093995552478447"]')
# dr.switch_to.frame(ww)
# sleep(2)
# dr.find_elements_by_xpath('/html/body')[0].send_keys("123455")
# sleep(1)
# dr.switch_to.parent_frame()
# dr.find_element_by_name("sendbtn").click()


# 定位一组对象：同时定位多个元素，结果是个列表
# 同时定位多个元素
# 层级定位：先定位大范围，再从大范围中定位需要的元素
# dr.父元素.子元素.动作
# dr.get('https://www.ctrip.com/')
# sleep(2)
# ww = dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# b = []
# for i in ww:
#     a = i.text
#     b.append(a)
#     sleep(3)
# print(len(ww))
# print(b)


# sleep(2)
# # iframe:内嵌框架,切换框架时，只可以用id或者name的值
# # 如果没有id和name。可以用定位方式，定位到框架赋值，再定位
# dr.switch_to.frame('login_frame')
# sleep(2)
# # 退出到第一层框架:
# dr.switch_to.default_content()
# # 退出到上一层框架:
# dr.switch_to.parent_frame()


# 浏览器管理窗口：
# 浏览器会对打开的窗口生成一个唯一标识窗口的句柄
# 谷歌产生的句柄是一串字符，火狐产生的是一堆数字
# dr.get('https://www.douban.com')
# sleep(2)
# d = dr.current_window_handle
# print(d)
# dr.find_element_by_link_text('豆瓣读书').click()
# sleep(2)
# # 获取所有窗口的句柄
# dd = dr.window_handles
# print(dd)
# # 切换窗口
# dr.switch_to.window(dd[-1])
# print(dr.title)

# 弹出框处理:
# dr.get('file:///D:\qqdown\\abc.html')
# sleep(2)
# dr.find_element_by_xpath('/html/body/button').click()
# sleep(2)
# ww = dr.switch_to.alert
# print(ww.text)   #获取弹出框上的文本
# # ww.accept()  #点击弹出框上的确定
# ww.send_keys("一giao我哩giao")   #给弹出框输入文本
# ww.accept()
# ww.dismiss()    #点击弹出框的取消

# 执行Javascript函数：
# 滚动条滚动到指定位置：
# dr.get('https://www.ifeng.com')
# sleep(2)
# dd = dr.find_element_by_xpath('//*[@id="homeNewsList"]/div[1]/a[1]')
# dr.execute_script('arguments[0].scrollIntoView();',dd)
# 更改滚动条的高度滑动，数字指的是高度
# for i in range(0,100000,2000):
#     js=f"var q=document.documentElement.scrollTop={i}"
#     dr.execute_script(js)
#     sleep(1)

# 智能等待
# dr.get("https://www.jd.com")
# sleep(2)
# import selenium.webdriver.support.ui as ui
# until = ui.WebDriverWait(dr,10)
# # 定位要出现的元素:
# until.until(lambda dr:dr.find_element_by_xpath('//*[@id="logo"]/h1/a').is_displayed())
# dr.find_element_by_xpath('//*[@id="J_cate"]/ul/li[1]/a').click()

# 鼠标操作
# from selenium.webdriver.common.action_chains import ActionChains
# dr.get("https://www.jd.com")
# sleep(2)
# ww = dr.find_elements_by_class_name('cate_menu_item')
# for i in ww:
#     ActionChains(dr).move_to_element(i).perform()  #动作链,模拟真实鼠标移动
   #鼠标拖拽
# dr.get('https://qzone.qq.com/')
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys("109865366")
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys("22e241dwd")
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
# dd = dr.find_element_by_xpath('//*[@id="tcaptcha_iframe"]')
# dr.switch_to.frame(dd)
# sleep(5)
# ww = dr.find_element_by_xpath('//*[@id="slideBlock"]')
# # ActionChains(dr).drag_and_drop(起始位,终止位)
# ActionChains(dr).drag_and_drop_by_offset(ww,170,0).perform()

#163邮箱
# dr.get('https://mail.163.com/')
# sleep(2)
# dr.find_element_by_id('switchAccountLogin').click()
# sleep(2)
# ww = dr.find_element_by_xpath('//*[@style="width: 100%; height: 100%; border: none; background: none;"]')
# sleep(2)
# print(ww)
# dr.switch_to.frame(ww)
# sleep(2)
# # dr.find_element_by_xpath('//*[@id="auto-id-1566652034132"]').send_keys("18237820536")
# dr.find_element_by_xpath('//*[@placeholder="邮箱帐号或手机号码"]').send_keys('18237820536')


#百度输入法
# from selenium.webdriver.common.action_chains import ActionChains
# dr.get('https://shurufa.baidu.com/')
# sleep(2)
# ww = dr.find_element_by_id('user-login')
# ActionChains(dr).move_to_element(ww).perform()
# sleep(1)
# dr.find_element_by_id('user-login-pop').click()
# # ww = dr.find_element_by_xpath('//*[@id="TANGRAM__PSP_5__"]/iframe')
# # dr.switch_to.frame(ww)
# dr.find_element_by_id('TANGRAM__PSP_10__userName').send_keys('18237820536')



# 自动化脚本的多种断言方法：
# dr.get('https://www.douban.com/')
# sleep(2)
# dr.find_element_by_class_name('https://www.douban.com/').click()
# dd = dr.window_handles
# dr.switch_to.window(dd[-1])
# ee = dr.find_element_by_class_name('hot-tags-col5 s').find_elements_by_class_name('tag')[0].text



# dr.get('https://www.ctrip.com/#ctm_ref=ssc_hp_elevator_car')
# sleep(6)
# t = dr.find_element_by_class_name('product-hd').find_element_by_xpath('/html/body/div[14]/div[1]/div[2]/div[5]/div/div[1]/ul/li[2]').text
# print(t)
# tt = []
# for i in t:
#     h = i.text
#     tt.append(h)
#     sleep(2)
# print(tt)



# tt = dr.title
# print(tt)
# v = dr.find_element_by_class_name('keyword-short').find_elements_by_tag_name('span')
# tt = []
# for i in v:
#     h = i.text
#     tt.append(h)
#     sleep(2)
# print(tt)

# t = dr.find_elements_by_xpath('/html/body/div[14]/div[4]/div[2]/div[2]/div[1]/dl/dd/span[1]').
# tt = []
# for i in t:
#     j =
#     tt.append(j)
#     sleep(2)
# print(tt)
# dr.find_element_by_xpath('/html/body/div[14]/div[4]/div[2]/div[2]/div[1]/dl/dd/span[2]')
# p = t.text
# print(p)
# r = []
# for i in v:
#     h = i.
#     r.append(h)
#     sleep(2)
# print(r)








# sleep(2)
# dr.switch_to._frame('login_frame')
# sleep(2)