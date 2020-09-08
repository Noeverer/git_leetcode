#!/usr/bin/python3.6
#coding:utf-8

"""
岛屿问题

"""

while 1:
    M,N = list(map(int,input().split(',')))
    inp = []
    # print(M,N,34343)
    for i in range(M):
        inpp = input().split()[0]
        inpu = []
        for m in inpp:
            inpu.append(m)
        inp.append(inpu)
    print(inp,1212121)
    def dfs(inp,r,c):
        inp[r][c]='S'
        for x,y in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if x>=0 and x<M and y>=0 and y<N and inp[x][y]=='H':
                dfs(inp,x,y)
    def nums(inp,M,N):
        if M==0:
            return 0
        num_is = 0
        for r in range(M):
            for c in range(N):
                if inp[r][c]=='H':
                    num_is += 1
                    dfs(inp,r,c)
        return num_is
    print(nums(inp,M,N))
    break