"""
Topics: | Array | Binary Search |
"""

class Solution:

    def searchInsert(self, nums, target):
        """
        Time:  O(log(n))
        Space: O(1)
        """
        return self.binary_search(nums, target)

    def binary_search(self, nums, target):
        """Return the index of target in nums, if found.

        If not found, return index to insert it in increasing order."""
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
