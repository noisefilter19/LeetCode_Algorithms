"""
Topics: | Greedy |

I'm not sure I agree with this being categorized as "greedy". It's less about
optimal substructure and greedy choices leading to an optimal solution than
it is just a simple counting problem.
"""

class Solution:

    def minDeletionSize(self, A):
        """
        Time:  O(kn)  [n = len(A), k = len(A[0])]
        Space: O(1)
        """
        if not A or not A[0]:
            return 0

        count_deletions = 0
        for c in range(len(A[0])):
            if not self.is_column_nondecreasing(c, A):
                count_deletions += 1
        return count_deletions

    def is_column_nondecreasing(self, col, A):
        for row in range(1, len(A)):
            if A[row][col] < A[row - 1][col]:
                return False
        return True
