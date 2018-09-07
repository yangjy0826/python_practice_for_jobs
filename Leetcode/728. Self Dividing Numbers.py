class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l_out = []
        for i in range(left,right+1):
            if 0<i<10:
                l_out.append(i)
            else:
                string = str(i)
                count = 0
                for j in range(len(string)):
                    if string[j] == '0':
                        break
                    if i%int(string[j]) == 0:
                        count+=1
                if count == len(string):
                    l_out.append(i)
        return l_out