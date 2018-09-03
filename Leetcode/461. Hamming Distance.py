# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.

# My code only beats 20% submissions:
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        str_x = bin(x)[2:]
        str_y = bin(y)[2:]
        # print(str_x,str_y)
        if len(str_x) == len(str_y):
            pass
        elif len(str_x) > len(str_y):
            for i in range(len(str_x) - len(str_y)):
                str_y = '0' + str_y
        else: # len(str_x) < len(str_y)
            for i in range(len(str_y) - len(str_x)):
                str_x = '0' + str_x
        # print(str_x,str_y)
        hamming = 0
        for i in range(len(str_x)):
            if str_x[i] != str_y[i]:
                hamming += 1
        return hamming

# Here is a code beats 100% submissions:
# class Solution(object):e
#     def hammingDistance(self, x, y):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#
#         result = str(bin(x ^ y)[2:])   # ^是Python中的异或运算。比如x = 1, y = 4 时，x^y = 5
#
#         return result.count("1")
