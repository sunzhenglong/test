# !/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep
import pytest
@pytest.fixture()
def setup_module():
    print('所有用力执行前清理一次')
def test_1(cl):
    dr = cl
    dr.get('https://www.douban.com')
    dr.find_element_by_link_text('豆瓣读书').click()
    sleep(2)
    dd = dr.window_handles
    print(dd)
    dr.switch_to.window(dd[-1])
    print(dr.title)
    assert dr.title == "豆瓣读书"
def test_2(cl):
    dr = cl
    dr.get('https://mail.qq.com/cgi-bin/frame_html?sid=qkhCMqwFLVcICEkU&r=92a7c775c842ba458e6c684bde66e5d2')
    sleep(2)
    ww = dr.find_element_by_id('login_frame')
    print(ww)
    dr.switch_to.frame('login_frame')
    sleep(2)
    dr.find_element_by_id('u').send_keys('1098555106')
    dr.find_element_by_id('p').send_keys('a1098555106')
    dr.find_element_by_id("login_button").click()
    sleep(10)
    dd = dr.window_handles
    dr.switch_to.window(dd[-1])
    dr.find_element_by_id('composebtn').click()
    sleep(2)
    dr.switch_to.parent_frame()
    dr.switch_to.frame('mainFrame')
    sleep(2)
    dr.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('1170339464@qq.com')
    sleep(1)
    dr.find_element_by_id("subject").send_keys('haha')
    sleep(2)
    ww = dr.find_elements_by_class_name('qmEditorIfrmEditArea')[0]
    # ww = dr.find_element_by_xpath('//*[@id="_156664726215107093995552478447"]')
    dr.switch_to.frame(ww)
    sleep(2)
    dr.find_elements_by_xpath('/html/body')[0].send_keys("123455")
    sleep(1)
    dr.switch_to.parent_frame()
    dr.find_element_by_name("sendbtn").click()