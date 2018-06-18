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