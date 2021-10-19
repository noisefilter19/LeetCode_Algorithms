class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ab_sum_counts = {}
        for a in A:
            for b in B:
                count = ab_sum_counts.get(a + b, 0)
                ab_sum_counts[a + b] = count + 1
        ans = 0
        for c in C:
            for d in D:
                ans += ab_sum_counts.get(-(c + d), 0)
        return ans
