# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
# You may return any answer array that satisfies this condition.
#
# Example
# 1:
# Input: [4, 2, 5, 7]
# Output: [4, 5, 2, 7]
# Explanation: [4, 7, 2, 5], [2, 5, 4, 7], [2, 7, 4, 5] would also have been accepted.
#
# Note:
# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000

class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        N = len(A)
        for i in range(N):
            if A[i]%2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        A_new = []
        for j in range(int(N/2)):
            A_new.append(even[j])
            A_new.append(odd[j])
        return(A_new)

# Others' faster code:
# class Solution(object):
#     def sortArrayByParityII(self, A):
#         N = len(A)
#         ans = [None] * N
#
#         t = 0
#         for i, x in enumerate(A):
#             if x % 2 == 0:
#                 ans[t] = x
#                 t += 2
#
#         t = 1
#         for i, x in enumerate(A):
#             if x % 2 == 1:
#                 ans[t] = x
#                 t += 2
#
#         # We could have also used slice assignment:
#         # ans[::2] = (x for x in A if x % 2 == 0)
#         # ans[1::2] = (x for x in A if x % 2 == 1)
#
#         return ans