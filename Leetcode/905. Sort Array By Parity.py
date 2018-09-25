# Example
# 1:
#
# Input: [3, 1, 2, 4]
# Output: [2, 4, 3, 1]
# The
# outputs[4, 2, 3, 1], [2, 4, 1, 3], and [4, 2, 1, 3]
# would
# also
# be
# accepted.
#
# Note:
#
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = []
        C = []
        for nums in A:
            if nums % 2 == 0:
                B.append(nums)
            else:
                C.append(nums)
        return B + C
