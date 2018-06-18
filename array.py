# 题目来自《剑指offer》
# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# -*- coding:utf-8 -*-
# import numpy as np


class Solution:
    # array 二维列表
    # def Find(self, target, array):
    def __init__(self, target, array):
        # write code here
        self.target = target
        self.array = array

    def Find(self):
        c = 0
        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                if self.array[i][j] == self.target:
                    c += 1
        if c == 0:
            return False
        else:
            return True


tar = 7
# arr = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])
arr = [[1, 2, 8, 9], [4, 7, 10, 13]]
obj = Solution(tar, arr)
Result = obj.Find()
print(Result)
'''
c = 0
# for i in range(obj.array.shape[0]):
# for j in range(obj.array.shape[1]):
for i in range(len(obj.array)):
    for j in range(len(obj.array[0])):
        if obj.array[i][j] == obj.target:
            c += 1
if c == 0:
    print("false")
else:
    print("true")
'''
