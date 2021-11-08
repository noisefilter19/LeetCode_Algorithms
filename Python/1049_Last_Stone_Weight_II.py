# Problem Link: https://leetcode.com/problems/last-stone-weight-ii/

"""
The idea is to simply divide the stones into two groups such that the difference between the sum of the two groups is minimum.
"""

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)
        dp = [False for i in range((s//2)+1)]	# We need to find the max number less than sum(stones)/2 which can be the sum of a subset of stones
        dp[0] = True
        
        stones.sort()
        for i in range(len(stones)):
            for j in range(s//2, -1, -1):
                if j < stones[i]:
                    break
                dp[j] = dp[j] or dp[j-stones[i]]
        
        # print(dp)
        temp = 0
        for j in range(s//2+1):
            if dp[j]:
                temp = j
        return (s-temp)-temp	# difference between the sum of the two groups