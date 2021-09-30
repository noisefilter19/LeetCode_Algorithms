/* https://leetcode.com/problems/contains-duplicate-iii/

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false 

Constraints:
    0 <= nums.length <= 2 * 104
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 104
    0 <= t <= 231 - 1
*/


// Runtime : 20 ms


bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
    if(nums.size()==1 || nums.size()==0)        // If the size of the vector is 0 or 1, false is returned.
        return false;
    for(int i=0;i<nums.size()-1;i++)
    {
        for(int j=i+1;j<nums.size();j++)
        {
            if((j-i)>k)                         // Checking every possible pair for the given conditions.
                break;
            long long l=abs(nums[j]-nums[i]);
            if(l<=t)
                return true;
        }
    }
    return false;
}
