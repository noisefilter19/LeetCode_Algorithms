class Solution {
public:
    int jump(vector<int>& nums) {
        vector<int> dp(nums.size(),100001);
        int maxJumps;
        dp[0]=0;
        for(int i=0;i<nums.size();i++){
            maxJumps=nums[i];
            for(int j=i+1;(j<=(i+maxJumps)&&(j)<nums.size());j++){
                dp[j]=min(dp[j],dp[i]+1);
                // cout<<i<<" "<<j<<" "<<dp[j]<<endl;
            }
            // cout<<i<<endl;
        }
        return dp[nums.size()-1];
    }
};
