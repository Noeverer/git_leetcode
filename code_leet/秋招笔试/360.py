#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Ante Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: 360.py
@time: 2020-08-22 下午 8:43
"""

N,M = [4,3]
# print(N,M,12121)
nums = [1,2,1]

# print(nums,232322)
N_list = [i for i in range(1,N+1)]
def mov1(li):
    li.append(li[0])
    return li[1:]
def mov2(li):
    for i in range(0,len(li)-1,2):
        temp = li[i+1]
        li[i+1] = li[i]
        li[i] = temp
    return li[:]
for mov in nums:
    if mov==1:
        N_list = mov1(N_list)[:]
    elif mov ==2:
        N_list = mov2(N_list)[:]
print(N_list)


'''while 1:
    N,M = [int(i) for i in input().split()]
    # print(N,M,12121)
    nums = []
    for _ in range(M):
        nums+=[int(i) for i in input().split()]
    # print(nums,232322)
    N_list = [i for i in range(1,N+1)]
    def mov1(li):
        li.append(li[0])
        return li[1:]
    def mov2(li):
        for i in range(0,len(li)-1,2):
            temp = li[i+1]
            li[i+1] = li[i]
            li[i] = temp
        return li[:]
     for mov in nums:
        if mov==1:
            N_list = mov1(N_list)[:]
        elif mov ==2:
            N_list = mov2(N_list)[:]
    print(' '.join(N_list))
    break'''
