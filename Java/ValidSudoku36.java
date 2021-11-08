public class ValidSudoku36 {
    public boolean isValidSudoku(char[][] board) {
        for (int row=0; row < 9; row++){
            for (int col=0; col < 9; col++){
                if (!isValidNum(board[row][col], row, col, board))
                    return false;
            }}
        return true;
    }

    public boolean isValidNum(char c, int row, int col, char[][] board){
        if (c != '.'){
            int num = Integer.parseInt(String.valueOf(c));
            return !isInRow(num, board, row, col) && !isInCol(num, board, row, col)
                    && !isInBox(num, board, row - row % 3, col - col % 3, row, col);
        }
        else
            return true;
    }

    public boolean isInRow(int num, char[][] board, int row, int col){
        for (int i=0 ;i < 9; i++){
            if (board[row][i] == '.')
                continue;
            if (i != col && Integer.parseInt(String.valueOf(board[row][i])) == num)
                return true;
        }
        return false;
    }

    public boolean isInCol(int num, char[][] board, int row, int col){
        for (int i=0 ;i < 9; i++){
            if (board[i][col] == '.')
                continue;
            if (i != row && Integer.parseInt(String.valueOf(board[i][col])) == num)
                return true;
        }
        return false;
    }

    public boolean isInBox(int num, char[][] board, int startRow, int startCol, int itRow, int itCol){
        for (int row = 0 ;row < 3; row++){
            for (int col = 0 ;col < 3; col++){
                if (board[row+startRow][col+startCol] == '.')
                    continue;
                if (row+startRow == itRow && col+startCol == itCol)
                    continue;
                if (Integer.parseInt(String.valueOf(board[row+startRow][col+startCol])) == num)
                    return true;
            }
        }
        return false;
    }
}
