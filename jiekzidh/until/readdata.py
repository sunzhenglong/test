# !/usr/bin/env python
# -*- coding:utf-8 -*-
with open(file='F:\jiekzidh\data\datas',mode='r',encoding='utf-8') as fb:
    a = fb.read().replace('\n','').split(';')
c = []
for i in a:
    b = tuple(i.split(','))
    c.append(b)
