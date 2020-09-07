#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Ante Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: 332. 重新安排行程.py
@time: 2020-08-27 下午 3:54
"""

def findItinerary(tickets):
        def check(s1,s):
            def sort_help(s1,s2):
                for i in range(min(len(s1),len(s2))):
                    if ord(s1[i]) > ord(s2[i]):
                        return 0
                    elif ord(s1[i]) == ord(s2[i]):
                        continue
                    elif ord(s1[i]) < ord(s2[i]):
                        return 1
                if len(s1)>len(s2):
                    return 0
                else:
                    return 1
            s.insert(0,s1)
            for s_idx in range(1,len(s)):
                if sort_help(s[s_idx-1],s[s_idx]) == 0:
                    temp = s[s_idx]
                    s[s_idx] = s[s_idx-1]
                    s[s_idx-1] = temp
            return s

        d_tic = {}
        for ticket in tickets:
            if ticket[0] in d_tic:
                new_ticket = check(ticket[1],d_tic[ticket[0]])
                d_tic[ticket[0]] = new_ticket
            else:
                d_tic[ticket[0]] = [ticket[1],]
        print(d_tic,12121)
        res = ['JFK']
        start = 'JFK'
        while d_tic.get(start):
            res.append(d_tic.get(start)[0])
            d_tic[start].pop(0)
            start = res[-1]
        print(res)
        return res



# findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]


import collections,heapq
def findItinerary1(tickets):
    def dfs(curr):
        while vec[curr]:
            tmp = heapq.heappop(vec[curr])
            dfs(tmp)
        stack.append(curr)
    vec = collections.defaultdict(list)
    for key,val in tickets:
        vec[key].append(val)
    for key in vec:
        heapq.heapify(vec[key])
    # print(vec.items(),heapq)

    stack = list()
    dfs("JFK")
    print(stack[::-1])
findItinerary1(tickets)


