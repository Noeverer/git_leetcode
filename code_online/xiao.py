#!/usr/bin/python3.6
#coding:utf-8

"""
@author: Ante Liu
@contact: robotliu0327@gmail.com
@software: PyCharm
@file: xiao.py
@time: 2020-08-30 下午 7:42
"""

n,m = 3,4
# 3 4
# beef 1
# noodle 2
# chicken 1
#
# jack order beef
# jack release beef
# jack order chicken
# rose order chicken

m_inps = ['jack order beef','jack release beef','jack order noodle','jack1 order noodle','rose order noodle','rose order beef']
food_num = {'beef':1,'noodle':2,'chicken':1}
order_food = {} # name : food

def pl(food_num,order_food):
    for mm in m_inps:
        m_inp = list(mm.split(' '))
        if m_inp[1] == 'order':
            if order_food.get(m_inp[0])==None and food_num[m_inp[2]] > 0:  # 没点餐，还用餐可用,点餐数为一
                    order_food[m_inp[0]] = m_inp[2]
                    food_num[m_inp[2]] -= 1
                    print('yes12121')
                # else:
                #     print('no45454')
            # elif order_food.get(m_inp[0])!=None and:
            #     print('no343434')
            else:
                print('no454545')
        elif m_inp[1] == 'release':  # 释放餐
            if order_food.get(m_inp[0]):
                order_food.pop(m_inp[0])
                food_num[m_inp[2]] += 1
                print('yes232323')
    print(m_inp, 232323)

pl(food_num,order_food)
