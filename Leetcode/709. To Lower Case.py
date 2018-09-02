# The problem is:
# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

# Example 1:

# Input: "Hello"
# Output: "hello"
# Example 2:

# Input: "here"
# Output: "here"
# Example 3:

# Input: "LOVELY"
# Output: "lovely"

# My code beats 100% of others:
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        out_str = ''
        for i in range(len(str)):
            if 97<=ord(str[i])<=122:
                out_str += str[i]
            elif 65<=ord(str[i])<=90:
                out_str += chr(ord(str[i]) + 32)
            else:
                out_str += str[i]
        return out_str
        # return str.lower() #SLOWER
