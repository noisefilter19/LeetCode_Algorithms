class Solution:
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def enough(x):
            count = 0
            for i in range(1, m+1):
                count += min(x//i, n)
            return count >= k
            
        lo, hi = 1, m*n
        while (lo < hi):
            mid = lo + (hi - lo) // 2
            if not enough(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo
        