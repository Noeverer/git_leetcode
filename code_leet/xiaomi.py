#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Ante Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: xiaomi.py
@time: 2020-09-08 下午 6:59
"""
while 1:

    def exist(board,word):
        n,m = len(board),len(board[0])
        def nei(i,j):
            for r,c in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0<=r<n and 0<=r<m:
                    yield r,c
        def track(i,j,l=0):
            if l==len(word)-1 and board[i][j]==word[l]:
                return True
            if board[i][j] ==word[l]:
                board[i][j]='.'
                for r,c in nei(i,j):
                    if track(r,c,l+1):
                        return True
                board[i][j]=word[l]
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if track(i,j):
                        return True
        return False
