"""
Topics: | Array |
"""

class Solution(object):

    def generate(self, num_rows):
        """
        Time:  O(n^2)
        Space: O(n^2)

        [n = num_rows]
        """
        if num_rows == 0: return []

        pascal = [[1] * (cols + 1) for cols in range(num_rows)]

        for row in range(2, num_rows):
            for col in range(1, row):
                left_parent = pascal[row - 1][col - 1]
                right_parent = pascal[row -1][col]
                pascal[row][col] = left_parent + right_parent

        return pascal
