# 题目来自于京东2019校招

#!/bin/python
# -*- coding: utf8 -*-
# 时间限制：C/C++语言 1000MS；其他语言 3000MS
# 内存限制：C/C++语言 65536KB；其他语言 589824KB
# 题目描述：
# 对于仅由小写字母组成的字符串A和B，如果分别存在一个小写字母a到z的排列，使得将A中所有字母a替换为排列的第一个字母，所有字母b替换为排列的第二个字母……所有字母z替换为排列的最后一个字母之后，A和B完全相同，那么称字符串A和B相似，如abcc和xyaa。现在给定仅由小写字母组成且长度不超过105的字符串S和T，求S中有多少子串与T相似？
#
# 输入
# 第一行和第二行分别输入字符串S和T。
#
# 输出
# 输出字符串S中与T相似的子串数目。
#
#
# 样例输入
# ababcb
# xyx
# 样例输出
# 3
#
# Hint
# 样例解释
# S中与T相似的子串分别是aba、bab、bcb，总共3个。

import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************
def solve(S, T):
    l_sub_S_num = []
    for i in range(len(S)-len(T)+1):
        sub_S = S[i:i+len(T)]
        count = 0
        l_count = []
        sub_S_num = ''

        for j in range(len(sub_S)):
            if sub_S[0:j].count(sub_S[j]) == 0:
                count += 1
                l_count.append(count)
                sub_S_num += str(count)
            else:
                l_count.append(count)
                # print(sub_S.index(sub_S[j]))
                sub_S_num += str(l_count[sub_S.index(sub_S[j])])
                # print(sub_S_num)
        l_sub_S_num.append(sub_S_num)
    # print(l_sub_S_num)
    count = 0
    l_count = []
    T_num = ''
    for k in range(len(T)):
        if T[0:k].count(T[k]) == 0:
            count += 1
            l_count.append(count)
            T_num += str(count)
        else:
            l_count.append(count)
            # print(sub_S.index(sub_S[j]))
            T_num += str(l_count[T.index(T[k])])
    # print(T_num)
    count = 0
    for i in range(len(l_sub_S_num)):
        if l_sub_S_num[i] == T_num:
            # print(l_sub_S_num[i])
            count += 1
    return count


S = 'ababcb'
T = 'xyx'
solve(S, T)









# ******************************结束写代码******************************

#
# try:
#     _S = raw_input()
# except:
#     _S = None
#
# try:
#     _T = raw_input()
# except:
#     _T = None
#
# res = solve(_S, _T)
#
# print str(res) + "\n"
