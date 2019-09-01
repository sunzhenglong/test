import allure
import pytest
# feature# 标注测试用例是属于哪个模块的
@allure.feature("模块一")
def test_1():
    assert 0 == 0
@allure.feature("模块一")
def test_2():
    assert 1 == 1
@allure.feature("模块一")
def test_3():
    assert 2 == 2
#story:对一个测试用例的详细描述
@allure.feature("模块二")
@allure.story("这是一个很giao的测试用例")
def test_3():
    assert 0 > 1
@allure.feature("模块二")
@allure.story("这是一个特别giao的测试用例")
def test_4():
    """
    这是一个一giao我哩giao的用例
    """
    assert "giao哥牛逼" in "牛逼"
#测试用例的优先级
"""
Blocker级别：阻塞中断缺陷
Critical：严重缺陷
Normal：普通级别
Minor：次要
Trivial：轻微
"""
#severity   标注测试用例的优先级
@allure.feature("模块三")
@allure.severity("critical")
def test_5():
    assert 0 == 0
@allure.feature("模块三")
@allure.severity("minor")
def test_6():
    assert 0 == 0
@allure.feature("模块三")
@allure.severity("trivial")
def test_7():
    assert 0 == 0
#step  记录测试用例中的一些步骤，日志代码可以通过step记录到报告中
@allure.step("字符串相加:{0},{1}")
def str_add(str1,str2):
    if not isinstance(str1,str):#isinstance  判断数据类型的类,参数1和参数2是否是同一类型，是的话返回true
        return f"{str1}不是字符串类型的"
    if not isinstance(str2,str):
        return f"{str2}不是字符串类型的"
    return str1 + str2
@allure.feature("模块四")
def test_8():
    str1 = "giao哥"
    str2 = "牛逼"
    assert str_add(str1,str2) == "giao哥牛逼"

#issue和testcase
#对issue和testcase 生成一个网址
@allure.step("字符串相加：{0}，{1}")
#测试步骤，可通过format机制自动获取函数参数
def str_add(str1, str2):
    print('hello')
    if not isinstance(str1, str):
        return "%s is not a string" % str1
    if not isinstance(str2, str):
        return "%s is not a string" % str2
    return str1 + str2

@allure.feature('模块五')
@allure.story('一个比较giao的用例')
@allure.severity('blocker')
@allure.issue("http://www.baidu.com")
@allure.testcase("http://www.testlink.com")
def test_case():
    str1 = 'hello'
    str2 = 'world'
    assert str_add(str1, str2) == 'helloworld'
# git-->svn-->jenkins-->执行代码-->生成报告-->查看
# py.test test_1.py/ --alluredir ./result/
# allure generate ./result/ -o ./report/ --clean
# allure open -h 127.0.0.1 -p 8083 ./report/