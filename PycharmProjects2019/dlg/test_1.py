#pytest是python自动化测试的一个工具库
# 作用：
# 1.调整测试用例的运行顺序
# 2.对测试用例传入测试数据
# 3.对测试用例设置断言
# 4.pytest与allure生成测试报告
# 特点：
# 灵活，支持的插件丰富
import pytest
# 自动化测试用例指的是什么
# 指的是一个函数，必须以test开头
# def test_0():
# 计算100之内的所有整数和
#     n = 0
#     for i in range(101):
#         n += i
# 预期结果是5050
# 代码运算结果为实际结果
#     assert n == 5050
# assert:断言，拿实际结果和预期结果之间的对比

# 执行测试用例
# 1.pytest
# 2.py.test
# 效果一样

# allure生成测试报告
# py.test test_1.py/ --alluredir ./result/
# allure generate ./result/ -o ./report/ --clean
# allure open -h 127.0.0.1 -p 8083 ./report/
