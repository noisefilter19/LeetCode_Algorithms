int dp[1001][1001];

int solve(vector<int>& nums, int i, int j) {
    if(i > j) return 0;
    if(i == j) return nums[i];
    if(dp[i][j] != -1) return dp[i][j];
    dp[i][j] = max({solve(nums,i,j - 2) + nums[j],solve(nums,i + 2,j) + nums[i],solve(nums,i + 1,j - 1)});
    return dp[i][j];
}


class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n == 1) return nums[0];
        memset(dp,-1,sizeof(dp));
        return max(solve(nums,0,n - 2),solve(nums,1,n - 1));
    }
};