#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Ante Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: 7.py
@time: 2020-08-21 上午 11:43
"""
'''
def PolygonArea(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

# examples
corners = [(2.0, 1.0), (4.0, 5.0), (7.0, 8.0)]
pp = PolygonArea(corners)
print(pp)
'''

from sympy import *
x = symbols('x')
print(integrate(x, (2*x*x+x+3, 1, 2)))
