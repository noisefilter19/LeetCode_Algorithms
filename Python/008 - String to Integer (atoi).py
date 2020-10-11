"""
Topics: | Math | String |
"""

class Solution:

    def myAtoi(self, str):
        """
        Time:  O(n)
        Space: O(n)
        """
        if not str: return 0

        str = str.lstrip()
        if not str: return 0

        i = 0
        negative = False
        if str[0] == '+':
            i += 1
        elif str[0] == '-':
            negative = True
            i += 1
        elif not str[0].isdigit():
            return 0

        value = 0
        while i < len(str) and str[i].isdigit():
            value *= 10
            value += int(str[i])
            i += 1
        if negative: value = -value

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if value > INT_MAX:
            return INT_MAX
        elif value < INT_MIN:
            return INT_MIN
        else:
            return value
