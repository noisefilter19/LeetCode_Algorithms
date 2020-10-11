"""
Topics: | Array |
"""

class Solution:

    def flipAndInvertImage(self, A):
        """
        Time:  O(mn)  [m = len(A), n = len(A[0])]
        Space: O(1)
        """
        if not A or not A[0]:
            return None

        middle = (len(A[0]) + 1) // 2
        for row in A:
            for left in range(middle):
                right = len(row) - 1 - left
                row[left], row[right] = row[right] ^ 1, row[left] ^ 1
        return A
