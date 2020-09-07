#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Ante Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: tencent.py
@time: 2020-08-23 下午 9:32
"""
n,m,k=5,3,2

two_way = [[1,2],[2,3],[3,4]]
gate = [[4,5],[1,2]]

table = [[float('inf')]*(n+1) for _ in range(n+1)]
print(table,12121)
for i,j in gate:
    table[i][j] = 0
for i,j in two_way:
    table[i][j]=1
print(table,23232)

for row in range(1,n+1):
    for col in range(1,n+1):
        if row >= col and table[row][col]==float('inf'):
            table[row][col] = min(
                table[row-1][col],
                table[row][col-1],
                table[row-1][col-1],
            )
        else:
            print('None')
print(table[-1][-1])


