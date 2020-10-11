"""
Topics: | Array |
"""

class Solution:

    def findMaxConsecutiveOnes(self, nums):
        """
        Time:  O(n)
        Space: O(1)
        """
        current_streak = 0
        max_streak = 0
        for num in nums:
            if num == 1:
                current_streak += 1
                max_streak = max(current_streak, max_streak)
            else:
                current_streak = 0
        return max_streak
