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