"""
Topics: | Array |
"""

class Solution:

    def sortArrayByParity(self, A):
        """
        Time:  O(n)
        Space: O(1)
        """
        lo = 0
        hi = len(A) - 1
        while lo < hi:
            while A[lo] % 2 == 0 and lo < hi:
                lo += 1
            while A[hi] % 2 == 1 and lo < hi:
                hi -= 1
            A[lo], A[hi] = A[hi], A[lo]
        return A
