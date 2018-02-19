//Given an array of integers, return indices of the two numbers such that they add up to a specific target.

public class Solution {
    int[] result = new int[2];
    int flag=0;
    public int[] TwoSum(int[] nums, int target) {
        for(int i=0; i<nums.Length; i++){
            for(int j=(i+1); j<nums.Length; j++){  
                if(i!=j){
                    if(nums[i]+nums[j]==target){
                        result[0]=i;
                        result[1]=j;
                        flag = 1;
                        break;
                    }
                }
            }
            if(flag==1){
                break;
            }
        }
      return result;
    }
}
