# LeetCode Problem Link - https://leetcode.com/problems/sum-of-subsequence-widths

class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ret_int = 0
        A_len = len(A)
        A.sort(key=lambda x: int(x), reverse=True)
        
        for x in range(A_len):
            ret_int += A[x] * (2**(A_len - x - 1) - 2**(x))
        
        return ret_int % (10**9 + 7)
