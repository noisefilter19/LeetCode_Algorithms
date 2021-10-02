# Problem Link:    https://leetcode.com/problems/valid-sudoku/
# 36. Valid Sudoku

'''
Problem statement:
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''

'''
Example:
    Input:
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    Output:
        True
'''
class Solution:
    def isValidSudoku(self, board):
        # First check if any number is repeated in same row or column.
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]==".":
                    continue
                if board[i].count(board[i][j])>1:   #check for row
                    return False
                c=0
                for k in range(len(board)):
                    if board[k][j]==board[i][j]:    #check for column
                        c+=1
                if c>1:
                    return False    
        # Now check for sinlge-single 3x3 matrix if it contain all different elemnts or not 
        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                nums = [0]*10
                for ii in range(i,i+3):
                    for jj in range(j,j+3):
                        if board[ii][jj] != '.': 
                            if nums[int(board[ii][jj])] <1:
                                nums[int(board[ii][jj])] = int(board[ii][jj])
                            else:
                                return False
        return True