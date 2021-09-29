from math import inf

class Solution:
    dp=[]
    def initDP(self,n):
        self.dp=[[-1 for i in range(n+1)] for j in range(n+1)]
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        self.initDP(n)
        return(self.minCost([1]+nums+[1],1,n))
    
    
    def minCost(self,m,i,j):

        if(i==j):
            return m[i-1]*m[i]*m[i+1]
        if(i>j):
            return 0
        
        if(self.dp[i][j]!=-1):
            return self.dp[i][j]
        mini=0
        for k in range(i,j+1):
            val=self.minCost(m,i,k-1)+self.minCost(m,k+1,j)+m[i-1]*m[k]*m[j+1]
            mini=max(mini,val)
        self.dp[i][j]=mini
        return mini
