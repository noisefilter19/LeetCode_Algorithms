class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
