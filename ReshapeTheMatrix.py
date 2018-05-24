'''
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
'''
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        siz = 0
        nc = 0
        lst=[]
        ans = []
        final_ans = []
        for arr in nums:
            siz = siz + len(arr)
        
        if not(siz == (r*c)):
            return nums
        else:
            for arr in nums:
                for a in arr:
                    lst.append(a)
            for i in range(0,r):
                if(i>0):
                    nc=c*i
                for j in range(0+nc,c+nc):
                #for i in range(0,c):
                    ans.append(lst[j])
                    
                    # lst.append(j)
                    # del lst[j]
                
                final_ans.append(ans)
                ans = []
            return final_ans
