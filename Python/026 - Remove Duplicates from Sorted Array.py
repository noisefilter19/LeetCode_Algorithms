"""
Topics: | Array | Two Pointers |
"""

class Solution:

    def removeDuplicates(self, nums):
        """
        Time:  O(n)
        Space: O(1)
        """
        if not nums:
            return 0

        read = 1
        write = 1
        while read < len(nums):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1
            read += 1
        return write
