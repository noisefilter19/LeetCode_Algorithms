# https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column={}
        row={}
        box={}
        for i in range(len(board)):
            column[i]=[]
            row[i]=[]
            box[i]=[]
        for i in range(len(board)):
            for j in range(len(board)):
                row[i].append(board[i][j])
                column[j].append(board[i][j])
                box[(i//3)*3+j//3].append(board[i][j])
                
        for i in range(len(board)):
            for j in range(1,10):
                if row[i].count(str(j))>1:
                    return False
                if column[i].count(str(j))>1:
                    return False
                if box[i].count(str(j))>1:
                    return False
        return True
