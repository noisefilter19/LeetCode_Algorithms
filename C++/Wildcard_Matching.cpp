
https://leetcode.com/problems/wildcard-matching/

class Solution {
public:
    bool isMatch(string s, string p) {
        const int a =s.size();
        const int b =p.size();
        bool dp[a+1][b+1];
        dp[0][0]=1;
        for(int i=1;i<=s.size();i++){
            dp[i][0]=0;
        }
        for(int i=1;i<=p.size();i++){
            if(p[i-1]=='*' and dp[0][i-1]==1){
                dp[0][i]=1;
            }else{
                dp[0][i]=0;
            }
        }
        for(int j=0;j<p.size();j++){
            for(int i=0;i<s.size();i++){
                if((s[i]==p[j] or p[j]=='?') and(dp[i][j]==1)){
                    dp[i+1][j+1]=1;
                }else if(p[j]=='*'){
                    if(dp[i+1][j]==1 or dp[i][j+1]==1){
                        dp[i+1][j+1]=1;
                    }else{
                        dp[i+1][j+1]=0;
                    }
                }else{
                    dp[i+1][j+1]=0;
                }
            }
        }
        return dp[a][b];
    }
};