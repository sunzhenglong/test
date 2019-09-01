# !/usr/bin/env python
# -*- coding:utf-8 -*-
import allure
from time import sleep
from until.llog import get_logger
log = get_logger(filename="test_01.py")
def test_1(cl):
    dr,el = cl
    sleep(3)
    dr.find_element_by_id("com.baidu.aiboard:id/iv_ar").click()
    dr.find_element_by_id("com.baidu.aiboard:id/ar_toolbar_collection").click()
    t_1 = dr.find_element_by_id("com.baidu.aiboard:id/start_record").text
    log.info("进入到'我的'界面")
    assert t_1 == "开始录制"
# py.test test_1.py/ --alluredir ./result/
# allure generate ./result/ -o ./report/ --clean
# allure open -h 127.0.0.1 -p 8083 ./report/