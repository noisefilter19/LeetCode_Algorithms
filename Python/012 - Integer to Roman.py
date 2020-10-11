"""
Topics: | Math | String |
"""

class Solution:

    def intToRoman(self, num):
        """
        Time:  O(n)
        Space: O(1)
        """
        result = []
        for numeral, value in self.numeral_values:
            if num >= value:
                result.append(numeral * (num // value))
                num %= value
        return ''.join(result)


    numeral_values = [ ("M", 1000),
                       ("CM", 900),
                       ("D",  500),
                       ("CD", 400),
                       ("C",  100),
                       ("XC",  90),
                       ("L",   50),
                       ("XL",  40),
                       ("X",   10),
                       ("IX",   9),
                       ("V",    5),
                       ("IV",   4),
                       ("I",    1) ]
