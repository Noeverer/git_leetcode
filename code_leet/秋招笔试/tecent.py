#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Ante Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: tecent.py
@time: 2020-09-06 下午 9:19
"""
import itertools
import collections
a = collections.Counter([1,2,3,4,1])
b = collections.Counter([1,2,3,4,2])
c = collections.Counter([1,2,3,4,2])
res = [a,b,c]
ress = list(itertools.combinations(res,r=2))
for ress1,ress2 in ress:
    print(ress1,ress2)
    if ress1==ress2:
        print('yes')

print(a==b)