class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        n_out = 0
        for i in range(len(J)):
            for j in range(len(S)):
                if S[j] == J[i]:
                    n_out += 1
        return n_out