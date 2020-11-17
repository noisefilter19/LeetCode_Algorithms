class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles = piles[::-1]
        answer = 0
        n = len(piles) // 3
        for i in range(1, 2 * n, 2):
            answer += piles[i]
        return ans
