"""
Topics: | Math | String |
"""

class Solution:

    def romanToInt(self, roman):
        """
        Time:  O(n)
        Space: O(1)
        """
        vals = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        integer = 0
        for i in range(0, len(roman) - 1):
            if vals[roman[i]] < vals[roman[i+1]]:
                integer -= vals[roman[i]]
            else:
                integer += vals[roman[i]]
        integer += vals[roman[-1]]

        return integer
