class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int>ans(2);
        auto low = lower_bound(nums.begin(), nums.end(), target);
        ans[0] = low - nums.begin();
        auto high = upper_bound(nums.begin(), nums.end(), target);
        ans[1] = high - nums.begin() - 1;
        if(low == nums.end() || *low != target) 
            ans[0] = ans[1] = -1;
        return ans;
    }
};
