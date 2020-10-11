"""
Topics: | Array | Divide and Conquer | Dynamic Programming |
"""

class Solution:

    def maxSubArray(self, nums):
        """
        Time:  O(n)
        Space: O(1)
        """
        if not nums: return None

        max_sum = float('-inf')
        curr_sum = 0  # Optimal sum ending with the current number
        for n in nums:
            curr_sum = max(n, curr_sum + n)
            max_sum = max(max_sum, curr_sum)
        return max_sum
