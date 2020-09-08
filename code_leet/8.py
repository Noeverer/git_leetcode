#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Ante Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: 8.py
@time: 2020-08-24 上午 1:07
"""


def repeatedSubstringPattern(s):
    '''
    # 没有思考到有序的性质
    if len(s)<=1:
        return False
    ss = collections.Counter(s)
    # print(ss)
    if len(ss)==1:
        return True
    for idx,sss in enumerate(ss.items()):
        if idx==0:
            first = sss[1]
            continue
        if first != sss[1]:
            return False
    return True
    '''
    L, R = 0, 0
    length = len(s)
    new_cross = 0
    while R < length - 1:
        R += 1
        if s[L] == s[R] and L != R:
            rep = s[L:R]
            if length % (R - L) != 0:
                return False
            print(L, R, 12121)
            for i, j in list(zip(list(range(R, length, R - L)), list(range(2*R-L,length,R-L)))):
                if s[i:j] != s[L:R]:
                    return False
        return True
    return True
