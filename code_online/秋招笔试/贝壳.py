#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Ante Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: 贝壳.py
@time: 2020-09-07 下午 2:59
"""
import collections,itertools
res = list(itertools.permutations([1,2,3,4],2))
cache = list(itertools.combinations_with_replacement(['J','S','B'],2))

cache = {'JJ':0,'JS': -1,'JB':1,'SJ':-1,'SS':0,'SB':-1,'BJ':-1,'BS':1,'BB':0}



print(cache)