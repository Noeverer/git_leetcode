#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Ante Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: xiecheng.py
@time: 2020-09-08 下午 7:37
you
i love you,oyu love me
jack
"""
import collections,itertools
#while 1:
    #for _ in range(3):
w ='you' #input().split()
s = 'i love you,oyu love me'#input().split()
r = 'jack'#input().split()
res = collections.Counter(w)
ans =[]
i=0
j=1
while j<len(s):
    t =s[j]
    d =ord(t)
    if (90<d<97) or d<65 or d>122:
        word = s[i:j]
        if collections.Counter(word)==ans:
            ans.append(r)
        else:
            ans.append(word)
        ans.append(s[j])
        i=j+1
    j+=1
word=s[i:j]
if j-i==len(w) and collections.Counter(word)==res:
    ans.append(r)
else:
    ans.append(word)
print(''.join(ans))












# mm_cc =[''.join(i) for i in list(itertools.permutations('you',len('you')))]
# print(mm_cc,12121)
# for mm_cces in mm_cc:
#     sent = sent.replace(mm_cces,re_word)
# print(sent)


# for se in range(len(sent)):
#     see = sent[se:se+len(m_word)]
#     mm_c = collections.Counter(see)
#     if mm_c == m_c:
#         print(see)


