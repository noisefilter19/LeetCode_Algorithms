class Solution {
public:
    void generateSubset(vector<int> &nums, int i, int j, vector<int> &ans) {
        if (i == j) {
            ans.push_back(0);
            return;
        }
        vector<int> temp;
        generateSubset(nums, i + 1, j, ans);
        for (auto key: ans) {
            temp.push_back(key);
            temp.push_back(key + nums[i]);
        }
        
        ans = temp;
    }
    
    int minAbsDifference(vector<int>& nums, int goal) {
        vector<int> left, right;
        
        generateSubset(nums, 0, nums.size()/2, left);
        generateSubset(nums, nums.size()/2, nums.size(), right);
        sort(left.begin(), left.end());
        sort(right.begin(), right.end());
        
        int ans = abs(goal);
        
        for (int left_: left) {
            int y = goal - left_;
            int i = lower_bound(right.begin(), right.end(), y) - right.begin();
            if(i) ans = min(ans, abs(right[i-1]-y));
            if(i < right.size()) ans = min(ans, abs(right[i]-y));
          }
        
        return ans;
    }
};