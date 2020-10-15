"""
LeetCode link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
Difficulty: Hard
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        height = len(matrix)
        width = len(matrix[0])
        
        def neighbors(i, j):
            if i > 0:
                yield i - 1, j
            if i < height - 1:
                yield i + 1, j
            if j > 0:
                yield i, j - 1
            if j < width - 1:
                yield i, j + 1
        
        longestFrom = [[None] * width for _ in range(height)]
        
        def findLongestFrom(i, j):
            if longestFrom[i][j] is not None:
                return longestFrom[i][j]
            
            value = matrix[i][j]
            longestFrom[i][j] = out = max(
                (1 + findLongestFrom(r, c) for r, c in neighbors(i, j) if matrix[r][c] > value),
                default=1
            )
            return out
        
        
        for i in range(height):
            for j in range(width):
                if longestFrom[i][j] is None:
                    findLongestFrom(i, j)
                    
        return max(max(row) for row in longestFrom)
