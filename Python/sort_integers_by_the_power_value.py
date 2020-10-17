# https://github.com/noisefilter19/LeetCode_Algorithms/issues/457

class Solution:
    table = dict()
    
    def getPower(self, x: int) -> int:
        if x == 1:
            return 0
        if x in self.table:
            return self.table[x]
        if x % 2 == 0:
            self.table[x] = 1 + self.getPower(x / 2)
        else:
            self.table[x] = 1 + self.getPower(3 * x + 1)
        return self.table[x]
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        ans = dict()
        for x in range(lo, hi + 1):
            ans[x] = self.getPower(x)
        return sorted(ans, key = ans.get)[k - 1]
