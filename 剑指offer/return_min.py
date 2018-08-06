# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        self.rotateArray = rotateArray
        if len(self.rotateArray) == 0:
            return 0
        else:
            self.rotateArray = sorted(self.rotateArray)
            return self.rotateArray[0]