class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<vector<int>> dp(nums.size()+1,vector<int>(nums.size()+1,0));
        vector<int> a;
        vector<int> s=nums;
        sort(s.begin(),s.end());
        a.push_back(s[0]);
        for(int i=1;i<s.size();i++){
            if(s[i]!=s[i-1])
                a.push_back(s[i]);
        }
        for(int i=0;i<nums.size();i++){
            for(int j=0;j<a.size();j++){
                if(nums[i]==a[j]){
                    dp[i+1][j+1]=1+dp[i][j];
                }else{
                    dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1]);
                }
            }
        }
        return dp[nums.size()][a.size()];
    }
};
