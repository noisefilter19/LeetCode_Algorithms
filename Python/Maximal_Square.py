class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp=[]
        if len(matrix)==0:
            return 0
        col=len(matrix[0])
        for i in range(len(matrix)+1):
            dp.append([])
            for j in range(col+1):
                dp[i].append(0)
        mx=0
        for i in range(1,len(matrix)+1):
            for j in range(1,col+1):
                if matrix[i-1][j-1]=='1':
                    dp[i][j]=min(dp[i-1][j],min(dp[i-1][j-1],dp[i][j-1]))+1
                    if dp[i][j]>mx:
                        mx=dp[i][j]
        return mx*mx
