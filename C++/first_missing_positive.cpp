class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        vector<bool> nums_map(n+1);
        for (int i = 0; i < n; i++) {
            if(nums[i]<=n && nums[i]>0) { 
                nums_map[nums[i]] = true;
            }
        }
        for (int i=0; i<n; i++) 
            if (!nums_map[i]) 
                return i+1; 
        
        return n+1;
    }
};

