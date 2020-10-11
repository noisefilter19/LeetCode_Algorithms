"""
Topics: | Array |
"""

class Solution:

    def dominantIndex(self, nums):
        """
        Time:  O(n)  [exactly one pass through nums]
        Space: O(1)
        """
        largest = float('-inf')
        second_largest = float('-inf')
        largest_index = -1

        for i, num in enumerate(nums):
            if num > largest:
                second_largest = largest
                largest = num
                largest_index = i
            elif num > second_largest and num < largest:
                second_largest = num

        if (largest >= 2 * second_largest):
            return largest_index
        else:
            return -1
