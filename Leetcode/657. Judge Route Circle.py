# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, 
#judge if this robot makes a circle, which means it moves back to the original place.

# The move sequence is represented by a string. And each move is represent by a character. 
#The valid robot moves are R (Right), L (Left), U (Up) and D (down). 
#The output should be true or false representing whether the robot makes a circle.

# Example 1:

# Input: "UD"
# Output: true
 

# Example 2:

# Input: "LL"
# Output: false

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
