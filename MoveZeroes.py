'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Example:
Input: [0,1,0,3,12], Output: [1,3,12,0,0]
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index=0
        dup=nums
        if (0 in dup):
            for n in dup:
                print n
                if(n==0):
                    nums.insert(len(nums), 0)
                    nums.remove(n)
                index=index+1    
