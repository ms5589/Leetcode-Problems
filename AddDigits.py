'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
Input: 38
Output: 2 (Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.)
'''
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        word = str(num)
        num_dup = num
        while (num_dup > 9):
            #print num_dup
            word = str(num_dup)
            num_dup = 0
            for i in word:
               num_dup = num_dup + int(i)
        return num_dup
