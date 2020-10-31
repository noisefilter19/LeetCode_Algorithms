# Problem link: https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map
# where the width of each bar is 1,
# compute how much water it can trap after raining.

# Input: heights = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map is represented by array
#              [0,1,0,2,1,0,1,3,2,1,2,1].
#              In this case, 6 units of rain water (blue section)
#              are being trapped.

"""
Approach:
1. Get the maximum left and right heights for every column.
2. Iterate through and calculate the trapped water for each column
   using the left and right heights.
"""


class Solution:
    def trap_water(self, heights: list[int], left, right):
        capacity = 0
        for i in range(len(heights)):
            capacity += min(left[i], right[i]) - heights[i]
        return capacity

    def left_right_max(self, heights: list[int]):
        l_max = []
        r_max = []
        lmax = 0
        rmax = 0
        for i in range(len(heights)):
            if heights[i] > lmax:
                lmax = heights[i]
            l_max.append(lmax)
            if heights[-(i + 1)] > rmax:
                rmax = heights[-(i + 1)]
            r_max.append(rmax)
        # print(l)
        # print(r[::-1])
        return l_max, r_max[::-1]

    def trap(self, heights: list[int]) -> int:
        l_max, r_max = self.left_right_max(heights)
        return self.trap_water(heights, l_max, r_max)
