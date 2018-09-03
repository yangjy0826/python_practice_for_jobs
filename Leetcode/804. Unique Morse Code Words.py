class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        l = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        l_t = []
        for i in range(len(words)):
            transformation = ''
            for j in range(len(words[i])):
                transformation += l[ord(words[i][j])-97]
            l_t.append(transformation)
        return len(list(set(l_t)))