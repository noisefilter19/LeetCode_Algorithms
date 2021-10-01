//https://leetcode.com/problems/maximal-square/


//This algorithm finds the maximum size of square(area of square) that contains all ones in the given m*n matrix.
//This solution takes O(rows*columns) time and O(columns) space (m=rows, n=columns).

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int rows=matrix.size(),cols;
        if(rows==0)return 0;
        cols=matrix[0].size();
        int ans=0,i,j;
        //This solution uses only O(columns) extra space instead of traditional O(rows*columns) space.
        int dp[2][cols];
        for(i=0;i<cols;i++)
        {
            dp[0][i]=matrix[0][i]-'0';
            ans=max(ans,dp[0][i]);
        }
        //We use two flag variables to alternate between the rows of dp matrix, thus saving space.
        bool f1=1,f2=0;
        for(i=1;i<rows;i++)
        {
            for(j=0;j<cols;j++)
            {
                if(j==0)dp[f1][j]=matrix[i][j]-'0';
                else if(matrix[i][j]=='0')
                {
                    dp[f1][j]=0;
                }
                else dp[f1][j]=1+(min(dp[f2][j-1],min(dp[f2][j],dp[f1][j-1])));
                ans=max(ans,dp[f1][j]);
            }
            f1^=1;f2^=1;
        }
        return ans*ans; //ans is side of square, so return (ans*ans) to get area of square.
    }
};
