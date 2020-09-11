#!/usr/bin/python3.6
#coding:utf-8

"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import itertools

def combine( n: int, k: int):
    '''
    使用python函数库的方式
    '''
    return list(itertools.combinations(list(range(1,n+1)),k))



def combine2( n: int, k: int):
    '''
    使用回溯的方式需要注意位置信息的更新：是从第
    '''
    res = []
    def back(curr,site):
        if len(curr) == k:
            res.append(curr[:])
        for sit in range(site,n+1):
            if sit in curr:
                continue
            curr.append(sit)
            back(curr,sit+1) # 相当于限定下一次座位只能从我后面以为去做
            curr.pop()
    back([],1)
    return res

print(combine2(4,2))


