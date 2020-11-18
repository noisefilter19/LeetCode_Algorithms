//LeetCode Problem link - https://leetcode.com/problems/word-search/

class Solution {
public:
    bool wordFound(vector<vector <char>> mat, string word, int index, int row, int col, int ROW, int COL)
    {
        if(index>=word.size())
            return true;
        if(!(checkBound(row, col, ROW, COL) && word[index]==mat[row][col]))
            return false;
        if(index==word.size()-1)
            return true;
        mat[row][col]='0';
        if(checkBound(row+1, col, ROW, COL) && word[index+1]==mat[row+1][col])
            if(wordFound(mat, word, index+1, row+1, col, ROW, COL))
                return true;
        if(checkBound(row-1, col, ROW, COL) && word[index+1]==mat[row-1][col])
            if(wordFound(mat, word, index+1, row-1, col, ROW, COL))
                return true;
        if(checkBound(row, col+1, ROW, COL) && word[index+1]==mat[row][col+1])
            if(wordFound(mat, word, index+1, row, col+1, ROW, COL))
                return true;
        if(checkBound(row, col-1, ROW, COL) && word[index+1]==mat[row][col-1])
            if(wordFound(mat, word, index+1, row, col-1, ROW, COL))
                return true;
        return false;
    }
    
    
    bool checkBound(int row, int col, int ROW, int COL)
    {
        if(row>=ROW || col>=COL || row<0 || col<0)
                return false;
        return true;
    }
    
    bool exist(vector<vector<char>>& board, string word) {
        vector<vector <char>> v=board;
        int ROW=v.size();
        int COL=v[0].size();
        for(int i=0;i<v.size();i++)
            for(int j=0;j<v[i].size();j++)
                if(v[i][j]==word[0] && wordFound(v, word, 0, i, j, ROW, COL)==true)
                    return true;
        return false;
    }
};
