//LeetCode Problem link - https://leetcode.com/problems/longest-palindromic-substring/

class Solution {
public:
    string longestPalindrome(string str) {
        int n=str.length();
        vector<vector<int>> dp(n,vector<int>(n,0));
        int maxLen=-10,si=0,ei=0;
        for(int gap=0;gap<n;gap++)
        {
            for(int i=0,j=gap;j<n;i++,j++)
            {
                if(gap==0)
                    dp[i][j]=1;
                else if(gap==1 && str[i]==str[j])
                    dp[i][j]=2;
                else if(str[i]==str[j] && dp[i+1][j-1]!=0)
                {   
                        dp[i][j]=gap+1;
                }
                if(dp[i][j]>maxLen)
                    {
                        maxLen=dp[i][j];
                        si=i;
                        ei=j;
                    }
            }
        }
        
        return str.substr(si,ei-si+1);
    }
};
