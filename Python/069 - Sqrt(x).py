"""
Topics: | Math | Binary Search |
"""

class Solution:

    def mySqrt(self, x: 'int') -> 'int':
        low, high = 1, x

        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1

        return high
