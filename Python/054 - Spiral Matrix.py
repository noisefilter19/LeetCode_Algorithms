"""
Topics: | Array |
"""

class Solution(object):

    def spiralOrder(self, matrix):
        """
        Time:  O(mn)
        Space: O(mn)
        """
        traversal = []

        if not matrix or not matrix[0]:
            return traversal

        row_start = 0
        row_end = len(matrix)
        col_start = 0
        col_end = len(matrix[0])

        while (row_start < row_end and col_start < col_end):
            # Traverse the top row
            for c in range(col_start, col_end):
                traversal.append(matrix[row_start][c])
            row_start += 1

            # Traverse the right column
            for r in range(row_start, row_end):
                traversal.append(matrix[r][col_end - 1])
            col_end -= 1

            # Traverse the bottom row, if unseen elements remain
            if row_start < row_end:
                for c in reversed(range(col_start, col_end)):
                    traversal.append(matrix[row_end - 1][c])
                row_end -= 1

            # Traverse the left column, if unseen elements remain
            if col_start < col_end:
                for r in reversed(range(row_start, row_end)):
                    traversal.append(matrix[r][col_start])
                col_start += 1

        return traversal
