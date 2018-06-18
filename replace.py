# 题目来自《剑指offer》
# 请实现一个函数，将一个字符串中的空格替换成“%20”。
# 例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def __init__(self,s):
        self.s = s

    def replaceSpace(self):
        # write code here
        '''
        s_replace = self.s.replace(' ', '%20')
        return s_replace
        '''
        s_replace = ''
        for i in range(len(self.s)):
            if self.s[i] == ' ':
                s_replace = s_replace + '%20'
            else:
                s_replace = s_replace + self.s[i]
        return s_replace


str1 = 'We Are Happy'
out1 = Solution(str1)
Result = out1.replaceSpace()
print(Result)
