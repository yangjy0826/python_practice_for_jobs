class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = []
        for num in A:
            B += num
        C = []
        l = len(A[0])
        for i in range(l):
            C.append(B[i::l])
        return C
