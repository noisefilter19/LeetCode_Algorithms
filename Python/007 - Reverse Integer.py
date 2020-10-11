"""
Topics: | Math |
"""

class Solution:

    def reverse(self, x):
        """
        Time:  O(log(x))
        Space: O(1)
        """
        is_negative = x < 0
        x = abs(x)
        reversed = 0
        while x:
            reversed *= 10
            reversed += x % 10
            x //= 10

        INT_MAX_32 = 2**31 - 1
        if reversed > INT_MAX_32:
            return 0
        elif is_negative:
            return -reversed
        else:
            return reversed
