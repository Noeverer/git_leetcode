#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Ante Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: itertools_fun.py
@time: 2020-08-26 上午 9:45
"""

import sys
sys.setrecursionlimit(3000)  # 解除递归的限制


from itertools import *

'''
# def count(firstval=0, step=1):
#             x = firstval
#             while 1:
#                 yield x
#                 x += step
c = count(10)  # 迭代器的作用
'''


'''
# 产生累加效应
print(list(accumulate([1,2,3,4,5])))
'''

pro = list(product('abcd',repeat=2))

permu = list(permutations('abcd',r=2))

combin = list(combinations('abcd',r=3))

print(pro,'\n',
      permu,'\n',
      combin ,'\n',)






