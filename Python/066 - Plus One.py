"""
Topics: | Array | Math |
"""

class Solution:

    def plusOne(self, digits):
        """
        Time:  O(n)
        Space: O(1)
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9 and carry == 1:
                digits[i] = 0
            else:
                digits[i] += carry
                carry = 0
                break

        # If we still have a carry, `digits` was all 9's;
        # need to add a new digit to the result
        if carry == 1:
            digits = [1] + digits

        return digits
