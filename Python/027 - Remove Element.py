"""
Topics: | Array | Two Pointers |
"""

class Solution:

    def removeElement(self, nums, val):
        """
        Time:  O(n)
        Space: O(1)
        """
        left = 0
        right = len(nums) -1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left
