"""
Topics: | None |
"""

from collections import deque

class Solution:

    def findDiagonalOrder(self, matrix):
        """
        Time:  O(mn)
        Space: O(mn)
        """
        if not matrix or not matrix[0]:
            return []

        rows = len(matrix)
        cols = len(matrix[0])
        diagonals = [deque() for _ in range(rows + cols + 1)]

        for r in range(rows):
            for c in range(cols):
                diagonal_index = r + c
                if diagonal_index % 2 == 0:
                    diagonals[diagonal_index].appendleft(matrix[r][c])
                else:
                    diagonals[diagonal_index].append(matrix[r][c])

        flattened_diagonals = [num for diagonal in diagonals for num in diagonal]
        return flattened_diagonals
