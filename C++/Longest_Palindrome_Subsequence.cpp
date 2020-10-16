class Solution {
public:
    int longestPalindromeSubseq(string s) {
        string s2 = string(s.rbegin(),s.rend());
        int dp[s.size() + 1][s2.size()+1];
        
        for(int i = 0 ; i< s.size() + 1 ; i++){
            dp[i][0] = 0;
        }
        for(int i = 1 ; i< s2.size() + 1 ; i++){
            dp[0][i] = 0;
        }
        
        for(int i = 1 ; i<= s.size() ; i++){
            for(int j = 1 ; j<= s2.size() ; j++){
                if(s[i-1] == s2[j-1]){
                    dp[i][j] = dp[i-1][j-1] + 1;
                }else{
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1]);
                }
            }
        }
        
        return dp[s.size()][s2.size()];
    }
};
