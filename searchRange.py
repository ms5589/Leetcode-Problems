# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        if target in nums:
            count=0
            for n in nums:
                if(n==target):
                    val1 = count
                    result.append(val1)
                    break
                count=count+1
            for n in range(len(nums)-1,-1,-1):
                if(nums[n]==target):
                    val2 = n
                    result.append(val2)
                    break
            return result
        else:
            return [-1,-1]
