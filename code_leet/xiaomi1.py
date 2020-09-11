#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Ante Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: xiaomi1.py
@time: 2020-09-08 下午 8:22


you
i love you,oyu love me
jack
"""
import itertools,collections,re
m_word = 'you'
sent = 'i love your,oyu love me'
re_word = 'jack'

m_c = collections.Counter(m_word)
mm_cc = [''.join(i) for i in list(itertools.permutations(m_word, len(m_word)))]
# sent = ''.join(sent.replace(',', ' ').replace('.', ' ').split(' '))
sentsent = sent.split()

# for idx,sen in enumerate(sent.split()):
#     if ',' in sen:
#         sentsent.pop(idx)
#     for id_se,se in enumerate(sen.split(',')):
#         sentsent.insert(idx+id_se,se)
#
# for id_ss,ss in enumerate(sentsent):
#     if len(ss)==len(m_word) and collections.Counter(ss) == m_c:
#         sentsent[id_ss]=re_word
# print(sentsent)
# mm_cc = [''.join(i) for i in list(itertools.permutations(m_word, len(m_word)))]
# sent = ''.join(sent.replce(',',' ').replace('.',' ').split(' '))
for mm_cces in mm_cc:
    sent = re.sub(r'', re_word)
print(sent)








    #sent = sent.replace(mm_cces, re_word)
