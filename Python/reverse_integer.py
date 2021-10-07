"""
Link to Problem: https://leetcode.com/problems/reverse-integer/

7. Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        sign = None if not str(x).startswith("-") else "-"
        x = str(abs(x))[::-1]
        x = x.lstrip("0")
        final = int(sign + x if sign else x)
        
        if (final <= (-2**31)) or (final >= (2**31 -1)):
            return 0
        return final
