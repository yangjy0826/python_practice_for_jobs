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