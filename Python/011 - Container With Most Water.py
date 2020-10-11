"""
Topics: | Array | Two Pointers |
"""

class Solution:

    def maxArea(self, heights):
        """
        Time:  O(n)
        Space: O(1)
        """
        max_area = 0

        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            max_area = max(area, max_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area
