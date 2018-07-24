'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        f=[]
        s=[]
        
        while not(l1 is None):
            print l1.val
            f.append(str(l1.val))
            l1=l1.next
        
        while not(l2 is None):
            print l2.val
            s.append(str(l2.val))
            l2=l2.next
        
        f=f[::-1] #reverse the elements in f
        s=s[::-1]
        
        f= ''.join(f[0:len(f)]) #join the character to a string
        s= ''.join(s[0:len(s)])
        
        ans = str(int(f)+int(s))
        
        ans = ans[::-1]
        ansList = []
        
        for x in ans:
            ansList.append(int(x))
            
        return ansList
        
