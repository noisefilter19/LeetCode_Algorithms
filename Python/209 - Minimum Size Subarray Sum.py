"""
Topics: | Array | Two Pointers | Binary Search |
"""

class Solution:

    def minSubArrayLen(self, min_sum, nums):
        """
        Time:  O(n)  [linear "sliding window"]
        Space: O(1)
        """
        result = len(nums) + 1
        curr_sum = 0
        left = 0
        for right, num in enumerate(nums):
            curr_sum += num
            while curr_sum >= min_sum and left < len(nums):
                result = min(result, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        return result if result <= len(nums) else 0
