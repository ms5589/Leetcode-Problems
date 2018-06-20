''' Initially, there is a Robot at position (0, 0). 
Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.
The move sequence is represented by a string. And each move is represent by a character. 
The valid robot moves are R (Right), L (Left), U (Up) and D (down). 
The output should be true or false representing whether the robot makes a circle. '''

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        up =0
        left =0
        right =0
        down =0
        
        for move in moves:
            if(move =='U'):
                up = up +1
            if(move =='L'):
                left = left +1
            if(move =='R'):
                right = right +1
            if(move =='D'):
                down = down +1
        if (up==down) and (left==right):
            return True
        else:
            return False
