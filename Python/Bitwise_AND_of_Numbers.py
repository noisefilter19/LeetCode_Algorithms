class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        p=31
        if m==0:
            return 0
        while p>=0:
            if pow(2,p) in range(m,n+1):
                return pow(2,p)&m
            p-=1
        res=m
        for i in range(m+1,n+1):
            res=res&i
        return res
