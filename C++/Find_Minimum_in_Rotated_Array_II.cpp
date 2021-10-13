//https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
class Solution {
public:
    int findMin(vector<int>& nums) {
        int ans=nums[0];
        int n=nums.size();
        int l=0,r=n-1;
        while(l<=r)
        {
            int mid=l+(r-l)/2;
            if(nums[mid]<=nums[r])
                ans=min(ans,nums[mid]);
            if(nums[mid]<nums[r])
                r=mid-1;
            else if(nums[mid]>nums[r])
                l=mid+1;
            else
                r--;
        }
        return ans;
    }
};