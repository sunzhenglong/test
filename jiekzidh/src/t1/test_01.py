import pytest
import requests
from until.readdata import c
@pytest.mark.parametrize('x,y,z,r',c)
def test_1(x,y,z,r,cl):
    headers,url = cl
    payload = f"username={z}&password={r}"
    response = requests.request("POST", url, data=payload, headers=headers)
    try:
        assert 'welcome' in response.text
        print(response.text)
    except:
        assert 'login' in response.text
        print(response.text)