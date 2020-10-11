"""
Topics: | Depth-first Search | Breadth-first Search | Union Find |
"""

class Solution:

    def numIslands(self, grid):
        """
        Time:  O(mn)
        Space: O(mn)
        """
        if not grid or not grid[0]:
            return 0

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    self.DFS(grid, r, c)
                    count += 1
        return count

    def DFS(self, grid, r, c):
        if (r < 0 or c < 0
                or r >= len(grid) or c >= len(grid[0])
                or grid[r][c] != '1'):
            return
        grid[r][c] = 'X'
        self.DFS(grid, r - 1, c)
        self.DFS(grid, r + 1, c)
        self.DFS(grid, r, c - 1)
        self.DFS(grid, r, c + 1)
