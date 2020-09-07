#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Ante Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: jd.py
@time: 2020-08-27 下午 8:11
"""


'''
3
    1
  2 1 2
3 4 2 1 3
'''
n=3
num = [[1],[2,1,2],[3,4,2,1,3]]
if 0<n<=100:
    print(212121)


import itertools
path = num[0]
for i in range(1,n):
    path = list(sum(m)  for m in list(itertools.product(set(path),set(num[i]))))
print(max(path))


# ll = itertools.product(set(num[1]),set(num[2]))
# print(max([sum(i) for i in list(ll)]))






# def dfs(path,curr):
#     if len(curr) == n:
#         return curr
#     for pa in num[len(curr):]:
#         curr.append(pp)
#         dfs(curr)
#         curr.pop()
# res = dfs(path=0,[])
# print(res)