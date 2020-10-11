"""
Topics: | Array | Two Pointers | Binary Search |
"""

class Solution:

    def twoSum(self, numbers, target):
        """
        Time:  O(n)
        Space: O(1)

        Two other O(n) time solutions:
          - binary search for (target - num) for each num in numbers
          - in a dict, map num to index for each num in numbers; lookup
            (target - num) in that dict to see if the complement has
            already been seen; O(n) space
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum_left_right = numbers[left] + numbers[right]
            if sum_left_right == target:
                return [left + 1, right + 1]
            elif sum_left_right < target:
                left += 1
            else:
                right -= 1

        return None
