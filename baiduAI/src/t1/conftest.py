import pytest
@pytest.fixture()
def cl():
    from appium import webdriver
    from time import sleep
    import yaml
    with open(file="F:\\baiduAI\element\login",mode="r",encoding="utf-8") as fb:
        el = yaml.load(fb,Loader=yaml.FullLoader)
        print(el)
    d = {
            "device": "android",
            "platformName": "Android",
            "platformVersion": "8.1.0",
            "deviceName": "ff4497fc0105",
            "appPackage": "com.baidu.aiboard",
            "appActivity": "com.baidu.input.SplashActivity",
            "noReset": "true"
        }
    dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
    sleep(5)
    return dr,el

