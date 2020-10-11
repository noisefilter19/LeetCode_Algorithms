"""
Topics: | None |
"""

class Solution:

    def maxIncreaseKeepingSkyline(self, grid):
        """
        Time:  O(mn)  [m rows, n columns]
        Space: O(m + n)
        """
        row_maxes, col_maxes = self.get_max_heights(grid)
        total_increase = 0
        for r, row in enumerate(grid):
            for c, height in enumerate(row):
                total_increase += min(row_maxes[r], col_maxes[c]) - height
        return total_increase

    def get_max_heights(self, grid):
        row_maxes = [0] * len(grid)
        col_maxes = [0] * len(grid[0])
        for r, row in enumerate(grid):
            for c, height in enumerate(row):
                row_maxes[r] = max(row_maxes[r], height)
                col_maxes[c] = max(col_maxes[c], height)
        return row_maxes, col_maxes
