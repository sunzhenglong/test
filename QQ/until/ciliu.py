# def hd(dr,t=500):
#     # 获取手机屏幕的尺寸
#         l = dr.get_window_size()  #获取屏幕大小
#         # 放缩屏幕
#         x1 = l["width"] * 0.5
#         x2 = l["width"] * 0.75
#         y1 = l["height"] * 0.35
#         y2 = l["height"] * 0.65
#
#         # 上滑
#         dr.swipe(x1,y2,x1,y1,duration=t)

import requests

url = "http://127.0.0.1:5000/login"

payload = "username=zhangsan&password=123"
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "acea1789-ecba-46b5-8e29-7ed4013f0b02,8f99af04-57ae-4c4d-a367-1bad34582e00",
    'Host': "127.0.0.1:5000",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "30",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)