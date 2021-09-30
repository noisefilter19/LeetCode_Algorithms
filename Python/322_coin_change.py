# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        n=len(coins)
        for i in range(1, amount+1):
            for j in range(0, n):
                if(coins[j]<=i):
                    dp[i]=min(dp[i],dp[i-coins[j]]+1)
        if dp[amount]>amount:
            return -1
        else:
            return dp[amount]
                
            
        
