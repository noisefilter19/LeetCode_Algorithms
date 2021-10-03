class Solution {
    int [][] grid;
    boolean [][] seen;
    public int maxAreaOfIsland(int[][] grid) {
        this.grid = grid;
        seen = new boolean [grid.length][grid[0].length];
        
        int count = 0;
        
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                count = Math.max(count, dfs(i,j));
            }
        }
        return count;
    }
    
    public int dfs(int r, int c){
        if(r<0 || c<0 || r>=grid.length || c>=grid[0].length || seen[r][c] || grid[r][c] == 0 ) return 0;
        
        seen[r][c] = true;
        
        return( 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1)+ dfs(r, c-1) );
    }
}
