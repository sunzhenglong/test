import pytest
# @pytest.fixture()
# def cl():
#     import yaml
#     from appium import webdriver
#     from time import sleep
#     with open(file="F:\Bdinput\element\login",mode="r",encoding="utf-8") as fb:
#         el = yaml.load(fb,Loader=yaml.FullLoader)
#         print(el)
#     d = {
#         "device": "android",
#         "platformName": "Android",
#         "platformVersion": "8.1.0",
#         "deviceName": "ff4497fc0105",
#         "appPackage": "com.baidu.input",
#         "appActivity": ".ImeAppMainActivity",
#         "noReset": True,
#         # 'unicodeKeyboard': "true",
#         # 'resetKeyboard': "true"
#     }
#     dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
#     # sleep(3)
#     # dr.find_element_by_id(el["a1"]).click()
#     # sleep(2)
#     # dr.find_element_by_id(el["a2"]).find_element_by_xpath("//*[@index='3']").click()
#     # dr.find_element_by_id(el["a5"]).click()
#     return el,dr



# @pytest.fixture()
# def test_2():
#         print("1111")