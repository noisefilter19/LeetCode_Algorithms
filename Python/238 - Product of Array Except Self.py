"""
Topics: | Array |
"""

class Solution:

    def productExceptSelf(self, A):
        """
        Time:  O(n)
        Space: O(n)
        """
        B = [1] * len(A)

        p = 1
        for i in range(len(A)):
            B[i] *= p
            p *= A[i]

        p = 1
        for i in reversed(range(len(A))):
            B[i] *= p
            p *= A[i]

        return B
