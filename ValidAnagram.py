'''
Given two strings s and t , write a function to determine if t is an anagram of s.
Note: You may assume the string contains only lowercase alphabets.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if(len(s)==len(t)):
            x={}
            for letter in s:
                if(letter in x):
                    x[letter] = x[letter]+1
                else:
                    x[letter] = 1
            y={}
            for letter in t:
                if(letter in y):
                    y[letter] = y[letter]+1
                else:
                    y[letter] = 1
            # print 'x: ',x,' y: ',y
            if(x==y):
                return True
            else:
                return False
        else:
            return False
