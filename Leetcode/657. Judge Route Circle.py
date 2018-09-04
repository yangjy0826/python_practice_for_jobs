# My answer only beats 20% of the submissions
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        p = [0, 0]
        for i in range(len(moves)):
            if moves[i] == 'U':
                p[1] += 1
            elif moves[i] == 'D':
                p[1] -= 1
            elif moves[i] == 'R':
                p[0] += 1
            else: # moves[i] == 'L'
                p[0] -= 1
        if p == [0,0]:
            return True
        else:
            return False

# A code that beats 100%:

def judgeCircle(self, moves):
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')