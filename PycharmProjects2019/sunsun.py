# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# time.sleep(5)
# driver.get("https://www.ifeng.com/")

# 服务端
# import socket
# a = ("127.0.0.1",9000)
# b = socket.socket()
# b.bind(a)
# b.listen(5)
# c,adress = b.accept()
# d = c.recv(1024).decode("utf-8")
# print(d)
# e = input("")
# c.sendall(e.encode)

# import paramiko
# a = paramiko.SSHClient()
# a.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# a.connect(
#     username='root',
#     password='123456'
# )
# a = paramiko.Transport()
# a.connect()
# import pytest
# import allure
