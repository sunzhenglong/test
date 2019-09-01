import pytest
# def test_1():
#     a = 1
#     b = 2
#     c = a + b
# #     # 实际结果是3，预期结果是2
# #     # 设定断言
#     assert c == 1
# def test_2():
#     str_1 = "hello pytest"
#     str_2 = "python"
# #     # 设定断言，判断str_2 在 str_1内
#     assert str_2 in str_1
# #
# def test_three():
#     n = 100
#     # 设定断言，判断n小于101
#     assert n < 101
# pytest：
# 查找当前目录下，所有文件或目录，找包含test目录或者文件
# 如果找到test目录，类似于cd，开始执行搜索包含test开头的文件
# 找到文件后搜索test开头的所有函数
#
# _____ERROR collecting test session ____
# 简单的说就是，未收集到可以执行的测试用例！
#
# 参数：
# 1.-v:使输出的信息更详细
# 2.-q:简化输出，不可与-v连用
# 3.-k:匹配关键字,指定包含设置的关键字运行
# 4.脚本名::用例名字     ---->运行执行脚本中的具体用例
# 5.-s:输出测试用例中print内的信息
# 例：pytest test_01.py::"test_three"

