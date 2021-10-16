class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def explore(grid, r, c, visited):
            rowInbound = 0 <= r <len(grid)
            colInbound = 0 <= c < len(grid[0])
            
            if not(rowInbound) or not(colInbound):return 0
            if grid[r][c] == 0: return 0
            elem = str(r)+','+str(c)
            if visited.__contains__(elem): return 0
            visited.add(elem)
          
            
            return 1 + explore(grid,r-1,c,visited) + explore(grid,r+1,c,visited)+explore(grid,r,c+1,visited) + explore(grid,r,c-1,visited)
        
        visited = set()
        max_c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_c = max(max_c,explore(grid,i,j,visited))
        return max_c
        