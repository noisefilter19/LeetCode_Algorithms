class Solution {
public:
    bool validTicTacToe(vector<string>& board) {
        int x = 0, o = 0; //Number of X and O
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                if(board[i][j] == 'X') x++;
                if(board[i][j] == 'O') o++;
            }
        }
                 if(x <o || x-o> 1) return false; //X goes first, x is greater than or equal to o, and the difference does not exceed 1
                 if(x <= 2) return true; //There is no possibility of connecting into a line, do not need to make subsequent judgments, return directly
        int xl = 0, ol = 0;
                 for(int i = 0; i <3; i++){ //Check the horizontal and vertical connection
            if(board[i][0] == board[i][1] && board[i][1] == board[i][2]){
                if(board[i][0] == 'X') xl++;
                if(board[i][0] == 'O') ol++;
            }
            if(board[0][i] == board[1][i] && board[1][i] == board[2][i]){
                if(board[0][i] == 'X') xl++;
                if(board[0][i] == 'O') ol++;
            }   
        }
                 //Check the connection of the diagonal
        if(board[0][0] == board[1][1] && board[1][1] == board[2][2]){
                if(board[0][0] == 'X') xl++;
                if(board[0][0] == 'O') ol++;
        }
        if(board[0][2] == board[1][1] && board[1][1] == board[2][0]){
                if(board[0][2] == 'X') xl++;
                if(board[0][2] == 'O') ol++;
        }
                 if(xl> 1 || ol> 1 || (xl&&ol)) return false; //There is more than 1 connection, error
                 if(xl == 1 && x == o) return false; //X is connected first, O does not stop in time, error
                 if(ol == 1 && x> o) return false; //O is connected first, X does not stop in time, error
        return true;
    }
};
