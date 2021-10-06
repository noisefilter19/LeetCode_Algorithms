/*
  *Solution to :- Minimize Maximum Pair Sum in Array
  *Author :- hitesh22rana
  *ref :- https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
*/

class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int i = 0 , j = nums.length-1;
        int ans = -1;
        
        while(i < j) {
            ans = Math.max(nums[i] + nums[j] , ans);
            i++;
            j--;
        }
        return ans;
    }
}