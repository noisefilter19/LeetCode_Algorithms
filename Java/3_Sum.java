//Problem Link: https://leetcode.com/problems/3sum/
// Problem Description:
/* Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
 * Find all unique triplets in the array which gives the sum of zero.
 * Notice that the solution set must not contain duplicate triplets.
 
 * Input: nums = [-1,0,1,2,-1,-4]
 * Output: [[-1,-1,2],[-1,0,1]]
 */

//Solution

class Solution {
    // function threeSum takes an array of integers as a argument
    // returns a list of lists of integers
    public List<List<Integer>> threeSum(int[] nums) {
        int i = 0, j = 0;
        Arrays.sort(nums);
    
        List<List<Integer>> res = new ArrayList();
        
        for(int k = 0; k < nums.length-1; k++) {
            i = k + 1;
            j = nums.length-1;
            int ele = nums[k];
            
            if (k > 0 && nums[k] == nums[k-1])  continue;
            
            while ( i < j){
                
                if (i-1 > k &&  nums[i] == nums[i-1]) {
                    i++;
                    continue;
                }
                
                if ( -ele == nums[i] + nums[j]) {
                    List<Integer> list = new ArrayList();
                    list.add(ele);
                    list.add(nums[i]);
                    list.add(nums[j]);
                    
                    res.add( new ArrayList(list) );
                    i++;
                    j--;
                }
                else if (-ele > nums[i] + nums[j])  i++;
                else  j--;                                   
            }
        } 
        return res;
    }
}
