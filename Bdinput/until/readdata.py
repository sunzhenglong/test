# !/usr/bin/env python
# -*- coding:utf-8 -*-
import time
with open(file="F:\Bdinput\data\BDdata",mode="r",encoding="utf-8") as fb:
    data = fb.read().split(";")
    print(data)
g = []
for i in data:
    a = i.replace('\n','').split(",")
    b = tuple(a)
    g.append(b)
    print(g)