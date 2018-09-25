class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        m1 = A[0] # max
        m2 = A[0] # min
        for num in A:
            if num > m1:
                m1 = num
            elif num < m2:
                m2 = num
        # m1 = max(A)
        # m2 = min(A)
        d = m1-m2-K*2
        if d<=0:
            return 0
        else:
            return d