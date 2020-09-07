#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Ante Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: 中兴.py
@time: 2020-09-03 下午 8:48
"""

n, m, k = 3, 10 ,1000
# price = []
# for _ in range(n):
#     price.append(list(map(int, input().split())))
# print(price, 232323)
price=[[100, 5 ,3],[50, 3, 2],[300,3 ,3]]

weights = []
costs = []
like = []
for pri in price:
    weights.append(pri[1])
    costs.append(pri[0])
    like.append(pri[2])

print(weights,costs,like)
def back(weight, count, weights, costs):
    preline, curline = [0] * (weight + 1), [0] * (weight + 1)
    for i in range(count):
        for j in range(weight + 1):
            if weights[i] <= j:
                curline[j] = max(preline[j], 1 + preline[j - weights[i]])
        preline = curline[:]
    return curline


res = back(m, n, weights, costs)
print(res)
