import requests
import pytest
@pytest.fixture()
def cl():
    url = "http://127.0.0.1:5000/login"
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
    return headers,url