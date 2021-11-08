/* https://leetcode.com/problems/search-in-rotated-sorted-array/ */
class Solution {
public:
    int search(vector<int>& nums, int target) {
        if(nums.size() == 0)
            return -1;
        
        int mid, l = 0, r = nums.size()-1;
        
        while(l <= r) {
            mid = (l+r)/2;
            if(nums[mid] == target)
                return mid;
            if(nums[mid] > nums[r]) {
                if(target < nums[mid] && target >= nums[l]) {
                    r = mid-1;
                }
                else {
                    l = mid+1;
                }
            }
            else if(nums[mid] < nums[l]){
                if(target <= nums[r] && target > nums[mid])
                    l = mid+1;
                else
                    r = mid-1;
            }
            else {
                if(target > nums[mid])
                    l = mid+1;
                else
                    r = mid-1;
            }
        }
        
        return -1;
        
    }
};
