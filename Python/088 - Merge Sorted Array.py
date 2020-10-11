"""
Topics: | Array | Two Pointers |
"""

class Solution:

    def merge(self, A, m, B, n):
        """
        Time:  O(m + n)
        Space: O(1)
        """
        i = m - 1  # Read index in A
        j = n - 1  # Read index in B
        k = m + n - 1  # Write index in A

        while i >= 0 and j >= 0:
            if A[i] >= B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1
            k -= 1

        if j >= 0:
            A[:j+1] = B[:j+1]
