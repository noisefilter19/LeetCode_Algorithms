"""
Topics: | Array |
"""

class Solution:

    def arrayPairSum(self, nums):
        """
        Time:  O(n*log(n))
        Space: O(1)
        """
        nums.sort()
        sum_mins = 0
        for i in range(0, len(nums), 2):
            sum_mins += nums[i]
        return sum_mins
