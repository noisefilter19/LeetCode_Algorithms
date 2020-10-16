# 200 Numbers of Islands Leetcode Medium Problem
# Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#  ["1","1","1","1","0"],
#  ["1","1","0","1","0"],
#  ["1","1","0","0","0"],
#  ["0","0","0","0","0"]
# ]
# Output: 1
# islands only calulated if they are present in horizontal and vertical direction no cross direction are allowed


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'


# Solution
class Solution:
    def numIslands(self, grid):
        self.rows = len(grid)
        if self.rows == 0:
            return 0
        self.cols = len(grid[0])
        island_num = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == "1":
                    self.isIsland(grid, i, j)
                    island_num += 1
        return island_num

    def isIsland(self, grid, i, j) -> int:
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols or grid[i][j] != "1":
            return
        grid[i][j] = "2"
        self.isIsland(grid, i+1, j)
        self.isIsland(grid, i, j+1)
        self.isIsland(grid, i-1, j)
        self.isIsland(grid, i, j-1)


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# test = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
#        ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
# p = Solution()
# result = p.numIslands(test)
# print(result)
