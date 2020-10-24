class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat: return [[]]
        m = len(mat)
        n = len(mat[0])
        dlen = m + n - 1
        diff = n - m     
        diagonals = []
        for i in range(dlen):
            diagonals.append([])
        for i in range(m):
            for j in range(n):
                diagonals[diff + i-j].append(mat[i][j])
        
        for i in range(dlen):
            diagonals[i] = sorted(diagonals[i])

        for i in range(m):         
            for j in range(n):
                i_d = diff + i - j
                j_d = min(j, i)
                mat[i][j] = diagonals[i_d][j_d] 
        
        return mat
