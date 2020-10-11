//https://leetcode.com/problems/count-square-submatrices-with-all-ones/solution/
class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int result=0;
        int row = matrix.size();
        int col = matrix[0].size();
        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                if(matrix[i][j]>0 && i>0 && j>0)
                {
                    matrix[i][j]=min(matrix[i-1][j],min(matrix[i-1][j-1],matrix[i][j-1]))+1;
                }
                result+=matrix[i][j];
            }
        }
        
        return result;
    }
};