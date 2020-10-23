"""
https://leetcode.com/problems/rotting-oranges/

Comments included with the code. 

The idea is to go a BFS level order traversal from each rotting orange, then
add 1 to minutes elapsed after each level. Keep a count of how many pure oranges
remained at each point, and when they reach zero, return minutes elapsed.

"""

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dirs = [(0,1),(1,0), (-1,0), (0,-1)]
        q = []
        rows, cols = len(grid), len(grid[0])
        pure_count =0
        # we will do a bfs from a rotten orange

        # first, get the number of pure oranges
        # then add all the rotten oranges in a queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j]==1:
                    pure_count+=1
        if pure_count==0:
            return 0
        if not q:
            return -1

        # making minutes start from -1, for convenience,
        # as at the next (0th) minute, we will just add
        # the neighbors to the queue, not rot them until the minute after that.
        minutes=-1

        while q:
            next_level = []
            for i, j in q:
                for dx, dy in dirs:
                    x,y = i+dx, j+dy
                    if x>=0 and y>=0 and x<rows and y<cols and grid[x][y]==1:
                        grid[x][y] = 2
                        pure_count-=1
                        next_level.append((x,y))
            q = next_level
            minutes+=1
        return minutes if pure_count==0 else -1
