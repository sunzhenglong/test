# !/usr/bin/env python
# -*- coding:utf-8 -*-
def cl():
    import pytest
    from time import sleep
    from selenium import webdriver
    dr = webdriver.Chrome()
    sleep(4)
    return dr