"""
Topics: | Array |
"""

class Solution:

    def fairCandySwap(self, A, B):
        """
        Time:  O(a + b)
        Space: O(a + b)  [arguably O(1)]
        """
        sum_A, sum_B = sum(A), sum(B)
        target_sum = (sum_A + sum_B) // 2

        set_A, set_B = set(A), set(B)
        for bar_A in set_A:
            bar_B = target_sum - (sum_A - bar_A)
            if bar_B in set_B:
                return [bar_A, bar_B]

        return [-1, -1]
