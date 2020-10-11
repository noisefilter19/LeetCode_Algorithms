"""
Topics: | Bit Manipulation |
"""

class Solution:

    def hammingDistance(self, x, y):
        """
        Time:  O(b)  [b = number of 1 bits in x ^ y]
        Space: O(1)
        """
        distance = 0
        xor = x ^ y
        while xor:
            distance += 1
            xor = xor & (xor - 1)
        return distance
