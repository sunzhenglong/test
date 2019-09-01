# python 装饰器
# 将函数作为参数进行返回给别的函数使用
# def foo(func):
#     print("执行foo函数开始")
#     func()
#     print("执行foo函数结束")
# def koo():
#     print("执行了koo函数")
# foo(koo)

def out(func):
    print("执行out函数")
    def inner():
        func()
    print("执行out函数结果")
    return inner

# # python的语法糖  @out 使用out这个装饰器
@out
def say_hello():
    print("hello,装饰器")
out(say_hello)()
# say_hello()



