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
class Solution:
    def combine( n: int, k: int):
        '''
        使用python函数库的方式
        :param k:
        :return:
        '''
        return list(itertools.combinations(list(range(1,n+1)),k))



