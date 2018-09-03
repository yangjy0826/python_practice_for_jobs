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

# class Solution(object):e
#     def hammingDistance(self, x, y):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#
#         result = str(bin(x ^ y)[2:])
#
#         return result.count("1")