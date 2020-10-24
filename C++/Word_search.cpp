// https://leetcode.com/problems/word-search/

class Solution {

    bool dfs(vector<vector<char>>& board, string word, int i, int j, int rows, int cols, int word_iter){

        if (word_iter == word.length()){
            return true;
        }

        if (i<0 || i>=rows || j<0 || j>=cols || board[i][j] != word[word_iter]){
            return false;
        }


        char tmp = board[i][j];
        board[i][j] = ' ';

        bool found = dfs(board, word, i+1, j, rows, cols, word_iter+1) || 
                     dfs(board, word, i-1, j, rows, cols, word_iter+1) || 
                     dfs(board, word, i, j+1, rows, cols, word_iter+1) || 
                     dfs(board, word, i, j-1, rows, cols, word_iter+1);

        board[i][j] = tmp;
        return found;
    }

public:
    bool exist(vector<vector<char>>& board, string word) {
        
        int word_length = word.length();
        int rows = board.size();
        int cols = board[0].size();

        // look for first element
        for (int i = 0; i < rows; ++i){
            for (int j = 0; j < cols; ++j){
                if (board[i][j] == word[0] && dfs(board, word, i, j, rows, cols, 0)){
                    return true;
                }
            }
        }
        return false;
    }
};
