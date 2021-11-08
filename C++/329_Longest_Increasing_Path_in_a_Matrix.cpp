class Solution {
private:
    int m, n;
    vector<vector<int>> maxDepth;
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        m = matrix.size();
        if (m == 0)
            return 0;
        n = matrix[0].size();
        maxDepth = vector<vector<int>>(m, vector<int>(n, 0));
        int longestPath = 1;
        
        for (int i=0; i<m; i++)
            for (int j=0; j<n; j++)
            {
                int md = CalculateMaxDepth(i, j, matrix);
                if (md > longestPath)
                    longestPath = md;
            }
        return longestPath;
    }
    
    int CalculateMaxDepth(int x, int y, const vector<vector<int>>& matrix) {
        if (maxDepth[x][y] != 0)
            return maxDepth[x][y];
        
        int md = 1;
        int num = matrix[x][y];

        if (isValid(x-1, y) && matrix[x-1][y] < num) {
            int mdd = 1+CalculateMaxDepth(x-1, y, matrix);
            md = md > mdd ? md : mdd;
        }
        
        if (isValid(x+1, y) && matrix[x+1][y] < num) {
            int mdd = 1+CalculateMaxDepth(x+1, y, matrix);
            md = md > mdd ? md : mdd;
        }
        
        if (isValid(x, y-1) && matrix[x][y-1] < num) {
            int mdd = 1+CalculateMaxDepth(x, y-1, matrix);
            md = md > mdd ? md : mdd;
        }
        
        if (isValid(x, y+1) && matrix[x][y+1] < num) {
            int mdd = 1+CalculateMaxDepth(x, y+1, matrix);
            md = md > mdd ? md : mdd;
        }
        
        maxDepth[x][y] = md;
        return md;
    }
    
    bool isValid(int x, int y) {
        return x>=0 && x<m && y>=0 && y<n;
    }
};