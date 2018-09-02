# You're given strings J representing the types of stones that are jewels, and S representing the stones you have. 
# Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. 
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:

# Input: J = "aA", S = "aAAbbbb"
# Output: 3
# Example 2:

# Input: J = "z", S = "ZZ"
# Output: 0
# Note:

# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.


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
 
# There is a solution using one line python which beats 100% of other users:
# return sum([i in J for i in S])
# The idea of his coding is:
# I did the mistake of checking J in S, what kanikel doing is reverse. he is checking if S in J, that's smart. 
# [i in J for i in s] means, for every element of S, check if its in J. 
# So for example if you run with J = "aA" , S = "aAAbbbb", i in j, return True or False. For this example output will be 
# [True, True, True, False, False, False, False]. If you take sum of this True=1, False =0, this will return 3.
