#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Ante Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: 322. 零钱兑换.py
@time: 2020-08-21 下午 12:36
"""
'''
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1

示例 2:

输入: coins = [2], amount = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution1:
    # 带字典的解法
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(count):
            if count in memo:
                return memo[count]
            if count==0:
                return 0
            if count < 0:
                return -1
            res = float("inf")
            for coin in coins:
                if dp(count-coin)==-1:
                    continue
                res = min(res,1+dp(count-coin))
            memo[count] = res if res != float("inf") else -1
            return memo[count]
        return dp(amount)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        暴力解法：利用递归的解法
        '''
        # def dp(amount):
        #     if amount < 0:
        #         return -1
        #     if amount == 0:
        #         return 0
        #     res = float('inf')
        #     for coin in coins:
        #         subproblem = dp(amount-coin)
        #         if subproblem==-1:
        #             continue
        #         res = min(subproblem + 1,res)
        #     return res if res != float('inf') else -1
        # return dp(amount)


    # dp table的解法
    def coinChange1(self, coins: List[int], amount: int) -> int:
        '''
        带dp table字典的解法:很聪明的自底向上
        '''
        dp = [float('inf') for i in range(amount+1)]
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin<0:
                    continue
                dp[i] = min(dp[i],1+dp[i-coin])
        return dp[-1] if dp[-1] != float('inf') else -1




