# My answer beats 25% of submissions:
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        A_out = []
        for i in range(len(A)):
            B = []
            for j in range(len(A[i])):
                B.append(1-A[i][len(A[i]) - j - 1])
            A_out.append(B)
        return A_out


# There is a code beats 70% of others
class Solution:
    def flipAndInvertImage(self, A):
        res = []
        for i in A:
            res.append([0 if x == 1 else 1 for x in i][::-1])
        return res
# and to explain [::-1]:
# Assumming a is a string. The Slice notation in python has the syntax -
# list[<start>:<stop>:<step>]
# So, when you do a[::-1] , it starts from the end, towards the first, taking each element. So it reverses a. This is applicable for lists/tuples as well.
# Example:
# >>> a = '1232'
# >>> a[::-1]
# '2321'