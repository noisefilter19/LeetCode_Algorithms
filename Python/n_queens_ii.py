# Problem link: https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.result = 0
        self.backtrack(0, n, [])
        
        return self.result
    
    
    def isValid(self, i, j, n, positions):
        if 0 <= i < n and 0 <= j < n:
            for pos in positions:
                i1, j1 = pos
                
                if (i1 == i or j1 == j) or (abs(i-i1) == abs(j-j1)):
                    return False
                
            return True
        
        return False
    
    def backtrack(self, row, n, qPos):
        
        if row == n:
            self.result += 1
            return
        
        for i in range(n):
            if self.isValid(row, i, n, qPos):
                
                qPos.append((row, i))
                
                self.backtrack(row+1, n, qPos)
                
                qPos.pop(-1)
