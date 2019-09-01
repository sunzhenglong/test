import pytest
@pytest.fixture()
def cl():
    import yaml
    from appium import webdriver
    from time import sleep
    with open(file="F:\QQ\element\login.yaml",mode="r",encoding="utf-8") as fb:
        el = yaml.load(fb,Loader=yaml.FullLoader)
        print(el)
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
    dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
    sleep(3)
    return el,dr

