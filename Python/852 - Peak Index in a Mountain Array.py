"""
Topics: | Binary Search |
"""

class Solution:

    def peakIndexInMountainArray(self, nums):
        """
        Time:  O(log(n))
        Space: O(1)
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
        return low
