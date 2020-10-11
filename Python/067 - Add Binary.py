"""
Topics: | Math | String |
"""

from collections import deque

class Solution(object):

    def addBinary(self, a, b):
        """
        Time:  O(a + b)
        Space: O(a + b)
        """
        maxlen = max(len(a), len(b))
        a = a.zfill(maxlen)
        b = b.zfill(maxlen)

        result = deque()
        carry = 0
        for a_bit, b_bit in (zip(reversed(a), reversed(b))):
            bit_sum = carry
            bit_sum += (1 if a_bit == '1' else 0)
            bit_sum += (1 if b_bit == '1' else 0)
            carry, result_bit = divmod(bit_sum, 2)
            result.appendleft('1' if result_bit else '0')

        if carry:
            result.appendleft('1' if carry else '0')

        return ''.join(result)
